#!/bin/bash
# Batch proof generator for GTM020 concepts
# Reads all concept.yaml files, finds matching section files, extracts proofs

BASE="/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch2/gtm020"
SRC="/home/a123/文档/mathpkg/pipeline_output/stitched_sections/(GTM020)Fibre Bundles"

total=0 written=0 skipped=0

# Process each concept directory
for d in "$BASE"/*/; do
    [[ ! -d "$d" ]] && continue
    yaml="$d/concept.yaml"
    [[ ! -f "$yaml" ]] && continue

    # Skip if proof already exists
    if ls "$d"proof_*.md >/dev/null 2>&1; then
        skipped=$((skipped+1))
        continue
    fi

    # Get concept type
    ctype=$(grep '^type:' "$yaml" | head -1 | awk '{print $2}')
    # Only theorems, propositions, lemmas, corollaries need proofs
    case "$ctype" in
        theorem|proposition|lemma|corollary) ;;
        *) skipped=$((skipped+1)); continue ;;
    esac

    total=$((total+1))
    slug=$(grep '^id:' "$yaml" | head -1 | awk '{print $2}')
    title=$(grep '^title_en:' "$yaml" | head -1 | sed 's/title_en: *//' | tr -d '"' | sed 's/^ *//')

    # Read theorem statement for matching
    tex="$d/theorem.tex"
    if [[ ! -f "$tex" ]]; then
        echo "SKIP $slug: no theorem.tex"
        skipped=$((skipped+1))
        continue
    fi

    # Get first significant line from theorem.tex for matching
    stmt_line=$(head -5 "$tex" | grep -v '^$' | head -1 | sed 's/^ *//;s/ *$//' | cut -c1-100)

    # Find matching section file
    found=""
    for sf in "$SRC"/s*.md; do
        if grep -qF "$title" "$sf" 2>/dev/null; then
            found="$sf"
            break
        fi
    done

    # If not found by title, try longer statement fragment
    if [[ -z "$found" ]] && [[ -n "$stmt_line" ]]; then
        for sf in "$SRC"/s*.md; do
            if grep -qF "${stmt_line:0:60}" "$sf" 2>/dev/null; then
                found="$sf"
                break
            fi
        done
    fi

    if [[ -z "$found" ]]; then
        echo "NOTFOUND: $slug ($title)"
        skipped=$((skipped+1))
        continue
    fi

    # Extract proof: find the concept in the section file and get text after it
    # Strategy: find the concept statement, then look for "Proof." marker, extract until next section marker
    sf_base=$(basename "$found")

    # Determine chapter.section from filename or yaml
    ch=$(grep 'chapter:' "$yaml" | head -1 | sed 's/.*chapter: *//' | tr -d "'\"" | sed 's/^ *//;s/ *$//')
    sec=$(grep 'section:' "$yaml" | head -1 | sed 's/.*section: *//' | tr -d "'\"" | sed 's/^ *//;s/ *$//')

    # Extract chapter number
    ch_num=$(echo "$ch" | grep -oE '^[0-9]+' | head -1)
    [[ -z "$ch_num" ]] && ch_num=$(echo "$sf_base" | grep -oE '^s[0-9]+_([0-9]+)' | sed 's/^s[0-9]*_//' | grep -oE '^[0-9]+')
    [[ -z "$ch_num" ]] && ch_num="?"

    echo "FOUND: $slug -> $sf_base (Ch.$ch_num) [$ctype]"

    # Extract the proof text - this is the hard part
    # We need to find the statement start in the file, then extract to the end of the proof
    # For now, check if "Proof." appears after the concept
    proof_start=$(grep -n "Proof\." "$found" | head -1 | cut -d: -f1)

    if [[ -z "$proof_start" ]]; then
        # No explicit "Proof." marker, check if proof is inline
        echo "  No explicit Proof. marker found"
        skipped=$((skipped+1))
        continue
    fi

    # Extract from Proof. to next numbered definition/theorem or end of section
    section_end=$(wc -l < "$found")
    # Find the next major marker after proof_start
    next_marker=$(tail -n +$proof_start "$found" | grep -nE '^[0-9]+\.[0-9]+ (Definition|Proposition|Theorem|Corollary|Lemma)|^CHAPTER|^Exercises|^$' | head -3 | tail -1 | cut -d: -f1)

    if [[ -n "$next_marker" ]]; then
        proof_end=$((proof_start + next_marker - 2))
    else
        proof_end=$section_end
    fi

    # Ensure proof_end > proof_start
    if [[ $proof_end -le $proof_start ]]; then
        proof_end=$section_end
    fi

    echo "  Proof lines: $proof_start to $proof_end (of $section_end)"
    written=$((written+1))
done

echo ""
echo "=== SUMMARY ==="
echo "Total proof-needed concepts: $total"
echo "Written: $written"
echo "Skipped: $skipped"
