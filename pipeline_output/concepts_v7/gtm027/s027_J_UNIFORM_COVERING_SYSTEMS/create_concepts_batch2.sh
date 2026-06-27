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
# SECTION P (Almost Open Sets)
# ============================================================

# 17. almost-open-set
write_yaml "almost-open-set" \
  "almost-open-set" \
  "Almost Open Set" \
  "definition" "topology" "topological-groups" "advanced" \
  '"almost-open", "meager", "Baire-category"' \
  "" '"meager-set", "Baire-category", "topological-group"' "" \
  "6" "P" "Problem P: definition of almost open sets"

cat > "$BASE/almost-open-set/theorem.tex" << 'EOF'
A subset $A$ is \text{almost open} in $X$ iff there are meager sets $B$ and $C$ such that $(A \sim B) \cup C$ is open.
EOF

write_intro "almost-open-set" \
  "A set is almost open if it differs from an open set by a meager set—specifically, it can be made open by removing a meager set and then adding another meager set. This is a Baire category refinement of the notion of openness. Almost open sets form a $\sigma$-algebra containing all Borel sets, making them a crucial bridge between topology and measure-theoretic (category) considerations in topological groups."

# 18. properties-of-almost-open-sets
write_yaml "properties-of-almost-open-sets" \
  "properties-of-almost-open-sets" \
  "Closure Properties of Almost Open Sets" \
  "theorem" "topology" "topological-groups" "advanced" \
  '"almost-open", "Borel-set", "sigma-algebra", "Baire-category"' \
  "" '"almost-open-set", "Borel-set", "meager-set"' "" \
  "6" "P" "Problem P(a): properties of almost open sets"

cat > "$BASE/properties-of-almost-open-sets/theorem.tex" << 'EOF'
Countable unions and complements of almost open sets are almost open. Every Borel set is almost open.
(The family of Borel sets is the smallest family $\mathcal{B}$ such that $\mathcal{B}$ contains all open sets, and countable unions and complements of members of $\mathcal{B}$ belong to $\mathcal{B}$.)
EOF

write_intro "properties-of-almost-open-sets" \
  "The collection of almost open sets is closed under countable unions and complements, hence forms a $\sigma$-algebra. Moreover, this $\sigma$-algebra contains all Borel sets. This means that modulo meager sets, every Borel set is indistinguishable from an open set—a powerful fact used in the proof of the Banach-Kuratowski-Pettis theorem and other category-based arguments in topological groups."

# 19. banach-kuratowski-pettis-theorem
write_yaml "banach-kuratowski-pettis-theorem" \
  "banach-kuratowski-pettis-theorem" \
  "Banach-Kuratowski-Pettis Theorem" \
  "theorem" "topology" "topological-groups" "advanced" \
  '"Banach-Kuratowski-Pettis", "almost-open", "non-meager", "topological-group"' \
  "" '"topological-group", "almost-open-set", "Baire-category"' "" \
  "6" "P" "Problem P(b): Banach-Kuratowski-Pettis Theorem"

cat > "$BASE/banach-kuratowski-pettis-theorem/theorem.tex" << 'EOF'
If $A$ contains a non-meager almost open subset of a topological group $X$, then $AA^{-1}$ is a neighborhood of the identity element.
EOF

write_intro "banach-kuratowski-pettis-theorem" \
  "The Banach-Kuratowski-Pettis theorem states that if a set $A$ in a topological group contains a non-meager almost open subset, then the product set $AA^{-1}$ is a neighborhood of the identity. This is a fundamental result in the category theory of topological groups, generalizing the fact that in a non-meager group, the difference of two non-meager sets contains a neighborhood of the identity. It has deep consequences for automatic continuity and open mapping theorems."

# 20. almost-open-subgroup-dichotomy
write_yaml "almost-open-subgroup-dichotomy" \
  "almost-open-subgroup-dichotomy" \
  "Almost Open Subgroup Dichotomy" \
  "theorem" "topology" "topological-groups" "advanced" \
  '"almost-open", "subgroup", "meager", "open-closed"' \
  "" '"topological-group", "almost-open-set", "subgroup"' "" \
  "6" "P" "Problem P(c): almost open subgroup dichotomy"

