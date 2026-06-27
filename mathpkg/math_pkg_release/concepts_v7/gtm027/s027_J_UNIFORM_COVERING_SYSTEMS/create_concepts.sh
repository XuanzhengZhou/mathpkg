#!/bin/bash
BASE="/home/a123/文档/mathpkg/pipeline_output/concepts_v7/gtm027/s027_J_UNIFORM_COVERING_SYSTEMS"
set -e

write_yaml() {
  local dir="$1" id="$2" title="$3" type="$4" dom="$5" sub="$6" diff="$7" tags="$8" req="$9" rec="${10}" sug="${11}" ch="${12}" sec="${13}" role="${14}"
  cat > "$BASE/$dir/concept.yaml" << YEOF
id: $id
title_en: "$title"
title_zh: ""
type: $type
domain: $dom
subdomain: $sub
difficulty: $diff
tags: [$tags]
depends_on:
  required: [$req]
  recommended: [$rec]
  suggested: [$sug]
source_books:
  - book_id: "gtm027"
    author: "John L. Kelley"
    title: "General Topology"
    chapter: "$ch"
    section: "$sec"
    pages: ""
    role_in_book: "$role"
content_hash: ""
extraction_date: "2026-06-25"
extraction_agent: "v7-section-test"
YEOF
}

write_intro() {
  local dir="$1" text="$2"
  cat > "$BASE/$dir/introduce.en.md" << IEOF
---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

$text
IEOF
}

# ============================================================
# SECTION J: UNIFORM COVERING SYSTEMS
# ============================================================

# 1. uniform-covering-system
write_yaml "uniform-covering-system" \
  "uniform-covering-system" \
  "Uniformity Defined by a Covering System" \
  "definition" "topology" "uniform-spaces" "intermediate" \
  '"uniformity", "covering", "star-refinement", "uniform-cover"' \
  "" '"uniformity", "refinement", "star-refinement"' "" \
  "6" "J" "Problem: definition of uniformity via covering systems"

cat > "$BASE/uniform-covering-system/theorem.tex" << 'EOF'
Let $\Phi$ be a collection of covers of a set $X$ such that:
\begin{enumerate}
\item[(i)] if $\alpha$ and $\beta$ are members of $\Phi$, then there is a member of $\Phi$ which is a refinement of both $\alpha$ and $\beta$;
\item[(ii)] if $\alpha \in \Phi$, then there is a member of $\Phi$ which is a star refinement of $\alpha$;
\item[(iii)] if $\alpha$ is a cover of $X$ and some refinement of $\alpha$ belongs to $\Phi$, then $\alpha$ belongs to $\Phi$.
\end{enumerate}
Let $\mathcal{U}$ be the uniformity for $X$ such that the family of all sets of the form $\bigcup \{A \times A : A \in \alpha\}$ for $\alpha$ in $\Phi$ is a base for $\mathcal{U}$. Then $\Phi$ is precisely the family of all covers of $X$ which are uniform relative to $\mathcal{U}$.
EOF

write_intro "uniform-covering-system" \
  "A uniformity on a set $X$ can be defined equivalently in terms of coverings rather than entourages. A collection $\Phi$ of covers satisfying three axioms—pairwise refinement, star refinement, and upward closure under refinement—defines a uniformity $\mathcal{U}$ via the diagonal neighborhoods $\bigcup\{A \times A : A \in \alpha\}$. Conversely, $\Phi$ recovers exactly the family of all uniform covers relative to $\mathcal{U}$. This covering approach was pioneered by Tukey and earlier by Alexandroff and Urysohn."

# ============================================================
# SECTION K: TOPOLOGICALLY COMPLETE SPACES: METRIZABLE SPACES
# ============================================================

# 2. metrically-topologically-complete
write_yaml "metrically-topologically-complete" \
  "metrically-topologically-complete" \
  "Metrically Topologically Complete Space" \
  "definition" "topology" "metric-spaces" "intermediate" \
  '"metric-completeness", "topological-completeness", "metrizable"' \
  "" '"complete-metric-space", "metric-topology"' "" \
  "6" "K" "Problem: definition of metric topological completeness"

cat > "$BASE/metrically-topologically-complete/theorem.tex" << 'EOF'
A topological space $(X, \mathcal{J})$ is called \text{metrically topologically complete} iff there is a metric $d$ for $X$ such that $(X, d)$ is complete and $\mathcal{J}$ is the metric topology.
EOF

