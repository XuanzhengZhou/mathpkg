#!/bin/bash
# Simple robust proof generator for GTM020
# Uses find to avoid ARG_MAX issues

BASE="/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch2/gtm020"
SRC="/home/a123/文档/mathpkg/pipeline_output/stitched_sections/(GTM020)Fibre Bundles"

count=0; wrote=0; skip=0

# Process each concept directory using find with process substitution to avoid subshell
while IFS= read -r -d '' d; do
    yaml="$d/concept.yaml"
    [ ! -f "$yaml" ] && continue

    # Check if proof already exists
    if find "$d" -maxdepth 1 -name 'proof_*.md' -print0 2>/dev/null | grep -qz .; then
        skip=$((skip+1))
        continue
    fi

    # Get type
    ctype=$(grep '^type:' "$yaml" | head -1 | awk '{print $2}')
    case "$ctype" in
        theorem|proposition|lemma|corollary) ;;
        *) skip=$((skip+1)); continue ;;
    esac

    count=$((count+1))
    slug=$(grep '^id:' "$yaml" | head -1 | awk '{print $2}')
    title=$(grep '^title_en:' "$yaml" | head -1 | sed 's/title_en: *//' | tr -d '"'"'" | sed 's/^ *//;s/ *$//')
    ch=$(grep '^ *chapter:' "$yaml" | head -1 | sed 's/.*chapter: *//' | tr -d "'\"" | sed 's/^ *//;s/ *$//')
    sec=$(grep '^ *section:' "$yaml" | head -1 | sed 's/.*section: *//' | tr -d "'\"" | sed 's/^ *//;s/ *$//')

    # Try to extract chapter number from the chapter field
    ch_num=$(echo "$ch" | grep -oE '^[0-9]+' | head -1)

    # Find matching section file by searching for the title
    found=""
    for sf in "$SRC"/s*.md; do
        [ ! -f "$sf" ] && continue
        if grep -qF "$title" "$sf" 2>/dev/null; then
            found="$sf"
            break
        fi
    done

    if [ -z "$found" ]; then
        continue
    fi

    sf_base=$(basename "$found")

    # Get chapter.section from filename like sXXX_Ch.Sec_Type.md
    cs=$(echo "$sf_base" | grep -oP '_\K[0-9]+\.[0-9]+(?=_)' | head -1)
    [ -z "$cs" ] && cs="${ch_num}.${sec}"
    [ -z "$cs" ] && cs="${ch_num}"

    pf="proof_gtm020_${cs}.en.md"
    pfpath="$d$pf"

    # Extract proof: find the concept statement, take everything after "Proof."
    # More robust: find lines starting with "Proof." and extract
    proof_text=$(awk -v title="$title" '
        BEGIN { found=0; capture=0; }
        {
            if (!found) {
                if (index($0, title) > 0) { found=1; }
            } else if (!capture) {
                if ($0 ~ /^Proof\./ || $0 ~ /Proof\./) { capture=1; print $0; }
            } else {
                # Stop at next numbered concept or chapter boundary
                if ($0 ~ /^[0-9]+\.[0-9]+ (Definition|Proposition|Theorem|Corollary|Lemma)/) { exit; }
                if ($0 ~ /^CHAPTER [0-9]/) { exit; }
                if ($0 ~ /^Exercises/) { exit; }
                print;
            }
        }
    ' "$found" 2>/dev/null)

    if [ -z "$proof_text" ] || [ $(echo "$proof_text" | wc -l) -lt 2 ]; then
        # Try alternative: extract everything after the title line until next marker
        proof_text=$(awk -v title="$title" '
            BEGIN { found=0; }
            {
                if (!found) {
                    if (index($0, title) > 0) { found=1; next; }
                } else {
                    if ($0 ~ /^[0-9]+\.[0-9]+ (Definition|Proposition|Theorem|Corollary|Lemma)/) { exit; }
                    if ($0 ~ /^CHAPTER [0-9]/) { exit; }
                    if ($0 ~ /^Exercises/) { exit; }
                    if ($0 ~ /^$/) { print; next; }
                    print;
                }
            }
        ' "$found" 2>/dev/null | head -60)
    fi

    if [ -z "$proof_text" ] || [ $(echo "$proof_text" | wc -c) -lt 20 ]; then
        continue
    fi

    # Write proof file with YAML frontmatter
    cat > "$pfpath" << YEOF
---
role: proof
locale: en
of_concept: $slug
source_book: gtm020
source_chapter: "$ch"
source_section: "$sec"
---

$proof_text
YEOF

    wrote=$((wrote+1))
    if [ $((wrote % 25)) -eq 0 ]; then
        echo "  Progress: $wrote proofs written, $count processed..."
    fi
done < <(find "$BASE" -mindepth 1 -maxdepth 1 -type d -print0)

echo "=== SUMMARY: $wrote proofs written, $count processed, $skip skipped ==="
