#!/usr/bin/env python3
"""Extract all concepts from GTM116 Measure and Integral into v7 strict format."""
import re, os, yaml, hashlib, json

BOOK_FILE = "/home/a123/文档/mathpkg/pipeline_output/stitched/(GTM116)Measure and Integral/_full.md"
OUT_DIR = "/home/a123/文档/mathpkg/pipeline_output/v7_test/staging_v2/_GTM116_Measure_and_Integral"

os.makedirs(OUT_DIR, exist_ok=True)

# Manually curated concept list based on thorough reading of the book
# Each entry: (ch, ctype, title_en, slug, latex_statement)
concepts = []

# Chapter 0: Preliminaries
concepts.append((0, 'proposition', 'Decomposition Lemma for Vector Lattices',
    'decomposition-lemma-for-vector-lattices',
    'If $x \\ge 0$, $y \\ge 0$, $z \\ge 0$ and $z \\le x + y$, then there exist $u$ and $v$ such that $z = u + v$, $0 \\le u \\le x$, and $0 \\le v \\le y$.'))
concepts.append((0, 'definition', 'Absolute Value in a Vector Lattice',
    'absolute-value-in-vector-lattice',
    'For each member $x$ of a vector lattice $E$, the absolute value of $x$ is defined to be $|x| = x^+ + x^-$, where $x^+ = x \\lor 0$ and $x^- = -(x \\land 0)$.'))
concepts.append((0, 'definition', 'Disjoint Vectors in a Vector Lattice',
    'disjoint-vectors-in-vector-lattice',
    'Vectors $x$ and $y$ in a vector lattice are disjoint iff $|x| \\land |y| = 0$.'))
concepts.append((0, 'proposition', 'Characterization of Vector Lattice Ordering via Absolute Value',
    'characterization-of-vector-lattice-ordering-via-absolute-value',
    'If $E$ is a vector space over $\\mathbb{R}$, $A: E \\to E$, $A \\circ A = A$, $A$ is absolutely homogeneous (i.e., $A(rx) = |r|A(x)$), and $A$ is additive on $A[E]$, then $E$ is a vector lattice and $A$ is the absolute value, provided one defines $x \\ge y$ to mean $A(x - y) = x - y$.'))
concepts.append((0, 'proposition', 'Summability Over Decomposition',
    'summability-over-decomposition',
    'If $\\mathcal{A}$ is a decomposition of $T$ and $x$ is summable$^*$ over $T$, then $A \\mapsto \\sum_A x$ is summable$^*$ over $\\mathcal{A}$ and $\\sum_T x = \\sum_{A \\in \\mathcal{A}} \\sum_A x$.'))
concepts.append((0, 'proposition', 'Summability Over Product',
    'summability-over-product',
    'If $x$ is summable$^*$ over $Y \\times Z$, then $\\sum_{Y \\times Z} x = \\sum_{y \\in Y} \\sum_{z \\in Z} x(y,z) = \\sum_{z \\in Z} \\sum_{y \\in Y} x(y,z)$ whenever the iterated sums exist.'))

# Chapter 1: Pre-Measures
concepts.append((1, 'definition', 'Length Function',
    'length-function',
    'A non-negative real valued function $\\lambda$ on $\\mathcal{J}$ with $\\lambda(\\varnothing) = 0$ is a length function for $\\mathbb{R}$ iff: (1) Boundary inequality: if $a < b$ then $\\lambda[a:b] \\ge \\lambda\\{a\\} + \\lambda\\{b\\}$; (2) Regularity: $\\lambda\\{a\\} = \\inf\\{\\lambda[a - e : a + e] : e > 0\\}$; (3) Additive property: if $a \\le b \\le c$ then $\\lambda[a:b] + \\lambda[b:c] = \\lambda[a:c] + \\lambda[b:b]$.'))
concepts.append((1, 'definition', 'Discrete Length Function',
    'discrete-length-function',
    'A length function $\\lambda$ is discrete iff $\\lambda[a:b] = \\sum_{x \\in [a:b]} \\lambda\\{x\\}$ for every closed interval $[a:b]$.'))
concepts.append((1, 'definition', 'Continuous Length Function',
    'continuous-length-function',
    'A length function $\\lambda$ is continuous iff $\\lambda\\{x\\} = 0$ for all $x$ in $\\mathbb{R}$.'))
concepts.append((1, 'proposition', 'Decomposition of Length into Continuous and Discrete Parts',
    'decomposition-of-length-into-continuous-and-discrete-parts',
    'Each length function $\\lambda$ can be represented uniquely as the sum $\\lambda = \\lambda_c + \\lambda_d$ of a continuous length $\\lambda_c$ and a discrete length $\\lambda_d$.'))
concepts.append((1, 'proposition', 'Normalized Distribution Function for a Length',
    'normalized-distribution-function-for-a-length',
    'The normalized distribution function $F$ for a length $\\lambda$ is given by $F(x) = \\lambda[0:x]$ for $x \\ge 0$ and $F(x) = -\\lambda[x:0]$ for $x < 0$. Then $\\lambda = \\lambda_F$.'))
concepts.append((1, 'theorem', 'Uniqueness of Translation Invariant Length',
    'uniqueness-of-translation-invariant-length',
    'There is, to a constant multiple, a unique translation invariant length---each invariant length $\\lambda$ is $\\lambda[0:1]\\ell$, where $\\ell$ is the usual length.'))
concepts.append((1, 'theorem', 'Extension of Length to Exact Function on Lattice',
    'extension-of-length-to-exact-function-on-lattice',
    'Each length function $\\lambda$ on $\\mathcal{J}$ extends uniquely to an exact function $\\mu$ on the lattice $\\mathcal{L}(\\mathcal{J})$ of unions of finitely many closed intervals.'))
concepts.append((1, 'definition', 'Exact Function',
    'exact-function',
    'A non-negative real valued function $\\mu$ on a lattice $\\mathcal{A}$ of sets with $\\varnothing \\in \\mathcal{A}$ and $\\mu(\\varnothing) = 0$ is exact iff $\\mu(A) = \\mu(B) + \\sup\\{\\mu(C): C \\in \\mathcal{A}, C \\subset A \\setminus B\\}$ for all $A, B \\in \\mathcal{A}$ with $B \\subset A$.'))

# Chapter 1 Supplements
concepts.append((1, 'definition', 'Content for Locally Compact Hausdorff Space',
    'content-for-locally-compact-hausdorff-space',
    'A content for a locally compact Hausdorff space $X$ is a non-negative, real valued, monotone, additive, subadditive function $\\mu$ on the family of compact subsets of $X$.'))
concepts.append((1, 'proposition', 'Regular Content is Exact and Hypercontinuous',
    'regular-content-is-exact-and-hypercontinuous',
    'A content $\\mu$ on the family of compact subsets of $X$ is regular iff it is exact, and this is the case iff it is hypercontinuous.'))
concepts.append((1, 'definition', 'Hypercontinuous Content',
    'hypercontinuous-content',
    'A content $\\mu$ is hypercontinuous iff $\\mu(\\bigcap_{\\alpha \\in D} E_\\alpha) = \\lim_{\\alpha \\in D} \\mu(E_\\alpha)$ for every decreasing net $\\{E_\\alpha\\}_{\\alpha}$ of compact subsets.'))
concepts.append((1, 'theorem', 'Existence of G-Invariant Regular Content',
    'existence-of-g-invariant-regular-content',
    'If the action of a group $G$ by homeomorphisms on a locally compact Hausdorff space $X$ is transitive and semi-rigid, then there is a regular $G$ invariant content for $X$ that is not identically zero.'))
concepts.append((1, 'theorem', 'Carathéodory Measurable Sets Form a Sigma-Field',
    'caratheodory-measurable-sets-form-sigma-field',
    'If $v$ is countably subadditive non-negative $\\mathbb{R}^*$ valued on $\\mathcal{P}(X)$ and $v(\\varnothing) = 0$, then the family $\\mathcal{M}$ of Carathéodory $v$ measurable sets is a $\\sigma$-field and $v$ is countably additive on $\\mathcal{M}$.'))

# Chapter 2: Pre-Measure to Pre-Integral
concepts.append((2, 'definition', 'Ring of Sets',
    'ring-of-sets',
    'A ring of sets is a non-empty family $\\mathcal{A}$ of sets such that if $A$ and $B$ are members of $\\mathcal{A}$ then $A \\cup B$ and $A \\setminus B$ also belong to $\\mathcal{A}$.'))