write_intro "metrically-topologically-complete" \
  "A metrically topologically complete space is a topological space that admits at least one complete metric compatible with its topology. This is stronger than mere metrizability: the space must be homeomorphic to a complete metric space. The notion separates topological properties from the particular choice of metric and plays a key role in characterizing absolute $G_\delta$ spaces."

# 3. absolute-g-delta-space
write_yaml "absolute-g-delta-space" \
  "absolute-g-delta-space" \
  "Absolute G-delta Space" \
  "definition" "topology" "metric-spaces" "intermediate" \
  '"absolute-G-delta", "metrizable", "G-delta-set", "topological-embedding"' \
  "" '"G-delta-set", "metric-space", "topological-embedding"' "" \
  "6" "K" "Problem: definition of absolute G-delta"

cat > "$BASE/absolute-g-delta-space/theorem.tex" << 'EOF'
A topological space $(X, \mathcal{J})$ is an \text{absolute $G_{\delta}$} iff it is metrizable and is a $G_{\delta}$ (a countable intersection of open sets) in every metric space in which it is topologically embedded.
EOF

write_intro "absolute-g-delta-space" \
  "An absolute $G_\delta$ space is a metrizable space that, whenever embedded in any metric space, appears as a countable intersection of open subsets. This property characterizes precisely those metrizable spaces that are metrically topologically complete. The equivalence between metric topological completeness and being an absolute $G_\delta$ is a classical result due to Alexandroff and Hausdorff."

# ============================================================
# SECTION L: TOPOLOGICALLY COMPLETE SPACES: UNIFORMIZABLE SPACES
# ============================================================

# 4. topologically-complete-uniformizable
write_yaml "topologically-complete-uniformizable" \
  "topologically-complete-uniformizable" \
  "Topologically Complete Space (Uniform Version)" \
  "definition" "topology" "uniform-spaces" "intermediate" \
  '"topological-completeness", "uniformity", "uniform-topology"' \
  "" '"uniform-space", "complete-uniform-space"' "" \
  "6" "L" "Problem: definition of topological completeness for uniformizable spaces"

cat > "$BASE/topologically-complete-uniformizable/theorem.tex" << 'EOF'
A topological space $(X, \mathfrak{J})$ is said to be \text{topologically complete} iff there is a uniformity $\mathfrak{U}$ for $X$ such that $(X, \mathfrak{U})$ is complete and $\mathfrak{J}$ is the uniform topology.
EOF

write_intro "topologically-complete-uniformizable" \
  "For uniformizable (completely regular) spaces, topological completeness generalizes metric topological completeness. A space is topologically complete if it admits some complete uniformity compatible with its topology. This definition does not require metrizability and applies to all completely regular spaces, with the largest compatible uniformity playing a distinguished role."

# 5. completeness-under-coarser-uniformity
write_yaml "completeness-under-coarser-uniformity" \
  "completeness-under-coarser-uniformity" \
  "Completeness Inheritance Under Coarser Uniformities" \
  "theorem" "topology" "uniform-spaces" "intermediate" \
  '"completeness", "uniformity", "coarser-uniformity"' \
  "" '"uniform-space", "complete-uniform-space"' "" \
  "6" "L" "Problem L(a): completeness and coarser uniformities"

cat > "$BASE/completeness-under-coarser-uniformity/theorem.tex" << 'EOF'
If $\mathfrak{U}$ and $\mathfrak{V}$ are uniformities for $X$ such that $\mathfrak{U} \subset \mathfrak{V}$, if $(X, \mathfrak{V})$ is complete, and if the topology of $\mathfrak{U}$ is identical with that of $\mathfrak{V}$, then $(X, \mathfrak{U})$ is complete.
EOF

write_intro "completeness-under-coarser-uniformity" \
  "This theorem establishes that completeness is preserved when passing to a coarser uniformity, provided both uniformities induce the same topology. It is a crucial technical result: if a space is complete under a finer uniformity, it remains complete under any coarser uniformity with the same topology. This property is used to characterize topological completeness for completely regular spaces."

# 6. characterization-of-topologically-complete
write_yaml "characterization-of-topologically-complete" \
  "characterization-of-topologically-complete" \
  "Characterization of Topologically Complete Completely Regular Spaces" \
  "corollary" "topology" "uniform-spaces" "intermediate" \
  '"topological-completeness", "completely-regular", "largest-uniformity"' \
  "" '"completely-regular-space", "complete-uniform-space"' "" \
  "6" "L" "Problem L(a) corollary: characterization of topologically complete spaces"

cat > "$BASE/characterization-of-topologically-complete/theorem.tex" << 'EOF'
A completely regular space is topologically complete iff it is complete relative to the largest uniformity whose topology is $\mathfrak{J}$.
EOF

