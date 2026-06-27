#!/usr/bin/env python3
"""Checker: compile .lean file, write .done or .fail marker."""
import json, os, sys, subprocess

INPUT_FILE = '/home/a123/文档/mathpkg/pipeline_output/191_definitions.json'
LEAN_PROJ = '/home/a123/文档/mathpkg/lean/MathPkg'
DONE_DIR = '/home/a123/文档/mathpkg/pipeline_output/def_done'

def main():
    idx = int(sys.argv[1])
    os.makedirs(DONE_DIR, exist_ok=True)
    df = os.path.join(DONE_DIR, f'done_{idx}.json')
    ff = os.path.join(DONE_DIR, f'fail_{idx}.json')

    # Already done?
    if os.path.exists(df):
        print('ALREADY_DONE')
        return

    # Get concept
    data = json.load(open(INPUT_FILE))
    c = data[idx]
    cid = c['id']
    lean_file = os.path.join(LEAN_PROJ, 'MathPkg', 'Pipeline', f'{cid}.lean')

    # File missing
    if not os.path.exists(lean_file):
        json.dump({'idx': idx, 'cid': cid, 'status': 'no_file',
                    'statement': c['statement'],
                    'gapfill': c.get('gapfill_proof', '')[:1500]},
                   open(ff, 'w'))
        print(f'NO_FILE: {cid}')
        return

    # Compile
    cmd = f'cd {LEAN_PROJ} && export PATH="$HOME/.elan/bin:$PATH" && timeout 30 lake env lean MathPkg/Pipeline/{cid}.lean 2>&1'
    r = subprocess.run(['bash', '-c', cmd], capture_output=True, text=True, timeout=40)
    output = r.stdout + r.stderr
    has_error = 'error:' in output

    if r.returncode == 0 and not has_error:
        json.dump({'idx': idx, 'cid': cid, 'status': 'ok'}, open(df, 'w'))
        print(f'PASS: {cid}')
    else:
        errors = [l.strip() for l in output.split('\n') if 'error:' in l][:5]
        json.dump({'idx': idx, 'cid': cid, 'status': 'fail', 'errors': errors,
                    'statement': c['statement'],
                    'gapfill': c.get('gapfill_proof', '')[:1500]},
                   open(ff, 'w'))
        print(f'FAIL: {cid} ({len(errors)} errors)')

if __name__ == '__main__':
    main()