concepts.append((2, 'definition', 'Modular Function on a Lattice of Sets',
    'modular-function-on-lattice-of-sets',
    'A function $\\mu$ is modular iff it is a real valued function on a lattice $\\mathcal{A}$ of sets, $\\varnothing \\in \\mathcal{A}$, $\\mu(\\varnothing) = 0$, and $\\mu(A) + \\mu(B) = \\mu(A \\cup B) + \\mu(A \\cap B)$ for all $A, B$ in $\\mathcal{A}$.'))
concepts.append((2, 'theorem', 'Extension of Modular Function to Generated Ring',
    'extension-of-modular-function-to-generated-ring',
    'The ring $\\mathcal{R}$ generated by a lattice $\\mathcal{A}$ of sets consists of unions of finitely many disjoint sets of the form $A \\setminus B$ with $A, B$ in $\\mathcal{A}$. Each modular function $\\mu$ on $\\mathcal{A}$ has a unique finitely additive extension $\\mu^*$ to $\\mathcal{R}$.'))
concepts.append((2, 'definition', 'Pre-Measure',
    'pre-measure',
    'A function $\\mu$ on a family $\\mathcal{A}$ of sets is called a pre-measure provided $\\mathcal{A}$ is closed under finite intersection and $\\mu$ has a countably additive, non-negative real valued extension to the ring $\\mathcal{R}$ generated by $\\mathcal{A}$.'))
concepts.append((2, 'proposition', 'Exact Function Continuous at Empty is a Pre-Measure',
    'exact-function-continuous-at-empty-is-pre-measure',
    'The unique finitely additive extension of an exact function $\\mu$ on a lattice $\\mathcal{A}$ to the ring $\\mathcal{R}$ generated by $\\mathcal{A}$ is continuous at $\\varnothing$ iff $\\mu$ is continuous at $\\varnothing$, and in this case the extension is a pre-measure.'))
concepts.append((2, 'definition', 'Pre-Integral',
    'pre-integral',
    'A pre-integral is a positive linear functional $I$ on a vector function lattice $L$ with truncation such that $\\lim_n I(f_n) = 0$ for every decreasing sequence $\\{f_n\\}_n$ in $L$ that converges pointwise to zero.'))
concepts.append((2, 'definition', 'A-Simple Function',
    'a-simple-function',
    'If $\\mathcal{A}$ is a family of subsets of $X$, then a function $f$ on $X$ is $\\mathcal{A}$ simple iff $f$ is a finite linear combination of characteristic functions of members of $\\mathcal{A}$.'))
concepts.append((2, 'theorem', "Dini's Theorem",
    'dinis-theorem',
    'If a decreasing sequence $\\{f_n\\}_n$ of upper semi-continuous functions on $[a:b]$, or on $\\mathbb{R}$ with compact supports, converges pointwise to zero, then it converges to zero uniformly.'))
concepts.append((2, 'proposition', 'Positive Linear Functional on C_c(R) is a Pre-Integral',
    'positive-linear-functional-on-cc-r-is-pre-integral',
    'Each positive linear functional, and in particular the Riemann integral, on either $C[a:b]$ or $C_c(\\mathbb{R})$, is a pre-integral.'))
concepts.append((2, 'proposition', 'Volume Function Induces a Pre-Integral on L^n',
    'volume-function-induces-pre-integral',
    'If $a_i \\in \\mathbb{R}$ and $A_i \\in \\mathcal{J}_n$ for $i = 1, 2, \\ldots, k$, and if $\\sum_{i=1}^{k} a_i \\chi_{A_i} \\ge 0$, then $\\sum_{i=1}^{k} a_i \\lambda_n(A_i) \\ge 0$. The function $I^n$ on $L^n$ defined by $I^n(\\sum_i a_i \\chi_{A_i}) = \\sum_i a_i \\lambda_n(A_i)$ is a pre-integral.'))
concepts.append((2, 'proposition', 'Positive Linear Functional on C_c(R^n) is Pre-Integral',
    'positive-linear-functional-on-cc-rn-is-pre-integral',
    'Every positive linear functional $I$ on $C_c(\\mathbb{R}^n)$, and in particular the iterated Riemann integral, is a pre-integral.'))
concepts.append((2, 'proposition', 'Positive Linear Functional on C_c(X) or C_0(X) is Pre-Integral',
    'positive-linear-functional-on-cc-or-c0-is-pre-integral',
    'If $I$ is a positive linear functional on either $C_c(X)$ or $C_0(X)$, where $X$ is a locally compact Hausdorff space, then $I$ is a pre-integral.'))

# Chapter 3: Pre-Integral to Integral
concepts.append((3, 'definition', 'Integral with Beppo Levi Property',
    'integral-beppo-levi-property',
    'An integral is a positive linear functional $I$ on a vector function lattice $L$ with truncation that has the Beppo Levi property: if $\\{f_n\\}_n$ is an increasing sequence in $L$, $\\sup_n I(f_n) < \\infty$, and $f(x) = \\sup_n f_n(x) < \\infty$ for all $x$, then $f \\in L$ and $I(f) = \\lim_n I(f_n)$.'))
concepts.append((3, 'definition', 'L1 Semi-Norm',
    'l1-semi-norm',
    'For $f$ in the domain $L$ of a pre-integral $I$, the $L_1$ semi-norm is defined by $\\|f\\|_1 = I(|f|)$.'))
concepts.append((3, 'definition', 'I-Null Set',
    'i-null-set',
    'A subset $E$ of $X$ is $I$ null iff there is a sequence $\\{f_n\\}_n$ in $L$ with summable norms such that $\\sum_n |f_n(x)| = \\infty$ for each $x$ in $E$.'))
concepts.append((3, 'proposition', 'Characterization of Completeness via Swift Convergence',
    'characterization-of-completeness-via-swift-convergence',
    'A semi-normed space $E$ is complete iff each swiftly convergent sequence in $E$ converges to a member of $E$, or iff each sequence in $E$ with summable norms is norm summable to a member of $E$.'))
concepts.append((3, 'lemma', 'Fundamental Lemma for Daniell Extension',
    'fundamental-lemma-for-daniell-extension',
    'If $\\{f_n\\}_n$ is a sequence in $L$, $\\sum_n \\|f_n\\| < \\infty$ and $\\sum_n f_n(x) \\ge 0$ for $I$ a.e. $x$, then $\\sum_n I(f_n) \\ge 0$. If $\\{g_n\\}_n$ is a swiftly convergent sequence in $L$ and $\\lim_n g_n(x) \\ge 0$ for $I$ a.e. $x$ then $\\lim_n I(g_n) \\ge 0$.'))
concepts.append((3, 'definition', 'Daniell Extension of a Pre-Integral',
    'daniell-extension-of-pre-integral',
    'The Daniell extension $I^1$ on $L^1$ of a pre-integral $I$ on $L$ is defined by: $f \\in L^1$ iff $f(x) = \\sum_n f_n(x)$ for $I$ a.e. $x$ for some sequence $\\{f_n\\}_n$ in $L$ with $\\sum_n \\|f_n\\| < \\infty$, and $I^1(f) = \\sum_n I(f_n)$.'))
concepts.append((3, 'theorem', 'Norm Completeness of Integral Domain',
    'norm-completeness-of-integral-domain',
    'If $J$ is an integral on $M$, then each swiftly convergent sequence in $M$ is dominated $J$ a.e. by a member of $M$ and converges $J$ a.e. and in norm to a member of $M$. In particular $M$ is norm complete.'))
concepts.append((3, 'proposition', 'Daniell Extension is Smallest Null Complete Integral Extension',
    'daniell-extension-is-smallest-null-complete-extension',
    'The Daniell extension of a pre-integral is its smallest null complete integral extension. In particular, every null complete integral that extends an integral $I$ on $L$ also extends its null completion $I^\\vee$ on $L^\\vee$.'))
concepts.append((3, 'theorem', 'Monotone Convergence Theorem for Integrals',
    'monotone-convergence-theorem-for-integrals',
    'If $J$ is an integral on $M$ and $\\{f_n\\}_n$ is an increasing sequence in $M$ such that $\\sup_n J(f_n) < \\infty$, then $\\{f_n\\}_n$ converges $J$ a.e. to a member $f$ of $M$ and $J(f) = \\lim_n J(f_n)$.'))