cat > "$BASE/almost-open-subgroup-dichotomy/theorem.tex" << 'EOF'
An almost open subgroup of a non-meager topological group $X$ is either meager in $X$ or open and closed in $X$.
EOF

write_intro "almost-open-subgroup-dichotomy" \
  "An almost open subgroup of a non-meager topological group exhibits a striking dichotomy: it is either meager (topologically small) or both open and closed (topologically large). There is no middle ground. This result highlights the rigidity of subgroup structure under Baire category constraints and is used to deduce that certain algebraically defined subgroups must be either negligible or the whole space."

# ============================================================
# SECTION Q: COMPLETION OF TOPOLOGICAL GROUPS
# ============================================================

# 21. cauchy-nets-left-right-uniformity
write_yaml "cauchy-nets-left-right-uniformity" \
  "cauchy-nets-left-right-uniformity" \
  "Cauchy Nets Under Left and Right Uniformities" \
  "proposition" "topology" "topological-groups" "intermediate" \
  '"Cauchy-net", "left-uniformity", "right-uniformity", "inversion"' \
  "" '"topological-group", "Cauchy-net", "uniformity"' "" \
  "6" "Q" "Problem Q(a): Cauchy nets under left and right uniformities"

cat > "$BASE/cauchy-nets-left-right-uniformity/theorem.tex" << 'EOF'
If $\{x_n, n \in D\}$ is a Cauchy net relative to $\mathcal{L}$, then $\{(x_n)^{-1}, n \in D\}$ is also a Cauchy net relative to $\mathcal{L}$. (Equivalently, $\mathcal{L}$ and $\mathcal{R}$ have the same Cauchy nets.) Left translation by a fixed member of the group is $\mathcal{R}$-uniformly continuous, right translation is $\mathcal{R}$-uniformly continuous, and inversion ($x \mapsto x^{-1}$) is $\mathcal{R}$-uniformly continuous. Multiplication ($\langle x, y \rangle \mapsto xy$) is usually not uniformly continuous.
EOF

write_intro "cauchy-nets-left-right-uniformity" \
  "In a topological group, inversion preserves Cauchy nets with respect to the left uniformity, and the left and right uniformities share the same Cauchy nets. Moreover, left and right translations are uniformly continuous with respect to the right uniformity, and inversion is uniformly continuous. However, the multiplication map is generally not uniformly continuous. These facts determine when a topological group admits a two-sided completion."

# 22. topological-group-completion
write_yaml "topological-group-completion" \
  "topological-group-completion" \
  "Completion of a Topological Group" \
  "theorem" "topology" "topological-groups" "advanced" \
  '"completion", "topological-group", "two-sided-uniformity", "Hausdorff"' \
  "" '"topological-group", "uniform-space", "completion"' "" \
  "6" "Q" "Problem Q(b): topological group completion"

cat > "$BASE/topological-group-completion/theorem.tex" << 'EOF'
Let $(G, \cdot, \mathcal{R})$ be a Hausdorff topological group, let $(H, \mathcal{R})$ be a Hausdorff completion of the uniform space $(G, \mathcal{R})$, and let $\mathcal{S}$ be the topology of $\mathcal{R}$. Then the group operation $\cdot$ can be extended in a unique way such that $(H, \cdot, \mathcal{R})$ becomes a topological group and $\mathcal{R}$ becomes its two-sided uniformity.
EOF

write_intro "topological-group-completion" \
  "Given a Hausdorff topological group $G$ with its right uniformity, the uniform space completion $H$ carries a unique extension of the group operation making it a topological group. Moreover, the right uniformity on the completion becomes the two-sided uniformity. This theorem provides the foundation for studying complete topological groups and shows that the completion of a topological group is again a topological group in a natural way."