write_intro "characterization-of-topologically-complete" \
  "This corollary gives a practical criterion: to check topological completeness of a completely regular space, one need only verify completeness with respect to the largest (finest) uniformity compatible with the topology. If the space is complete under that maximal uniformity, it is topologically complete; the converse follows from the inheritance theorem under coarser uniformities."

# 7. separation-of-f-sigma-set-in-complete-uniform-space
write_yaml "separation-of-f-sigma-set-in-complete-uniform-space" \
  "separation-of-f-sigma-set-in-complete-uniform-space" \
  "Separation of F-sigma Sets in Complete Uniform Spaces" \
  "theorem" "topology" "uniform-spaces" "intermediate" \
  '"F-sigma", "complete-uniform-space", "continuous-function", "separation"' \
  "" '"uniform-space", "F-sigma-set", "continuous-real-function"' "" \
  "6" "L" "Problem L(b): separation of F-sigma sets"

cat > "$BASE/separation-of-f-sigma-set-in-complete-uniform-space/theorem.tex" << 'EOF'
Let $(X, \mathfrak{U})$ be a complete uniform space, let $F$ be an $F_{\sigma}$ (a countable union of closed sets) and let $x \in X \sim F$. Then there is a continuous real-valued function on $X$ which is positive on $F$ and $0$ at $x$.
EOF

write_intro "separation-of-f-sigma-set-in-complete-uniform-space" \
  "In a complete uniform space, $F_\sigma$ sets can be separated from points outside them by continuous real-valued functions. Specifically, given an $F_\sigma$ set $F$ and a point $x$ not in $F$, there exists a continuous function that is strictly positive on $F$ and zero at $x$. This result relies on the device used earlier in the chapter (6.K(a)) and has consequences for the existence of complete uniform subspaces."

# 8. existence-of-complete-open-set-containing-f-sigma
write_yaml "existence-of-complete-open-set-containing-f-sigma" \
  "existence-of-complete-open-set-containing-f-sigma" \
  "Existence of Complete Open Set Containing an F-sigma Set" \
  "corollary" "topology" "uniform-spaces" "intermediate" \
  '"complete-uniform-space", "F-sigma", "open-set"' \
  "" '"uniform-space", "F-sigma-set"' "" \
  "6" "L" "Problem L(b) corollary: existence of complete open set"

cat > "$BASE/existence-of-complete-open-set-containing-f-sigma/theorem.tex" << 'EOF'
Consequently there is an open set $V$ and a uniformity $\mathfrak{V}$ for $V$ such that $V$ contains $F$, $x \notin V$, $(V, \mathfrak{V})$ is complete, and the topology of $\mathfrak{V}$ is identical with the relativized topology of $\mathfrak{U}$.
EOF

write_intro "existence-of-complete-open-set-containing-f-sigma" \
  "As a consequence of the separation theorem for $F_\sigma$ sets, one can find an open set $V$ that contains the $F_\sigma$ set $F$ but excludes the point $x$, and moreover $V$ admits a complete uniformity compatible with the relative topology. This construction is important for localizing completeness properties within open subspaces of a complete uniform space."

# ============================================================
# SECTION M: THE DISCRETE SUBSPACE ARGUMENT; COUNTABLE COMPACTNESS
# ============================================================

# 9. uniformly-discrete-from-non-totally-bounded
write_yaml "uniformly-discrete-from-non-totally-bounded" \
  "uniformly-discrete-from-non-totally-bounded" \
  "Uniformly Discrete Subsets from Non-Totally Bounded Sets" \
  "theorem" "topology" "uniform-spaces" "intermediate" \
  '"totally-bounded", "uniformly-discrete", "pseudo-metric", "uniform-space"' \
  "" '"totally-bounded-set", "uniform-space", "pseudo-metric"' "" \
  "6" "M" "Problem M(a): discrete subspace argument"

cat > "$BASE/uniformly-discrete-from-non-totally-bounded/theorem.tex" << 'EOF'
If a subset $A$ of a uniform space $(X, \mathfrak{U})$ is not totally bounded, then there is a member $U$ of $\mathfrak{U}$ and an infinite subset $B$ of $A$ such that $U[x]$ is disjoint from $U[y]$ for every pair of distinct points of $B$; equivalently, there is a pseudo-metric $d$ in the gage of $\mathfrak{U}$ such that $d(x, y) \geq 1$ for distinct points $x$ and $y$ of $B$. (A set such as $B$ might be called uniformly discrete.)
EOF