concepts.append((3, 'corollary', 'Order Completeness of Integral Domain',
    'order-completeness-of-integral-domain',
    'If $J$ is an integral on $M$, then a non-empty subset $W$ of $M$ that is closed under $\\lor$ has a $\\ge_J$ supremum, provided $\\sup\\{J(g): g \\in W\\} < \\infty$. In particular, $M$ with the ordering $\\ge_J$ is order complete.'))
concepts.append((3, 'lemma', "Fatou's Lemma",
    'fatous-lemma',
    'Suppose $J$ is an integral on $M$ and $\\{f_n\\}_n$ is a sequence of non-negative members of $M$ such that $\\liminf_n J(f_n) < \\infty$ and $\\liminf_n f_n(x) < \\infty$ for all $x$. Then $\\liminf_n f_n \\in M$ and $J(\\liminf_n f_n) \\le \\liminf_n J(f_n)$.'))
concepts.append((3, 'theorem', 'Dominated Convergence Theorem for Integrals',
    'dominated-convergence-theorem-for-integrals',
    'If $J$ is an integral on $M$, $\\{f_n\\}_n$ is a sequence in $M$ converging $J$ a.e. to a real valued function $f$, and $|f_n| \\le g \\in M$ $J$ a.e. for all $n$, then $f \\in M$ and $J(f) = \\lim_n J(f_n)$.'))

# Chapter 4: Integral to Measure
concepts.append((4, 'definition', 'Measure',
    'measure',
    'A measure is a real valued, non-negative, countably additive function on a $\\delta$-ring $\\mathcal{A}$.'))
concepts.append((4, 'definition', 'Delta-Ring',
    'delta-ring',
    'A $\\delta$-ring is a ring $\\mathcal{A}$ of sets such that if $\\{A_n\\}_n$ is a sequence in $\\mathcal{A}$, then $\\bigcap_n A_n \\in \\mathcal{A}$. Equivalently, a ring closed under countable intersection.'))
concepts.append((4, 'definition', 'Standard Measure',
    'standard-measure',
    'A measure $\\mu$ on a $\\delta$-ring $\\mathcal{A}$ is standard iff whenever $\\{A_n\\}_n$ is a disjoint sequence in $\\mathcal{A}$ with $\\sum_n \\mu(A_n) < \\infty$, then $\\bigcup_n A_n \\in \\mathcal{A}$.'))
concepts.append((4, 'proposition', 'Integral to Measure Correspondence',
    'integral-to-measure-correspondence',
    'If $J$ is an integral on $M$, $\\mathcal{B} = \\{B: \\chi_B \\in M\\}$ and $\\eta(B) = J(\\chi_B)$ for $B$ in $\\mathcal{B}$, then $\\mathcal{B}$ is a $\\delta$-ring and $\\eta$ is a standard measure on $\\mathcal{B}$. The measure induced by an integral is always a standard measure.'))
concepts.append((4, 'proposition', 'Minimal Measure Extending a Length Function is Borel',
    'minimal-measure-extending-length-is-borel',
    'The minimal measure extending a length function is a Borel measure for $\\mathbb{R}$, and every Borel measure is such an extension.'))
concepts.append((4, 'definition', 'Borel Measure for the Real Line',
    'borel-measure-for-real-line',
    'A measure on the Borel $\\delta$-ring $\\mathcal{B}^{\\delta}(\\mathbb{R})$ (the $\\delta$-ring generated by the compact subsets of $\\mathbb{R}$) is a Borel measure for $\\mathbb{R}$.'))
concepts.append((4, 'lemma', 'Delta-Ring Closed Under Dominated Countable Union',
    'delta-ring-closed-under-dominated-countable-union',
    'Each $\\delta$-ring is closed under dominated countable union, and each ring that is closed under dominated countable disjoint union is a $\\delta$-ring.'))
concepts.append((4, 'theorem', 'Generated Delta-Rings and Uniqueness of Measure Extension',
    'generated-delta-rings-and-uniqueness-of-measure-extension',
    'Suppose a family $\\mathcal{A}$ is closed under finite intersections. Then two measures on the $\\delta$-ring generated by $\\mathcal{A}$ that agree on $\\mathcal{A}$ agree everywhere. Consequently each pre-measure on $\\mathcal{A}$ extends to a unique measure on the generated $\\delta$-ring.'))
concepts.append((4, 'lemma', 'Approximation from Above and Below in Daniell Extension',
    'approximation-from-above-and-below-in-daniell-extension',
    'If $I$ is a pre-integral on $L$, $f \\in L^1$ and $e > 0$, then there is a member $g$ of $L$ and a sequence $\\{h_n\\}_n$ in $L$ with $\\sum_n \\|h_n\\| < e$ such that $f = g + \\sum_n h_n$ and $\\|f - g\\|_1 < e$.'))
concepts.append((4, 'proposition', 'Inner Approximation for Daniell-Induced Measure',
    'inner-approximation-for-daniell-induced-measure',
    'If $\\nu$ on $\\mathcal{C}$ is the measure induced by the Daniell extension $I^1$ of a pre-integral $I$ on $L^{\\mathcal{A}}$, then each member of $\\mathcal{C}$ has inner approximations in $\\mathcal{A}_\\delta$. Moreover, for each $C$ in $\\mathcal{C}$ there is $A$ in $\\mathcal{A}_{\\delta\\sigma}$ such that $A \\subset C$ and $\\nu(C \\setminus A) = 0$.'))
concepts.append((4, 'corollary', 'Regularity of Lebesgue-Stieltjes Measures',
    'regularity-of-lebesgue-stieltjes-measures',
    'If $B$ belongs to the domain of a Lebesgue-Stieltjes measure $\\eta$ (in particular if $B \\in \\mathcal{B}^{\\delta}(\\mathbb{R})$), then for $e > 0$ there is a compact set $K$ and an open set $U$ such that $K \\subset B \\subset U$ and $\\eta(K) + e \\ge \\eta(B) \\ge \\eta(U) - e$.'))
concepts.append((4, 'proposition', 'Standardized Completion of Minimal Measure',
    'standardized-completion-of-minimal-measure',
    'Let $\\lambda$ be a pre-measure on $\\mathcal{A}$, $I^\\lambda$ on $L^{\\mathcal{A}}$ the induced pre-integral, and let $\\nu$ on $\\mathcal{C}$ be the measure induced by the Daniell extension of $I^\\lambda$. Then every complete standard measure extending $\\lambda$ is an extension of $\\nu$. Consequently $\\nu$ is the standardized completion of the minimal measure extending $\\lambda$.'))
concepts.append((4, 'proposition', 'Properties of Borel-Lebesgue Measure',
    'properties-of-borel-lebesgue-measure',
    'Borel-Lebesgue measure $\\Lambda_n$ is the minimal measure extending the volume function, $\\Lambda^n$ is its standardized completion, and both $\\Lambda_n$ and $\\Lambda^n$ are translation invariant. The Daniell extension of the iterated Riemann integral on $C_c(\\mathbb{R}^n)$ is identical with the Lebesgue integral.'))
concepts.append((4, 'corollary', 'Existence of Haar Measure',
    'existence-of-haar-measure',
    'There is a regular left invariant Borel measure, not identically zero, for each locally compact Hausdorff topological group.'))

# Chapter 5: Measurability and Sigma-Simplicity
concepts.append((5, 'definition', 'Sigma-Ring',
    'sigma-ring',
    'A $\\sigma$-ring is a ring $\\mathcal{A}$ of sets that is closed under countable union.'))
concepts.append((5, 'definition', 'Sigma-Field',
    'sigma-field',
    'A $\\sigma$-field, or $\\sigma$-algebra, or Borel field, is a field of sets that is closed under countable union or, equivalently, closed under countable intersection.'))
concepts.append((5, 'definition', 'Borel Field of the Real Numbers',
    'borel-field-of-real-numbers',
    'The Borel field $\\mathcal{B}(\\mathbb{R})$ is the $\\sigma$-field for $\\mathbb{R}$ generated by the family of all open subsets of $\\mathbb{R}$. It is also the $\\sigma$-field generated by the compact sets, or by the closed intervals $[a:b]$.'))

