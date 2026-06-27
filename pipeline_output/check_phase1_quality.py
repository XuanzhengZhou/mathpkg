#!/usr/bin/env python3
"""QC checker for Phase 1 gap-fill outputs (including redo)."""
import json, os, re, sys

GAP_DIR = '/home/a123/文档/mathpkg/pipeline_output/gapfill_output'
INPUT_FILE = '/home/a123/文档/mathpkg/pipeline_output/p1_gapfill.json'
REDO_INPUT = '/home/a123/文档/mathpkg/pipeline_output/p1_gapfill_redo.json'
REDO_INDICES = [0, 1, 2, 3, 6, 8, 12, 13, 14, 16, 17, 18, 19, 20]
REDO_OFFSET = 100

VAGUE = [
    r'\bclearly\b', r'\bobviously\b', r'\bit follows that\b',
    r'\bone can show\b', r'\btrivially\b', r'\bit is easy to see\b',
    r'\bstraightforward\b', r'\bthe result follows\b',
    r'\bimmediate\b', r'\bevidently\b',
]
REF = [
    r'\b[Tt]heorem\b', r'\b[Ll]emma\b', r'\b[Cc]orollary\b',
    r'\b[Dd]efinition\b', r'\b[Aa]xiom\b', r'\b[Pp]roposition\b',
    r'\b[Bb]y\b', r'\b[Ss]ince\b', r'\b[Bb]ecause\b', r'\b[Uu]sing\b',
    r'\b[Aa]pply\b', r'\b[Tt]herefore\b', r'\b[Hh]ence\b', r'\b[Tt]hus\b',
]

def check_proof(proof):
    failures = []
    if len(proof.strip()) < 50:
        failures.append(f'Too short ({len(proof)} chars)')
    steps = re.findall(r'^\s*(\d+)\.?\s', proof, re.MULTILINE)
    if len(steps) < 2:
        failures.append(f'Only {len(steps)} numbered steps')
    for p in VAGUE:
        if re.search(p, proof, re.IGNORECASE):
            failures.append(f'Vague: "{re.search(p, proof, re.IGNORECASE).group()}"')
            break
    sl = [l.strip() for l in proof.split('\n') if re.match(r'^\d+\.?\s', l.strip())]
    refs = sum(1 for l in sl if any(re.search(rp, l, re.IGNORECASE) for rp in REF))
    if sl and refs < len(sl) * 0.5:
        failures.append(f'Only {refs}/{len(sl)} steps ref theorems')
    if sl and not re.search(r'∎|QED|conclusion|therefore|hence|thus|proved', sl[-1], re.IGNORECASE):
        failures.append('No conclusion')
    return failures, len(steps)

results = {'pass': [], 'fail': [], 'missing': []}

# Check original files
with open(INPUT_FILE) as f:
    concepts = json.load(f)
for i, c in enumerate(concepts):
    cid, gf = c['id'], os.path.join(GAP_DIR, f'gap_{i}.json')
    if i in REDO_INDICES:
        continue  # checked in redo pass
    if not os.path.exists(gf):
        results['missing'].append({'index': i, 'id': cid, 'reason': 'File missing'})
        continue
    try:
        proof = json.load(open(gf)).get('expanded_proof', '')
    except Exception as e:
        results['fail'].append({'index': i, 'id': cid, 'reason': str(e)})
        continue
    fbs, ns = check_proof(proof)
    (results['fail'] if fbs else results['pass']).append(
        {'index': i, 'id': cid, 'reason': '; '.join(fbs), 'proof_preview': proof[:200], 'steps': ns})

# Check redo files
if os.path.exists(REDO_INPUT):
    with open(REDO_INPUT) as f:
        redo = json.load(f)
    for ri, oi in enumerate(REDO_INDICES):
        c, gf = redo[ri], os.path.join(GAP_DIR, f'gap_{ri + REDO_OFFSET}.json')
        cid = c['id']
        if not os.path.exists(gf):
            results['missing'].append({'index': oi, 'id': cid, 'reason': 'Redo missing'})
            continue
        try:
            proof = json.load(open(gf)).get('expanded_proof', '')
        except Exception as e:
            results['fail'].append({'index': oi, 'id': cid, 'reason': str(e)})
            continue
        fbs, ns = check_proof(proof)
        (results['fail'] if fbs else results['pass']).append(
            {'index': oi, 'id': cid, 'reason': '; '.join(fbs), 'proof_preview': proof[:200], 'steps': ns})

# Report
print(f"\n{'='*60}")
print("Phase 1 QC Report")
print(f"{'='*60}")
print(f"PASS: {len(results['pass'])}  FAIL: {len(results['fail'])}  MISSING: {len(results['missing'])}")
for label, items in [('PASSED', results['pass']), ('FAILED', results['fail']), ('MISSING', results['missing'])]:
    if items:
        print(f"\n--- {label} ---")
        for r in items:
            icon = '✅' if label == 'PASSED' else ('❌' if label == 'FAILED' else '⚠️')
            print(f"  {icon} [{r['index']}] {r['id']}")
            if label != 'PASSED':
                print(f"      {r.get('reason','')}")

failed = [r['index'] for r in results['fail']] + [r['index'] for r in results['missing']]
with open(os.path.join(GAP_DIR, '_failed_indices.json'), 'w') as f:
    json.dump(sorted(failed), f)
print(f"\nTotal: {len(results['pass'])}/{len(concepts)+len(redo) if os.path.exists(REDO_INPUT) else len(concepts)} passed")
print(f"Failed indices: {failed}")
sys.exit(0 if not failed else 1)
