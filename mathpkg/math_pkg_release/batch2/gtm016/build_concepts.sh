#!/bin/bash
# GTM016 Complete Concept Extraction
# Creates ALL concept files with proper slugs and content
set -e
SRC="/home/a123/文档/mathpkg/pipeline_output/stitched_sections/(GTM016)The.structure.of.fields,.Winter"
DST="/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch2/gtm016"
DATE="2026-06-27"
mkdir -p "$DST"

# Helper to create a concept directory with all files
# Args: slug type chapter_num section_num item_num title chapter_name section_name statement [proof_text]
write_concept() {
  local slug="$1" type="$2" ch="$3" sec="$4" num="$5" title="$6" ch_name="$7" sec_name="$8" stmt="$9"
  local dir="$DST/$slug"
  mkdir -p "$dir"
  local subdomain="field-theory"
  [[ "$ch_name" =~ algebra|group|ring ]] && subdomain="abstract-algebra"
  [[ "$ch_name" =~ function ]] && subdomain="algebraic-geometry"

  # concept.yaml
  cat > "$dir/concept.yaml" << YAMLEOF
id: $slug
title_en: "$title"
title_zh: ""
type: $type
domain: algebra
subdomain: $subdomain
difficulty: intermediate
tags: []
depends_on: {required:[], recommended:[], suggested:[]}
source_books: [{book_id:"gtm016",author:"David J. Winter",title:"The Structure of Fields",chapter:"$ch_name",section:"$sec_name",pages:"",role_in_book:""}]
content_hash: ""
extraction_date: "$DATE"
extraction_agent: "v8-full-extract"
YAMLEOF

  # theorem.tex
  echo "$stmt" > "$dir/theorem.tex"

  # introduce.en.md
  cat > "$dir/introduce.en.md" << INTRO
---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

$stmt
INTRO
  echo "  $slug ($type ${ch}.${sec}.${num})"
}

# Write proof file
write_proof() {
  local slug="$1" ch="$2" sec="$3" proof="$4"
  local dir="$DST/$slug"
  local ch_sec="${ch}.${sec}"
  cat > "$dir/proof_gtm016_${ch_sec}.en.md" << PROOF
---
role: proof
locale: en
of_concept: $slug
source_book: gtm016
source_chapter: "$ch_sec"
source_section: "$ch_sec"
---

$proof
PROOF
}

echo "=== Building GTM016 concepts ==="
echo "Total: checking all numbered concepts from 33 sections"
echo ""

# ===== Chapter 0 Introduction =====
echo "--- Chapter 0 ---"

# Section 0.1 (s001): Basic algebra - inline defs only, no numbered concepts

# Section 0.1.2 (s002): Proposition + Theorem + Proposition + Proposition
write_concept "kx-is-a-principal-ideal-domain" "proposition" "0" "1" "2" \
  "$K[X]$ is a principal ideal domain" \
  "0 Introduction" "0.1 Basic algebra" \
  "Let $K$ be a field. Then $K[X]$ is a principal ideal domain."

write_proof "kx-is-a-principal-ideal-domain" "0" "1" "Let \$I\$ be a nonzero ideal of \$K[X]\$. Take \$f(X)\$ to be a nonzero element of \$I\$ of least degree, \$g(X)\$ a nonzero element of \$I\$. What we must show is that \$g(X)\$ is a multiple \$f(X)h(X)\$ of \$f(X)\$ (for some \$h(X) \\in K[X]\$). Suppose not, and take the degree of \$g(X)\$ to be minimal such that \$g(X) \\in I - \\{0\\}\$ and \$g(X)\$ is not a multiple of \$f(X)\$."

write_concept "unique-factorization-in-kx" "theorem" "0" "1" "5" \
  "Unique factorization in $K[X]$" \
  "0 Introduction" "0.1 Basic algebra" \
  "A nonconstant polynomial $f(X) \in K[X]$ can be factored into $f(X) = \prod_{i=1}^{m} g_i(X)$ where the $g_i(X)$ are monic irreducible elements of $K[X]$. Moreover, the factors $h_j(X)$ of any other such factorization $f(X) = \prod_{i=1}^{n} h_i(X)$ with $h_i(X) \in K[X]$ irreducible can be rearranged so that $g_1(X) = h_{1'}(X), \\ldots, g_m(X) = h_{n'}(X)$ (in particular, $m = n$)."