# 23. homeomorphism-group-cauchy-counterexample
write_yaml "homeomorphism-group-cauchy-counterexample" \
  "homeomorphism-group-cauchy-counterexample" \
  "Counterexample: Homeomorphism Group of the Interval" \
  "definition" "topology" "topological-groups" "advanced" \
  '"homeomorphism-group", "Cauchy-net", "counterexample", "left-right-uniformity"' \
  "" '"topological-group", "homeomorphism", "Cauchy-sequence"' "" \
  "6" "Q" "Problem Q(c): counterexample for right completion"

cat > "$BASE/homeomorphism-group-cauchy-counterexample/theorem.tex" << 'EOF'
Let $G$ be the group of all homeomorphisms of the closed unit interval $[0,1]$ onto itself with composition for group operation and with the topology of the (right invariant) metric: $$d(f, g) = \sup \left\{ |f(x) - g(x)| : x \in [0,1] \right\}.$$ There is a sequence $\{f_n, n \in \omega\}$ in $G$ which converges uniformly to a function which is not one to one, and the sequence $\{(f_n)^{-1}, n \in \omega\}$ is therefore not Cauchy relative to the left uniformity. The group $G$ is already complete relative to the two-sided uniformity $\mathcal{U}$, for $\mathcal{U}$ is the uniformity of the metric: $d(x, y) + d(x^{-1}, y^{-1})$.
EOF

write_intro "homeomorphism-group-cauchy-counterexample" \
  "The homeomorphism group of $[0,1]$ under the sup-metric provides a concrete counterexample where the left and right uniformities have different Cauchy sequences. A sequence can be right-Cauchy but its inverses fail to be left-Cauchy. Consequently, a 'right completion' need not exist. Nevertheless, the group is already complete under the two-sided uniformity, which is metrized by $d(x,y) + d(x^{-1}, y^{-1})$. This example shows that the existence of a two-sided completion requires compatibility between left and right uniformities."

# 24. metrizable-group-completeness
write_yaml "metrizable-group-completeness" \
  "metrizable-group-completeness" \
  "Metric Completeness Implies Uniform Completeness for Metrizable Groups" \
  "theorem" "topology" "topological-groups" "intermediate" \
  '"metrizable-group", "metric-completeness", "uniform-completeness", "two-sided-uniformity"' \
  "" '"topological-group", "metrizable-space", "complete-uniform-space"' "" \
  "6" "Q" "Problem Q(d): metric completeness implies uniform completeness"

cat > "$BASE/metrizable-group-completeness/theorem.tex" << 'EOF'
Let $(G, \cdot, \mathfrak{J})$ be a metrizable topological group. If $G$ is metrically topologically complete, then $G$ is complete relative to its two-sided uniformity $\mathcal{U}$.
EOF

write_intro "metrizable-group-completeness" \
  "For metrizable topological groups, metric topological completeness implies completeness with respect to the two-sided uniformity. This result bridges the metric and uniform notions of completeness in the group setting. However, the theorem does not extend to non-metrizable groups, as noted in the text—the deduction relies essentially on metrizability."

# ============================================================
# SECTION R: CONTINUITY AND OPENNESS OF HOMOMORPHISMS
# ============================================================

# 25. closed-graph-theorem-topological-groups
write_yaml "closed-graph-theorem-topological-groups" \
  "closed-graph-theorem-topological-groups" \
  "Closed Graph Theorem for Topological Groups" \
  "theorem" "topology" "topological-groups" "advanced" \
  '"closed-graph-theorem", "topological-group", "homomorphism", "continuity"' \
  "" '"topological-group", "homomorphism", "closed-graph"' "" \
  "6" "R" "Problem R(a): closed graph theorem for topological groups"

cat > "$BASE/closed-graph-theorem-topological-groups/theorem.tex" << 'EOF'
Let $G$ be a topological group, let $H$ be a metrizable topological group which is complete relative to its right uniformity, and let $f$ be a homomorphism of $G$ into $H$ such that
\begin{enumerate}
\item[(i)] the graph of $f$ is a closed subset of $G \times H$, and
\item[(ii)] the closure of $f^{-1}[V]$ belongs to $\mathcal{U}$ whenever $V \in \mathcal{V}$.
\end{enumerate}
Then $f$ is continuous.
EOF

