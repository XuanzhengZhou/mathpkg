#!/bin/bash
# Batch process: for each concept directory, find matching section and create proof file
# Only processes theorem/proposition/lemma/corollary concepts (not definitions)

set -e

BASE="/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch2/gtm020"
SECTIONS_DIR="/home/a123/文档/mathpkg/pipeline_output/stitched_sections/(GTM020)Fibre Bundles"

count=0
skipped=0
written=0

for d in "$BASE"/*/; do
    yaml="$d/concept.yaml"
    [ ! -f "$yaml" ] && continue

    # Check if proof already exists
    proof_count=$(ls "$d"proof_*.md 2>/dev/null | wc -l)
    if [ "$proof_count" -gt 0 ]; then
        skipped=$((skipped+1))
        continue
    fi

    # Get type: only process theorem/proposition/lemma/corollary
    type=$(grep '^type:' "$yaml" | head -1 | awk '{print $2}')
    case "$type" in
        theorem|proposition|lemma|corollary) ;;
        *) skipped=$((skipped+1)); continue ;;
    esac

    # Get metadata
    slug=$(grep '^id:' "$yaml" | head -1 | awk '{print $2}')
    ch=$(grep 'chapter:' "$yaml" | head -1 | sed 's/.*chapter: *//' | tr -d "'" | sed 's/^ *//;s/ *$//')
    sec=$(grep 'section:' "$yaml" | head -1 | sed 's/.*section: *//' | tr -d "'" | sed 's/^ *//;s/ *$//')
    title_en=$(grep 'title_en:' "$yaml" | head -1 | sed 's/.*title_en: *//' | tr -d '"')

    # Extract chapter number
    ch_num=$(echo "$ch" | grep -oE '^[0-9]+' | head -1)
    [ -z "$ch_num" ] && ch_num=$(echo "$ch" | grep -oP '\d+' | head -1)

    echo "[$count] Processing: $slug (Ch.$ch_num Sec.$sec, $type)"
    count=$((count+1))

    # Read the theorem statement from theorem.tex
    tex_file="$d/theorem.tex"
    [ ! -f "$tex_file" ] && { echo "  No theorem.tex, skipping"; skipped=$((skipped+1)); continue; }

    # Get the first line of the statement for matching
    stmt_first=$(head -3 "$tex_file" | tr '\n' ' ' | sed 's/  */ /g' | cut -c1-120 | sed 's/[][\*^$]/\\&/g')

    # Search for the concept in section files
    # Strategy: search for the section label pattern
    found_file=""

    # Try to find matching section file
    for sf in "$SECTIONS_DIR"/s*.md; do
        fname=$(basename "$sf")
        # Match by chapter+section pattern in filename
        if echo "$fname" | grep -qE "^s[0-9]+_${ch_num}\.${sec}_"; then
            found_file="$sf"
            break
        fi
        # Also try matching just the section number
        if echo "$fname" | grep -qE "^s[0-9]+_${ch_num}\."; then
            # Check if this section file contains our concept
            if grep -qF "$title_en" "$sf" 2>/dev/null; then
                found_file="$sf"
                break
            fi
        fi
    done

    # If not found by filename, search by content
    if [ -z "$found_file" ]; then
        for sf in "$SECTIONS_DIR"/s*.md; do
            if grep -qF "$title_en" "$sf" 2>/dev/null; then
                found_file="$sf"
                break
            fi
        done
    fi

    if [ -z "$found_file" ]; then
        echo "  WARNING: No section file found for $slug"
        skipped=$((skipped+1))
        continue
    fi

    echo "  Found in: $(basename "$found_file")"

    # Extract chapter number from section filename for the proof filename
    proof_ch=$(basename "$found_file" | grep -oE '^s[0-9]+_([0-9]+)' | sed 's/^s[0-9]*_//')
    [ -z "$proof_ch" ] && proof_ch="$ch_num"
    proof_sec=$(basename "$found_file" | grep -oE '_([0-9]+\.[0-9]+)_' | tr -d '_' | head -1)
    [ -z "$proof_sec" ] && proof_sec="$sec"

    # Determine section number for the proof filename
    # Format: proof_gtm020_Ch.Sec.en.md
    if [ -n "$proof_sec" ] && [ "$proof_sec" != "''" ]; then
        proof_file="proof_gtm020_${proof_ch}.${proof_sec}.en.md"
    elif [ -n "$sec" ] && [ "$sec" != "''" ]; then
        proof_file="proof_gtm020_${ch_num}.${sec}.en.md"
    else
        proof_file="proof_gtm020_${ch_num}.en.md"
    fi

    echo "  Proof file: $proof_file"
    echo "  Chapter: $ch, Section: $sec"

    # Mark that we processed this
    written=$((written+1))
done

echo ""
echo "=== SUMMARY ==="
echo "Total processed: $count"
echo "Written: $written"
echo "Skipped: $skipped"