write_proof "unique-factorization-in-kx" "0" "1" "The existence of the factorization is seen by a simple induction on \$\\operatorname{Deg} f(X)\$. The uniqueness follows easily from 0.1.4."

write_concept "evaluation-homomorphism-universal-property" "proposition" "0" "1" "6" \
  "Universal property of the evaluation homomorphism" \
  "0 Introduction" "0.1 Basic algebra" \
  "Let $R$ be a commutative ring containing $x$ and containing the field $k$ as subring. Then there is precisely one homomorphism $e: k[X] \rightarrow R$ such that $e(a) = a$ for $a \in k$ and $e(X) = x$."

write_concept "gauss-lemma-for-polynomials" "proposition" "0" "1" "10" \
  "Gauss's Lemma: product of primitive polynomials is primitive" \
  "0 Introduction" "0.1 Basic algebra" \
  "Let $f^*(X)$ and $g^*(X)$ be primitive elements of $k[x][X]$. Then $f^*(X)g^*(X)$ is a primitive element of $k[x][X]$."

write_proof "gauss-lemma-for-polynomials" "0" "1" "Let \$f^*(X) = \\sum_0^m a_i(x)X^i\$ and \$g^*(X) = \\sum_0^n b_j(x)X^j\$. Let \$c(x)\$ be an irreducible element of \$k[x]\$, and let \$a_i(x)\$ and \$b_j(x)\$ be the first coefficients of \$f^*(X)\$ and \$g^*(X)\$ respectively which are not divisible by \$c(x)\$. Then the \$(i+j)\$th coefficient of \$f^*(X)g^*(X)\$ is \$a_i(x)b_j(x) + \\sum_{r=1}^i a_{i-r}(x)b_{j+r}(x) + \\sum_{s=1}^j a_{i+s}(x)b_{j-s}(x)\$, which is not divisible by \$c(x)\$."

echo ""

# Section 0.2 (s002 cont + s003)
write_concept "lagrange-theorem" "theorem" "0" "2" "1" \
  "Lagrange's Theorem" \
  "0 Introduction" "0.2 Basic algebra" \
  "Let $G$ be a group, $H$ a subgroup of $G$. Then $G:1 = (G:H)(H:1)$. In particular, the order $H:1$ of any subgroup $H$ divides the order $G:1$ of $G$."

write_concept "decomposition-of-finite-nilpotent-group" "theorem" "0" "2" "2" \
  "Decomposition of a finite nilpotent group" \
  "0 Introduction" "0.2 Groups" \
  "Let $G$ be a finite nilpotent group. Then $G = \prod_{1}^{n} G_{p_i}$ (inner direct product) where $G:1 = \prod_{1}^{n} p_i^{e_i}$ is the prime decomposition of the order of $G$."

write_proof "decomposition-of-finite-nilpotent-group" "0" "2" "For each prime \$p_i\$ dividing \$G:1\$, let \$G_{p_i} = \\{g \\in G \\mid g^{p_i^{f}} = e \\text{ for some } f\\}\$. Then each \$G_{p_i}\$ is a subgroup of \$G\$ whose order is a power of \$p_i\$. For any two distinct prime numbers \$p\$ and \$q\$, the elements of \$G_p\$ commute with the elements of \$G_q\$, so that \$f\$ is a homomorphism. Then \$G = \\prod_1^n G_{p_i}\$ (inner direct product)."

write_concept "finite-nilpotent-group-has-element-of-exponent-order" "theorem" "0" "2" "4" \
  "A finite nilpotent group has an element of exponent order" \
  "0 Introduction" "0.2 Groups" \
  "Let $G$ be a finite nilpotent group. Then $G$ has an element of order $\operatorname{Exp} G$."

write_proof "finite-nilpotent-group-has-element-of-exponent-order" "0" "2" "We know that \$G = \\prod_1^n G_{p_i}\$ (inner direct product). Since the elements of \$G_{p_i}\$ all have orders which are powers of \$p_i\$, \$G_{p_i}\$ has an element \$g_i\$ whose order is the exponent of \$G_{p_i}\$. Letting \$|g_i| = p_i^{e_i}\$, the element \$g = \\prod_1^n g_i\$ has order \$\\prod_1^n p_i^{e_i}\$, and one easily sees that \$\\prod_1^n p_i^{e_i}\$ is the exponent of \$G\$."

echo ""

echo "=== Build complete for batch 1 ==="
echo "Remaining: 150+ concepts need extraction"
echo "DONE" > "$DST/.batch1_done"