concepts.append((5, 'proposition', 'Structure of Generated Delta-Rings and Sigma-Rings',
    'structure-of-generated-delta-and-sigma-rings',
    'Suppose $\\mathcal{A}$ is a non-empty family of subsets of $X$ and $\\mathcal{D}, \\mathcal{S}, \\mathcal{F}$ are respectively the $\\delta$-ring, $\\sigma$-ring and $\\sigma$-field generated by $\\mathcal{A}$. Then: (i) each member of $\\mathcal{D}$ can be covered by finitely many members of $\\mathcal{A}$; (ii) each member of $\\mathcal{D}$ belongs to the $\\delta$-ring generated by a countable subfamily of $\\mathcal{A}$; (iii) $\\mathcal{S} = \\mathcal{D}_{\\sigma}$.'))
concepts.append((5, 'lemma', 'Borel Field Generated by Half-Infinite Intervals',
    'borel-field-generated-by-half-infinite-intervals',
    'The Borel field $\\mathcal{B}(\\mathbb{R})$ is the $\\sigma$-field generated by sets of the form $(-\\infty:r)$ with $r$ rational. The Borel field $\\mathcal{B}(\\mathbb{R}^*)$ is similarly generated by sets $[-\\infty:r)$.'))
concepts.append((5, 'definition', 'Borel Space',
    'borel-space',
    'A borel space is a pair $(X, \\mathcal{A})$ where $\\mathcal{A}$ is a $\\sigma$-field for $X$. Members of $\\mathcal{A}$ are called measurable sets.'))
concepts.append((5, 'definition', 'Measurable Function Between Borel Spaces',
    'measurable-function-between-borel-spaces',
    'If $(X, \\mathcal{A})$ and $(Y, \\mathcal{B})$ are borel spaces, a function $f: X \\to Y$ is $\\mathcal{A} - \\mathcal{B}$ measurable iff $f^{-1}[B] \\in \\mathcal{A}$ for all $B$ in $\\mathcal{B}$.'))
concepts.append((5, 'corollary', 'Measurability via Generating Family',
    'measurability-via-generating-family',
    'If $f^{-1}[G] \\in \\mathcal{A}$ for all members $G$ of a family $\\mathcal{G}$ that generates $\\mathcal{B}$, then $f$ is $\\mathcal{A} - \\mathcal{B}$ measurable.'))
concepts.append((5, 'proposition', 'Product Sigma-Field Properties',
    'product-sigma-field-properties',
    'If $(X, \\mathcal{A})$ and $(Y, \\mathcal{B})$ are borel spaces, then (i) $\\mathcal{A} \\otimes \\mathcal{B}$ is the smallest $\\sigma$-field making projections measurable; (ii) $\\mathcal{B}(\\mathbb{R}) \\otimes \\mathcal{B}(\\mathbb{R}) = \\mathcal{B}(\\mathbb{R}^2)$; (iii) $f: Z \\to X \\times Y$ is $\\mathcal{C} - \\mathcal{A} \\otimes \\mathcal{B}$ measurable iff $P_1 \\circ f$ and $P_2 \\circ f$ are measurable.'))
concepts.append((5, 'theorem', 'Algebraic Operations Preserve Measurability',
    'algebraic-operations-preserve-measurability',
    'If $h$ and $k$ are real valued $\\mathcal{A}$ measurable functions and $r \\in \\mathbb{R}$, then $rh$, $h+k$, $hk$, $h \\lor k$, $h \\land k$, $h \\land 1$, $|h|^p$, and (where $h$ is non-vanishing) $1/h$ are all $\\mathcal{A}$ measurable.'))
concepts.append((5, 'theorem', 'Infima, Suprema, and Limits of Measurable Functions',
    'infima-suprema-and-limits-of-measurable-functions',
    'If $\\{f_n\\}_n$ is a sequence of real$^*$ valued $\\mathcal{A}$ measurable functions, then $\\inf_n f_n$, $\\sup_n f_n$, $\\liminf_n f_n$ and $\\limsup_n f_n$ are all $\\mathcal{A}$ measurable. In particular, if $\\{f_n\\}_n$ converges pointwise to $f$ then $f$ is $\\mathcal{A}$ measurable.'))
concepts.append((5, 'lemma', 'Representation Lemma for Measurable Functions',
    'representation-lemma-for-measurable-functions',
    'If $f$ is a real$^*$ valued function, then $f^+$ is both $\\mathcal{F}_f$ and $\\mathcal{G}_f$ $\\sigma^+$-simple, and $f$ is both $\\mathcal{F}_f$ and $\\mathcal{G}_f$ $\\sigma$-simple. Consequently, if $\\mathcal{A}$ is a $\\sigma$-field, then a real$^*$ valued function is $\\mathcal{A}$ $\\sigma$-simple iff it is $\\mathcal{A}$ measurable.'))
concepts.append((5, 'theorem', 'Characterization of Sigma-Simple Functions',
    'characterization-of-sigma-simple-functions',
    'If $\\mathcal{A}$ is a $\\delta$-ring, a real valued function $f$ is $\\mathcal{A}$ $\\sigma$-simple iff it has a support in $\\mathcal{A}_{\\sigma}$ and is locally $\\mathcal{A}$ measurable. Moreover, if $f \\ge 0$, it is $\\mathcal{A}$ $\\sigma^+$-simple.'))
concepts.append((5, 'lemma', 'Approximating Characteristic Functions by Truncations',
    'approximating-characteristic-functions-by-truncations',
    'If $f: X \\to \\mathbb{R}^*$ and $a \\in \\mathbb{R}$, then $\\{n(f \\land a - f \\land (a - n^{-1}))\\}_n$ is a decreasing sequence converging pointwise to $\\chi_{\\{x: f(x) \\ge a\\}}$, and $\\{n(f \\land (a + n^{-1}) - f \\land a)\\}_n$ is increasing and converges to $\\chi_{\\{x: f(x) > a\\}}$.'))
concepts.append((5, 'theorem', 'Characterization of Pre-Integral Domain via Truncation Ring',
    'characterization-of-pre-integral-domain-via-truncation-ring',
    'If $I$ is a pre-integral on $L$ and $\\mathcal{T}$ is its truncation $\\delta$-ring, then $f \\in L$ iff $f(x) = \\sum_n a_n \\chi_{A_n}(x)$ for all $x$, for some $\\{a_n\\}_n$ in $\\mathbb{R}$ and $\\{A_n\\}_n$ in $\\mathcal{T}$ such that $\\sum_n |a_n| \\mu(A_n) < \\infty$, and $I(f) = \\sum_n a_n \\mu(A_n)$.'))
concepts.append((5, 'corollary', 'Minimal Integral Extension of a Pre-Integral',
    'minimal-integral-extension-of-pre-integral',
    'Each pre-integral $I$ on $L$ has a minimal integral extension $I_1 = I^1 | L^1 \\cap L_{\\sigma}$; that is, every integral extension of $I$ is an extension of $I_1$.'))

# Chapter 6: The Integral I_mu on L_1(mu)
concepts.append((6, 'definition', 'Mu-Integrable Function',
    'mu-integrable-function',
    'A real valued function $f$ is $\\mu$ integrable ($f \\in L_1(\\mu)$) iff there exist sequences $\\{A_n\\}_n$ in $\\mathcal{A}$ and $\\{a_n\\}_n$ in $\\mathbb{R}$ such that $\\sum_n |a_n| \\mu(A_n) < \\infty$ and $f(x) = \\sum_n a_n \\chi_{A_n}(x)$ for every $x$ in $X$. In this case $I_{\\mu}(f) = \\sum_n a_n \\mu(A_n)$.'))
concepts.append((6, 'theorem', 'Each Integral is Integral with Respect to a Measure',
    'each-integral-is-integral-with-respect-to-measure',
    'Each integral $J$ on $M$ is the integral with respect to a measure---the measure induced by $J$. If $\\mu$ is a measure, the measure induced by $I_{\\mu}$ is the standardization of $\\mu$.'))
concepts.append((6, 'theorem', "Egorov's Theorem",
    'egorovs-theorem',
    'If a sequence $\\{f_n\\}_n$ of $\\mathcal{A}$ $\\sigma$-simple functions converges to $f$ $\\mu$ a.e. and $\\{|f_n| \\land 1\\}_n$ is dominated $\\mu$ a.e. by a $\\mu$ integrable function, then $\\{f_n\\}_n$ converges to $f$ almost uniformly.'))
concepts.append((6, 'theorem', 'Riesz Representation Theorem for C_c(R)',
    'riesz-representation-theorem-for-cc-r',
    'Each positive linear functional on $C_c(\\mathbb{R})$ is the restriction to $C_c(\\mathbb{R})$ of the integral with respect to a unique Borel measure $\\mu$ for $\\mathbb{R}$, and $C_c(\\mathbb{R})$ is dense in $L_1(\\mu)$.'))
