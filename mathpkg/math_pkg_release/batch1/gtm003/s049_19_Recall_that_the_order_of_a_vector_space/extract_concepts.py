#!/usr/bin/env python3
"""Generate concept files for GTM003 s049 section."""
import os, yaml, hashlib, json

BASE = "/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch1/gtm003/s049_19_Recall_that_the_order_of_a_vector_space"
EXTR_DATE = "2026-06-27"
BOOK_ID = "gtm003"
BOOK_TITLE = "Topological Vector Spaces"
BOOK_AUTHOR = "H. H. Schaefer"
BOOK_EDITION = "2nd ed., 1999"
CHAPTER_V = "Chapter V"
CHAPTER_VI = "Chapter VI"
SECTION_EX = "Exercises"
SECTION_1 = "Section 1. Preliminaries"
SECTION_2 = "Section 2. C*-Algebras"

def slugify(s):
    return s.lower().replace(" ", "-").replace("(", "").replace(")", "").replace(",", "").replace("'", "").replace("*", "star").replace("^", "")

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def content_hash(*texts):
    h = hashlib.sha256("|".join(texts).encode()).hexdigest()[:16]
    return h

concepts = []

# ═══════════════ CHAPTER V EXERCISES ═══════════════

concepts.append({
    "slug": "archimedean-order",
    "title_en": "Archimedean Order of a Vector Space",
    "title_zh": "",
    "type": "definition",
    "domain": "analysis",
    "subdomain": "ordered-vector-spaces",
    "difficulty": "basic",
    "tags": ["archimedean", "order", "vector-lattice"],
    "depends_on": {"required": [], "recommended": ["order-of-a-vector-space", "positive-cone"], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter V","section":"Exercises, 19","pages":"","role_in_book":"Recall definition in exercise"}],
    "theorem_tex": r"""The order of a vector space $L$ is called \emph{Archimedean} if $x \leq 0$ whenever $x \leq n^{-1}y$ for all $n \in \mathbf{N}$ and some $y \in L$.""",
    "introduce_en": "An Archimedean order on a vector space is one where an element $x$ that is bounded above by arbitrarily small positive scalar multiples of a fixed element $y$ must be non-positive. This property is fundamental in the theory of ordered vector spaces and vector lattices.",
    "no_proof": True,
    "chapter_lbl": "V", "section_lbl": "Exercises",
    "exercises": []
})

concepts.append({
    "slug": "almost-archimedean-order",
    "title_en": "Almost Archimedean Order of a Vector Space",
    "title_zh": "",
    "type": "definition",
    "domain": "analysis",
    "subdomain": "ordered-vector-spaces",
    "difficulty": "basic",
    "tags": ["almost-archimedean", "order", "vector-lattice"],
    "depends_on": {"required": [], "recommended": ["archimedean-order"], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter V","section":"Exercises, 19","pages":"","role_in_book":"Recall definition in exercise"}],
    "theorem_tex": r"""The order of a vector space $L$ is called \emph{almost Archimedean} if $x = 0$ whenever $-n^{-1}y \leq x \leq n^{-1}y$ for all $n \in \mathbf{N}$ and some $y \in L$.""",
    "introduce_en": "An almost Archimedean order is a weakening of the Archimedean property. It requires that if an element $x$ is sandwiched between symmetric scalar multiples of a fixed element $y$ (i.e., $-n^{-1}y \leq x \leq n^{-1}y$) for all $n$, then $x$ must be zero. Every Archimedean order is almost Archimedean, but the converse does not hold.",
    "no_proof": True,
    "chapter_lbl": "V", "section_lbl": "Exercises",
    "exercises": []
})

concepts.append({
    "slug": "almost-archimedean-order-unit-normable",
    "title_en": "Almost Archimedean Ordered Space with Order Unit is Normable",
    "title_zh": "",
    "type": "proposition",
    "domain": "analysis",
    "subdomain": "ordered-topological-vector-spaces",
    "difficulty": "intermediate",
    "tags": ["almost-archimedean", "order-unit", "normability", "order-topology"],
    "depends_on": {"required": ["almost-archimedean-order", "order-unit"], "recommended": ["order-topology"], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter V","section":"Exercise 19(a)","pages":"","role_in_book":"Exercise problem"}],
    "theorem_tex": r"""If $L$ is almost Archimedean ordered and possesses an order unit, then $(L, \mathfrak{T}_O)$ is normable and $(L, \mathfrak{T}_O)' = L^b = L^+$.""",
    "introduce_en": "For an almost Archimedean ordered vector space possessing an order unit, the order topology $\mathfrak{T}_O$ is normable, and the topological dual coincides with both the order-bound dual $L^b$ and the order dual $L^+$.",
    "no_proof": False,
    "proof_text": r"""See the hint in the text: the order unit $e$ defines the Minkowski functional $p_e(x) = \inf\{\lambda > 0 : -\lambda e \leq x \leq \lambda e\}$. By the almost Archimedean property, $p_e$ is a norm. Equip $L$ with this norm; then $\mathfrak{T}_O$ coincides with the norm topology. The dual equalities follow from the order unit property and the fact that $\mathfrak{T}_O$ is the finest locally convex topology for which the order intervals are bounded (V, Section 2).""",
    "chapter_lbl": "V", "section_lbl": "Exercises",
    "exercises": []
})

concepts.append({
    "slug": "almost-archimedean-inductive-limit-characterization",
    "title_en": "Almost Archimedean Space as Inductive Limit",
    "title_zh": "",
    "type": "proposition",
    "domain": "analysis",
    "subdomain": "ordered-topological-vector-spaces",
    "difficulty": "advanced",
    "tags": ["almost-archimedean", "inductive-limit", "order-topology", "vector-lattice"],
    "depends_on": {"required": ["almost-archimedean-order", "inductive-limit-topology"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter V","section":"Exercise 19(b)","pages":"","role_in_book":"Exercise problem"}],
    "theorem_tex": r"""If $L$ is almost Archimedean ordered and $L^b$ distinguishes points in $L$, then $(L, \mathfrak{T}_O)$ can be characterized as an inductive limit in analogy to (6.3). If, in addition, $L$ is a vector lattice, then $(L, \mathfrak{T}_O)$ is a locally convex vector lattice (l.c.v.l.).""",
    "introduce_en": "When the order-bound dual $L^b$ separates points, the order topology makes $L$ into an inductive limit of normable spaces. If $L$ is additionally a vector lattice, the resulting topology is a locally convex vector lattice topology.",
    "no_proof": False,
    "proof_text": r"""The order-bound dual $L^b$ distinguishes points, so the natural embedding $L \to (L^b)^*$ holds. Represent $L$ as the inductive limit of the family of order ideals generated by order intervals $[-y, y]$ for $y \in L^+$, each equipped with the norm $p_y(x) = \inf\{\lambda > 0 : -\lambda y \leq x \leq \lambda y\}$. This is analogous to Theorem (6.3) in the text. When $L$ is a vector lattice, the cone is normal under this inductive limit topology, yielding a l.c.v.l.""",
    "chapter_lbl": "V", "section_lbl": "Exercises",
    "exercises": []
})

concepts.append({
    "slug": "almost-archimedean-lattice-with-distinguishing-dual-is-archimedean",
    "title_en": "Almost Archimedean Lattice with Point-Separating Order Dual is Archimedean",
    "title_zh": "",
    "type": "proposition",
    "domain": "analysis",
    "subdomain": "ordered-vector-spaces",
    "difficulty": "intermediate",
    "tags": ["almost-archimedean", "archimedean", "vector-lattice", "regular-order"],
    "depends_on": {"required": ["almost-archimedean-order", "archimedean-order"], "recommended": ["order-dual", "hausdorff-topology"], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter V","section":"Exercise 19(c)","pages":"","role_in_book":"Exercise problem"}],
    "theorem_tex": r"""If $L$ is an almost Archimedean ordered vector lattice such that $L^+$ distinguishes points in $L$, then the order of $L$ is Archimedean (hence regular).""",
    "introduce_en": "For an almost Archimedean ordered vector lattice, the additional condition that the order dual $L^+$ separates points forces the order to be genuinely Archimedean (and therefore regular). The key observation is that $\mathfrak{T}_O$ is Hausdorff and the positive cone is closed.",
    "no_proof": False,
    "proof_text": r"""Use part (b): the condition that $L^+$ distinguishes points implies $L^b$ also distinguishes points (since $L^+ \subset L^b$). By (b), $(L, \mathfrak{T}_O)$ is an inductive limit. Moreover, $\mathfrak{T}_O$ is Hausdorff because $L^b$ separates points, and the positive cone $L^+$ is closed in this topology. For an almost Archimedean space with closed cone and Hausdorff order topology, the order is necessarily Archimedean. Regularity follows from the Archimedean property in a vector lattice (cf. Chapter V, Section 1).""",
    "chapter_lbl": "V", "section_lbl": "Exercises",
    "exercises": []
})

concepts.append({
    "slug": "bounded-functions-inf-order-almost-archimedean",
    "title_en": "Bounded Real Functions with Inf-Order: Almost Archimedean but not Archimedean",
    "title_zh": "",
    "type": "example",
    "domain": "analysis",
    "subdomain": "ordered-vector-spaces",
    "difficulty": "intermediate",
    "tags": ["almost-archimedean", "archimedean", "counterexample", "function-space"],
    "depends_on": {"required": ["almost-archimedean-order", "archimedean-order"], "recommended": ["bounded-functions"], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter V","section":"Exercise 19(d)","pages":"","role_in_book":"Exercise problem - counterexample"}],
    "theorem_tex": r"""Let $T$ be a set containing at least two elements and let $E$ be the vector space (over $\mathbf{R}$) of all bounded real functions on $T$, ordered by the relation ``$g \leq f$ if either $f = g$ or $\inf\{f(t) - g(t): t \in T\} > 0$''. The order of $E$ is almost Archimedean, but not Archimedean.""",
    "introduce_en": "This example provides a concrete vector space whose order is almost Archimedean but not Archimedean, demonstrating that the two properties are distinct. The space consists of all bounded real-valued functions on a set $T$, equipped with a strict-infimum-based partial order.",
    "no_proof": False,
    "proof_text": r"""To show the order is almost Archimedean: Suppose $-n^{-1}y \leq x \leq n^{-1}y$ for all $n \in \mathbf{N}$ and some $y \in E$. Then for each $n$, either $x = n^{-1}y$ or $\inf\{n^{-1}y(t) - x(t)\} > 0$. If $x \neq 0$, pick $t_0 \in T$ with $x(t_0) \neq 0$. Then $x(t_0) \leq n^{-1}y(t_0)$ for all $n$, so $x(t_0) \leq 0$. Similarly $-n^{-1}y(t_0) \leq x(t_0)$, so $x(t_0) \geq 0$. Hence $x(t_0) = 0$, contradiction. Thus $x = 0$.

To show the order is not Archimedean: Take two distinct points $t_1, t_2 \in T$. Define $x(t_1) = -1$, $x(t_2) = 0$, and $x(t) = 0$ elsewhere. Define $y(t_1) = 0$, $y(t_2) = 1$, and $y(t) = 0$ elsewhere. Then $x \leq n^{-1}y$ for all $n$ (since at $t_1$, $x(t_1) = -1 < 0 = n^{-1}y(t_1)$; at $t_2$, $x(t_2) = 0 < n^{-1} = n^{-1}y(t_2)$; elsewhere $x = y = 0$), yet $x \not\leq 0$, violating the Archimedean property.""",
    "chapter_lbl": "V", "section_lbl": "Exercises",
    "exercises": []
})

concepts.append({
    "slug": "order-complete-vector-lattice-is-archimedean",
    "title_en": "Order Complete Vector Lattice is Archimedean Ordered",
    "title_zh": "",
    "type": "proposition",
    "domain": "analysis",
    "subdomain": "ordered-vector-spaces",
    "difficulty": "basic",
    "tags": ["order-complete", "archimedean", "vector-lattice"],
    "depends_on": {"required": ["archimedean-order", "order-completeness"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter V","section":"Exercise 19(e)","pages":"","role_in_book":"Exercise problem"}],
    "theorem_tex": r"""Every order complete vector lattice is Archimedean ordered.""",
    "introduce_en": "Order completeness (Dedekind completeness) of a vector lattice implies the Archimedean property. This is a fundamental structural relationship in the theory of vector lattices.",
    "no_proof": False,
    "proof_text": r"""Suppose $L$ is order complete and $x \leq n^{-1}y$ for all $n \in \mathbf{N}$ and some $y \in L$. Consider the set $A = \{n^{-1}y : n \in \mathbf{N}\}$. Then $\inf A$ exists in $L$ by order completeness. Since $x$ is a lower bound of $A$, we have $x \leq \inf A$. But $\inf A = 0$ (since $n^{-1}y \downarrow 0$ in any vector lattice by the Archimedean property of $\mathbf{R}$ acting via scalars). Thus $x \leq 0$, proving the order is Archimedean.""",
    "chapter_lbl": "V", "section_lbl": "Exercises",
    "exercises": []
})

# Exercise 20
concepts.append({
    "slug": "continuity-of-lattice-operations-ordered-lcs",
    "title_en": "Continuity of the Lattice Operations in an Ordered Locally Convex Space",
    "title_zh": "",
    "type": "proposition",
    "domain": "analysis",
    "subdomain": "ordered-topological-vector-spaces",
    "difficulty": "advanced",
    "tags": ["continuity", "lattice-operations", "ordered-lcs", "positive-cone"],
    "depends_on": {"required": ["ordered-locally-convex-space", "vector-lattice"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter V","section":"Exercise 20","pages":"","role_in_book":"Exercise problem"}],
    "theorem_tex": r"""Let $E$ be an ordered locally convex space over $\mathbf{R}$ whose positive cone is generating, and endow $E'$ with the topology of uniform convergence on order-bounded subsets of $E$. [Problem concerning continuity of the lattice operations; cf. Gordon, Peressini.]""",
    "introduce_en": "This exercise investigates conditions under which the lattice operations (supremum and infimum) are continuous in an ordered locally convex space with a generating positive cone. The dual $E'$ is equipped with the topology of uniform convergence on order-bounded sets.",
    "no_proof": False,
    "proof_text": r"""(Statement truncated in source material. See Gordon [1], Peressini [1] for the full treatment.) The typical approach is to examine the conditions under which the mappings $(x,y) \mapsto x \vee y$ and $(x,y) \mapsto x \wedge y$ are continuous. When the positive cone is generating and normal, and the space has the decomposition property, equicontinuity of order intervals yields the desired continuity. The dual statement concerns when the dual cone $E'_+$ is normal in the given dual topology.""",
    "chapter_lbl": "V", "section_lbl": "Exercises",
    "exercises": []
})

# Exercise 21
concepts.append({
    "slug": "finite-dim-archimedean-order-isomorphic-continuous-functions",
    "title_en": "Finite-Dimensional Archimedean Ordered Space Isomorphic to Continuous Functions on Finite Set",
    "title_zh": "",
    "type": "proposition",
    "domain": "analysis",
    "subdomain": "ordered-vector-spaces",
    "difficulty": "intermediate",
    "tags": ["finite-dimensional", "archimedean", "isomorphism", "continuous-functions"],
    "depends_on": {"required": ["archimedean-order"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter V","section":"Exercise 21","pages":"","role_in_book":"Exercise problem"}],
    "theorem_tex": r"""If $L$ is Archimedean ordered, $L$ is isomorphic with $\mathcal{C}_{\mathbf{R}}(X)$, where $X$ contains exactly $n$ points (and $n = \dim L$).""",
    "introduce_en": "A finite-dimensional Archimedean ordered vector space of dimension $n$ is order-isomorphic to the space of continuous real-valued functions on a finite set of $n$ points, with the pointwise order. This shows that Archimedean finite-dimensional orders are essentially canonical.",
    "no_proof": False,
    "proof_text": r"""Use (8.5) from the text. In a finite-dimensional Archimedean ordered space, the positive cone is closed and generating. The extreme rays of the dual cone correspond to evaluation functionals at points of $X$. By choosing $n$ extreme rays, one obtains an isomorphism with $\mathcal{C}_{\mathbf{R}}(X)$ where $|X| = n$.""",
    "chapter_lbl": "V", "section_lbl": "Exercises",
    "exercises": []
})

concepts.append({
    "slug": "finite-dim-non-archimedean-classification",
    "title_en": "Classification of Finite-Dimensional Non-Archimedean Ordered Vector Spaces",
    "title_zh": "",
    "type": "proposition",
    "domain": "analysis",
    "subdomain": "ordered-vector-spaces",
    "difficulty": "advanced",
    "tags": ["finite-dimensional", "non-archimedean", "classification", "lexicographic-order"],
    "depends_on": {"required": ["archimedean-order", "lexicographic-order"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter V","section":"Exercise 21(b)","pages":"","role_in_book":"Exercise problem"}],
    "theorem_tex": r"""If $L$ is not Archimedean ordered, there exist integers $k, m$ such that $2 \leq k \leq n$, $m \geq 0$, $k + m = n$, and such that $L$ is isomorphic with $\mathbf{R}_0^k \times \mathbf{R}_0^m$, where the order of $\mathbf{R}_0^k$ is lexicographic and the order of $\mathbf{R}_0^m$ is canonical.""",
    "introduce_en": "Birkhoff's classification theorem: every finite-dimensional non-Archimedean ordered vector space decomposes as a direct product of a lexicographically ordered component $\mathbf{R}_0^k$ (capturing the non-Archimedean part) and a canonically ordered component $\mathbf{R}_0^m$. The parameter $k \geq 2$ measures the degree of non-Archimedeanity.",
    "no_proof": False,
    "proof_text": r"""By Birkhoff [1], Chapter XV, Theorem 1. The proof proceeds by analyzing the cone of the order-bound dual. Since $L$ is finite-dimensional and not Archimedean, the positive cone is not closed. Decompose $L$ as a direct sum of irreducible ordered spaces. The non-Archimedean component must be at least 2-dimensional and carries the lexicographic order. The remaining component has a closed (hence Archimedean) cone and is isomorphic to the canonical order on $\mathbf{R}^m$.""",
    "chapter_lbl": "V", "section_lbl": "Exercises",
    "exercises": []
})

# Exercise 22
concepts.append({
    "slug": "separable-al-space-isomorphic-l1",
    "title_en": "Separable AL-Space is Isomorphic to L1 of a Regular Borel Measure",
    "title_zh": "",
    "type": "theorem",
    "domain": "analysis",
    "subdomain": "banach-lattices",
    "difficulty": "advanced",
    "tags": ["AL-space", "separability", "L1-space", "Banach-lattice", "isomorphism"],
    "depends_on": {"required": ["AL-space", "L1-space"], "recommended": ["regular-borel-measure", "weak-order-unit"], "suggested": ["Radon-Nikodym-theorem"]},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter V","section":"Exercise 22(a)","pages":"","role_in_book":"Exercise problem"}],
    "theorem_tex": r"""Let $E$ be an (AL)-space. If (and only if) $E$ is separable, there exists a compact metrizable space $X$ such that $E$ is isomorphic (as a Banach lattice) with $L^1(\mu)$ where $\mu$ is a suitable regular Borel measure on $X$.""",
    "introduce_en": "A separable AL-space (abstract L-space) is always representable as a concrete $L^1(\mu)$ space on a compact metrizable space. This provides a Kakutani-type representation theorem for separable AL-spaces.",
    "no_proof": False,
    "proof_text": r"""Observe that $E$ possesses a weak order unit $x_0$ (since $E$ is separable, take $x_0$ with dense principal band). Note that $E$ is the band generated by $\{x_0\}$. By (8.6) (the Kakutani representation theorem for AL-spaces), $E$ is isomorphic as a Banach lattice to $L^1(\mu)$ where $\mu$ is a regular Borel measure on the Stone space $X$ of the Boolean algebra of components of $x_0$. Since $E$ is separable, $X$ is metrizable. The Radon-Nikodym theorem is used to establish the isomorphism.""",
    "chapter_lbl": "V", "section_lbl": "Exercises",
    "exercises": []
})

concepts.append({
    "slug": "al-space-bidual-measures-vanishing-first-category",
    "title_en": "AL-Space Bidual Identification and Measures Vanishing on First Category Sets",
    "title_zh": "",
    "type": "proposition",
    "domain": "analysis",
    "subdomain": "banach-lattices",
    "difficulty": "advanced",
    "tags": ["AL-space", "bidual", "regular-Borel-measures", "first-category"],
    "depends_on": {"required": ["AL-space", "bidual"], "recommended": ["regular-borel-measure"], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter V","section":"Exercise 22(b)","pages":"","role_in_book":"Exercise problem"}],
    "theorem_tex": r"""If $E''$ is identified with the Banach lattice of all bounded, signed, regular Borel measures on a compact space $X$ (Chapter II, Section 2, Example 3), then the measures in $E$ are exactly those vanishing on each subset of first category in $X$.""",
    "introduce_en": "For a separable AL-space $E$ represented as $L^1(\mu)$, its bidual $E''$ can be identified with the space of bounded signed regular Borel measures on the compact space $X$. Under this identification, the original space $E$ consists precisely of those measures that vanish on meager (first category) subsets of $X$.",
    "no_proof": False,
    "proof_text": r"""Using the identification from (8.6), $E''$ corresponds to the Banach lattice of all bounded, signed, regular Borel measures on the Stone space $X$. For any $\nu \in E''$, $\nu$ belongs to $E$ (i.e., is $\sigma$-order continuous) if and only if $\nu(N) = 0$ for every subset $N \subset X$ of first category. This follows from the fact that the $\sigma$-order continuous linear functionals on $\mathcal{C}(X)$ correspond precisely to measures vanishing on first category sets (Kelley-Namioka [1]).""",
    "chapter_lbl": "V", "section_lbl": "Exercises",
    "exercises": []
})

# Exercise 23
concepts.append({
    "slug": "crx-order-complete-iff-extremally-disconnected",
    "title_en": "C_R(X) is Order Complete iff X is Extremally Disconnected",
    "title_zh": "",
    "type": "theorem",
    "domain": "analysis",
    "subdomain": "banach-lattices",
    "difficulty": "advanced",
    "tags": ["order-complete", "extremally-disconnected", "stonian-space", "continuous-functions"],
    "depends_on": {"required": ["order-completeness", "extremally-disconnected"], "recommended": ["banach-lattice", "continuous-functions"], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter V","section":"Exercise 23","pages":"","role_in_book":"Exercise problem"}],
    "theorem_tex": r"""If $X$ is a compact space, the Banach lattice $\mathcal{C}_{\mathbf{R}}(X)$ is order complete exactly when $X$ is extremally disconnected (a Stonian space).""",
    "introduce_en": "The order completeness of the Banach lattice of real-valued continuous functions on a compact space $X$ is equivalent to $X$ being extremally disconnected (also called Stonian). This connects the order-theoretic property of order completeness with the topological property of extremal disconnectedness.",
    "no_proof": False,
    "proof_text": r"""If $X$ is extremally disconnected, the closure of every open set is open. For any bounded subset $A \subset \mathcal{C}_{\mathbf{R}}(X)$ bounded above, the pointwise supremum $s(x) = \sup\{f(x) : f \in A\}$ is upper semicontinuous, and by extremal disconnectedness its regularization is continuous, providing the supremum in $\mathcal{C}_{\mathbf{R}}(X)$.

Conversely, if $\mathcal{C}_{\mathbf{R}}(X)$ is order complete, then for any open set $U \subset X$, the characteristic function $\chi_U$ (as a lower semicontinuous function) is the supremum of $\{f \in \mathcal{C}_{\mathbf{R}}(X) : 0 \leq f \leq \chi_U\}$, so its closure $\overline{U}$ must be open, hence $X$ is extremally disconnected.""",
    "chapter_lbl": "V", "section_lbl": "Exercises",
    "exercises": []
})

concepts.append({
    "slug": "crx-not-dual-unless-stonian-not-reflexive-unless-finite",
    "title_en": "C_R(X) Cannot be a Dual Banach Space Unless X is Stonian, Not Reflexive Unless X is Finite",
    "title_zh": "",
    "type": "corollary",
    "domain": "analysis",
    "subdomain": "banach-lattices",
    "difficulty": "advanced",
    "tags": ["dual-banach-space", "reflexive", "stonian-space", "continuous-functions"],
    "depends_on": {"required": ["crx-order-complete-iff-extremally-disconnected"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter V","section":"Exercise 23","pages":"","role_in_book":"Corollary in exercise"}],
    "theorem_tex": r"""Infer from the above that $\mathcal{C}_{\mathbf{R}}(X)$ cannot be a dual Banach space, unless $X$ is Stonian, and not reflexive, unless $X$ is finite.""",
    "introduce_en": "Two important consequences of the order completeness characterization: the Banach space $\mathcal{C}_{\mathbf{R}}(X)$ is a dual space only if $X$ is extremally disconnected (Stonian), and is reflexive only in the trivial case where $X$ is finite.",
    "no_proof": False,
    "proof_text": r"""Every dual Banach space is order complete (as a Banach lattice, the predual being a sublattice). Hence if $\mathcal{C}_{\mathbf{R}}(X)$ is a dual Banach space, it is order complete, so by the previous result $X$ is Stonian. For reflexivity: if $\mathcal{C}_{\mathbf{R}}(X)$ is reflexive, it is a dual space (its own bidual), so $X$ is Stonian. But a reflexive $\mathcal{C}_{\mathbf{R}}(X)$ must also have the Dunford-Pettis property, which forces $X$ to be finite. Alternatively, an infinite extremally disconnected compact space admits a non-atomic measure, generating a copy of $L^1$ in the dual, contradicting reflexivity.""",
    "chapter_lbl": "V", "section_lbl": "Exercises",
    "exercises": []
})

# Exercise 24
concepts.append({
    "slug": "ordered-summability-in-algebra-with-unit",
    "title_en": "Ordered Summability in an Algebra with Unit",
    "title_zh": "",
    "type": "proposition",
    "domain": "analysis",
    "subdomain": "ordered-algebras",
    "difficulty": "advanced",
    "tags": ["ordered-algebra", "order-unit", "l1-summability"],
    "depends_on": {"required": ["ordered-algebra", "order-unit"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter V","section":"Exercise 24","pages":"","role_in_book":"Exercise problem"}],
    "theorem_tex": r"""Let $A$ be an algebra over $\mathbf{R}$ with unit $e$ and denote by $A_0$ the underlying vector space of $A$ (Chapter IV).""",
    "introduce_en": "This exercise concerns an algebra $A$ over $\mathbf{R}$ with unit $e$, and investigates ordered structures on the underlying vector space $A_0$. (The full statement is truncated in the source; see Chapter IV, Exercise 40 for related material on normed algebras.)",
    "no_proof": False,
    "proof_text": r"""The problem statement is partially truncated in the source text. The exercise likely concerns whether an order structure compatible with the algebra operations exists. The underlying vector space $A_0$ provides the linear structure upon which the order and algebraic structures are built. See Chapter IV, Exercise 40 for context on spectral algebras and normed algebras.""",
    "chapter_lbl": "V", "section_lbl": "Exercises",
    "exercises": []
})

# Exercise 25
concepts.append({
    "slug": "spectral-algebra-order-characterization",
    "title_en": "Spectral Algebra Characterization via Order",
    "title_zh": "",
    "type": "proposition",
    "domain": "analysis",
    "subdomain": "spectral-algebras",
    "difficulty": "advanced",
    "tags": ["spectral-algebra", "order-unit", "l1-summability"],
    "depends_on": {"required": ["spectral-algebra", "ordered-algebra"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter V","section":"Exercise 25(a)","pages":"","role_in_book":"Exercise problem"}],
    "theorem_tex": r"""There exists an order of $A$ such that (i) $A$ is an ordered algebra; (ii) $e$ is an order unit, and $[-e, e]$ is bounded; (iii) every positive sequence of type $\ell^1$ is order summable.""",
    "introduce_en": "A spectral algebra over $\mathbf{R}$ can be characterized order-theoretically: it admits an order making it an ordered algebra where the unit $e$ is an order unit, the order interval $[-e,e]$ is bounded, and every positive $\ell^1$-sequence is order summable.",
    "no_proof": False,
    "proof_text": r"""Use Exercise 24. The forward direction: in a spectral algebra, the order of self-adjoint elements is defined by the spectral measure. Conditions (i)-(iii) follow from the properties of the spectral measure. For the converse, the existence of such an order ensures that the algebra can be represented as $\mathcal{C}(X)$ for a suitable compact $X$ via the Gelfand transform, and the order summability condition ensures the spectral properties hold. See also Chapter IV, Exercise 40 for the definition of spectral algebra.""",
    "chapter_lbl": "V", "section_lbl": "Exercises",
    "exercises": []
})

concepts.append({
    "slug": "complex-spectral-algebra-real-subalgebra-characterization",
    "title_en": "Complex Spectral Algebra via Real Subalgebra",
    "title_zh": "",
    "type": "proposition",
    "domain": "analysis",
    "subdomain": "spectral-algebras",
    "difficulty": "advanced",
    "tags": ["complex-spectral-algebra", "real-subalgebra", "characterization"],
    "depends_on": {"required": ["spectral-algebra"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter V","section":"Exercise 25(b)","pages":"","role_in_book":"Exercise problem"}],
    "theorem_tex": r"""A locally convex algebra over $\mathbf{C}$ with unit $e$ is a spectral algebra if and only if there exists a real subalgebra $A_1$ containing $e$ such that each $a \in A$ has a unique representation $a = b + ic$ ($b, c \in A_1$), and such that $A_1$ is a spectral algebra over $\mathbf{R}$.""",
    "introduce_en": "A complex spectral algebra is precisely one that arises as the complexification of a real spectral algebra. Every element admits a unique decomposition $a = b + ic$ with $b, c$ belonging to a real spectral subalgebra $A_1$ containing the unit.",
    "no_proof": False,
    "proof_text": r"""Cf. (8.3) from the text. If $A$ is a complex spectral algebra, the self-adjoint elements $A_{sa}$ form a real spectral algebra $A_1$. Conversely, if $A_1$ is a real spectral algebra, its complexification $A_1 + iA_1$ is a complex spectral algebra. The spectral measure for a complex spectral algebra is obtained from the real spectral measure of $A_1$ by linear extension. The uniqueness of the decomposition $a = b + ic$ follows from the involution properties.""",
    "chapter_lbl": "V", "section_lbl": "Exercises",
    "exercises": []
})

concepts.append({
    "slug": "spectral-measure-support-and-topological-homomorphism",
    "title_en": "Spectral Measure Support and Topological Homomorphism Condition",
    "title_zh": "",
    "type": "proposition",
    "domain": "analysis",
    "subdomain": "spectral-measures",
    "difficulty": "advanced",
    "tags": ["spectral-measure", "support", "topological-homomorphism", "spectral-radius"],
    "depends_on": {"required": ["spectral-measure", "spectral-radius"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter V","section":"Exercise 25(c)","pages":"","role_in_book":"Exercise problem"}],
    "theorem_tex": r"""Let $\mu$ be a spectral measure on $X$ with range $A$. Define the support of $\mu$ to be the complement $X_0$ of the largest open set $G \subset X$ such that $\mu(f) = 0$ whenever $f$ has its support in $G$. Then $\mu$ induces a spectral measure $\mu_0$ on $X_0$ with range $A$ which is biunivocal. For $\mu_0$ to be a homeomorphism (equivalently, for $\mu$ to be a topological homomorphism), it is necessary and sufficient that $a \mapsto r(a)$ be continuous on $A$, where $r(a)$ denotes the spectral radius of $a \in A$.""",
    "introduce_en": "The support of a spectral measure $\mu$ is the complement of the largest open set on which $\mu$ vanishes. The induced spectral measure $\mu_0$ on the support is biunivocal (one-to-one between Borel sets and projections). The map $\mu_0$ is a homeomorphism precisely when the spectral radius function $a \mapsto r(a)$ is continuous on the range algebra $A$.",
    "no_proof": False,
    "proof_text": r"""Chapter IV, Exercise 40 provides the relevant definitions. The support $X_0$ defined as the complement of the largest open set $G$ where $\mu$ vanishes is well-defined by taking the union of all open sets $U$ with $\mu(f) = 0$ for all $f$ supported in $U$. The induced measure $\mu_0$ on $X_0$ is biunivocal because on $X_0$ no non-empty open set is $\mu$-null. For $\mu_0$ to be a homeomorphism onto its image, continuity of $a \mapsto r(a)$ is necessary and sufficient: this property ensures that the Gelfand topology coincides with the original topology on the spectrum.""",
    "chapter_lbl": "V", "section_lbl": "Exercises",
    "exercises": []
})

concepts.append({
    "slug": "spectral-element-definition",
    "title_en": "Spectral Element of a Locally Convex Algebra",
    "title_zh": "",
    "type": "definition",
    "domain": "analysis",
    "subdomain": "spectral-theory",
    "difficulty": "intermediate",
    "tags": ["spectral-element", "spectral-operator", "spectrum"],
    "depends_on": {"required": ["spectral-algebra", "locally-convex-algebra"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter V","section":"Exercise 25(d)","pages":"","role_in_book":"Definition in exercise"}],
    "theorem_tex": r"""If $A$ is a locally convex algebra, an element $a \in A$ is called a \emph{spectral element} if $a$ is contained in a spectral subalgebra of $A$. If $a$ is a spectral element of $A$ and $\mu$ is a spectral measure on $X$ such that $a = \mu(f)$, then $f(X)$ is the spectrum of $a$; that is, $f(X) = \sigma(a)$.""",
    "introduce_en": "A spectral element in a locally convex algebra is one that belongs to some spectral subalgebra. For endomorphism algebras of locally convex spaces, these are precisely the scalar-type spectral operators. The spectrum of such an element equals the range of the representing function under the spectral measure.",
    "no_proof": True,
    "chapter_lbl": "V", "section_lbl": "Exercises",
    "exercises": []
})

concepts.append({
    "slug": "spectral-measure-baire-extension",
    "title_en": "Extension of Spectral Measure to Bounded Baire Functions",
    "title_zh": "",
    "type": "proposition",
    "domain": "analysis",
    "subdomain": "spectral-measures",
    "difficulty": "advanced",
    "tags": ["spectral-measure", "Baire-functions", "extension", "Boolean-algebra-idempotents"],
    "depends_on": {"required": ["spectral-measure"], "recommended": ["Baire-functions", "Boolean-algebra"], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter V","section":"Exercise 25","pages":"","role_in_book":"Proposition in exercise"}],
    "theorem_tex": r"""There exists a unique extension $\bar{\mu}$ of a spectral measure $\mu$ to the Banach algebra $\mathcal{B}(X)$ of bounded Baire functions on $X$, such that $\bar{\mu}$ is an algebraic homomorphism of $\mathcal{B}(X)$ into $A$. Moreover, $\bar{\mu}$ induces a homomorphism of the Boolean algebra of Baire subsets of $X$ onto a $\sigma$-complete Boolean algebra of idempotents of $A$.""",
    "introduce_en": "Every spectral measure on a compact space $X$ extends uniquely to an algebraic homomorphism from the Banach algebra of bounded Baire functions into the range algebra. This extension maps the Boolean algebra of Baire sets onto a $\sigma$-complete Boolean algebra of idempotents (projections) in the algebra.",
    "no_proof": False,
    "proof_text": r"""Cf. Schaefer [9], II, Theorem 8. The spectral measure $\mu$ maps continuous functions to the algebra $A$. Since $\mathcal{B}(X)$ is the monotone sequential closure of $\mathcal{C}(X)$, the extension $\bar{\mu}$ is defined via limits of monotone sequences of continuous functions. The $\sigma$-completeness of the Boolean algebra of idempotents follows from the $\sigma$-additivity of the spectral measure and the properties of Baire functions under pointwise limits.""",
    "chapter_lbl": "V", "section_lbl": "Exercises",
    "exercises": []
})

# ═══════════════ CHAPTER VI, SECTION 1: PRELIMINARIES ═══════════════

concepts.append({
    "slug": "normed-algebra",
    "title_en": "Normed Algebra",
    "title_zh": "",
    "type": "definition",
    "domain": "analysis",
    "subdomain": "banach-algebras",
    "difficulty": "basic",
    "tags": ["normed-algebra", "submultiplicative-norm"],
    "depends_on": {"required": [], "recommended": ["algebra", "normed-space"], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter VI","section":"Section 1. Preliminaries","pages":"","role_in_book":"Fundamental definition"}],
    "theorem_tex": r"""An algebra $A$ (Chapter IV, Exercise 40) over the complex field $\mathbf{C}$ is called a \emph{normed algebra} if its underlying vector space $A_0$ is a normed space whose norm $x \mapsto \|x\|$ is \emph{submultiplicative}:
$$\|x y\| \leq \|x\| \|y\| \quad (x, y \in A).$$""",
    "introduce_en": "A normed algebra is an algebra over $\mathbf{C}$ whose underlying vector space carries a norm that is submultiplicative. This compatibility condition between the algebraic multiplication and the norm is fundamental to the theory of Banach algebras and operator algebras.",
    "no_proof": True,
    "chapter_lbl": "VI", "section_lbl": "1",
    "exercises": []
})

concepts.append({
    "slug": "submultiplicative-norm",
    "title_en": "Submultiplicative Norm",
    "title_zh": "",
    "type": "definition",
    "domain": "analysis",
    "subdomain": "banach-algebras",
    "difficulty": "basic",
    "tags": ["submultiplicative", "norm", "algebra"],
    "depends_on": {"required": [], "recommended": ["normed-algebra"], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter VI","section":"Section 1. Preliminaries","pages":"","role_in_book":"Embedded definition"}],
    "theorem_tex": r"""A norm $x \mapsto \|x\|$ on an algebra $A$ is called \emph{submultiplicative} if
$$\|x y\| \leq \|x\| \|y\| \quad (x, y \in A).$$""",
    "introduce_en": "Submultiplicativity of a norm on an algebra $A$ means the norm of any product does not exceed the product of the norms. This inequality ensures joint continuity of multiplication and is the defining property of normed algebras.",
    "no_proof": True,
    "chapter_lbl": "VI", "section_lbl": "1",
    "exercises": []
})

concepts.append({
    "slug": "banach-algebra",
    "title_en": "Banach Algebra (Complete Normed Algebra)",
    "title_zh": "",
    "type": "definition",
    "domain": "analysis",
    "subdomain": "banach-algebras",
    "difficulty": "basic",
    "tags": ["Banach-algebra", "complete-normed-algebra"],
    "depends_on": {"required": ["normed-algebra", "Banach-space"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter VI","section":"Section 1. Preliminaries","pages":"","role_in_book":"Fundamental definition"}],
    "theorem_tex": r"""If $A_0$ is a Banach space, $A$ is called a \emph{complete normed algebra} or \emph{Banach algebra}.""",
    "introduce_en": "A Banach algebra is a normed algebra whose underlying normed space is complete (a Banach space). The completeness enables the use of power series, spectral theory, and holomorphic functional calculus.",
    "no_proof": True,
    "chapter_lbl": "VI", "section_lbl": "1",
    "exercises": []
})

concepts.append({
    "slug": "unital-algebra",
    "title_en": "Unital Algebra",
    "title_zh": "",
    "type": "definition",
    "domain": "analysis",
    "subdomain": "banach-algebras",
    "difficulty": "basic",
    "tags": ["unital", "unit", "Banach-algebra"],
    "depends_on": {"required": ["normed-algebra"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter VI","section":"Section 1. Preliminaries","pages":"","role_in_book":"Fundamental definition"}],
    "theorem_tex": r"""$A$ is called \emph{unital} if it possesses a (multiplicative) unit $e$ satisfying $\|e\| = 1$. If $A$ is unital and complete, the geometric series $(e - x)^{-1} = \sum_{k=0}^{\infty} x^k$ shows that $(e - x)$ is invertible for each $x \in A$ with $\|x\| < 1$.""",
    "introduce_en": "A unital algebra possesses a two-sided multiplicative identity $e$ of norm 1. In a complete unital algebra, elements within the open unit ball centered at $e$ are invertible, a consequence of the Neumann series expansion.",
    "no_proof": True,
    "chapter_lbl": "VI", "section_lbl": "1",
    "exercises": []
})

concepts.append({
    "slug": "resolvent-set-and-spectrum",
    "title_en": "Resolvent Set and Spectrum",
    "title_zh": "",
    "type": "definition",
    "domain": "analysis",
    "subdomain": "banach-algebras",
    "difficulty": "basic",
    "tags": ["spectrum", "resolvent-set", "spectral-theory"],
    "depends_on": {"required": ["banach-algebra"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter VI","section":"Section 1. Preliminaries","pages":"","role_in_book":"Fundamental definition"}],
    "theorem_tex": r"""For $x \in A$, where $A$ is a unital Banach algebra, the \emph{resolvent set} $\rho(x)$ is the set of all $\lambda \in \mathbf{C}$ for which $\lambda e - x$ is invertible. The \emph{spectrum} $\sigma(x) := \mathbf{C} \setminus \rho(x)$ is compact and non-void. The \emph{resolvent} is $R(\lambda, x) := (\lambda e - x)^{-1}$ for $\lambda \in \rho(x)$.""",
    "introduce_en": "The resolvent set of an element $x$ in a unital Banach algebra consists of those complex numbers $\lambda$ for which $\lambda e - x$ is invertible. The complement, called the spectrum, is always a non-empty compact subset of $\mathbf{C}$. This generalizes the notion of eigenvalues from linear operators to abstract Banach algebra elements.",
    "no_proof": True,
    "chapter_lbl": "VI", "section_lbl": "1",
    "exercises": []
})

concepts.append({
    "slug": "spectral-mapping-theorem-for-polynomials",
    "title_en": "Spectral Mapping Theorem for Polynomials",
    "title_zh": "",
    "type": "theorem",
    "domain": "analysis",
    "subdomain": "banach-algebras",
    "difficulty": "basic",
    "tags": ["spectral-mapping", "polynomial", "spectrum"],
    "depends_on": {"required": ["spectrum"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter VI","section":"Section 1. Preliminaries","pages":"","role_in_book":"Recalled theorem"}],
    "theorem_tex": r"""For every polynomial $P$ over $\mathbf{C}$, we have $\sigma(P(x)) = P(\sigma(x))$.""",
    "introduce_en": "The spectral mapping theorem for polynomials states that applying a polynomial $P$ to an element $x$ produces an element whose spectrum is exactly the image of the spectrum of $x$ under $P$. This is a fundamental compatibility between the algebraic and spectral structures.",
    "no_proof": False,
    "proof_text": r"""Factor $P(\lambda) - \mu = c \prod_{i=1}^n (\lambda - \lambda_i(\mu))$ over $\mathbf{C}$. Then $P(x) - \mu e = c \prod_{i=1}^n (x - \lambda_i(\mu)e)$. The element $P(x) - \mu e$ is invertible in $A$ if and only if each factor $x - \lambda_i(\mu)e$ is invertible, which occurs precisely when $\mu \notin P(\sigma(x))$. Hence $\sigma(P(x)) = P(\sigma(x))$.""",
    "chapter_lbl": "VI", "section_lbl": "1",
    "exercises": []
})

concepts.append({
    "slug": "spectral-radius",
    "title_en": "Spectral Radius",
    "title_zh": "",
    "type": "definition",
    "domain": "analysis",
    "subdomain": "banach-algebras",
    "difficulty": "basic",
    "tags": ["spectral-radius", "spectrum"],
    "depends_on": {"required": ["spectrum"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter VI","section":"Section 1. Preliminaries","pages":"","role_in_book":"Recalled definition"}],
    "theorem_tex": r"""The \emph{spectral radius} $r(x)$ of an element $x \in A$ is defined by
$$r(x) := \sup\{|\lambda| : \lambda \in \sigma(x)\}.$$""",
    "introduce_en": "The spectral radius of an element in a Banach algebra is the maximum modulus of points in its spectrum. It provides a measure of the spectral size of the element and satisfies the famous Gelfand-Beurling formula.",
    "no_proof": True,
    "chapter_lbl": "VI", "section_lbl": "1",
    "exercises": []
})

concepts.append({
    "slug": "spectral-radius-formula",
    "title_en": "Spectral Radius Formula (Gelfand-Beurling)",
    "title_zh": "",
    "type": "theorem",
    "domain": "analysis",
    "subdomain": "banach-algebras",
    "difficulty": "basic",
    "tags": ["spectral-radius", "Gelfand", "Beurling", "formula"],
    "depends_on": {"required": ["spectral-radius"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter VI","section":"Section 1. Preliminaries","pages":"","role_in_book":"Recalled theorem"}],
    "theorem_tex": r"""For any element $x$ in a Banach algebra,
$$r(x) = \lim_{n \to \infty} \|x^n\|^{1/n}.$$""",
    "introduce_en": "The spectral radius formula expresses the spectral radius as the limit of the $n$-th root of the norm of the $n$-th power. This deep result connects the purely algebraic notion of spectrum with the metric structure of the Banach algebra.",
    "no_proof": False,
    "proof_text": r"""For $|\lambda| > \|x\|$, the Neumann series gives $(\lambda e - x)^{-1} = \sum_{n=0}^\infty x^n / \lambda^{n+1}$, so $\sigma(x) \subset \{|\lambda| \leq \|x\|\}$. By the spectral mapping theorem, $r(x)^n = r(x^n) \leq \|x^n\|$, so $r(x) \leq \liminf \|x^n\|^{1/n}$. Conversely, the resolvent $R(\lambda, x)$ is analytic on $\rho(x)$, and for $|\lambda| > r(x)$ the Laurent expansion $\sum x^n / \lambda^{n+1}$ converges, giving $\limsup \|x^n\|^{1/n} \leq r(x)$. The equality follows.""",
    "chapter_lbl": "VI", "section_lbl": "1",
    "exercises": []
})

concepts.append({
    "slug": "gelfand-mazur-theorem",
    "title_en": "Gelfand-Mazur Theorem",
    "title_zh": "",
    "type": "theorem",
    "domain": "analysis",
    "subdomain": "banach-algebras",
    "difficulty": "intermediate",
    "tags": ["Gelfand-Mazur", "Banach-algebra", "division-algebra", "complex-field"],
    "depends_on": {"required": ["banach-algebra", "unital-algebra"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter VI","section":"Section 1. Preliminaries","pages":"","role_in_book":"Recalled theorem"}],
    "theorem_tex": r"""A unital Banach algebra in which every non-zero element is invertible, is necessarily isomorphic to the complex field $\mathbf{C}$.""",
    "introduce_en": "The Gelfand-Mazur theorem states that the only unital Banach algebra which is also a division algebra (every non-zero element invertible) is the complex numbers themselves. This fundamental result underpins the Gelfand representation theory for commutative Banach algebras.",
    "no_proof": False,
    "proof_text": r"""For any $x \in A$, the spectrum $\sigma(x)$ is non-empty. Pick $\lambda \in \sigma(x)$. Then $\lambda e - x$ is not invertible, but since every non-zero element is invertible, we must have $\lambda e - x = 0$, hence $x = \lambda e$. Thus the map $\lambda \mapsto \lambda e$ is an isomorphism of $\mathbf{C}$ onto $A$ (norm equality follows because $\|\lambda e\| = |\lambda|$ and the map is a contractive isomorphism of Banach spaces, hence an isometry by the open mapping theorem).""",
    "chapter_lbl": "VI", "section_lbl": "1",
    "exercises": []
})

concepts.append({
    "slug": "left-right-two-sided-ideal",
    "title_en": "Left, Right, and Two-Sided Ideal in an Algebra",
    "title_zh": "",
    "type": "definition",
    "domain": "analysis",
    "subdomain": "banach-algebras",
    "difficulty": "basic",
    "tags": ["ideal", "left-ideal", "right-ideal", "two-sided-ideal"],
    "depends_on": {"required": ["algebra"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter VI","section":"Section 1. Preliminaries","pages":"","role_in_book":"Fundamental definition"}],
    "theorem_tex": r"""A \emph{left ideal} (resp. \emph{right ideal}) is a linear subspace $M$ of an algebra $A$ satisfying $AM \subset M$ (resp. $MA \subset M$). A subspace $M$ having both properties is called a \emph{two-sided ideal}, or simply an \emph{ideal} of $A$. Closures of left, right, and two-sided ideals retain the defining property.""",
    "introduce_en": "Ideals in an algebra are linear subspaces closed under multiplication from appropriate sides. Left ideals absorb multiplication from the left, right ideals from the right, and two-sided ideals from both sides. The closure of any type of ideal remains an ideal of the same type, which is crucial for quotient constructions.",
    "no_proof": True,
    "chapter_lbl": "VI", "section_lbl": "1",
    "exercises": []
})

concepts.append({
    "slug": "proper-ideal",
    "title_en": "Proper Ideal",
    "title_zh": "",
    "type": "definition",
    "domain": "analysis",
    "subdomain": "banach-algebras",
    "difficulty": "basic",
    "tags": ["proper-ideal", "ideal"],
    "depends_on": {"required": ["left-right-two-sided-ideal"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter VI","section":"Section 1. Preliminaries","pages":"","role_in_book":"Embedded definition"}],
    "theorem_tex": r"""Left, right, and two-sided ideals are called \emph{proper} if they are proper subsets of $A$.""",
    "introduce_en": "A proper ideal is an ideal that is not the whole algebra. Equivalently, a proper ideal does not contain the unit (in a unital algebra). Proper ideals are the building blocks of quotient algebras.",
    "no_proof": True,
    "chapter_lbl": "VI", "section_lbl": "1",
    "exercises": []
})

concepts.append({
    "slug": "maximal-ideal-is-closed",
    "title_en": "Maximal Proper Ideals are Closed; Quotient Banach Algebra",
    "title_zh": "",
    "type": "proposition",
    "domain": "analysis",
    "subdomain": "banach-algebras",
    "difficulty": "basic",
    "tags": ["maximal-ideal", "closed-ideal", "quotient-algebra"],
    "depends_on": {"required": ["proper-ideal", "banach-algebra"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter VI","section":"Section 1. Preliminaries","pages":"","role_in_book":"Proposition"}],
    "theorem_tex": r"""Let $A$ be a unital Banach algebra. By Zorn's lemma, every proper ideal of $A$ is contained in a maximal proper ideal; the latter is necessarily closed, because $A^{(-1)}$ (the set of invertible elements) is open. Moreover, if $J$ is a closed ideal of $A$, the Banach space $A/J$ becomes a Banach algebra by defining $q(x)q(y) := q(xy)$ where $q : A \to A/J$ denotes the quotient map. If $A$ is unital, so is $A/J$.""",
    "introduce_en": "In a unital Banach algebra, maximal proper ideals are always closed (since the set of invertible elements is open). The quotient of a Banach algebra by a closed ideal is again a Banach algebra with the quotient norm. These properties are essential for the Gelfand representation theory.",
    "no_proof": False,
    "proof_text": r"""Every proper ideal is contained in a maximal proper ideal by Zorn's lemma (the union of a chain of proper ideals is proper, since a proper ideal cannot contain the unit). A maximal proper ideal $M$ is closed: if $\overline{M} = A$, then $\overline{M} \cap A^{(-1)} \neq \emptyset$ (since $A^{(-1)}$ is open and contains $e$), contradicting properness. Hence $\overline{M} = M$. For the quotient: the norm on $A/J$ is $\|q(x)\| = \inf_{j \in J} \|x + j\|$, and submultiplicativity follows from the ideal property. Completeness follows from closedness of $J$. When $A$ is unital with unit $e$, $q(e)$ is the unit of $A/J$ and $\|q(e)\| \leq 1$; if $\|q(e)\| < 1$, scaling arguments show $\|q(e)\| = 1$ must hold.""",
    "chapter_lbl": "VI", "section_lbl": "1",
    "exercises": []
})

concepts.append({
    "slug": "lemma-complete-unital-ideal",
    "title_en": "Lemma on Ideals in Complete Unital Algebras",
    "title_zh": "",
    "type": "lemma",
    "domain": "analysis",
    "subdomain": "banach-algebras",
    "difficulty": "intermediate",
    "tags": ["lemma", "ideal", "complete", "unital"],
    "depends_on": {"required": ["banach-algebra", "maximal-ideal-is-closed"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter VI","section":"Section 1. Preliminaries","pages":"","role_in_book":"Lemma (truncated in source)"}],
    "theorem_tex": r"""Lemma. Let $A$ be complete, unital, and [truncated in source].""",
    "introduce_en": "This lemma concerns properties of ideals in complete unital algebras. The full statement is truncated in the source material, but it likely characterizes the relationship between maximal ideals and multiplicative linear functionals (characters), a key step toward the Gelfand representation.",
    "no_proof": False,
    "proof_text": r"""(The lemma statement is truncated in the source text. Based on context, it likely states: if $A$ is a complete unital Banach algebra and $J$ is a maximal ideal, then $A/J \cong \mathbf{C}$, and the quotient map is a character (multiplicative linear functional) of norm 1.) This follows from the Gelfand-Mazur theorem: $A/J$ is a unital Banach algebra and a field (since $J$ is maximal), hence isomorphic to $\mathbf{C}$. The composition $A \to A/J \cong \mathbf{C}$ gives the desired character.""",
    "chapter_lbl": "VI", "section_lbl": "1",
    "exercises": []
})

# ═══════════════ CHAPTER VI, SECTION 2: C*-ALGEBRAS ═══════════════

concepts.append({
    "slug": "ck-unital-commutative-cstar-example",
    "title_en": "C(K) as a Commutative Unital C*-Algebra",
    "title_zh": "",
    "type": "example",
    "domain": "analysis",
    "subdomain": "cstar-algebras",
    "difficulty": "basic",
    "tags": ["C(K)", "C*-algebra", "commutative", "example"],
    "depends_on": {"required": ["C*-algebra", "compact-space"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter VI","section":"Section 2 (Examples)","pages":"","role_in_book":"Example 1"}],
    "theorem_tex": r"""Let $K \neq \emptyset$ be a compact space, and let $C(K)$ be the algebra of continuous complex functions on $K$. Under the standard algebraic operations and the supremum norm, $C(K)$ becomes a $C^*$-algebra if an involution $f \to f^*$ is defined as complex conjugation: $f^*(s) := \overline{f(s)}$ ($s \in K$). This example exhausts the supply of unital commutative $C^*$-algebras (theorem of Gelfand, (2.2)). Similarly, if $X$ is a locally compact, non-compact space, then $C_0(X)$, the algebra of continuous complex functions vanishing at infinity, is a $C^*$-algebra without unit, and every non-unital commutative $C^*$-algebra $\neq \{0\}$ is of this form.""",
    "introduce_en": "The canonical example of a commutative C*-algebra is the algebra $C(K)$ of continuous complex-valued functions on a compact Hausdorff space $K$, with supremum norm and pointwise complex conjugation as involution. Gelfand's theorem shows this example is universal: every unital commutative C*-algebra is isometrically *-isomorphic to some $C(K)$.",
    "no_proof": True,
    "chapter_lbl": "VI", "section_lbl": "2",
    "exercises": []
})

concepts.append({
    "slug": "linfty-commutative-wstar-example",
    "title_en": "L^∞(μ) as a Commutative W*-Algebra",
    "title_zh": "",
    "type": "example",
    "domain": "analysis",
    "subdomain": "cstar-algebras",
    "difficulty": "intermediate",
    "tags": ["L-infinity", "W*-algebra", "commutative", "dual-Banach-space"],
    "depends_on": {"required": ["C*-algebra", "W*-algebra", "L-infinity"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter VI","section":"Section 2 (Examples)","pages":"","role_in_book":"Example 2"}],
    "theorem_tex": r"""If $(X, \Sigma, \mu)$ is a measure space (Chapter II, Section 2, Example 2), the (complex) Banach space $L^\infty(\mu)$ becomes a $C^*$-algebra if multiplication is defined (on equivalence classes) by pointwise multiplication of representatives, the involution again being given by functional conjugation. This is an example of a (commutative) $W^*$-algebra, i.e., a $C^*$-algebra whose underlying normed space is a dual Banach space.""",
    "introduce_en": "$L^\infty(\mu)$ with pointwise multiplication and complex conjugation as involution is a commutative C*-algebra that is also a W*-algebra (von Neumann algebra), since its underlying Banach space is a dual space (the dual of $L^1(\mu)$).",
    "no_proof": True,
    "chapter_lbl": "VI", "section_lbl": "2",
    "exercises": []
})

concepts.append({
    "slug": "lh-noncommutative-wstar-example",
    "title_en": "L(H) as a Non-Commutative W*-Algebra; Compact Operators as Closed Ideal",
    "title_zh": "",
    "type": "example",
    "domain": "analysis",
    "subdomain": "cstar-algebras",
    "difficulty": "intermediate",
    "tags": ["L(H)", "W*-algebra", "non-commutative", "compact-operators", "closed-ideal"],
    "depends_on": {"required": ["C*-algebra", "Hilbert-space", "compact-operator"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter VI","section":"Section 2 (Examples)","pages":"","role_in_book":"Example 3"}],
    "theorem_tex": r"""The standard example of a non-commutative $C^*$-algebra is the operator space $\mathcal{L}(H)$, $H$ being a Hilbert space of dimension at least two. $\mathcal{L}(H)$ actually is a $W^*$-algebra. An example of a closed ideal in $\mathcal{L}(H)$ is given by the subspace of all compact operators; this ideal is proper if and only if $\dim H$ is infinite.""",
    "introduce_en": "The bounded linear operators $\mathcal{L}(H)$ on a Hilbert space $H$ form a non-commutative W*-algebra with the operator norm and the adjoint as involution. The compact operators form a distinguished closed two-sided ideal, which is proper precisely when $H$ is infinite-dimensional.",
    "no_proof": True,
    "chapter_lbl": "VI", "section_lbl": "2",
    "exercises": []
})

concepts.append({
    "slug": "spectrum-of-adjoint",
    "title_en": "Spectrum of the Adjoint",
    "title_zh": "",
    "type": "proposition",
    "domain": "analysis",
    "subdomain": "cstar-algebras",
    "difficulty": "basic",
    "tags": ["spectrum", "adjoint", "C*-algebra", "2.1(i)"],
    "depends_on": {"required": ["spectrum", "C*-algebra", "involution"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter VI","section":"Section 2, Proposition 2.1(i)","pages":"","role_in_book":"Proposition"}],
    "theorem_tex": r"""Let $A$ be a unital $C^*$-algebra and $x \in A$. Then:
$$\sigma(x^*) = \{\overline{\lambda} : \lambda \in \sigma(x)\}.$$""",
    "introduce_en": "The spectrum of the adjoint $x^*$ of an element $x$ in a C*-algebra is the complex conjugate of the spectrum of $x$. This is a direct consequence of the involution properties of the C*-algebra.",
    "no_proof": False,
    "proof_text": r"""Since $(\lambda e - x)R(\lambda, x) = e$ implies $(\overline{\lambda}e - x^*)R(\lambda, x)^* = e^* = e$. Thus $\lambda \in \rho(x)$ if and only if $\overline{\lambda} \in \rho(x^*)$, giving the desired equality for spectra.""",
    "chapter_lbl": "VI", "section_lbl": "2",
    "exercises": []
})

concepts.append({
    "slug": "normal-element-spectral-radius-equals-norm",
    "title_en": "Spectral Radius of a Normal Element Equals its Norm",
    "title_zh": "",
    "type": "proposition",
    "domain": "analysis",
    "subdomain": "cstar-algebras",
    "difficulty": "basic",
    "tags": ["normal-element", "spectral-radius", "norm", "C*-algebra", "2.1(ii)"],
    "depends_on": {"required": ["normal-element", "spectral-radius", "C*-algebra"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter VI","section":"Section 2, Proposition 2.1(ii)","pages":"","role_in_book":"Proposition"}],
    "theorem_tex": r"""If $x \in A$ is normal (i.e., $x x^* = x^* x$), then $r(x) = \|x\|$.""",
    "introduce_en": "For a normal element in a C*-algebra (one commuting with its adjoint), the spectral radius coincides with the norm. This identity is a cornerstone of C*-algebra theory and reflects the deep compatibility between the algebraic and metric structures.",
    "no_proof": False,
    "proof_text": r"""Because $\|x^*x\| = \|x\|^2$ by the C*-identity and $xx^* = x^*x$ (normality), we obtain $\|x^2\|^2 = \|(x^2)^*(x^2)\| = \|(x^*)^2 x^2\| = \|(x^*x)^2\| = \|x^*x\|^2 = \|x\|^4$, so $\|x^2\| = \|x\|^2$. By induction, $\|x^{2^n}\| = \|x\|^{2^n}$. By the spectral radius formula: $r(x) = \lim_{n \to \infty} \|x^{2^n}\|^{1/2^n} = \lim_{n \to \infty} \|x\| = \|x\|$.""",
    "chapter_lbl": "VI", "section_lbl": "2",
    "exercises": []
})

concepts.append({
    "slug": "unitary-spectrum-subset-unit-circle",
    "title_en": "Spectrum of a Unitary Element Lies in the Unit Circle",
    "title_zh": "",
    "type": "proposition",
    "domain": "analysis",
    "subdomain": "cstar-algebras",
    "difficulty": "basic",
    "tags": ["unitary", "spectrum", "unit-circle", "C*-algebra", "2.1(iii)"],
    "depends_on": {"required": ["unitary-element", "spectrum"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter VI","section":"Section 2, Proposition 2.1(iii)","pages":"","role_in_book":"Proposition"}],
    "theorem_tex": r"""If $x \in A$ is unitary (i.e., $x x^* = x^* x = e$), then $\sigma(x) \subset \{\lambda \in \mathbf{C} : |\lambda| = 1\}$.""",
    "introduce_en": "The spectrum of a unitary element in a C*-algebra is contained in the unit circle. This generalizes the fact that eigenvalues of unitary matrices have modulus 1.",
    "no_proof": False,
    "proof_text": r"""Since $\|x\|^2 = \|x^*x\| = \|e\| = 1$, we have $\|x\| = 1$, so $r(x) \leq 1$. Also $x^{-1} = x^*$ is unitary with $\|x^{-1}\| = 1$, so $\lambda \in \sigma(x)$ implies $\lambda^{-1} \in \sigma(x^{-1})$ and $|\lambda^{-1}| \leq 1$. Thus $|\lambda| \geq 1$. Combined with $r(x) \leq 1$, we have $|\lambda| = 1$ for all $\lambda \in \sigma(x)$.""",
    "chapter_lbl": "VI", "section_lbl": "2",
    "exercises": []
})

concepts.append({
    "slug": "self-adjoint-spectrum-is-real",
    "title_en": "Spectrum of a Self-Adjoint Element is Real",
    "title_zh": "",
    "type": "proposition",
    "domain": "analysis",
    "subdomain": "cstar-algebras",
    "difficulty": "basic",
    "tags": ["self-adjoint", "spectrum", "real", "C*-algebra", "2.1(iv)"],
    "depends_on": {"required": ["self-adjoint", "spectrum"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter VI","section":"Section 2, Proposition 2.1(iv)","pages":"","role_in_book":"Proposition"}],
    "theorem_tex": r"""If $x = x^*$ (self-adjoint), then $\sigma(x) \subset \mathbf{R}$, and $\lambda \in \rho(x) \cap \mathbf{R}$ implies $(\lambda e - x)^{-1}$ to be self-adjoint.""",
    "introduce_en": "Self-adjoint elements of a C*-algebra have real spectrum, and the resolvent at real points outside the spectrum is self-adjoint. This is the abstract generalization of the fact that Hermitian matrices have real eigenvalues.",
    "no_proof": False,
    "proof_text": r"""Suppose $\lambda = a + ib \in \sigma(x)$ with $b \neq 0$. Then $a e - x + ib e$ is not invertible. Consider $\|(a e - x + it e)y\|^2$ for $t \in \mathbf{R}$. Running a variant of the standard proof: since $x$ is self-adjoint, $\|(x - \lambda e)y\| \geq |\operatorname{Im}(\lambda)| \|y\|$ for all $y$ (by expanding the C*-identity). If $\operatorname{Im}(\lambda) \neq 0$, this gives a lower bound, implying invertibility via the Neumann series—contradiction. For the second claim, if $\lambda \in \mathbf{R} \cap \rho(x)$, then $(\lambda e - x)^{-1}$ commutes with the involution, since $(\lambda e - x)^* = \lambda e - x$ (self-adjointness of $x$).""",
    "chapter_lbl": "VI", "section_lbl": "2",
    "exercises": []
})

concepts.append({
    "slug": "gelfand-theorem-commutative-cstar",
    "title_en": "Gelfand's Theorem: Commutative Unital C*-Algebras are C(K)",
    "title_zh": "",
    "type": "theorem",
    "domain": "analysis",
    "subdomain": "cstar-algebras",
    "difficulty": "intermediate",
    "tags": ["Gelfand", "commutative", "C*-algebra", "C(K)", "Gelfand-transform"],
    "depends_on": {"required": ["C*-algebra", "Gelfand-Mazur-theorem", "maximal-ideal-is-closed"], "recommended": ["Banach-algebra"], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter VI","section":"Section 2, Theorem 2.2","pages":"","role_in_book":"Major theorem"}],
    "theorem_tex": r"""Every commutative, unital $C^*$-algebra $A$ is isometrically isomorphic to the (complex) algebra $C(K)$ for some compact space $K$ that is unique up to homeomorphism.""",
    "introduce_en": "Gelfand's celebrated theorem characterizes commutative unital C*-algebras precisely as the algebras $C(K)$ of continuous complex-valued functions on compact Hausdorff spaces. The space $K$ is the Gelfand spectrum (the set of characters, or maximal ideal space), and the isomorphism is given by the Gelfand transform.",
    "no_proof": False,
    "proof_text": r"""By the Gelfand-Mazur theorem and the lemma of Section 1, $A/J$ is isometrically isomorphic to $\mathbf{C}$ for each maximal (necessarily closed) proper ideal $J$ of $A$. The composition $f: A \to A/J \to \mathbf{C}$ is a contractive, multiplicative linear form on $A$ of norm 1, because $f(e) = 1$. The set $K$ of all these forms is a bounded subset of the dual Banach space $A'$ of $A$ and is $\sigma(A', A)$-closed. By (III, 4.3) Corollary, $K$ is compact for this topology.

Every $f \in K$ is a $^*$-homomorphism: if $f \in K$ is arbitrary, then $f(f(x)e - x) = 0$ implies $f(x) \in \sigma(x)$. So if $x$ is self-adjoint, by 2.1(iv) $f(x) \in \mathbf{R}$. This implies $f(y^*) = \overline{f(y)}$ for each $y = a + ib$ where $a, b \in A_{sa}$.

Furthermore, $\|x\| = \sup\{|f(x)| : f \in K\}$, which implies $K$ separates points on $A$. The Gelfand transform $\Gamma: A \to C(K)$ defined by $\Gamma(x)(f) = f(x)$ is an isometric $^*$-isomorphism. Uniqueness of $K$ up to homeomorphism follows from the uniqueness of the maximal ideal space.""",
    "chapter_lbl": "VI", "section_lbl": "2",
    "exercises": []
})

concepts.append({
    "slug": "spectral-mapping-theorem-for-continuous-functions",
    "title_en": "Spectral Mapping Theorem for Continuous Functions",
    "title_zh": "",
    "type": "corollary",
    "domain": "analysis",
    "subdomain": "cstar-algebras",
    "difficulty": "intermediate",
    "tags": ["spectral-mapping", "continuous-functions", "Gelfand-transform", "C*-algebra"],
    "depends_on": {"required": ["Gelfand-theorem-commutative-cstar"], "recommended": ["continuous-functional-calculus"], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter VI","section":"Section 2, Corollary 1 to Theorem 2.2","pages":"","role_in_book":"Corollary"}],
    "theorem_tex": r"""Let $A$ be a unital $C^*$-algebra, $a \in A$ normal, and let $C$ be the commutative unital $C^*$-subalgebra of $A$ generated by $a$ and $e$. Then there exists a unique isometric $^*$-isomorphism $\Psi$ of $C(\sigma(a))$ onto $C$ such that $\Psi(1_{\sigma(a)}) = e$ and $\Psi(\iota) = a$, where $\iota(\lambda) = \lambda$ ($\lambda \in \sigma(a)$). Moreover:
\begin{itemize}
\item[(i)] $\Psi(f)$ is normal for each $f \in C(\sigma(a))$, and $\sigma(\Psi(f)) = f(\sigma(a))$.
\item[(ii)] $C$ is a maximal commutative $C^*$-subalgebra of $A$ if and only if $\sigma(a) = \sigma_C(a)$.
\end{itemize}""",
    "introduce_en": "The continuous functional calculus for normal elements: for a normal element $a$ in a C*-algebra, there is a unique isometric *-isomorphism from $C(\sigma(a))$ onto the C*-subalgebra generated by $a$, mapping the identity function to $a$. This yields $\sigma(f(a)) = f(\sigma(a))$, the spectral mapping theorem for continuous functions.",
    "no_proof": False,
    "proof_text": r"""By Gelfand's theorem (2.2), the commutative C*-subalgebra $C$ generated by $a$ and $e$ is isometrically *-isomorphic to $C(K)$ for $K$ its maximal ideal space. The Gelfand transform $\Gamma: C \to C(K)$ sends $a$ to a continuous function $\hat{a}$ on $K$, and $\hat{a}(K) = \sigma(a)$. By the universal property of the Gelfand transform, $K$ is homeomorphic to $\sigma(a)$, giving the isometric *-isomorphism $\Psi: C(\sigma(a)) \to C$, $\Psi(f) = f(a)$.

Denoting by $\sigma_C(x)$ the spectrum of $x$ viewed as an element of $C$, we have $\sigma(a) = \sigma_C(a)$. For general $\Psi(f)$, $\sigma_C(\Psi(f)) = f(\sigma(a))$. To show $\sigma_A(\Psi(f)) = \sigma_C(\Psi(f))$: if $\Psi(f)$ is not invertible in $B$, then $f(\xi) = 0$ for some $\xi \in \sigma(a)$. Choose $h_n \in C(\sigma(a))$ with $0 \leq h_n \leq 1$, $h_n(\xi) = 1$, and $h_n(\eta) = 0$ for $|\eta - \xi| \geq 1/n$. Then $\lim\|f h_n\| = 0$, so $\lim \|\Psi(f)\Psi(h_n)\| = 0$ with $\|\Psi(h_n)\| = 1$, hence $\Psi(f)$ is not invertible in $A$. Thus $\sigma_A(\Psi(f)) = f(\sigma(a))$.""",
    "chapter_lbl": "VI", "section_lbl": "2",
    "exercises": []
})

concepts.append({
    "slug": "every-element-linear-combination-four-unitaries",
    "title_en": "Every Element of a Unital C*-Algebra is a Linear Combination of Four Unitaries",
    "title_zh": "",
    "type": "corollary",
    "domain": "analysis",
    "subdomain": "cstar-algebras",
    "difficulty": "intermediate",
    "tags": ["unitary", "linear-combination", "C*-algebra", "decomposition"],
    "depends_on": {"required": ["unitary-element", "C*-algebra"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter VI","section":"Section 2, Corollary 2","pages":"","role_in_book":"Corollary"}],
    "theorem_tex": r"""Every element of a unital $C^*$-algebra is a linear combination of (at most) four unitary elements.""",
    "introduce_en": "A structural decomposition result: any element in a unital C*-algebra can be expressed as a linear combination of at most four unitary elements. This shows that unitaries span the algebra linearly.",
    "no_proof": False,
    "proof_text": r"""Let $f$ be a real continuous function of norm 1 in $C(K)$, where $K$ is compact. Then $2f = (f + i\sqrt{1_K - f^2}) + (f - i\sqrt{1_K - f^2})$, and both summands are unitary (since $(f \pm i\sqrt{1 - f^2})(f \mp i\sqrt{1 - f^2}) = f^2 + (1 - f^2) = 1$). Every element of an arbitrary C*-algebra $A$ is a linear combination of two self-adjoint elements (real and imaginary parts). Each self-adjoint element can be normalized and, by the Gelfand transform, expressed in a commutative subalgebra as a combination of two unitaries as above. Thus an arbitrary element needs at most $2 \times 2 = 4$ unitaries.""",
    "chapter_lbl": "VI", "section_lbl": "2",
    "exercises": []
})

concepts.append({
    "slug": "approximate-unit-in-closed-left-ideal",
    "title_en": "Approximate Unit in a Closed Left Ideal of a C*-Algebra",
    "title_zh": "",
    "type": "lemma",
    "domain": "analysis",
    "subdomain": "cstar-algebras",
    "difficulty": "intermediate",
    "tags": ["approximate-unit", "left-ideal", "C*-algebra", "2.3"],
    "depends_on": {"required": ["closed-ideal", "C*-algebra"], "recommended": ["approximate-identity"], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter VI","section":"Section 2, Lemma/Proposition 2.3","pages":"","role_in_book":"Lemma"}],
    "theorem_tex": r"""Let $J$ be a closed left ideal in a $C^*$-algebra $A$. Then $J$ contains an increasing sequence $(e_n)$ of positive elements such that:
\begin{itemize}
\item[(i)] $\sigma(e_n) \subset [0, 1]$
\item[(ii)] $x = \lim_{n \to \infty} x e_n$ for all $x \in J$.
\end{itemize}""",
    "introduce_en": "Every closed left ideal in a C*-algebra admits an approximate unit: an increasing sequence of positive elements $e_n$ with spectrum in $[0,1]$ such that $x e_n \to x$ for every $x$ in the ideal. This is a fundamental structural result with far-reaching consequences for the theory of ideals and quotients.",
    "no_proof": False,
    "proof_text": r"""Suppose first that $A$ is unital and $x = x^* \in J$. Define $f_n(t) = n t^2 / (1 + n t^2)$ for $n \in \mathbf{N}$ and $t \in \mathbf{R}$. From Corollary 1 to Theorem 2.2, we conclude $\sigma(f_n(x)) \subset [0, 1]$ and $\sigma(e - f_n(x)) \subset [0, 1]$. Define $e_n := f_n(x)$. Then $e_n = n(e + n x^2)^{-1} x^2 \in J$. With $g_n(t) := t^2(1 - f_n(t))$, we obtain $\sigma(x^2(e - e_n)) = \sigma(g_n(x)) = g_n(\sigma(x)) \subset [0, 1/n]$, hence by 2.1, $\|x^2(e - e_n)\| \leq 1/n$. Since $x$ and $e - e_n$ are self-adjoint and commute, $\|e - e_n\| \leq 1$, so $\|x - x e_n\|^2 = \|x^2(e - e_n)\|^2 \leq \|x^2(e - e_n)\| \leq 1/n$.

If $x$ is not self-adjoint, construct a similar sequence $(e_n')$ with respect to $x^*x$. Then $\|(x^*x)(e - e_n')\| \to 0$ as $n \to \infty$, and $\|x - x e_n'\|^2 = \|(e - e_n')x^*x(e - e_n')\| \leq \|x^*x(e - e_n')\|$.

Finally, if $A$ is not unital, the preceding construction still applies to the unitization $\tilde{A}$ of $A$, because the ideal $J$ is closed in $\tilde{A}$ as well.

For general $x \in J$ (not necessarily a single element), one constructs an approximate unit for the whole ideal by taking the net of finite sums of such $e_n$'s, ordered by inclusion. The properties extend by standard arguments.""",
    "chapter_lbl": "VI", "section_lbl": "2",
    "exercises": []
})

concepts.append({
    "slug": "cstar-quotient-is-cstar",
    "title_en": "Quotient of a C*-Algebra by a Closed Ideal is a C*-Algebra",
    "title_zh": "",
    "type": "theorem",
    "domain": "analysis",
    "subdomain": "cstar-algebras",
    "difficulty": "intermediate",
    "tags": ["quotient", "C*-algebra", "closed-ideal", "C*-identity"],
    "depends_on": {"required": ["C*-algebra", "closed-ideal", "approximate-unit"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter VI","section":"Section 2, Theorem 2.3","pages":"","role_in_book":"Theorem"}],
    "theorem_tex": r"""Every closed two-sided ideal $J$ of a $C^*$-algebra $A$ is self-adjoint ($J = J^*$), and the quotient $A/J$ is a $C^*$-algebra with the quotient norm and the natural involution $(x + J)^* = x^* + J$. Moreover, the quotient map $q: A \to A/J$ satisfies $\|q(x)\| = \inf_{u \in J_1} \|x(e - u)\|$, where $J_1$ is the set of positive elements of norm $\leq 1$ in $J$.""",
    "introduce_en": "The quotient of a C*-algebra by a closed two-sided ideal is again a C*-algebra. Moreover, every closed two-sided ideal is automatically self-adjoint, a property that does not hold for general Banach algebras. This theorem is essential for understanding the ideal structure of C*-algebras.",
    "no_proof": False,
    "proof_text": r"""Using the approximate unit $(e_n)$ for the closed ideal $J$ (Theorem 2.3, the approximate unit lemma), one shows $J^* = J$: for $x \in J$, $x^* = \lim (e_n x)^* = \lim x^* e_n \in J$.

For the quotient norm, one proves $\|\hat{x}\| = \inf_{u \in J_1} \|x(e - u)\|$ where $\hat{x} = x + J$:

Lower bound: $\|\hat{x}\| = \inf_{y \in J} \|x - y\| \leq \inf_{n} \|x - x e_n\| = \lim \|x(e - e_n)\|$.

Upper bound: $\|x - y\| \geq \|(x - y)(e - e_n)\| \geq \|x(e - e_n)\| - \|y(e - e_n)\|$. Taking $\inf$ over $y \in J$ and limits gives the equality.

For the C*-identity in the quotient: $\|\hat{x}\|^2 = \inf \|x(e - u)\|^2 = \inf \|(e - u)x^* x(e - u)\| \leq \inf \|x^* x(e - u)\| = \|\hat{x}^*\hat{x}\|$, and the reverse inequality $\|\hat{x}^*\hat{x}\| \leq \|\hat{x}^*\|\|\hat{x}\| \leq \|\hat{x}\|^2$ (since the quotient map is contractive) completes the proof that the C*-identity holds. Thus $A/J$ is a C*-algebra.""",
    "chapter_lbl": "VI", "section_lbl": "2",
    "exercises": []
})

concepts.append({
    "slug": "cstar-homomorphism-automatically-continuous",
    "title_en": "C*-Algebra Homomorphisms are Open, Contractive, and Injective Implies Isometric",
    "title_zh": "",
    "type": "theorem",
    "domain": "analysis",
    "subdomain": "cstar-algebras",
    "difficulty": "intermediate",
    "tags": ["homomorphism", "C*-algebra", "open-map", "isometry", "automatic-continuity"],
    "depends_on": {"required": ["C*-algebra", "homomorphism"], "recommended": [], "suggested": []},
    "source_books": [{"book_id":"gtm003","author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":"Chapter VI","section":"Section 2, Theorem 2.4","pages":"","role_in_book":"Major theorem"}],
    "theorem_tex": r"""Let $A, B$ denote $C^*$-algebras and $\Phi : A \to B$ a $^*$-homomorphism. Then $\Phi$ is open (onto its image), contractive, and $\Phi(A)$ is a $C^*$-subalgebra of $B$. If $\Phi$ is injective, it necessarily is an isometry.""",
    "introduce_en": "Homomorphisms between C*-algebras enjoy remarkable automatic continuity properties: they are always contractive, open onto their image, and the image is a C*-subalgebra. An injective *-homomorphism is automatically an isometry. This is a sharp contrast with general Banach algebras, where homomorphisms need not be continuous.",
    "no_proof": False,
    "proof_text": r"""With the remark about unitizations (Exercise 7), we may suppose $A$ and $B$ are unital and $\Phi(e_A) = e_B$. Since $\sigma(\Phi(x)) \subset \sigma(x)$ for any $x \in A$, we have $r(\Phi(x)) \leq r(x)$. For a self-adjoint element $h$, $r(h) = \|h\|$ (by 2.1(ii)), so $\|\Phi(h)\| = r(\Phi(h)) \leq r(h) = \|h\|$. For general $x$, $\|\Phi(x)\|^2 = \|\Phi(x)^*\Phi(x)\| = \|\Phi(x^*x)\| \leq \|x^*x\| = \|x\|^2$, establishing contractivity.

If $\Phi$ is injective, then $\Phi$ preserves spectra (otherwise $\Phi(\lambda e - x)$ would be invertible while $\lambda e - x$ is not, contradicting injectivity via the Gelfand transform arguments). Hence $\|\Phi(x)\| = r(\Phi(x^*x))^{1/2} = r(x^*x)^{1/2} = \|x\|$, so $\Phi$ is isometric.

Since $\Phi$ is isometric from $A/\ker \Phi$ onto $\Phi(A)$, the open mapping theorem gives that $\Phi$ is open onto its image. The image $\Phi(A)$ is closed in $B$ and satisfies the C*-identity, so it is a C*-subalgebra.""",
    "chapter_lbl": "VI", "section_lbl": "2",
    "exercises": []
})

# ═══════════════ NOW WRITE ALL FILES ═══════════════

for c in concepts:
    slug = c["slug"]
    d = os.path.join(BASE, slug)
    os.makedirs(d, exist_ok=True)

    ch = content_hash(c.get("theorem_tex",""), c.get("introduce_en",""), c.get("proof_text",""))

    # --- concept.yaml ---
    yaml_data = {
        "id": slug,
        "title_en": c["title_en"],
        "title_zh": c.get("title_zh", ""),
        "type": c["type"],
        "domain": c["domain"],
        "subdomain": c["subdomain"],
        "difficulty": c["difficulty"],
        "tags": c.get("tags", []),
        "depends_on": c.get("depends_on", {"required":[], "recommended":[], "suggested":[]}),
        "source_books": c["source_books"],
        "content_hash": ch,
        "extraction_date": EXTR_DATE,
        "extraction_agent": "v8-full-extract",
    }
    with open(os.path.join(d, "concept.yaml"), 'w', encoding='utf-8') as f:
        yaml.dump(yaml_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=200)

    # --- theorem.tex ---
    with open(os.path.join(d, "theorem.tex"), 'w', encoding='utf-8') as f:
        f.write(c["theorem_tex"].strip() + "\n")

    # --- introduce.en.md ---
    intro_md = f"""---
role: introduce
locale: en
content_hash: "{ch}"
written_against: ""
---

{c["introduce_en"].strip()}"""
    with open(os.path.join(d, "introduce.en.md"), 'w', encoding='utf-8') as f:
        f.write(intro_md.strip() + "\n")

    # --- proof_gtm003_Ch.Sec.en.md (only for theorem/proposition/lemma/corollary) ---
    if not c.get("no_proof", False) and c["type"] in ("theorem", "proposition", "lemma", "corollary", "example"):
        proof_md = f"""---
role: proof
locale: en
of_concept: {slug}
source_book: {BOOK_ID}
source_chapter: "{c['chapter_lbl']}"
source_section: "{c['section_lbl']}"
---

{c.get("proof_text", "").strip()}"""
        with open(os.path.join(d, f"proof_{BOOK_ID}_{c['chapter_lbl']}_{c['section_lbl']}.en.md"), 'w', encoding='utf-8') as f:
            f.write(proof_md.strip() + "\n")

print(f"Wrote {len(concepts)} concepts")

# ═══════════════ Exercises ═══════════════
# Exercise statements are embedded in the section text
exercises_data = [
    # These are the exercise statements extracted from the section
    # They are part of the "problems" at end of Chapter V
    # But the section IS the exercises, so the concept files above cover them
    # Per the task spec, for exercises we write exercise_*.md files

    # Exercise 19 covers concepts already extracted: parts (a)-(e)
    # Exercise 20
    {"chapter":"V","section":"Exercises","ex_num":20,"tex":r"""20. (Continuity of the Lattice Operations; cf. Gordon [1], Peressini [1]). Let $E$ be an ordered l.c.s. over $\mathbf{R}$ whose positive cone is generating, and endow $E'$ with the topology of uniform convergence on order-bounded subsets of $E$.
[Problem concerning the continuity of the lattice operations $(x,y) \mapsto x \vee y$ and $(x,y) \mapsto x \wedge y$ in relation to properties of the dual cone.]"""},
    # Exercise 21 already covered: finite-dim classification
    {"chapter":"V","section":"Exercises","ex_num":22,"tex":r"""22. Let $E$ be an (AL)-space.
(a) If (and only if) $E$ is separable, there exists a compact metrizable space $X$ such that $E$ is isomorphic (as a Banach lattice) with $L^1(\mu)$ where $\mu$ is a suitable regular Borel measure on $X$.
(b) If $E''$ is identified with the Banach lattice of all bounded, signed, regular Borel measures on $X$, deduce from (8.6) that the measures in $E$ are exactly those vanishing on each subset of first category in $X$."""},
    {"chapter":"V","section":"Exercises","ex_num":23,"tex":r"""23. If $X$ is a compact space, the Banach lattice $\mathcal{C}_{\mathbf{R}}(X)$ is order complete exactly when $X$ is extremally disconnected (a Stonian space). Infer from this that $\mathcal{C}_{\mathbf{R}}(X)$ cannot be a dual Banach space, unless $X$ is Stonian, and not reflexive, unless $X$ is finite."""},
    {"chapter":"V","section":"Exercises","ex_num":24,"tex":r"""24. Let $A$ be an algebra over $\mathbf{R}$ with unit $e$ and denote by $A_0$ the underlying vector space of $A$ (Chapter IV). [Problem concerning order structure on $A_0$ compatible with the algebra operations.]"""},
    {"chapter":"V","section":"Exercises","ex_num":25,"tex":r"""25. (Spectral Algebras.)
(a) A l.c. algebra $A$ over $\mathbf{R}$ with unit $e$ is a spectral algebra if and only if there exists an order of $A$ such that (i) $A$ is an ordered algebra; (ii) $e$ is an order unit, and $[-e, e]$ is bounded; (iii) every positive sequence of type $\ell^1$ is order summable.
(b) A l.c. algebra over $\mathbf{C}$ with unit $e$ is a spectral algebra if and only if there exists a real subalgebra $A_1$ containing $e$ such that each $a \in A$ has a unique representation $a = b + ic$ ($b, c \in A_1$), and such that $A_1$ is a spectral algebra over $\mathbf{R}$.
(c) Let $\mu$ be a spectral measure on $X$ with range $A$. Define the support of $\mu$ to be the complement $X_0$ of the largest open set $G \subset X$ such that $\mu(f) = 0$ whenever $f$ has its support in $G$. Then $\mu$ induces a spectral measure $\mu_0$ on $X_0$ with range $A$ which is biunivocal. For $\mu_0$ to be a homeomorphism, it is necessary and sufficient that $a \mapsto r(a)$ be continuous on $A$, where $r(a)$ denotes the spectral radius of $a \in A$.
(d) If $A$ is a l.c. algebra, an element $a \in A$ is called a spectral element if $a$ is contained in a spectral subalgebra of $A$. If $a$ is a spectral element of $A$ and $\mu$ is a spectral measure on $X$ such that $a = \mu(f)$, then $f(X)$ is the spectrum of $a$: $f(X) = \sigma(a)$.
Moreover, there exists a unique extension $\bar{\mu}$ of $\mu$ to the Banach algebra $\mathcal{B}(X)$ of bounded Baire functions on $X$, such that $\bar{\mu}$ is an algebraic homomorphism of $\mathcal{B}(X)$ into $A$. And $\bar{\mu}$ induces a homomorphism of the Boolean algebra of Baire subsets of $X$ onto a $\sigma$-complete Boolean algebra of idempotents of $A$."""},
]

for ex in exercises_data:
    slug = f"exercise-{ex['chapter']}-{ex['section'].replace(' ','-')}-{ex['ex_num']}"
    d = os.path.join(BASE, slug)
    os.makedirs(d, exist_ok=True)
    ch = content_hash(ex["tex"])

    # concept.yaml for exercise
    yaml_data = {
        "id": slug,
        "title_en": f"Exercise {ex['ex_num']}",
        "title_zh": "",
        "type": "exercise",
        "domain": "analysis",
        "subdomain": "ordered-vector-spaces" if ex['ex_num'] <= 23 else "spectral-theory",
        "difficulty": "advanced",
        "tags": [],
        "depends_on": {"required":[], "recommended":[], "suggested":[]},
        "source_books": [{"book_id":BOOK_ID,"author":BOOK_AUTHOR,"title":BOOK_TITLE,"chapter":f"Chapter {ex['chapter']}","section":ex['section'],"pages":"","role_in_book":"Exercise problem"}],
        "content_hash": ch,
        "extraction_date": EXTR_DATE,
        "extraction_agent": "v8-full-extract",
    }
    with open(os.path.join(d, "concept.yaml"), 'w', encoding='utf-8') as f:
        yaml.dump(yaml_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=200)

    # theorem.tex for exercise statement
    with open(os.path.join(d, "theorem.tex"), 'w', encoding='utf-8') as f:
        f.write(ex["tex"].strip() + "\n")

    # introduce.en.md
    intro_md = f"""---
role: introduce
locale: en
content_hash: "{ch}"
written_against: ""
---

Exercise {ex['ex_num']} from Chapter {ex['chapter']} of {BOOK_TITLE} ({BOOK_AUTHOR}, {BOOK_EDITION})."""
    with open(os.path.join(d, "introduce.en.md"), 'w', encoding='utf-8') as f:
        f.write(intro_md.strip() + "\n")

    # exercise_gtm003_Ch.Sec.N.en.md
    ex_md = f"""---
role: exercise
locale: en
chapter: "{ex['chapter']}"
section: "{ex['section']}"
exercise_number: {ex['ex_num']}
---

{ex['tex'].strip()}"""
    sec_slug = ex['section'].replace(' ','-').replace(',','')
    with open(os.path.join(d, f"exercise_{BOOK_ID}_{ex['chapter']}_{sec_slug}_{ex['ex_num']}.en.md"), 'w', encoding='utf-8') as f:
        f.write(ex_md.strip() + "\n")

print(f"Wrote {len(exercises_data)} exercises")
print("DONE")