write_intro "closed-graph-theorem-topological-groups" \
  "This is the closed graph theorem in the setting of topological groups. If the target group $H$ is metrizable and right-complete, any homomorphism $f: G \to H$ with a closed graph satisfying a mild condition on preimages of identity neighborhoods must be continuous. The proof applies Lemma 6.36 and uses a right-invariant metric on $H$. This generalizes the classical Banach closed graph theorem for linear operators."

# 26. open-mapping-theorem-topological-groups
write_yaml "open-mapping-theorem-topological-groups" \
  "open-mapping-theorem-topological-groups" \
  "Open Mapping Theorem for Topological Groups" \
  "theorem" "topology" "topological-groups" "advanced" \
  '"open-mapping-theorem", "topological-group", "homomorphism", "open-map"' \
  "" '"topological-group", "homomorphism", "closed-graph"' "" \
  "6" "R" "Problem R(a*): open mapping theorem for topological groups"

cat > "$BASE/open-mapping-theorem-topological-groups/theorem.tex" << 'EOF'
Dually, a homomorphism $g$ of $H$ into $G$ is open if
\begin{enumerate}
\item[(i)*] the graph of $g$ is a closed subset of $H \times G$, and
\item[(ii)*] the closure of $g[V]$ belongs to $\mathcal{U}$ whenever $V \in \mathcal{V}$.
\end{enumerate}
EOF

write_intro "open-mapping-theorem-topological-groups" \
  "This is the dual open mapping theorem. A homomorphism $g: H \to G$ from a metrizable right-complete group with a closed graph is open, provided the closure of the image of each identity neighborhood in $H$ is an identity neighborhood in $G$. The proof is dual to the closed graph theorem, applying Lemma 6.36 to the inverse relation $g^{-1}$."

# 27. automatic-closed-graph-conditions
write_yaml "automatic-closed-graph-conditions" \
  "automatic-closed-graph-conditions" \
  "Automatic Satisfaction of Closed Graph Conditions" \
  "theorem" "topology" "topological-groups" "advanced" \
  '"closed-graph-theorem", "Lindelof", "non-meager", "linear-topological-space"' \
  "" '"topological-group", "Lindelof-space", "linear-topological-space"' "" \
  "6" "R" "Problem R(b): automatic satisfaction of conditions"

cat > "$BASE/automatic-closed-graph-conditions/theorem.tex" << 'EOF'
If in the preceding theorem it is assumed that $H$ is a Lindel\"of space (each open cover has a countable subcover) and $G$ is non-meager, then condition (ii) is automatically satisfied; if further $g[H] = G$, then (ii)* is also automatically satisfied. If $G$ and $H$ are linear topological spaces, $f$ and $g$ are linear functions, $g[H] = G$, and $G$ is non-meager, then (ii) and (ii)* are automatically satisfied.
EOF

write_intro "automatic-closed-graph-conditions" \
  "When the target group $H$ is Lindelöf and the domain $G$ is non-meager, the technical condition (ii) on preimages of identity neighborhoods holds automatically. For linear maps between linear topological spaces, surjectivity of $g$ and non-meagerness of $G$ suffice for both conditions (ii) and (ii)*. This reveals the classical Banach closed graph and open mapping theorems as special cases of these more general group-theoretic results."

# ============================================================
# SECTION S: SUMMABILITY
# ============================================================

# 28. summability-in-topological-group
write_yaml "summability-in-topological-group" \
  "summability-in-topological-group" \
  "Summability in a Topological Group" \
  "definition" "topology" "topological-groups" "intermediate" \
  '"summability", "topological-group", "net", "unconditional-convergence"' \
  "" '"topological-group", "net", "series"' "" \
  "6" "S" "Problem S: definition of summability"