write_intro "uniformly-discrete-from-non-totally-bounded" \
  "If a subset of a uniform space fails to be totally bounded, one can extract an infinite uniformly discrete subset—points separated by a uniform entourage or, equivalently, at pseudo-metric distance at least 1. This 'discrete subspace argument' is a fundamental tool in uniform space theory, linking total boundedness to the absence of uniformly separated infinite subsets."

# 10. relatively-countably-compact
write_yaml "relatively-countably-compact" \
  "relatively-countably-compact" \
  "Relatively Countably Compact Subset" \
  "definition" "topology" "general-topology" "basic" \
  '"countably-compact", "cluster-point", "relative-compactness"' \
  "" '"compactness", "sequence", "cluster-point"' "" \
  "6" "M" "Problem M(b): definition of relatively countably compact"

cat > "$BASE/relatively-countably-compact/theorem.tex" << 'EOF'
A subset $A$ of a topological space $(X, \mathfrak{J})$ is called \text{relatively countably compact} iff each sequence in $A$ has a cluster point in $X$.
EOF

write_intro "relatively-countably-compact" \
  "A subset $A$ is relatively countably compact if every sequence in $A$ admits a cluster point somewhere in the ambient space $X$. This is a sequential compactness notion that is weaker than relative compactness (cluster points need not lie in $A$) but still imposes significant restrictions on the set, particularly in completely regular spaces where it forces total boundedness."

# 11. relatively-countably-compact-implies-totally-bounded
write_yaml "relatively-countably-compact-implies-totally-bounded" \
  "relatively-countably-compact-implies-totally-bounded" \
  "Relatively Countably Compact Implies Totally Bounded" \
  "theorem" "topology" "uniform-spaces" "intermediate" \
  '"relatively-countably-compact", "totally-bounded", "completely-regular"' \
  "" '"relatively-countably-compact", "totally-bounded", "completely-regular-space"' "" \
  "6" "M" "Problem M(b): relatively countably compact subsets are totally bounded"

cat > "$BASE/relatively-countably-compact-implies-totally-bounded/theorem.tex" << 'EOF'
Each relatively countably compact subset of a completely regular space $(X, \mathfrak{J})$ is totally bounded relative to the largest uniformity whose topology is $\mathfrak{J}$.
EOF

write_intro "relatively-countably-compact-implies-totally-bounded" \
  "In a completely regular space, every relatively countably compact subset must be totally bounded with respect to the finest compatible uniformity. This theorem connects sequential compactness notions to uniform space structure and is a key step in understanding the relationship between various compactness concepts in uniformizable spaces."

# ============================================================
# SECTION O: TOPOLOGICAL GROUPS: UNIFORMITIES AND METRIZATION
# ============================================================

# 12. left-right-two-sided-uniformities-topological-group
write_yaml "left-right-two-sided-uniformities-topological-group" \
  "left-right-two-sided-uniformities-topological-group" \
  "Left, Right, and Two-Sided Uniformities of a Topological Group" \
  "definition" "topology" "topological-groups" "intermediate" \
  '"topological-group", "left-uniformity", "right-uniformity", "two-sided-uniformity"' \
  "" '"topological-group", "uniformity"' "" \
  "6" "O" "Problem O: definition of left, right, and two-sided uniformities"

cat > "$BASE/left-right-two-sided-uniformities-topological-group/theorem.tex" << 'EOF'
Let $(G, \mathcal{J})$ be a topological group, and for each neighborhood $U$ of the identity let $U_L = \{(x, y) : x^{-1}y \in U\}$ and let $U_R = \{(x, y) : xy^{-1} \in U\}$. Consider the following uniformities for $G$: the \text{left uniformity} $\mathcal{L}$ having as a base the family of all sets $U_L$ with $U$ a neighborhood of the identity, the \text{right uniformity} $\mathcal{R}$ with all $U_R$ as a base, and the \text{two-sided uniformity} $\mathcal{U}$ having $\mathcal{L} \cup \mathcal{R}$ as a subbase.
EOF

write_intro "left-right-two-sided-uniformities-topological-group" \
  "Every topological group carries three natural uniformities. The left uniformity is generated by entourages $U_L = \{(x,y): x^{-1}y \in U\}$; the right uniformity uses $U_R = \{(x,y): xy^{-1} \in U\}$; and the two-sided uniformity is the supremum of both. These uniformities encode the uniform structure of the group operations and are essential for studying completeness and completion of topological groups."

