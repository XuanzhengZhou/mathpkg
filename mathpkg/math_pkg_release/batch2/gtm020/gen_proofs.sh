#!/bin/bash
# Generates proof files for all GTM020 concepts by reading section files
# For each concept directory: find matching section file, extract proof, write proof_*.md

BASE="/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch2/gtm020"
SRC="/home/a123/文档/mathpkg/pipeline_output/stitched_sections/(GTM020)Fibre Bundles"

total=0; written=0; skipped=0; notfound=0

echo "=== GTM020 Proof Generator ==="
echo "Started at $(date)"
echo ""

for d in "$BASE"/*/; do
    [[ ! -d "$d" || "$d" == "$BASE"/*.md/ ]] && continue
    yaml="$d/concept.yaml"
    [[ ! -f "$yaml" ]] && continue

    # Skip if proof already exists
    if ls "$d"proof_gtm020_*.md >/dev/null 2>&1; then
        skipped=$((skipped+1))
        continue
    fi

    # Get type: only theorem/proposition/lemma/corollary need proofs
    ctype=$(grep '^type:' "$yaml" | head -1 | awk '{print $2}')
    case "$ctype" in
        theorem|proposition|lemma|corollary) ;;
        *) skipped=$((skipped+1)); continue ;;
    esac

    total=$((total+1))
    slug=$(grep '^id:' "$yaml" | head -1 | awk '{print $2}')
    title=$(grep '^title_en:' "$yaml" | head -1 | sed 's/title_en: *//' | tr -d '"'"'" | sed 's/^ *//;s/ *$//')
    ch=$(grep 'chapter:' "$yaml" | head -1 | sed 's/.*chapter: *//' | tr -d "'\"" | sed 's/^ *//;s/ *$//')
    sec=$(grep 'section:' "$yaml" | head -1 | sed 's/.*section: *//' | tr -d "'\"" | sed 's/^ *//;s/ *$//')
    ch_num=$(echo "$ch" | grep -oE '^[0-9]+' | head -1)

    # Read the theorem statement
    tex="$d/theorem.tex"
    [[ ! -f "$tex" ]] && { notfound=$((notfound+1)); continue; }

    stmt=$(cat "$tex")

    # Extract first 80 chars for filename matching
    stmt_short=$(echo "$stmt" | head -3 | tr '\n' ' ' | sed 's/  */ /g' | sed 's/\\//g' | cut -c1-80)

    # Search for matching section file
    found=""
    for sf in "$SRC"/s*.md; do
        # Try matching by title in the file
        if grep -qF "$title" "$sf" 2>/dev/null; then
            found="$sf"
            break
        fi
    done

    # If not found by title, try statement fragment
    if [[ -z "$found" ]]; then
        stmt_search=$(echo "$stmt_short" | cut -c1-50)
        for sf in "$SRC"/s*.md; do
            if grep -qF "$stmt_search" "$sf" 2>/dev/null; then
                found="$sf"
                break
            fi
        done
    fi

    if [[ -z "$found" ]]; then
        notfound=$((notfound+1))
        continue
    fi

    sf_base=$(basename "$found")

    # Determine chapter.section for proof filename
    # Try to extract from section filename: sXXX_Ch.Sec_Type.md
    file_ch_sec=$(echo "$sf_base" | grep -oP '_\K[0-9]+\.[0-9]+(?=_)' | head -1)
    if [[ -n "$file_ch_sec" ]]; then
        proof_ch_sec="$file_ch_sec"
    elif [[ -n "$ch_num" && -n "$sec" && "$sec" != "''" ]]; then
        proof_ch_sec="${ch_num}.${sec}"
    else
        proof_ch_sec="${ch_num}"
    fi

    proof_file="proof_gtm020_${proof_ch_sec}.en.md"

    # Extract proof text from section file
    # Strategy: Find the concept statement, then extract everything until next numbered concept or gap
    proof_text=""

    # Find line number where the statement text appears
    stmt_search_simple=$(echo "$stmt" | grep -v '^$$' | head -2 | tr '\n' ' ' | sed 's/  */ /g' | cut -c1-120)

    # Use awk to find content after the concept statement
    script='
    BEGIN { found=0; proof=""; in_proof=0; }
    {
        if (!found && $0 ~ /'"$stmt_short"'/) { found=1; next; }
        if (!found && $0 ~ /'"$title"'/) { found=1; next; }
        if (found) {
            if ($0 ~ /^[0-9]+\.[0-9]+ (Definition|Proposition|Theorem|Corollary|Lemma)/) { exit; }
            if ($0 ~ /^CHAPTER/) { exit; }
            if ($0 ~ /^Exercises/) { exit; }
            if ($0 ~ /Proof\./) { in_proof=1; }
            proof = proof $0 "\n";
        }
    }
    END { print proof; }
    '

    proof_text=$(awk "$script" "$found" 2>/dev/null | head -80)

    if [[ -z "$proof_text" || $(echo "$proof_text" | wc -c) -lt 10 ]]; then
        notfound=$((notfound+1))
        continue
    fi

    # Write the proof file
    cat > "$d$proof_file" << YAMLEOF
---
role: proof
locale: en
of_concept: $slug
source_book: gtm020
source_chapter: "$ch"
source_section: "$sec"
---

$proof_text
YAMLEOF

    echo "WROTE: $slug -> $proof_file (from $sf_base)"
    written=$((written+1))
done

echo ""
echo "=== DONE ==="
echo "Total concepts needing proof: $total"
echo "Proofs written: $written"
echo "Already have proof: $skipped"
echo "Not found/skipped: $notfound"