cat > "$BASE/summability-in-topological-group/theorem.tex" << 'EOF'
Let $f$ be a function whose domain includes a set $A$ and whose values lie in a complete abelian Hausdorff topological group $G$. Let $\alpha$ be the family of finite subsets of $A$, and for $F$ in $\alpha$ let $S_F$ be the sum of $f(a)$ for $a$ in $F$. The family $\alpha$ is directed by $\supset$, and $\{S_F, F \in \alpha, \supset\}$ is a net in $G$. If this net converges to a member $s$ of $G$, then $f$ is said to be \text{summable over $A$}, $s$ is defined to be the sum of $f$ over $A$, and we write $$s = \sum \{f(a): a \in A\} = \sum_A f.$$
EOF

write_intro "summability-in-topological-group" \
  "Summability generalizes the notion of unconditional convergence of series to functions taking values in a complete abelian Hausdorff topological group. A function $f$ on $A$ is summable if the net of finite partial sums, indexed by the directed set of finite subsets ordered by reverse inclusion, converges. When it exists, the limit is denoted $\sum_A f$ and is independent of any ordering on $A$, capturing the idea of unordered summation."

# 29. cauchy-criterion-for-summability
write_yaml "cauchy-criterion-for-summability" \
  "cauchy-criterion-for-summability" \
  "Cauchy Criterion for Summability" \
  "theorem" "topology" "topological-groups" "intermediate" \
  '"summability", "Cauchy-criterion", "topological-group"' \
  "" '"summability", "topological-group", "Cauchy-condition"' "" \
  "6" "S" "Problem S(a): Cauchy criterion for summability"

cat > "$BASE/cauchy-criterion-for-summability/theorem.tex" << 'EOF'
The function $f$ is summable over $A$ iff for each neighborhood $U$ of $0$ in $G$ there is a finite subset $B$ of $A$ such that for every finite subset $C$ of $A \sim B$ it is true that $\sum_C f \in U$. Hence a function summable over $A$ is summable over each subset of $A$.
EOF

write_intro "cauchy-criterion-for-summability" \
  "The Cauchy criterion characterizes summability without reference to the limit: a function is summable exactly when the finite partial sums over sets disjoint from a sufficiently large finite set are arbitrarily close to zero. An immediate consequence is that summability over a set implies summability over every subset—a heredity property that parallels absolute convergence in the real case but holds here for all summable functions."

# ============================================================
# SECTION T (Uniformly Locally Compact Spaces)
# ============================================================

# 30. uniform-neighborhood-clopen-union
write_yaml "uniform-neighborhood-clopen-union" \
  "uniform-neighborhood-clopen-union" \
  "Uniform Neighborhoods Yield Clopen Unions" \
  "theorem" "topology" "uniform-spaces" "intermediate" \
  '"uniform-neighborhood", "clopen", "chain-argument"' \
  "" '"uniform-space", "clopen-set"' "" \
  "6" "T" "Problem T(a): uniform neighborhoods and clopen sets"

cat > "$BASE/uniform-neighborhood-clopen-union/theorem.tex" << 'EOF'
For each subset $A$ of $X$ the set $\bigcup \{U_n[A]: n \in \omega\}$ is both open and closed.
EOF

write_intro "uniform-neighborhood-clopen-union" \
  "In a uniform space, the union of iterated uniform neighborhoods $U_n[A]$ over all $n \in \omega$ is simultaneously open and closed for any subset $A$. This is essentially the chain argument used in studying components and connectedness in uniform spaces, and it provides a decomposition of the space into clopen invariant sets under the action of a uniform entourage."

# 31. compactness-of-uniform-neighborhood
write_yaml "compactness-of-uniform-neighborhood" \
  "compactness-of-uniform-neighborhood" \
  "Compactness of Uniform Neighborhoods of Compact Sets" \
  "theorem" "topology" "uniform-spaces" "intermediate" \
  '"uniform-neighborhood", "compact", "closed-neighborhood"' \
  "" '"uniform-space", "compact-set"' "" \
  "6" "T" "Problem T(b): compactness of uniform neighborhoods"

