#!/usr/bin/env python3
"""Fix the titles in all concept.yaml files for GTM022."""
import os, re, yaml

BASE = "/home/a123/文档/mathpkg/pipeline_output/v7_test/staging/_GTM022_An_Algebraic_Introduction_to_Mathematical_Logic"

for dirname in sorted(os.listdir(BASE)):
    dirpath = os.path.join(BASE, dirname)
    if not os.path.isdir(dirpath):
        continue
    
    yaml_path = os.path.join(dirpath, 'concept.yaml')
    if not os.path.exists(yaml_path):
        continue
    
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    old_title = data.get('title_en', '')
    ctype = data.get('type', '')
    
    # Read theorem.tex to get better title
    tex_path = os.path.join(dirpath, 'theorem.tex')
    if os.path.exists(tex_path):
        with open(tex_path, 'r', encoding='utf-8') as f:
            tex = f.read()
        
        # Extract first meaningful line
        first_line = tex.split('\n')[0].strip()
        # Remove excessive spaces
        first_line = re.sub(r'\s+', ' ', first_line)
        
        # Try to extract a named theorem in parentheses
        name_match = re.match(r'\(([^)]+)\)\s*(.*)', first_line)
        if name_match:
            formal_name = name_match.group(1).strip()
            rest = name_match.group(2).strip()
            # Build clean title
            label = dirname.split('_')[2]  # e.g., "thm" or "def" or "lem"
            # Get label number from directory name
            label_num_match = re.search(r'(def|thm|lem|prop|cor)_(\d+_\d+)', dirname)
            if label_num_match:
                num = label_num_match.group(2).replace('_', '.')
                new_title = f"{formal_name}"
            else:
                new_title = f"{formal_name}"
        else:
            # Clean up LaTeX for readability
            clean = first_line
            # Keep LaTeX inline math but shorten
            clean = re.sub(r'\s+', ' ', clean)
            # Truncate
            if len(clean) > 120:
                clean = clean[:120] + '...'
            
            label_num_match = re.search(r'(def|thm|lem|prop|cor)_(\d+_\d+)', dirname)
            if label_num_match:
                num = label_num_match.group(2).replace('_', '.')
                new_title = f"{ctype.title()} {num}: {clean}"
            else:
                new_title = clean
        
        if new_title != old_title:
            data['title_en'] = new_title
            with open(yaml_path, 'w', encoding='utf-8') as f:
                yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
            print(f"Fixed: {dirname[:60]}... -> {new_title[:80]}")

print("Done fixing titles")
