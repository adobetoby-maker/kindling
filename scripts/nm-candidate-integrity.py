#!/usr/bin/env python3
"""CPU-only ordered waveform/rest audit of separate provisional repair editions."""
import hashlib
import json
from pathlib import Path
import numpy as np
import soundfile as sf

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT/'books/book-2680-national-measure'
RECORDS = BOOK/'narration/breeze/local-repair-candidates-v1'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main(edition=1):
    records = BOOK/f'narration/breeze/local-repair-candidates-v{edition}'
    for directory in sorted(records.glob('chapter-*')):
        technical = json.loads((directory/'technical-review.json').read_text())
        manifest = json.loads((directory/'take-manifest.json').read_text())
        if hashlib.sha256(json.dumps(manifest,sort_keys=True).encode()).hexdigest() != technical['bindingSha256']:
            raise RuntimeError('Manifest changed')
        audio,master = Path(technical['audioPath']),Path(technical['wavPath'])
        if sha(audio) != technical['audioSha256']:
            raise RuntimeError('Candidate audio changed')
        source = BOOK/'manuscript'/f'{directory.name}.md'
        if sha(source) != technical['sourceSha256']:
            raise RuntimeError('Canonical source changed')
        output = directory/'assembly-integrity.json'
        if output.exists():
            prior = json.loads(output.read_text())
            if prior['audioSha256'] == technical['audioSha256'] and prior['masterSha256'] == sha(master):
                continue
            raise RuntimeError('Preserve differing prior waveform audit')
        max_error,authored,frames = 0.0,0,0
        with sf.SoundFile(master) as assembled:
            if assembled.samplerate != 24000 or assembled.channels != 1:
                raise RuntimeError('Unexpected candidate format')
            for take in manifest['takes']:
                path = Path(take['path'])
                if sha(path) != take['sha256']:
                    raise RuntimeError('Bound checkpoint changed')
                expected,rate = sf.read(path,dtype='float32')
                if rate != 24000 or expected.ndim != 1 or not np.isfinite(expected).all():
                    raise RuntimeError('Unexpected checkpoint format')
                fade = min(120,len(expected)//4)
                if fade:
                    expected[:fade] *= np.linspace(0,1,fade,dtype=np.float32)
                    expected[-fade:] *= np.linspace(1,0,fade,dtype=np.float32)
                expected[0] = expected[-1] = 0
                actual = assembled.read(len(expected),dtype='float32')
                if len(actual) != len(expected):
                    raise RuntimeError('Truncated candidate take')
                error = float(np.max(np.abs(expected-actual)))
                max_error = max(max_error,error)
                if error > 1/32768+1e-7:
                    raise RuntimeError(f"Wrong waveform/order/edge edit at {take['id']}")
                rests = int(rate*take['pauseAfterMs']/1000)
                silence = assembled.read(rests,dtype='float32')
                if len(silence) != rests or np.any(silence):
                    raise RuntimeError('Inserted rest differs')
                authored += rests
                frames += len(expected)+rests
            if frames != assembled.frames:
                raise RuntimeError('Extra or missing candidate samples')
        if sha(source) != technical['sourceSha256'] or sha(audio) != technical['audioSha256']:
            raise RuntimeError('Inputs changed during audit')
        report = {'sourceSha256':technical['sourceSha256'],'audioSha256':technical['audioSha256'],
                  'masterSha256':sha(master),'bindingSha256':technical['bindingSha256'],
                  'orderedWaveformsAndFiveMsEdges':'passed-within-one-PCM16-quantization-step',
                  'insertedSilenceAndFrameCount':'passed','maximumPcm16Difference':max_error,
                  'durationSec':frames/24000,'authoredRestSec':authored/24000,
                  'segments':len(manifest['takes']),'published':False,'ownerListening':'pending',
                  'scope':'Structural integrity only; not spoken coverage, mastering, pace or voice approval'}
        output.write_text(json.dumps(report,indent=2)+'\n')
        print(directory.name,'ordered waveforms/rests passed',flush=True)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--edition',type=int,choices=[1,2],default=1)
    main(parser.parse_args().edition)