# 13. topology-of-group-uniformities
write_yaml "topology-of-group-uniformities" \
  "topology-of-group-uniformities" \
  "The Topology of a Topological Group Coincides with Its Uniform Topologies" \
  "theorem" "topology" "topological-groups" "basic" \
  '"topological-group", "left-uniformity", "right-uniformity", "uniform-topology"' \
  "" '"topological-group", "uniformity", "uniform-topology"' "" \
  "6" "O" "Problem O(a): the topology is the uniform topology"

cat > "$BASE/topology-of-group-uniformities/theorem.tex" << 'EOF'
The topology $\mathcal{J}$ is the topology of each of $\mathcal{L}$, $\mathcal{R}$, and $\mathcal{U}$.
EOF

write_intro "topology-of-group-uniformities" \
  "For any topological group, the left, right, and two-sided uniformities all induce the original group topology. This fundamental fact ensures that the uniform structure is compatible with the given topology and allows one to freely use uniform concepts (completeness, total boundedness, uniform continuity) when studying topological groups."

# 14. generation-by-invariant-pseudometrics
write_yaml "generation-by-invariant-pseudometrics" \
  "generation-by-invariant-pseudometrics" \
  "Generation of Group Uniformities by Invariant Pseudo-Metrics" \
  "theorem" "topology" "topological-groups" "intermediate" \
  '"left-invariant", "right-invariant", "pseudo-metric", "uniformity"' \
  "" '"topological-group", "pseudo-metric", "uniformity"' "" \
  "6" "O" "Problem O(b): generation by invariant pseudo-metrics"

cat > "$BASE/generation-by-invariant-pseudometrics/theorem.tex" << 'EOF'
The uniformity $\mathcal{L}$ (respectively $\mathcal{R}$) is generated by the family of all left-invariant (right-invariant) pseudo-metrics which are continuous on $G \times G$.
EOF

write_intro "generation-by-invariant-pseudometrics" \
  "The left uniformity of a topological group is precisely the uniformity generated by all continuous left-invariant pseudo-metrics; similarly, the right uniformity comes from continuous right-invariant pseudo-metrics. This provides a concrete description of the uniform structure in terms of invariant distance-like functions and is essential for metrization theory of topological groups."

# 15. invariant-neighborhoods-characterization
write_yaml "invariant-neighborhoods-characterization" \
  "invariant-neighborhoods-characterization" \
  "Characterization of Groups with Invariant Neighborhood Bases" \
  "theorem" "topology" "topological-groups" "advanced" \
  '"invariant-neighborhood", "inner-automorphism", "two-sided-invariant", "pseudo-metric"' \
  "" '"topological-group", "inner-automorphism", "pseudo-metric"' "" \
  "6" "O" "Problem O(c): invariant neighborhoods characterization"

cat > "$BASE/invariant-neighborhoods-characterization/theorem.tex" << 'EOF'
Let $I$ be the family of all neighborhoods of the identity $e$ which are invariant under inner automorphisms. Then $I$ is a base for the neighborhood system of $e$ iff the family of all pseudo-metrics which are both left and right invariant and are continuous on $G \times G$ generates a uniformity whose topology is $\mathcal{J}$.
EOF

write_intro "invariant-neighborhoods-characterization" \
  "A topological group admits a base of inner-automorphism-invariant identity neighborhoods precisely when its topology can be generated by two-sided invariant continuous pseudo-metrics. This condition characterizes groups that are 'balanced' in the sense that their left and right uniform structures coincide, an important property for the theory of group completions and for topological groups that are also topological vector spaces."

# 16. affine-group-topology
write_yaml "affine-group-topology" \
  "affine-group-topology" \
  "The Affine Group as a Topological Group" \
  "definition" "topology" "topological-groups" "basic" \
  '"affine-group", "topological-group", "example"' \
  "" '"topological-group", "affine-transformation"' "" \
  "6" "O" "Problem O(d): the affine group example"

cat > "$BASE/affine-group-topology/theorem.tex" << 'EOF'
Let $G$ be the set of all real-valued functions of the form $g(x) = ax + b$ where $a \neq 0$. Then $G$ is a group under composition and may be topologized by agreeing that $g$ is near the identity iff $a$ is near $1$ and $|b|$ is near zero.
EOF

write_intro "affine-group-topology" \
  "The affine group $G = \{x \mapsto ax + b : a \neq 0\}$ of the real line, under composition, becomes a topological group when topologized by proximity of the parameters $(a,b)$ to $(1,0)$. This concrete example illustrates the natural topological group structure on a familiar transformation group and serves as a test case for the properties of left, right, and two-sided uniformities."

echo "=== BATCH 1 (concepts 1-16) COMPLETE ==="