concepts.append((6, 'definition', 'L_p Space',
    'lp-space',
    'For $1 \\le p < \\infty$, a real valued $\\mathcal{LA}$ measurable function $f$ belongs to $L_p(\\mu)$ iff $|f|^p \\in L_1(\\mu)$, and $\\|f\\|_p = (\\int |f|^p d\\mu)^{1/p}$. For $p = \\infty$, $f \\in L_{\\infty}(\\mu)$ iff $f$ is $\\mathcal{LA}$ measurable and bounded $\\mu$ a.e., and $\\|f\\|_{\\infty} = \\inf\\{b: |f(x)| \\le b \; \\mu \\text{ a.e.}\\}$.'))
concepts.append((6, 'proposition', "Hölder's Inequality and Minkowski's Inequality",
    'holder-and-minkowski-inequalities',
    'Suppose $1/p + 1/q = 1$ with $p, q > 0$. (Hölder) If $f \\in L_p(\\mu)$ and $g \\in L_q(\\mu)$, then $fg \\in L_1(\\mu)$ and $\\|fg\\|_1 \\le \\|f\\|_p \\|g\\|_q$, with equality iff $|f|^p$ and $|g|^q$ are proportional $\\mu$ a.e. (Minkowski) If $f, g \\in L_p(\\mu)$, then $f + g \\in L_p(\\mu)$ and $\\|f + g\\|_p \\le \\|f\\|_p + \\|g\\|_p$.'))
concepts.append((6, 'proposition', 'Dominated and Monotone Convergence in L_p',
    'dominated-and-monotone-convergence-in-lp',
    'Suppose $\\mu$ is a measure and $1 \\le p < \\infty$. (i) If $\\{f_n\\}_n$ in $L_p(\\mu)$ is dominated a.e. by $g \\in L_p(\\mu)$ and $f_n \\to f$ a.e., then $f \\in L_p(\\mu)$ and $\\|f - f_n\\|_p \\to 0$. (ii) A norm bounded, a.e. increasing sequence in $L_p(\\mu)$ converges a.e. and in norm to a member of $L_p(\\mu)$. (iii) $L_p(\\mu)$ is complete.'))
concepts.append((6, 'theorem', 'Continuity of Translation on L_p of Lebesgue Measure',
    'continuity-of-translation-on-lp-lebesgue',
    'If $f \\in L_p(\\Lambda^1)$ and $T_t(f)(x) = f(x + t)$ for $x, t \\in \\mathbb{R}$, then $t \\mapsto T_t(f)$ is a uniformly continuous map of $\\mathbb{R}$ into $L_p(\\Lambda^1)$.'))
concepts.append((6, 'theorem', 'Riesz Representation Theorem for Hilbert Space',
    'riesz-representation-theorem-for-hilbert-space',
    'Each bounded linear functional $F$ on a Hilbert space $E$ is of the form $F(x) = \\langle x, u \\rangle$ for some unique $u \\in E$. In particular, if $F$ is a bounded linear functional on $L_2(\\mu)$, there is $g \\in L_2(\\mu)$ such that $F(f) = \\int fg d\\mu$ for all $f \\in L_2(\\mu)$.'))
concepts.append((6, 'theorem', 'Continuity of Translation for Haar Measure',
    'continuity-of-translation-for-haar-measure',
    'If $\\eta$ is a left Haar measure for a locally compact Hausdorff topological group $G$, $1 \\le p < \\infty$ and $f \\in L_p(\\eta)$, then $\\|T_h(f) - f\\|_p$ is small for $h$ near the identity $e$ of $G$.'))

# Chapter 7: Integrals* and Products
concepts.append((7, 'definition', 'Integrable in the Extended Sense',
    'integrable-in-extended-sense',
    'A function $f$ is $\\mu$ integrable$^*$ iff for some sequences $\\{A_n\\}_n$ in $\\mathcal{A}$ and $\\{a_n\\}_n$ in $\\mathbb{R}$, $\\{a_n \\mu(A_n)\\}_n$ is summable$^*$ and $\\{a_n \\chi_{A_n}(x)\\}_n$ is summable$^*$ to $f(x)$ for each $x$. The class of all $\\mu$ integrable$^*$ functions is $L^*(\\mu)$.'))
concepts.append((7, 'proposition', 'Characterization of Integrable* Functions',
    'characterization-of-integrable-star-functions',
    'An $\\mathbb{R}^*$ valued function $f$ is $\\mu$ integrable$^*$ iff it is locally $\\mathcal{A}$ measurable with a support in $\\mathcal{A}_{\\sigma}$ and is bounded either below or above $\\mu$ a.e. by a $\\mu$ integrable function.'))
concepts.append((7, 'theorem', 'Beppo Levi Theorem for Integrable*',
    'beppo-levi-theorem-for-integrable-star',
    'If $\\{f_n\\}_n$ is an increasing sequence in $L^*(\\mu)$, $f(x) = \\sup_n f_n(x)$ for all $x$, and $\\sup_n I_{\\mu}^*(f_n) < \\infty$, then $f \\in L^*(\\mu)$ and $I_{\\mu}^*(f) = \\lim_n I_{\\mu}^*(f_n)$.'))
concepts.append((7, 'lemma', "Fatou's Lemma for Integrable*",
    'fatous-lemma-for-integrable-star',
    'If $\\{f_n\\}_n$ is a sequence in $L^*(\\mu)$ which is bounded below a.e. by an integrable function $g$, then $I_{\\mu}^*(\\liminf_n f_n) \\le \\liminf_n I_{\\mu}^*(f_n)$. If bounded above a.e. by an integrable function, then $I_{\\mu}^*(\\limsup_n f_n) \\ge \\limsup_n I_{\\mu}^*(f_n)$.'))
concepts.append((7, 'definition', 'Compatible Set for Product Measure',
    'compatible-set-for-product-measure',
    'A subset $C$ of $X \\times Y$ is compatible with measures $\\mu$ and $\\nu$ iff the iterated integrals $\\iint \\chi_C(x,y) d\\mu x d\\nu y$ and $\\iint \\chi_C(x,y) d\\nu y d\\mu x$ exist and are equal.'))
concepts.append((7, 'definition', 'Product Measure',
    'product-measure',
    'The product measure $\\mu \\otimes \\nu$ on the product $\\delta$-ring $\\mathcal{A} \\otimes \\mathcal{B}$ is defined by $\\mu \\otimes \\nu(C) = \\iint \\chi_C(x, y) d\\mu x d\\nu y$ for each compatible set $C$. It is the unique measure on $\\mathcal{A} \\otimes \\mathcal{B}$ satisfying $\\mu \\otimes \\nu(A \\times B) = \\mu(A)\\nu(B)$.'))
concepts.append((7, 'theorem', "Tonelli's Theorem",
    'tonellis-theorem',
    'If $f$ is a non-negative $\\mu \\otimes \\nu$ integrable$^*$ function, then the iterated integrals of $f$ exist and equal $I_{\\mu \\otimes \\nu}^*(f)$. That is, $I_{\\mu \\otimes \\nu}^*(f) = I_{\\mu}^* \\circ E^{\\nu}(f) = I_{\\nu}^* \\circ E_{\\mu}(f)$.'))
concepts.append((7, 'theorem', "Fubini's Theorem",
    'fubinis-theorem',
    'Let $\\mu$ and $\\nu$ be measures and let $(\\mu \\otimes \\nu)^\\vee$ be the completion of the product measure. Then $\\int f(x,y) d\\mu \\otimes \\nu(x,y) = \\int (\\int f(x,y) d\\nu y) d\\mu x$ for all $f \\in L_1(\\mu \\otimes \\nu)$, and also for $f \\in L_1((\\mu \\otimes \\nu)^\\vee)$ provided $\\nu$ is complete.'))

# Chapter 7 Supplement: Borel Product Measure
concepts.append((7, 'lemma', 'Hypercontinuity of Regular Borel Measures',
    'hypercontinuity-of-regular-borel-measures',
    'Suppose $\\lambda$ is a regular Borel measure for $Z$, $K$ is compact, $\\{f_\\alpha\\}_{\\alpha \\in D}$ is a decreasing net of non-negative u.s.c. functions vanishing outside $K$, and $f = \\inf_\\alpha f_\\alpha$. Then each $f_\\alpha$ and $f$ are $\\lambda$ integrable and $I_\\lambda(f) = \\inf_\\alpha I_\\lambda(f_\\alpha)$.'))