cat > "$BASE/compactness-of-uniform-neighborhood/theorem.tex" << 'EOF'
If $U$ is a closed neighborhood of the diagonal in $X \times X$, $A$ is a compact subset of $X$, and $U \circ U[x]$ is compact for each $x$ in $A$, then $U[A]$ is compact.
EOF

write_intro "compactness-of-uniform-neighborhood" \
  "When $U$ is a closed entourage and $A$ is compact, the uniform neighborhood $U[A]$ is compact provided that the double-relational image $U \circ U[x]$ is compact for each point of $A$. The proof uses the result from 6.A that $U[A]$ is closed. This theorem provides conditions under which the uniform thickening of a compact set remains compact."

# 32. connected-uniformly-locally-compact-sigma-compact
write_yaml "connected-uniformly-locally-compact-sigma-compact" \
  "connected-uniformly-locally-compact-sigma-compact" \
  "Connected Uniformly Locally Compact Spaces Are Sigma-Compact" \
  "theorem" "topology" "uniform-spaces" "intermediate" \
  '"uniformly-locally-compact", "sigma-compact", "connected"' \
  "" '"uniform-space", "locally-compact", "sigma-compact"' "" \
  "6" "T" "Problem T(c): connected uniformly locally compact implies sigma-compact"

cat > "$BASE/connected-uniformly-locally-compact-sigma-compact/theorem.tex" << 'EOF'
A connected uniformly locally compact space $(X, \mathfrak{U})$ is $\sigma$-compact (that is, $X$ is the union of a countable family of compact subsets).
EOF

write_intro "connected-uniformly-locally-compact-sigma-compact" \
  "In a connected uniform space that is uniformly locally compact, the entire space can be expressed as a countable union of compact subsets. Connectedness forces the 'local' compactness to propagate globally in a controlled way, preventing the space from being too large. This is a uniform analogue of the fact that connected locally compact metric spaces are $\sigma$-compact."

# 33. uniformly-locally-compact-decomposition
write_yaml "uniformly-locally-compact-decomposition" \
  "uniformly-locally-compact-decomposition" \
  "Decomposition of Uniformly Locally Compact Spaces" \
  "theorem" "topology" "uniform-spaces" "intermediate" \
  '"uniformly-locally-compact", "sigma-compact", "paracompact", "decomposition"' \
  "" '"uniform-space", "locally-compact", "paracompact"' "" \
  "6" "T" "Problem T(d): decomposition of uniformly locally compact spaces"

cat > "$BASE/uniformly-locally-compact-decomposition/theorem.tex" << 'EOF'
Each uniformly locally compact space is the union of a disjoint open family of $\sigma$-compact subspaces. Hence each such space is paracompact.
EOF

write_intro "uniformly-locally-compact-decomposition" \
  "Every uniformly locally compact space decomposes into a disjoint union of open $\sigma$-compact subspaces. As an immediate corollary, uniformly locally compact spaces are always paracompact. This decomposition result shows that uniform local compactness is a strong condition that forces the space to be a topological sum of reasonably 'small' pieces, each expressible as a countable union of compact sets."

# 34. uniformly-locally-compact-characterization
write_yaml "uniformly-locally-compact-characterization" \
  "uniformly-locally-compact-characterization" \
  "Characterization of Uniformly Locally Compact Topological Spaces" \
  "theorem" "topology" "uniform-spaces" "intermediate" \
  '"uniformly-locally-compact", "locally-compact", "paracompact", "characterization"' \
  "" '"uniform-space", "locally-compact", "paracompact"' "" \
  "6" "T" "Problem T(e): characterization of uniformly locally compact spaces"

cat > "$BASE/uniformly-locally-compact-characterization/theorem.tex" << 'EOF'
Let $(X, \mathfrak{J})$ be a topological space. Then there is a uniformity $\mathfrak{U}$ whose topology is $\mathfrak{J}$ such that $(X, \mathfrak{U})$ is uniformly locally compact iff $(X, \mathfrak{J})$ is locally compact and paracompact.
EOF