concepts.append((7, 'lemma', 'Compatibility of Limits of Decreasing Compact Nets',
    'compatibility-of-limits-of-decreasing-compact-nets',
    'If $\\{A_\\alpha\\}_{\\alpha \\in D}$ is a decreasing net of compact sets, each compatible with $\\mu$ and $\\nu$, and $A = \\bigcap_{\\alpha} A_\\alpha$, then $A$ is compatible and $\\iint \\chi_A d\\nu d\\mu = \\lim_\\alpha \\iint \\chi_{A_\\alpha} d\\nu d\\mu$.'))
concepts.append((7, 'theorem', 'Borel Product Measure Theorem',
    'borel-product-measure-theorem',
    'Each member $B$ of $\\mathcal{B}^{\\delta}(X \\times Y)$ is compatible with regular Borel measures $\\mu$ and $\\nu$, and each iterated integral of $\\chi_B$ is $\\mu \\otimes_{\\mathcal{B}} \\nu(B)$. The Borel product $\\mu \\otimes_{\\mathcal{B}} \\nu$ is a regular Borel measure that extends $\\mu \\otimes \\nu$, unique with respect to extending the map $D \\times E \\mapsto \\mu(D)\\nu(E)$ on compact rectangles.'))
concepts.append((7, 'proposition', 'Tonelli and Fubini Theorems for Borel Product',
    'tonelli-fubini-for-borel-product',
    'Let $\\mu$ and $\\nu$ be regular Borel measures for locally compact Hausdorff spaces. (Tonelli) If $f \\ge 0$ is locally Borel measurable with $\\sigma$-compact support, then the iterated integrals equal the extended integral w.r.t. $\\mu \\otimes_{\\mathcal{B}} \\nu$. (Fubini) If $f \\in L_1(\\mu \\otimes_{\\mathcal{B}} \\nu)$, then $\\int f d\\mu \\otimes_{\\mathcal{B}} \\nu = \\iint f(x,y) d\\mu x d\\nu y = \\iint f(x,y) d\\nu y d\\mu x$.'))

# Chapter 8: Measures* and Mappings
concepts.append((8, 'definition', 'Measure in the Extended Sense',
    'measure-in-extended-sense',
    'A measure$^*$ is a non-negative, countably additive, $\\mathbb{R}^*$ valued function $\\mu$ on a $\\delta$-ring $\\mathcal{A}$ with $\\mu(\\varnothing) = 0$. A measure is a finite valued measure$^*$.'))
concepts.append((8, 'definition', 'Canonical Extension of a Measure',
    'canonical-extension-of-measure',
    'The canonical extension $\\mu_{\\#}$ of a measure (or measure$^*$) $\\mu$ on $\\mathcal{A}$ is defined by $\\mu_{\\#}(B) = \\sup\\{\\mu(A): A \\in \\mathcal{A}, A \\subset B\\}$ for each $B$ in the $\\sigma$-field $\\mathcal{LA}$ of locally $\\mathcal{A}$ measurable sets.'))
concepts.append((8, 'proposition', 'Integrability with Respect to Canonical Extension',
    'integrability-with-respect-to-canonical-extension',
    'A real valued function $f$ is integrable w.r.t. $\\mu_{\\#}$ iff it is $\\mathcal{LA}$ measurable and agrees locally $\\mu$ a.e. with some $\\mu$ integrable function $g$, and in this case $\\int f d\\mu_{\\#} = \\int g d\\mu$.'))
concepts.append((8, 'lemma', 'Mapping Lemma for Measures',
    'mapping-lemma-for-measures',
    'If $T: X \\to Y$, $\\mu$ is a measure on $\\mathcal{A}$, $\\mathcal{B}$ is a $\\delta$-ring of subsets of $Y$ with $T^{-1}[B] \\in \\mathcal{LA}$ for all $B \\in \\mathcal{B}$, then the image measure $T\\mu(B) = \\mu_{\\#}(T^{-1}[B])$ satisfies $\\int f dT\\mu = \\int f \\circ T d\\mu_{\\#}$ for all non-negative $\\mathcal{B}$ $\\sigma$-simple $f$.'))
concepts.append((8, 'proposition', 'Images of Lambda Under Smooth Maps',
    'images-of-lambda-under-smooth-maps',
    'If $T$ is a continuously differentiable map of $(a:b)$ onto $(\\alpha:\\beta)$ and $T\'$ is never zero, then the Borel image $T_{\\mathcal{B}} \\Lambda_{(a:b)}$ is the indefinite integral $|(T^{-1})\'|.\\Lambda_{(\\alpha:\\beta)}$.'))
concepts.append((8, 'theorem', "Lebesgue's Differentiation Theorem",
    'lebesgue-differentiation-theorem',
    'If $w \\in L_1(\\Lambda)$ and $\\mu = w.\\Lambda$, then the difference quotient $\\Delta_h \\mu(x)/\\Delta_h \\Lambda(x) = (1/h)\\int_x^{x+h} w(t) d\\Lambda t$ converges to $w$ both in $L_1(\\Lambda)$ norm and $\\Lambda$ almost everywhere as $h \\to 0$.'))
concepts.append((8, 'proposition', 'Stieltjes Integral Equals Measure Integral for Continuous Functions',
    'stieltjes-integral-equals-measure-integral-for-continuous',
    'If a bounded function $f$ on $[a:b]$ is Stieltjes integrable w.r.t. an increasing function $F$ and is also integrable w.r.t. the measure $\\mu$ induced by $F$ (in particular if $f$ is continuous), then $\\int_a^b f(t) dF(t) = \\int f d\\mu$.'))
concepts.append((8, 'proposition', 'Stieltjes Integral with Respect to an Integral Function',
    'stieltjes-integral-with-respect-to-integral-function',
    'Suppose $g \\ge 0$ is Riemann integrable on $[a:b]$ and $G(x) = \\int_a^x g(t)dt + c$. Then each Riemann integrable function $f$ is Stieltjes integrable w.r.t. $G$ over $[a:b]$ and $\\int_a^b f(t) dG(t) = \\int_a^b f(t) g(t) dt$.'))
concepts.append((8, 'lemma', 'Decomposition of Open Sets into Half-Open Cubes',
    'decomposition-of-open-sets-into-half-open-cubes',
    'Each open subset $W$ of $\\mathbb{R}^p$ is the union of a disjoint countable family of half-open cubes $Q$ of arbitrarily small diameter whose closures are subsets of $W$.'))
concepts.append((8, 'theorem', 'Change of Variables Formula for Borel Images',
    'change-of-variables-formula-for-borel-images',
    'If $T$ is a $C^1$ one-to-one map with non-vanishing Jacobian on an open subset $U$ of $\\mathbb{R}^p$ and $V = T[U]$, then $T_{\\mathcal{B}} \\Lambda_U = |\\det(T^{-1})\'|.\\Lambda_V$ and $\\int f d\\Lambda_V = \\int (f \\circ T)|\\det T\'| d\\Lambda_U$ for all $f \\in L_1(\\Lambda_V)$.'))
concepts.append((8, 'proposition', 'Indefinite Integral of Locally Integrable Function is Regular Borel Measure',
    'indefinite-integral-is-regular-borel-measure',
    'Suppose $\\mu$ is a regular Borel measure for a locally compact Hausdorff space $X$ and $f \\in L^+(X)$. Then the indefinite integral $f.\\mu$ is a regular Borel measure if $f$ is locally $\\mu$ integrable, and if $f$ is $\\mu$ integrable then $f.\\mu$ is totally finite.'))

# Chapter 9: Signed Measures and Indefinite Integrals
concepts.append((9, 'definition', 'Signed Measure',
    'signed-measure',
    'A signed measure is a real (finite) valued, countably additive function on a $\\delta$-ring $\\mathcal{A}$.'))
concepts.append((9, 'lemma', 'Existence of Positive Subset for Signed Measure',
    'existence-of-positive-subset-for-signed-measure',
    'If $\\mu$ is a signed measure on $\\mathcal{A}$, $A \\in \\mathcal{A}$ and $\\mu(A) > 0$, then $A$ contains a $\\mu$ positive set $B$ with $\\mu(B) \\ge \\mu(A)$.'))