write_intro "uniformly-locally-compact-characterization" \
  "A topological space admits a compatible uniformity under which it is uniformly locally compact precisely when it is locally compact and paracompact. This theorem completely characterizes which topological spaces can be given a uniformly locally compact uniform structure, linking the purely topological properties of local compactness and paracompactness to the uniform notion of uniform local compactness."

# ============================================================
# SECTION U: THE UNIFORM BOUNDEDNESS THEOREM
# ============================================================

# 35. convex-symmetric-line-segment-neighborhood
write_yaml "convex-symmetric-line-segment-neighborhood" \
  "convex-symmetric-line-segment-neighborhood" \
  "Convex Symmetric Sets Containing Line Segments Are Neighborhoods" \
  "theorem" "topology" "topological-vector-spaces" "advanced" \
  '"convex", "symmetric", "line-segment", "neighborhood", "non-meager"' \
  "" '"topological-vector-space", "convex-set", "Baire-category"' "" \
  "6" "U" "Problem U(a): convex symmetric neighborhood theorem"

cat > "$BASE/convex-symmetric-line-segment-neighborhood/theorem.tex" << 'EOF'
Let $X$ be a real linear topological space which is not meager in itself and let $K$ be a closed convex subset of $X$ such that $K = -K$ and $K$ contains a line segment in each direction (that is, for each $x$ in $X$ there is a positive real number $t$ such that $sx \in K$ if $0 \leq s \leq t$). Then $K$ is a neighborhood of $0$.
EOF

write_intro "convex-symmetric-line-segment-neighborhood" \
  "In a non-meager real linear topological space, any closed, symmetric, convex set that contains a line segment in every direction must be a neighborhood of the origin. The proof uses the Baire category theorem: such a set $K$ cannot be meager, so by 6.P the difference $K - K = 2K$ is a neighborhood of $0$, and convexity then implies $K$ itself is a neighborhood. This lemma is the key to the uniform boundedness principle."

# 36. uniform-boundedness-theorem
write_yaml "uniform-boundedness-theorem" \
  "uniform-boundedness-theorem" \
  "Uniform Boundedness Theorem" \
  "theorem" "topology" "topological-vector-spaces" "advanced" \
  '"uniform-boundedness", "equicontinuity", "linear-functionals", "non-meager"' \
  "" '"topological-vector-space", "linear-functional", "equicontinuity"' "" \
  "6" "U" "Problem U(b): uniform boundedness theorem"

cat > "$BASE/uniform-boundedness-theorem/theorem.tex" << 'EOF'
Let $F$ be a family of continuous linear functions on a non-meager linear topological space. If $F$ is pointwise bounded (that is, for each $x$ the set $\{f(x): f \in F\}$ is bounded), then $F$ is equicontinuous.
EOF

write_intro "uniform-boundedness-theorem" \
  "The uniform boundedness theorem (also known as the Banach-Steinhaus theorem in its classical form) states that a pointwise bounded family of continuous linear functionals on a non-meager linear topological space is automatically equicontinuous. The proof uses part (a): the set $K = \{x: |f(x)| \leq 1 \text{ for all } f \in F\}$ is closed, convex, symmetric, and contains line segments in each direction by pointwise boundedness, hence is a neighborhood of $0$."

# ============================================================
# SECTION V: BOOLEAN SIGMA-RINGS
# ============================================================

# 37. closure-countable-union-boolean-sigma-ring
write_yaml "closure-countable-union-boolean-sigma-ring" \
  "closure-countable-union-boolean-sigma-ring" \
  "Closure of Countable Unions in Boolean Sigma-Rings" \
  "theorem" "topology" "boolean-algebras" "advanced" \
  '"Boolean-sigma-ring", "compact-open", "countable-union", "Stone-space"' \
  "" '"Boolean-ring", "Stone-representation", "compact-open-set"' "" \
  "6" "V" "Problem V(a): closure of countable union in Boolean sigma-ring"

cat > "$BASE/closure-countable-union-boolean-sigma-ring/theorem.tex" << 'EOF'
If $(\mathcal{Q}, \Delta, \cap)$ is a Boolean $\sigma$-ring, then the closure of the union of a countable subfamily of $\mathcal{Q}$ is a member of $\mathcal{B}$ (that is, the closure of the union of a countable family of compact open subsets of $X$ is compact and open).
EOF