concepts.append((9, 'theorem', 'Hahn Decomposition Theorem',
    'hahn-decomposition-theorem',
    'If $\\mu$ is a signed measure on a $\\delta$-ring $\\mathcal{A}$, then for each $A$ in $\\mathcal{A}$ there is a $\\mu$ positive set $A^+ \\subset A$ and a $\\mu$ negative set $A^- \\subset A$ such that $A^+ \\cap A^- = \\varnothing$, $A^+ \\cup A^- = A$, and $\\mu(A^+) = \\sup\\{\\mu(B): B \\subset A, B \\in \\mathcal{A}\\}$.'))
concepts.append((9, 'theorem', 'Jordan Decomposition Theorem',
    'jordan-decomposition-theorem',
    'Each signed measure $\\mu$ on a $\\delta$-ring $\\mathcal{A}$ can be written uniquely as $\\mu = \\mu^+ - \\mu^-$ where $\\mu^+$ and $\\mu^-$ are measures on $\\mathcal{A}$ that are mutually singular. Moreover $\\mu^+ = \\mu \\lor 0$ and $\\mu^- = (-\\mu) \\lor 0$ in the vector lattice of signed measures.'))
concepts.append((9, 'definition', 'Absolute Continuity and Singularity of Measures',
    'absolute-continuity-and-singularity-of-measures',
    'A measure $\\nu$ on $\\mathcal{A}$ is absolutely continuous w.r.t. $\\mu$ on $\\mathcal{A}$, $\\nu \\prec \\mu$, iff $\\nu(A) = 0$ whenever $\\mu(A) = 0$. Measures $\\mu$ and $\\nu$ are mutually singular, $\\mu \\perp \\nu$, iff they have disjoint carriers.'))
concepts.append((9, 'theorem', 'Lebesgue Decomposition Theorem',
    'lebesgue-decomposition-theorem',
    'Suppose $\\mu$ and $\\nu$ are measures on a $\\delta$-ring $\\mathcal{A}$, $\\nu_s(A) = \\sup\\{\\nu(B): B \\subset A, B \\in \\mathcal{A}, \\mu(B) = 0\\}$ and $\\nu_c = \\nu - \\nu_s$. Then $\\nu_s$ and $\\nu_c$ are measures, $\\nu_s$ is locally $\\perp$ to $\\nu_c$ and to $\\mu$, and $\\nu_c \\prec \\mu$.'))
concepts.append((9, 'theorem', 'Radon-Nikodym Theorem',
    'radon-nikodym-theorem',
    'If $\\mu$ and $\\nu$ are measures on a $\\delta$-ring $\\mathcal{A}$ and $\\nu \\prec \\mu$, then $\\nu = f.\\mu$ for some locally $\\mu$ integrable, locally $\\mathcal{A}$ measurable function $f$. For each $A$ in $\\mathcal{A}$, $\\nu(A) = \\int_A f d\\mu$. The function $f = d\\nu/d\\mu$ is unique up to locally $\\mu$ null sets.'))
concepts.append((9, 'definition', 'Decomposable Measure',
    'decomposable-measure',
    'A measure $\\mu$ on a $\\delta$-ring $\\mathcal{A}$ is decomposable iff there exists a decomposition for $\\mu$: a disjoint family $\\mathcal{D}$ in $\\mathcal{A}$ such that a set is locally $\\mathcal{A}$ measurable iff its intersection with each $D \\in \\mathcal{D}$ belongs to $\\mathcal{A}$, and a member $A$ of $\\mathcal{A}$ has $\\mu$ measure zero iff $\\mu(A \\cap D) = 0$ for all $D \\in \\mathcal{D}$.'))
concepts.append((9, 'lemma', 'Patchwork Lemma',
    'patchwork-lemma-for-decomposable-measures',
    'Suppose $\\mu$ is a measure on $\\mathcal{A}$ and $\\mathcal{D}$ is a decomposition for $\\mu$. Then: (i) if $f_D$ is $\\mathcal{LA}$ measurable with support $D$ for each $D \\in \\mathcal{D}$, then $f = \\sum_D f_D$ is $\\mathcal{LA}$ measurable; (ii) if $\\nu \\prec \\mu$, then $\\nu(C) = \\sum_{D \\in \\mathcal{D}} \\nu(C \\cap D)$ for each $C \\in \\mathcal{B}$.'))
concepts.append((9, 'corollary', 'Global Hahn Decomposition for Decomposable Signed Measures',
    'global-hahn-decomposition-for-decomposable-signed-measures',
    'If $\\nu$ is a signed measure and its variation $V_\\nu$ is decomposable, then there is a Hahn decomposition of $X$ for $\\nu$.'))
concepts.append((9, 'lemma', 'Maximal Disjoint Family of Tight Sets for Borel Measures',
    'maximal-disjoint-family-of-tight-sets-for-borel-measures',
    'If $\\mu$ is a regular Borel measure for a locally compact Hausdorff space $X$ and $\\mathcal{K}$ is a maximal disjoint family of $\\mu$ tight sets, then each member of $\\mathcal{B}^{\\delta}(X)$ intersects only countably many members of $\\mathcal{K}$ and $\\bigcup \\mathcal{K}$ is a carrier for $\\mu$.'))
concepts.append((9, 'corollary', 'Radon-Nikodym Theorem for Regular Borel Measures',
    'radon-nikodym-theorem-for-regular-borel-measures',
    'A signed measure that is absolutely continuous with respect to a regular Borel measure $\\mu$ for a locally compact space is an indefinite integral w.r.t. $\\mu$ of a locally Borel real valued function.'))
concepts.append((9, 'theorem', 'Uniqueness of Haar Measure',
    'uniqueness-of-haar-measure',
    'If $\\eta$ and $\\nu$ are left Haar measures for a locally compact Hausdorff topological group $G$, then $\\eta = k\\nu$ for some positive real number $k$.'))
concepts.append((9, 'proposition', 'Construction and Properties of the Modular Function',
    'construction-and-properties-of-modular-function',
    'If $\\eta$ is a left Haar measure for $G$, there is a continuous homomorphism $\\Delta: G \\to (\\mathbb{R}^+, \\times)$ (the modular function) such that $\\int f(xb) d\\eta x = \\Delta(b) \\int f(x) d\\eta x$ for all $b \\in G$ and $f \\in L_1(\\eta)$. The group $G$ is unimodular iff $\\Delta \\equiv 1$.'))
concepts.append((9, 'proposition', 'Right Haar Measure as Indefinite Integral',
    'right-haar-measure-as-indefinite-integral',
    'The right Haar measure $\\rho$ corresponding to a left Haar measure $\\eta$ (defined by $\\rho(E) = \\eta(E^{-1})$) agrees on $\\mathcal{B}^{\\delta}(G)$ with the indefinite integral $\\Delta.\\eta$. Consequently $\\rho$ and $\\eta$ are mutually absolutely continuous.'))

# Chapter 10: Banach Spaces
concepts.append((10, 'definition', 'Banach Space',
    'banach-space-definition',
    'A Banach space is a (real or complex) vector space $E$ with a norm $\\|\\|$ such that $E$ is a complete metric space under the metric $(u,v) \\mapsto \\|u - v\\|$.'))
concepts.append((10, 'lemma', 'Representation Lemma for Signed Measures on Simple Functions',
    'representation-lemma-for-signed-measures-on-simple-functions',
    'Suppose $\\mu$ is a signed measure on a $\\delta$-ring $\\mathcal{A}$, $\\|\\mu\\|_V < \\infty$, and $S$ is the class of $\\mathcal{A}$ $\\sigma$-simple functions with finite supremum norm. Then each $f \\in S$ is $\\mu$ integrable, $|\\int f d\\mu| \\le \\|f\\|_X \\|\\mu\\|_V$, and the linear functional $\\phi(f) = \\int f d\\mu$ satisfies $\\|\\phi\\| = \\|\\mu\\|_V$.'))
concepts.append((10, 'theorem', 'Riesz Representation Theorem for C_0(R)',
    'riesz-representation-theorem-for-c0-r',
    'For each bounded linear functional $\\phi$ on $C_0(\\mathbb{R})$ there is a unique signed Borel measure $\\mu$ for $\\mathbb{R}$ such that $\\phi(f) = \\int f d\\mu$ for all $f \\in C_0(\\mathbb{R})$, and $\\|\\phi\\| = \\|\\mu\\|_V$.'))
concepts.append((10, 'lemma', 'Norm of Linear Functional Represented by L_q Function',
    'norm-of-linear-functional-represented-by-lq-function',
    'Suppose $\\mu$ is a measure on $\\mathcal{A}$, $1 \\le p \\le \\infty$, $q$ is conjugate to $p$, $g$ is $\\mathcal{A}$ $\\sigma$-simple with $gf \\in L_1(\\mu)$ for all $\\mathcal{A}$ simple $f$, and $\\phi_g(f) = \\int gf d\\mu$. Then $\\|\\phi_g\\| = \\|g\\|_q$.'))
concepts.append((10, 'theorem', 'Representation Theorem for L_p(mu) Dual',
    'representation-theorem-for-lp-dual',
    'Suppose $\\mu$ is a measure on $\\mathcal{A}$, $p$ and $q$ are conjugate indices, $1 \\le p < \\infty$. If $p > 1$, or if $p = 1$ and $X \\in \\mathcal{A}_\\sigma$, then the map $g \\mapsto \\phi_g$ where $\\phi_g(f) = \\int fg d\\mu$ is an isometric isomorphism of $L_q(\\mu)$ onto $L_p(\\mu)^*$.'))
concepts.append((10, 'lemma', 'Representation of Bounded Linear Functionals on Simple Functions',
    'representation-of-bounded-linear-functionals-on-simple-functions',
    'If $\\mathcal{B}$ is a ring of sets, $\\phi \\in (L^{\\mathcal{B}})^*$ and $\\nu(B) = \\phi(\\chi_B)$ for $B \\in \\mathcal{B}$, then $\\nu$ is finitely additive and $\\|\\nu\\|_V = \\|\\phi\\|$. Conversely, the map $\\nu \\mapsto I^\\nu$ is a linear isometric surjection of $FA(\\mathcal{B})$ onto $(L^{\\mathcal{B}})^*$.'))
concepts.append((10, 'theorem', 'Riesz Representation Theorem for C_0(X)',
    'riesz-representation-theorem-for-c0-x',
    'For each bounded linear functional $\\phi$ on $C_0(X)$, where $X$ is a locally compact Hausdorff space, there is a unique regular Borel signed measure $\\mu$ of finite total variation such that $\\phi(f) = \\int f d\\mu$ for all $f \\in C_0(X)$ and $\\|\\phi\\| = \\|\\mu\\|_V$.'))
concepts.append((10, 'theorem', 'Representation Theorem for L_1(mu)* for Decomposable Measures',
    'representation-theorem-for-l1-dual-decomposable',
    'If $\\mu$ is a decomposable measure and $\\phi \\in L_1(\\mu)^*$, then there is a member $g \\in L_{\\infty}(\\mu)$ such that $\\phi(f) = \\int gf d\\mu$ for all $f \\in L_1(\\mu)$. The map $g \\mapsto \\phi_g$ is an isometric isomorphism of $L_{\\infty}(\\mu)$ onto $L_1(\\mu)^*$.'))
concepts.append((10, 'theorem', 'Hahn-Banach Extension Theorem',
    'hahn-banach-extension-theorem',
    'Suppose $F$ is a subspace of a real vector space $E$ and $p$ is a non-negative real valued function on $E$ such that $p(x + y) \\le p(x) + p(y)$ and $p(tx) = tp(x)$ for all $x, y \\in E$ and $t \\ge 0$. Then each linear functional $\\varphi$ on $F$ with $\\varphi \\le p$ extends to a linear functional $\\varphi\'$ on $E$ with $\\varphi\' \\le p$.'))
concepts.append((10, 'corollary', 'Evaluation Map into Second Adjoint is Linear Isometry',
    'evaluation-map-into-second-adjoint-is-linear-isometry',
    'The evaluation map $x \\mapsto \\mathcal{E}_x$ of a semi-normed space $E$ into its second adjoint $E^{**}$ is a linear isometry (i.e., $\\|\\mathcal{E}_x\\| = \\|x\\|$ for all $x$).'))
concepts.append((10, 'definition', 'Strongly Measurable Banach-Space-Valued Function',
    'strongly-measurable-banach-space-valued-function',
    'A function $f: X \\to E$, where $E$ is a Banach space, is strongly measurable iff $f$ is $\\mathcal{LA} - \\mathcal{B}_c(E)$ measurable, where $\\mathcal{B}_c(E)$ is the strong Borel $\\sigma$-field for $E$ generated by the open sets of $E$.'))
concepts.append((10, 'definition', 'Bochner Integrable Function',
    'bochner-integrable-function',
    'A function $f: X \\to E$ to a Banach space $E$ is Bochner integrable iff $f(x) = \\sum_n \\chi_{A_n}(x) a_n$ for all $x$, with $A_n \\in \\mathcal{A}$, $a_n \\in E$, and $\\sum_n \\mu(A_n)\\|a_n\\| < \\infty$. The Bochner integral is $\\int f d\\mu = \\sum_n \\mu(A_n) a_n$.'))
concepts.append((10, 'theorem', 'Sigma-Simple Representation of Strongly Measurable Functions',
    'sigma-simple-representation-of-strongly-measurable-functions',
    'If $f$ is a strongly measurable $E$-valued function with separable range and support in $\\mathcal{A}_{\\sigma}$, then there exist $\\{A_n\\}_n$ in $\\mathcal{A}$ and $\\{a_n\\}_n$ in $E$ such that $f(x) = \\sum_n \\chi_{A_n}(x) a_n$ and $\\|f(x)\\| \\le \\sum_n \\chi_{A_n}(x)\\|a_n\\| \\le \\|f(x)\\| + \\sum_k e_k \\chi_{C_k}(x)$ for all $x$.'))
concepts.append((10, 'theorem', 'Completeness of L_1(mu, E) for Bochner Integral',
    'completeness-of-l1-mu-e-for-bochner-integral',
    'If $E$ is a Banach space and $\\mu$ is a measure, then each swiftly convergent sequence in $L_1(\\mu, E)$ converges pointwise a.e. and in norm to a member of $L_1(\\mu, E)$, and consequently $L_1(\\mu, E)$ is a Banach space.'))

# Now create all the files
stats = {'theorem': 0, 'definition': 0, 'lemma': 0, 'proposition': 0, 'corollary': 0}

tex_map = {'theorem': 'theorem.tex', 'definition': 'definition.tex',
           'lemma': 'lemma.tex', 'proposition': 'proposition.tex',
           'corollary': 'corollary.tex'}

domain_map = {'theorem': 'analysis', 'definition': 'analysis', 'lemma': 'analysis',
              'proposition': 'analysis', 'corollary': 'analysis'}

for (ch, ctype, title_en, slug, statement) in concepts:
    folder = os.path.join(OUT_DIR, slug)
    os.makedirs(folder, exist_ok=True)

    tex_file = tex_map.get(ctype, 'theorem.tex')
    ch_str = str(ch) if ch is not None else ''

    yaml_data = {
        'id': slug,
        'title_en': title_en,
        'title_zh': '',
        'type': ctype,
        'domain': 'analysis',
        'subdomain': 'measure-theory',
        'difficulty': 'intermediate' if ch >= 3 else 'basic',
        'tags': [],
        'depends_on': {'required': [], 'recommended': [], 'suggested': []},
        'proof_deps': {},
        'source_books': [{
            'book_id': 'GTM116',
            'author': 'John L. Kelley, T.P. Srinivasan',
            'title': 'Measure and Integral',
            'chapter': ch_str,
            'section': '',
            'pages': '',
            'role_in_book': ''
        }],
        'content_hash': hashlib.md5(statement.encode()).hexdigest()[:16],
        'extraction_date': '2026-06-24',
        'extraction_agent': 'v7-strict'
    }

    with open(os.path.join(folder, 'concept.yaml'), 'w') as f:
        yaml.dump(yaml_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    with open(os.path.join(folder, tex_file), 'w') as f:
        f.write(statement + '\n')

    intro = f"""---
role: introduce
locale: en
content_hash: {hashlib.md5(statement.encode()).hexdigest()[:16]}
written_against: ""
---
{title_en} from Chapter {ch_str} of Kelley and Srinivasan's \\textit{{Measure and Integral}} (GTM 116)."""

    with open(os.path.join(folder, 'introduce.en.md'), 'w') as f:
        f.write(intro + '\n')

    stats[ctype] = stats.get(ctype, 0) + 1

total = sum(stats.values())
print(f"Total concepts extracted: {total}")
for k, v in sorted(stats.items()):
    print(f"  {k}: {v}")
print(f"Output directory: {OUT_DIR}")