write_intro "closure-countable-union-boolean-sigma-ring" \
  "In a Boolean $\sigma$-ring represented as compact open subsets of a locally compact Boolean (Stone) space, the closure of any countable union of members remains compact and open. This property is characteristic of $\sigma$-rings and reflects the fact that countable operations in the algebraic sense correspond to topological operations on the Stone space that preserve compact openness."

# 38. representation-modulo-meager-sets
write_yaml "representation-modulo-meager-sets" \
  "representation-modulo-meager-sets" \
  "Representation Modulo Meager Sets in Boolean Sigma-Rings" \
  "theorem" "topology" "boolean-algebras" "advanced" \
  '"Boolean-sigma-ring", "meager-set", "representation", "Stone-space"' \
  "" '"Boolean-ring", "Baire-category", "meager-set"' "" \
  "6" "V" "Problem V(b): representation modulo meager sets"

cat > "$BASE/representation-modulo-meager-sets/theorem.tex" << 'EOF'
Let $\mathcal{Q}$ be the smallest family of subsets of $X$ such that $\mathcal{B} \subseteq \mathcal{Q}$ and countable unions and symmetric differences of members of $\mathcal{Q}$ belong to $\mathcal{Q}$. Let $\mathcal{M}$ be the family of all meager subsets of $X$. Then for each member $A$ of $\mathcal{Q}$ there is a unique member $B$ of $\mathcal{B}$ such that $A \Delta B \in \mathcal{M}$.
EOF

write_intro "representation-modulo-meager-sets" \
  "Every member $A$ of the $\sigma$-algebra $\mathcal{Q}$ generated by the compact open sets $\mathcal{B}$ can be represented uniquely modulo meager sets by a compact open set $B$. That is, the symmetric difference $A \Delta B$ is meager. This representation theorem is a category-theoretic analogue of the measure-theoretic fact that measurable sets are approximated by open sets modulo null sets, and it relies on the Baire category theorem applied to the Stone space."

# 39. direct-sum-decomposition-sigma-ring
write_yaml "direct-sum-decomposition-sigma-ring" \
  "direct-sum-decomposition-sigma-ring" \
  "Direct Sum Decomposition of a Boolean Sigma-Ring" \
  "theorem" "topology" "boolean-algebras" "advanced" \
  '"Boolean-sigma-ring", "direct-sum", "sigma-ideal", "decomposition"' \
  "" '"Boolean-ring", "sigma-ideal", "direct-sum"' "" \
  "6" "V" "Problem V(c): direct sum decomposition"

cat > "$BASE/direct-sum-decomposition-sigma-ring/theorem.tex" << 'EOF'
The $\sigma$-ring $\mathcal{Q}$ is (additively) the direct sum of $\mathcal{B}$ and the $\sigma$-ideal $\mathcal{Q} \cap \mathcal{M}$. That is, every member of $\mathcal{Q}$ can be expressed uniquely as the symmetric difference of a member of $\mathcal{B}$ and a meager member of $\mathcal{Q}$, and $\mathcal{Q} \cap \mathcal{M}$ is a $\sigma$-ideal in $\mathcal{Q}$.
EOF

write_intro "direct-sum-decomposition-sigma-ring" \
  "The Boolean $\sigma$-ring $\mathcal{Q}$ decomposes as a direct sum: $\mathcal{Q} = \mathcal{B} \oplus (\mathcal{Q} \cap \mathcal{M})$, where $\mathcal{B}$ is the subring of compact open sets and $\mathcal{Q} \cap \mathcal{M}$ is the $\sigma$-ideal of meager members of $\mathcal{Q}$. This structural theorem shows that modulo meager sets, every $\sigma$-ring element corresponds to a unique compact open set, providing a canonical representation that generalizes the Loomis-Sikorski theorem for Boolean $\sigma$-algebras."

echo "=== BATCH 2 (concepts 17-39) COMPLETE ==="
