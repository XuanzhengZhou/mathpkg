#!/usr/bin/env python3
"""Create all concept files for GTM031 s038_1_Existence_of_a_basis section."""
import os

BASE = "/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch4/gtm031/s038_1_Existence_of_a_basis"

BOOK_INFO = {
    "book_id": "gtm031",
    "author": "Nathan Jacobson",
    "title": "Lectures in Abstract Algebra II: Linear Algebra",
    "chapter": "IV",
    "section": "1-6"
}

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

def concept_yaml(slug, title_en, type_, domain, subdomain, difficulty, tags, required, role_in_book, chapter_override=None, section_override=None):
    ch = chapter_override or BOOK_INFO["chapter"]
    sec = section_override or BOOK_INFO["section"]
    tags_str = "[" + ", ".join(tags) + "]"
    req_str = "[" + ", ".join(required) + "]"
    return f"""id: {slug}
title_en: "{title_en}"
title_zh: ""
type: {type_}
domain: {domain}
subdomain: {subdomain}
difficulty: {difficulty}
tags: {tags_str}
depends_on:
  required: {req_str}
  recommended: []
  suggested: []
source_books:
  - book_id: "{BOOK_INFO['book_id']}"
    author: "{BOOK_INFO['author']}"
    title: "{BOOK_INFO['title']}"
    chapter: "{ch}"
    section: "{sec}"
    pages: ""
    role_in_book: "{role_in_book}"
content_hash: ""
extraction_date: "2026-06-27"
extraction_agent: "v8-full-extract"
"""

def introduce_en(title_en, description):
    return f"""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
{description}
"""

def proof_md(slug, ch, sec, proof_text):
    return f"""---
role: proof
locale: en
of_concept: {slug}
source_book: {BOOK_INFO['book_id']}
source_chapter: "{ch}"
source_section: "{sec}"
---
{proof_text}
"""

def exercise_md(ch, sec, ex_num, statement):
    return f"""---
role: exercise
locale: en
chapter: "{ch}"
section: "{sec}"
exercise_number: {ex_num}
---
{statement}
"""

# ============================================================
# CONCEPT 1: generating-set
# ============================================================
slug = "generating-set"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Set of Generators of a Vector Space", "definition",
    "algebra", "linear-algebra", "basic",
    ["generating-set", "vector-space", "linear-combination", "span"],
    [],
    "Defines a generating set (set of generators) of a vector space over a division ring as a subset such that every vector is a finite linear combination of its elements."
))
write_file(os.path.join(d, "theorem.tex"), r"""Let $\Re$ be an arbitrary vector space over a division ring $\Delta$. A subset $S$ of $\Re$ is a \textit{set of generators} of $\Re$ if every vector in $\Re$ is a (finite) linear combination of the vectors belonging to $S$.
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Set of Generators of a Vector Space",
    "A set of generators for a vector space is a subset from which every vector can be expressed as a finite linear combination. This concept generalizes the notion of spanning set to arbitrary (possibly infinite-dimensional) vector spaces over division rings. It is the starting point for the existence theory of bases in the infinite-dimensional setting."
))

# ============================================================
# CONCEPT 2: linear-independence
# ============================================================
slug = "linear-independence"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Linear Independence (Arbitrary Subset)", "definition",
    "algebra", "linear-algebra", "basic",
    ["linear-independence", "vector-space", "basis-theory"],
    [],
    "Defines linear independence for arbitrary (possibly infinite) subsets of a vector space: a set S is linearly independent if every finite subset of S is linearly independent."
))
write_file(os.path.join(d, "theorem.tex"), r"""Let $\Re$ be an arbitrary vector space over a division ring $\Delta$. A subset $S$ of $\Re$ is \textit{linearly independent} if every finite subset $F$ of $S$ is linearly independent.
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Linear Independence (Arbitrary Subset)",
    "For arbitrary vector spaces, linear independence is defined through the finite subsets: an infinite set is linearly independent precisely when all its finite subsets are. This finitary condition extends the familiar finite-dimensional definition to the general case. It is essential for defining bases in infinite-dimensional vector spaces."
))

# ============================================================
# CONCEPT 3: basis
# ============================================================
slug = "basis-of-vector-space"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Basis of a Vector Space", "definition",
    "algebra", "linear-algebra", "basic",
    ["basis", "vector-space", "linear-independence", "generating-set"],
    ["generating-set", "linear-independence"],
    "Defines a basis as a linearly independent set of generators; equivalently, every vector can be expressed uniquely as a finite linear combination of basis elements."
))
write_file(os.path.join(d, "theorem.tex"), r"""Let $\Re$ be a vector space over a division ring $\Delta$. A subset $B$ which is linearly independent and a set of generators is a \textit{basis} in the sense that every vector can be written in one and only one way as a linear combination of elements in $B$.
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Basis of a Vector Space",
    "A basis is a linearly independent generating set. In arbitrary vector spaces, the defining property is that every vector has a unique representation as a finite linear combination of basis elements. The existence of bases for arbitrary vector spaces, proved using Zorn's Lemma, is a fundamental result of linear algebra in the infinite-dimensional setting."
))

# ============================================================
# CONCEPT 4: generators-contain-basis (theorem)
# ============================================================
slug = "generators-contain-basis"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Every Set of Generators Contains a Basis", "theorem",
    "algebra", "linear-algebra", "intermediate",
    ["basis", "generating-set", "zorn-lemma", "maximal-element", "vector-space"],
    ["generating-set", "linear-independence", "basis-of-vector-space", "zorns-lemma"],
    "Proves that any set of generators of a vector space contains a basis. The proof uses Zorn's Lemma to find a maximal linearly independent subset."
))
write_file(os.path.join(d, "theorem.tex"), r"""Let $\Re$ be a vector space over a division ring $\Delta$. Any set of generators $S$ of $\Re$ contains a basis for $\Re$.
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Every Set of Generators Contains a Basis",
    "This fundamental theorem guarantees the existence of a basis for any vector space that admits a generating set. The proof applies Zorn's Lemma to the collection of linearly independent subsets of the generating set, ordered by inclusion, and extracts a maximal element which is shown to be a basis."
))
write_file(os.path.join(d, f"proof_{BOOK_INFO['book_id']}_{BOOK_INFO['chapter']}.{BOOK_INFO['section']}.en.md"), proof_md(
    slug, BOOK_INFO["chapter"], BOOK_INFO["section"], r"""Let $S$ be a set of generators for $\Re$. Let $P$ be the collection of linearly independent subsets of $S$. Then $P$ is a partially ordered set relative to the relation of inclusion. Let $L$ be a linearly ordered subcollection of $P$, and let $U$ be the logical sum of the sets belonging to $L$. We assert that $U$ is linearly independent. Otherwise $U$ contains a dependent set $u_1, u_2, \cdots, u_m$. Now $u_i \in A_i \in L$. Also for any $i, j$ either $A_i \subseteq A_j$ or $A_j \subseteq A_i$. Hence one of the $A$'s, say $A_m$, contains all the others. Thus every $u_i \in A_m$ and $A_m$ contains a finite linearly dependent subset. This contradicts the assumption that $A_m \in P$; hence $U \in P$. It is clear that this element serves as an upper bound for all the $A \in L$. We can now apply Zorn's lemma to conclude that $P$ contains a maximal element, and this means that the set of generators $S$ contains a maximal linearly independent subset $B$. It is now easy to see that $B$ is a basis for $\Re$. If $y$ is any member of $S$ not contained in $B$, then the set $B \cup \{y\}$ is a dependent set. This implies that $y$ is a linear combination of elements of $B$ (Lemma 1 on p. 11). Hence every $s \in S$ is a linear combination of elements of $B$. It follows that $B$ is a set of generators and, since $B$ is a linearly independent set, $B$ is, in fact, a basis.
"""))

# ============================================================
# CONCEPT 5: independent-set-supplement-to-basis (theorem)
# ============================================================
slug = "independent-set-supplement-to-basis"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Linearly Independent Set Can Be Supplemented to a Basis", "theorem",
    "algebra", "linear-algebra", "intermediate",
    ["basis", "linear-independence", "extension", "zorn-lemma", "vector-space"],
    ["generating-set", "linear-independence", "basis-of-vector-space"],
    "States that any linearly independent set can be supplemented by elements from any basis to give a basis."
))
write_file(os.path.join(d, "theorem.tex"), r"""Let $\Re$ be a vector space over a division ring $\Delta$. Any linearly independent set of elements can be supplemented by elements from any basis to give a basis of $\Re$.
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Linearly Independent Set Can Be Supplemented to a Basis",
    "This theorem is the dual of the generators-contain-basis result: any linearly independent set can be extended to a basis. Together these two results establish the fundamental structure theory of bases in arbitrary vector spaces. The proof uses a cardinal number argument (due to Lowig) when the basis is infinite."
))
write_file(os.path.join(d, f"proof_{BOOK_INFO['book_id']}_{BOOK_INFO['chapter']}.{BOOK_INFO['section']}.en.md"), proof_md(
    slug, BOOK_INFO["chapter"], BOOK_INFO["section"], r"""It suffices to consider the case in which both bases $B$ and $C$ are infinite. Here the following argument due to Lowig can be applied. Express each $e_i$ of $B$ in terms of the $f_k$ of $C$ as
$$e_i = \beta_1 f_{k_1} + \beta_2 f_{k_2} + \cdots + \beta_m f_{k_m}$$
where the $\beta_j \neq 0$. Now every $f_k$ occurs in some such expression; for if a particular $f_k$ does not occur, then, since this $f_k$ is a linear combination of the $e$'s and each $e$ is a linear combination of $f$'s $\neq f_k$, $f_k$ is a linear combination of $f$'s $\neq f_k$. This contradicts the linear independence of the $f$'s.

We can now define a single-valued mapping $\phi$ of the set $C$ into the set $B$. Let $f_k \in C$ and let $e_i \equiv \phi(f_k)$ be one of the $e$'s in $B$ whose expression involves $f_k$. We thus obtain a single-valued mapping of the whole of $C$ into $B$. Let $B' = \phi(C)$ be the image set. If $e_{i'} \in B'$, the inverse image $\phi^{-1}(e_{i'})$ consists of those $f_k$ which occur in the expression for $e_{i'}$. Thus $\phi^{-1}(e_{i'})$ is a finite set. Now we have a 1-1 correspondence between the set $B'$ and the collection $\Gamma$ of inverse images $\phi^{-1}(e_{i'})$. The collection $\Gamma$ gives a decomposition of the set $C$ into non-overlapping finite sets. Moreover, since $C$ is infinite, $\Gamma$ is infinite. It follows easily from standard theorems in the theory of cardinal numbers that $C$ and $\Gamma$ have the same cardinal number. Hence the cardinal number of $B'$ is the same as that of $C$ and so the cardinal number of $B$ is greater than or equal to that of $C$.
"""))

# ============================================================
# CONCEPT 6: zorns-lemma
# ============================================================
slug = "zorns-lemma"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Zorn's Lemma", "lemma",
    "foundations", "set-theory", "intermediate",
    ["zorn-lemma", "axiom-of-choice", "partial-order", "maximal-element"],
    ["partially-ordered-set", "chain", "upper-bound"],
    "Zorn's Lemma: a partially ordered set in which every chain has an upper bound possesses a maximal element. Essential for proving existence of bases in infinite-dimensional vector spaces."
))
write_file(os.path.join(d, "theorem.tex"), r"""Let $P$ be a partially ordered set which has the property that every linearly ordered subset has an upper bound. Then $P$ possesses a maximal element.
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Zorn's Lemma",
    "Zorn's Lemma is a fundamental set-theoretic principle equivalent to the Axiom of Choice. It states that any partially ordered set in which every chain (linearly ordered subset) has an upper bound must contain at least one maximal element. It is an indispensable tool for proving existence results throughout algebra, including the existence of bases in arbitrary vector spaces, maximal ideals in rings, and algebraic closures of fields."
))

# ============================================================
# CONCEPT 7: partially-ordered-set
# ============================================================
slug = "partially-ordered-set"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Partially Ordered Set", "definition",
    "foundations", "set-theory", "basic",
    ["partial-order", "poset", "reflexive", "antisymmetric", "transitive"],
    [],
    "Recalls the definition of a partially ordered set: a set with a binary relation a <= b satisfying reflexivity, antisymmetry, and transitivity. Initially defined in Chapter I."
))
write_file(os.path.join(d, "theorem.tex"), r"""A \textit{partially ordered set} is a set $P$ in which a binary relation $a \leq b$ is defined such that:
\begin{enumerate}
\item[(i)] $a \leq a$ (reflexivity);
\item[(ii)] if $a \leq b$ and $b \leq a$, then $a = b$ (antisymmetry);
\item[(iii)] if $a \leq b$ and $b \leq c$, then $a \leq c$ (transitivity).
\end{enumerate}
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Partially Ordered Set",
    "A partially ordered set (or poset) generalizes the usual order on numbers to more abstract settings. The relation must satisfy reflexivity, antisymmetry, and transitivity. Posets are the natural setting for applying Zorn's Lemma, which requires the partial order structure to guarantee the existence of maximal elements."
))

# ============================================================
# CONCEPT 8: chain
# ============================================================
slug = "chain"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Chain (Linearly Ordered Set)", "definition",
    "foundations", "set-theory", "basic",
    ["chain", "linear-order", "total-order", "partial-order"],
    ["partially-ordered-set"],
    "A chain (linearly ordered set) is a partially ordered set in which any two elements are comparable."
))
write_file(os.path.join(d, "theorem.tex"), r"""A \textit{linearly ordered set} (or a \textit{chain}) is a partially ordered set with the property that for any two elements $a, b$, either $a \leq b$ or $b \leq a$.
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Chain (Linearly Ordered Set)",
    "A chain, also called a totally ordered set or linearly ordered set, is a partially ordered set where every pair of elements is comparable. Chains are the subsets to which the hypothesis of Zorn's Lemma refers: the condition that every chain has an upper bound."
))

# ============================================================
# CONCEPT 9: upper-bound
# ============================================================
slug = "upper-bound"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Upper Bound in a Partially Ordered Set", "definition",
    "foundations", "set-theory", "basic",
    ["upper-bound", "partial-order", "poset", "zorn-lemma"],
    ["partially-ordered-set"],
    "An upper bound of a subset S of a partially ordered set P is an element u in P such that s <= u for every s in S."
))
write_file(os.path.join(d, "theorem.tex"), r"""An \textit{upper bound} of a subset $S$ of a partially ordered set $P$ is an element $u \in P$ such that $s \leq u$ for every $s$ in $S$.
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Upper Bound in a Partially Ordered Set",
    "An upper bound of a subset is an element that dominates every member of the subset with respect to the partial order. The concept is central to Zorn's Lemma: the hypothesis requires that every chain possesses an upper bound."
))

# ============================================================
# CONCEPT 10: maximal-element
# ============================================================
slug = "maximal-element"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Maximal Element in a Partially Ordered Set", "definition",
    "foundations", "set-theory", "basic",
    ["maximal-element", "partial-order", "poset", "zorn-lemma"],
    ["partially-ordered-set"],
    "A maximal element m of a subset S is an element such that no s != m in S satisfies m <= s."
))
write_file(os.path.join(d, "theorem.tex"), r"""An element $m$ of a subset $S$ of a partially ordered set is \textit{maximal} if no $s \neq m$ in $S$ has the property $m \leq s$.
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Maximal Element in a Partially Ordered Set",
    "A maximal element is one that cannot be strictly exceeded within the subset. Note the distinction from a maximum (or greatest element): a maximal element need not be comparable to all other elements. Zorn's Lemma guarantees the existence of a maximal element (not necessarily a maximum) under the chain condition."
))

# ============================================================
# CONCEPT 11: invariance-of-basis-cardinality
# ============================================================
slug = "invariance-of-basis-cardinality"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Invariance of the Cardinal Number of a Basis", "theorem",
    "algebra", "linear-algebra", "intermediate",
    ["basis", "cardinal-number", "dimension", "invariance", "vector-space"],
    ["basis-of-vector-space", "generators-contain-basis"],
    "Any two bases of a vector space have the same cardinal number, establishing the well-definedness of dimension for arbitrary vector spaces."
))
write_file(os.path.join(d, "theorem.tex"), r"""Any two bases of a vector space $\Re$ over a division ring $\Delta$ have the same cardinal number.
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Invariance of the Cardinal Number of a Basis",
    "This theorem establishes that the cardinality of a basis is an invariant of the vector space, independent of the choice of basis. This justifies the definition of dimension for arbitrary (possibly infinite-dimensional) vector spaces. The proof uses a cardinal number comparison argument originally due to Lowig."
))
write_file(os.path.join(d, f"proof_{BOOK_INFO['book_id']}_{BOOK_INFO['chapter']}.{BOOK_INFO['section']}.en.md"), proof_md(
    slug, BOOK_INFO["chapter"], BOOK_INFO["section"], r"""We argue via the Lowig argument. Express each $e_i$ of $B$ in terms of the $f_k$ of $C$ as
$$e_i = \beta_1 f_{k_1} + \beta_2 f_{k_2} + \cdots + \beta_m f_{k_m}$$
where the $\beta_j \neq 0$. Now every $f_k$ occurs in some such expression; for if a particular $f_k$ does not occur, then, since this $f_k$ is a linear combination of the $e$'s and each $e$ is a linear combination of $f$'s $\neq f_k$, $f_k$ is a linear combination of $f$'s $\neq f_k$. This contradicts the linear independence of the $f$'s.

We can now define a single-valued mapping $\phi$ of the set $C$ into the set $B$. Let $f_k \in C$ and let $e_i \equiv \phi(f_k)$ be one of the $e$'s in $B$ whose expression involves $f_k$. We thus obtain a single-valued mapping of the whole of $C$ into $B$. Let $B' = \phi(C)$ be the image set. If $e_{i'} \in B'$, the inverse image $\phi^{-1}(e_{i'})$ consists of those $f_k$ which occur in the expression for $e_{i'}$. Thus $\phi^{-1}(e_{i'})$ is a finite set. Now we have a 1-1 correspondence between the set $B'$ and the collection $\Gamma$ of inverse images $\phi^{-1}(e_{i'})$. The collection $\Gamma$ gives a decomposition of the set $C$ into non-overlapping finite sets. Moreover, since $C$ is infinite, $\Gamma$ is infinite. It follows easily from standard theorems in the theory of cardinal numbers that $C$ and $\Gamma$ have the same cardinal number. Hence the cardinal number of $B'$ is the same as that of $C$ and so the cardinal number of $B$ is greater than or equal to that of $C$. By symmetry, we also have $|C| \geq |B|$, thus $|B| = |C|$.
"""))

# ============================================================
# CONCEPT 12: function-space-standard-basis
# ============================================================
slug = "function-space-standard-basis"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Standard Basis of the Function Space", "proposition",
    "algebra", "linear-algebra", "basic",
    ["function-space", "standard-basis", "kronecker-delta", "cardinal-number"],
    ["basis-of-vector-space"],
    "Constructs the space of all functions from an index set I to Delta and shows the Kronecker delta functions form a basis of cardinality |I|."
))
write_file(os.path.join(d, "theorem.tex"), r"""Let $\Delta$ be a division ring and $I$ be any set. Let $\Re$ be the set of functions from $I$ to $\Delta$ which vanish at all but a finite number of elements of $I$. For each $i \in I$, define $e_i$ to be the vector such that
$$e_i(j) = \delta_{ij}.$$
Then the set $\{e_i\}_{i \in I}$ is a basis of $\Re$, and the cardinal number of this basis equals the cardinal number of $I$.
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Standard Basis of the Function Space",
    "For any set I, the space of finitely supported functions from I to a division ring provides a canonical example of a vector space. The Kronecker delta functions form the standard basis, establishing a 1-1 correspondence between basis elements and index set elements. This construction shows that vector spaces of any given dimension exist."
))

# ============================================================
# CONCEPT 13: noether-basis-theorem
# ============================================================
slug = "noether-basis-theorem"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Noether Basis Theorem (Theorem 1)", "theorem",
    "algebra", "linear-algebra", "intermediate",
    ["noether-basis", "subspace", "complement", "basis", "emmy-noether"],
    ["basis-of-vector-space", "subspace-complement"],
    "Theorem 1 (Emmy Noether): For a subspace S of R with basis B, there exists a Noether basis for S relative to B — a basis for S obtained via the complement construction."
))
write_file(os.path.join(d, "theorem.tex"), r"""Let $\mathfrak{R}$ be a vector space over a division ring $\Delta$ with basis $B$. Let $\mathfrak{S}$ be a subspace of $\mathfrak{R}$. There exists a complement $\mathfrak{S}'$ of $\mathfrak{S}$ spanned by a subset $D = (e_k)$ of $B$. Let $C = (e_j)$ be the complement of $D$ in $B$. Then each $e_j = f_j - u_j$ where $f_j \in \mathfrak{S}$ and $u_j \in \mathfrak{S}'$, and $(f_j)$ is a basis for $\mathfrak{S}$ (a \textit{Noether basis}).
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Noether Basis Theorem (Theorem 1)",
    "Emmy Noether proved that every subspace of a vector space admits a basis naturally related to the ambient basis, called a Noether basis. This result establishes a precise relationship between the basis of a subspace and the basis of the whole space, generalizing the finite-dimensional situation where any basis of a subspace can be extended to a basis of the whole space."
))
write_file(os.path.join(d, f"proof_{BOOK_INFO['book_id']}_{BOOK_INFO['chapter']}.{BOOK_INFO['section']}.en.md"), proof_md(
    slug, BOOK_INFO["chapter"], BOOK_INFO["section"], r"""There exists a complement $\mathfrak{S}'$ of $\mathfrak{S}$ spanned by a subset $D = (e_k)$ of $B$. Let $C = (e_j)$ be the complement of $D$ in $B$. Then each $e_j = f_j - u_j$ where $f_j \in \mathfrak{S}$ and $u_j \in \mathfrak{S}'$ and, as we proceed to show, $(f_j)$ is a basis for $\mathfrak{S}$. The set $(f_j)$ is linearly independent, for let $\sum \beta_j f_j = 0$. Then $\sum \beta_j e_j + \sum \beta_j u_j = 0$; hence every $\beta_j = 0$ by the linear independence of the $e_j$. The set $(f_j)$ generates $\mathfrak{S}$; for if $y \in \mathfrak{S}$, then $y = \sum \beta_j e_j + \sum \gamma_k e_k = \sum \beta_j f_j - \sum \beta_j u_j + \sum \gamma_k e_k$. Then $y - \sum \beta_j f_j \in \mathfrak{S}'$, and hence $y - \sum \beta_j f_j = 0$. We note finally that, if $e_j$ and $e_{j'}$ are distinct elements in $C$, then $f_j \neq f_{j'}$. Otherwise $e_j - e_{j'} \in \mathfrak{S}'$, contrary to the fact that $B$ is a basis. We therefore see that the mapping $e_j \to f_j$ is 1-1 and this concludes the proof.
"""))

# ============================================================
# CONCEPT 14: row-finite-matrix
# ============================================================
slug = "row-finite-matrix"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Row-Finite Matrix", "definition",
    "algebra", "linear-algebra", "intermediate",
    ["row-finite-matrix", "infinite-matrix", "linear-transformation", "matrix-representation"],
    ["linear-transformation", "basis-of-vector-space"],
    "A row-finite matrix is an I x J matrix in which each row has only finitely many non-zero entries. Such matrices represent linear transformations between infinite-dimensional vector spaces."
))
write_file(os.path.join(d, "theorem.tex"), r"""Let $\mathfrak{R}$ and $\mathfrak{S}$ be vector spaces over a division ring $\Delta$ with bases $(e_i)_{i \in I}$ and $(f_j)_{j \in J}$ respectively. The matrix $(\alpha_{ij})$ of a linear transformation $A: \mathfrak{R} \to \mathfrak{S}$ defined by
$$e_i A = \sum_j \alpha_{ij} f_j$$
is \textit{row-finite}: for each fixed $i$, only finitely many $\alpha_{ij}$ are non-zero. The set of all $I \times J$ row-finite matrices is denoted by $M_{I \times J}^{\text{rf}}(\Delta)$.
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Row-Finite Matrix",
    "A row-finite matrix is the natural generalization of a finite matrix to the infinite-dimensional setting. Each row has only finitely many non-zero entries, corresponding to the fact that the image of each basis vector is a finite linear combination. The collection of row-finite matrices forms a ring under addition and the usual matrix multiplication (which remains well-defined due to the row-finiteness condition)."
))

# ============================================================
# CONCEPT 15: linear-transformations-isomorphic-to-row-finite-matrices
# ============================================================
slug = "lt-isomorphic-row-finite-matrices"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Isomorphism Between Linear Transformations and Row-Finite Matrices", "proposition",
    "algebra", "linear-algebra", "intermediate",
    ["linear-transformation", "row-finite-matrix", "isomorphism", "matrix-representation"],
    ["row-finite-matrix", "linear-transformation"],
    "The correspondence between linear transformations and row-finite matrices is a bijection; the matrix of a sum is the sum of matrices, giving a group isomorphism."
))
write_file(os.path.join(d, "theorem.tex"), r"""The correspondence $A \to (\alpha)$ determined by the matrix representation relative to bases of $\mathfrak{R}$ and $\mathfrak{S}$ is a 1-1 correspondence between the set $\mathfrak{L}(\mathfrak{R}, \mathfrak{S})$ of linear transformations and the set of row-finite $I \times J$ matrices. The matrix corresponding to the sum of two transformations is obtained by adding the corresponding component matrices.
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Isomorphism Between Linear Transformations and Row-Finite Matrices",
    "Just as in the finite-dimensional case, linear transformations between vector spaces with specified bases correspond bijectively to matrices. In the infinite-dimensional setting, the appropriate matrix class is the row-finite matrices. This correspondence respects addition, making it an isomorphism of additive groups."
))
write_file(os.path.join(d, f"proof_{BOOK_INFO['book_id']}_{BOOK_INFO['chapter']}.{BOOK_INFO['section']}.en.md"), proof_md(
    slug, BOOK_INFO["chapter"], BOOK_INFO["section"], r"""We can verify easily as in the finite case that the correspondence $A \to (\alpha)$ determined by $e_i A = \sum_j \alpha_{ij} f_j$ is 1-1 of the set $\mathfrak{L}(\mathfrak{R}, \mathfrak{S})$ of linear transformations onto the set of row finite $I \times J$ matrices. The matrix corresponding to the sum of two transformations is obtained from the two matrices by adding components $\alpha_{ii'}, \beta_{ii'}$. It follows that the row finite matrices form a group relative to this operation.
"""))

# ============================================================
# CONCEPT 16: product-of-row-finite-matrices
# ============================================================
slug = "product-of-row-finite-matrices"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Product of Row-Finite Matrices", "proposition",
    "algebra", "linear-algebra", "intermediate",
    ["row-finite-matrix", "matrix-multiplication", "ring-of-matrices", "composition"],
    ["row-finite-matrix", "lt-isomorphic-row-finite-matrices"],
    "The product of two row-finite I x I matrices is defined by the usual matrix multiplication formula (finite sum per entry) and is again row-finite. The set of row-finite matrices forms a ring isomorphic to the ring of linear transformations."
))
write_file(os.path.join(d, "theorem.tex"), r"""If $\mathfrak{L} = \mathfrak{L}(\mathfrak{R}, \mathfrak{R})$ and the matrix of $A$ and $B$ are determined by a single basis, then the element $\gamma_{i\lambda}$ of the matrix of $AB$ is
$$\gamma_{i\lambda} = \sum_k \alpha_{ik}\beta_{k\lambda}$$
where $A \to (\alpha)$ and $B \to (\beta)$. The sum is finite, and the product matrix $(\gamma) = (\alpha)(\beta)$ is row finite. The set $\Delta_I$ of $I \times I$ row finite matrices together with the indicated addition and multiplication is a ring isomorphic to the ring $\mathfrak{L}$.
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Product of Row-Finite Matrices",
    "Matrix multiplication for row-finite matrices generalizes the familiar finite-dimensional formula. The row-finiteness condition ensures that each entry of the product is a finite sum. Under addition and this multiplication, the set of square row-finite matrices forms a ring that is isomorphic to the ring of linear transformations (endomorphisms) of the vector space."
))

# ============================================================
# CONCEPT 17: change-of-basis-row-finite-matrices
# ============================================================
slug = "change-of-basis-row-finite"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Change of Basis for Row-Finite Matrices", "proposition",
    "algebra", "linear-algebra", "intermediate",
    ["change-of-basis", "row-finite-matrix", "transition-matrix", "invertible-matrix"],
    ["row-finite-matrix", "product-of-row-finite-matrices"],
    "Change of basis in the infinite-dimensional setting is expressed by mutually inverse row-finite matrices."
))
write_file(os.path.join(d, "theorem.tex"), r"""Let $(e_i)_{i \in I}$ and $(f_i)_{i \in I}$ be two bases of $\mathfrak{R}$ indexed by the same set $I$. Then there exist row-finite $I \times I$ matrices $(\mu)$ and $(\nu)$ such that
$$f_k = \sum_{\mu} \mu_{ki} e_i, \quad e_i = \sum_{\nu} \nu_{ik} f_k$$
and $(\mu)(\nu) = 1 = (\nu)(\mu)$ where $1$ is the matrix with elements $\delta_{ik}$. Thus $(\mu)$ is a unit in the ring $\Delta_I$ of row-finite matrices.
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Change of Basis for Row-Finite Matrices",
    "In the infinite-dimensional case, change of basis is expressed through mutually inverse row-finite matrices. This generalizes the finite-dimensional formula where transition matrices are invertible square matrices. The row-finite condition ensures that each basis vector is expressed as a finite linear combination of the other basis."
))

# ============================================================
# CONCEPT 18: vector-space-cardinality-lemma (Lemma 1)
# ============================================================
slug = "vector-space-cardinality-lemma"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Cardinal Number of an Infinite-Dimensional Vector Space (Lemma 1)", "lemma",
    "algebra", "linear-algebra", "intermediate",
    ["cardinal-number", "vector-space", "dimension", "infinite-cardinals"],
    ["basis-of-vector-space", "invariance-of-basis-cardinality"],
    "Lemma 1: If dim R = b is infinite and the cardinal number of Delta is d, then the cardinal number of R is bd."
))
write_file(os.path.join(d, "theorem.tex"), r"""If $\dim \mathfrak{R} = b$ is infinite and the cardinal number of $\Delta$ is $d$, then the cardinal number of $\mathfrak{R}$ is $bd$.
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Cardinal Number of an Infinite-Dimensional Vector Space (Lemma 1)",
    "This lemma computes the cardinality of an infinite-dimensional vector space as the product of the cardinalities of a basis and the underlying division ring. It is a crucial step in determining the dimension of the dual space."
))
write_file(os.path.join(d, f"proof_{BOOK_INFO['book_id']}_{BOOK_INFO['chapter']}.{BOOK_INFO['section']}.en.md"), proof_md(
    slug, BOOK_INFO["chapter"], BOOK_INFO["section"], r"""If $(e_i)$ is a basis for $\mathfrak{R}$, every non-zero vector $x$ in $\mathfrak{R}$ has a unique representation as
$$x = \sum_{j=1}^{N} \xi_{i_j} e_{i_j}, \quad \xi_{i_j} \neq 0.$$
Thus with each $x \neq 0$ we can associate a uniquely determined subset $\{e_{i_1}, e_{i_2}, \cdots, e_{i_N}\}$ and a unique $N$-tuple $(\xi_{i_1}, \xi_{i_2}, \cdots, \xi_{i_N})$ with non-zero components in $\Delta$. Since $(e_i)$ is infinite, the cardinal number of the set of subsets containing $N$ elements of $(e_i)$ equals $b$. On the other hand, the cardinal number of the set of $N$-tuples $(\xi_{i_1}, \xi_{i_2}, \cdots, \xi_{i_N})$ is either $d (= d^N)$ or it is finite. In either case the cardinal number of the set of pairs consisting of the set $\{e_{i_1}, e_{i_2}, \cdots, e_{i_N}\}$ and the $N$-tuple $(\xi_{i_1}, \xi_{i_2}, \cdots, \xi_{i_N})$ is $db$. It follows that the cardinal number of $\mathfrak{R}$ is $bd$.
"""))

# ============================================================
# CONCEPT 19: strongly-independent-collection
# ============================================================
slug = "strongly-independent-collection"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Strongly Independent Collection of Sequences", "definition",
    "algebra", "linear-algebra", "advanced",
    ["strongly-independent", "sequences", "dual-space", "linear-independence"],
    ["linear-independence"],
    "A collection F of sequences with entries in Delta is strongly independent if every finite square matrix chosen from the collection is non-singular."
))
write_file(os.path.join(d, "theorem.tex"), r"""A collection $F$ of sequences $(\gamma_1, \gamma_2, \cdots)$ with entries in a division ring $\Delta$ is \textit{strongly independent} if every finite square matrix chosen from the collection is non-singular. We choose a finite square matrix from $F$ by selecting first a finite set of sequences
$$(\gamma_1^{(1)}, \gamma_2^{(1)}, \cdots), (\gamma_1^{(2)}, \gamma_2^{(2)}, \cdots), \cdots, (\gamma_1^{(n)}, \gamma_2^{(n)}, \cdots)$$
and then a set $i_1, i_2, \cdots, i_n$ of indices, obtaining the matrix
$$\begin{bmatrix}
\gamma_{i_1}^{(1)} & \gamma_{i_2}^{(1)} & \cdots & \gamma_{i_n}^{(1)} \\
\cdot & \cdot & \cdots & \cdot \\
\cdot & \cdot & \cdots & \cdot \\
\gamma_{i_1}^{(n)} & \gamma_{i_2}^{(n)} & \cdots & \gamma_{i_n}^{(n)}
\end{bmatrix}$$
and requiring this matrix to be non-singular.
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Strongly Independent Collection of Sequences",
    "A strongly independent collection of sequences is a stronger condition than ordinary linear independence: every finite square submatrix formed from the sequences (by selecting finitely many coordinates) must be non-singular. This concept is essential for constructing a large linearly independent set in the dual space and proving the dimensionality formula for the dual."
))

# ============================================================
# CONCEPT 20: strongly-independent-existence-lemma (Lemma 2)
# ============================================================
slug = "strongly-independent-existence-lemma"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Existence of a Large Strongly Independent Collection (Lemma 2)", "lemma",
    "algebra", "linear-algebra", "advanced",
    ["strongly-independent", "dual-space", "cardinal-number", "zorn-lemma"],
    ["strongly-independent-collection", "zorns-lemma", "vector-space-cardinality-lemma"],
    "Lemma 2: There exists a strongly independent collection of sequences with cardinal number at least the cardinality of the division ring d."
))
write_file(os.path.join(d, "theorem.tex"), r"""There exists a strongly independent collection of sequences with entries in $\Delta$ whose cardinal number is $\geq d$, where $d$ is the cardinal number of the division ring $\Delta$.
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Existence of a Large Strongly Independent Collection (Lemma 2)",
    "This lemma constructs a strongly independent collection of sequences of size at least the cardinality of the division ring. The proof uses Zorn's Lemma to obtain a maximal such collection, then shows by an inductive construction that any maximal collection must have cardinality at least d. This is the key ingredient in the proof that the dual space has dimension d^b."
))
write_file(os.path.join(d, f"proof_{BOOK_INFO['book_id']}_{BOOK_INFO['chapter']}.{BOOK_INFO['section']}.en.md"), proof_md(
    slug, BOOK_INFO["chapter"], BOOK_INFO["section"], r"""We partially order the strongly independent collections $F$ by inclusion. If a set $\{F\}$ of these collections is linearly ordered, clearly $\bigcup F$ is strongly independent. By Zorn's lemma, there exists a maximal strongly independent collection $M$. We shall prove, by induction, that if the cardinal number of $M$ is less than $d$, then we can construct a sequence $X \notin M$ such that $M \cup \{X\}$ is strongly independent, thereby contradicting the maximality of $M$. Suppose that we have found the first $p$ elements $\xi_1, \xi_2, \cdots, \xi_p$ of $X$ so that every $q \times q$ matrix, $q \leq p$, chosen from $M \cup \{(\xi_1, \xi_2, \cdots, \xi_p)\}$ is non-singular. We shall determine $\xi_{p+1}$ so that every $r \times r$ matrix, $r \leq p+1$, of the form
$$\begin{bmatrix} A & * \\ \xi_{i_1}, \cdots, \xi_{i_{r-1}} & \xi_{p+1} \end{bmatrix}$$
where $A$ is an $(r-1) \times (r-1)$ matrix determined by $M$, be non-singular. Now for each matrix of this form, in which $\xi_{p+1}$ is regarded as an indeterminate, there is just one choice of $\xi_{p+1}$ in $\Delta$ making it singular. Thus, $A$ is a non-singular matrix; hence its row vectors are left linearly independent. It follows that the row vector $(\xi_{i_1}, \xi_{i_2}, \cdots, \xi_{i_{r-1}})$ can be written in one and only one way as a linear combination of the rows of $A$. Then if $\mu$ represents the same linear combination of the elements of the last column, the matrix is non-singular provided that $\xi_{p+1} \neq \mu$. We note next that the cardinal number of the collection of such matrices in which $\xi_{p+1}$ is an indeterminate is less than $d$. By our assumption the cardinal number of $M$ is less than $d$. The cardinal number of the set of matrices under consideration is the product of the cardinal number of sets of $r-1$ sequences chosen from $M$ times the cardinal number of $r-1$ elements chosen in the integers $1, 2, \cdots, p$. The result is either finite or the cardinal number of $M$. In either case it is less than $d$. Since the cardinal number of $\Delta$ is $d$, we can choose $\xi_{p+1}$ so that all such matrices are non-singular. This completes the proof by induction of the existence of $X$ such that $M \cup \{X\}$ is strongly independent. We have therefore contradicted the maximality of $M$ and established the lemma.
"""))

# ============================================================
# CONCEPT 21: dual-space-dimension-theorem (Theorem 2)
# ============================================================
slug = "dual-space-dimension-theorem"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Dimensionality of the Dual Space (Theorem 2)", "theorem",
    "algebra", "linear-algebra", "advanced",
    ["dual-space", "dimension", "cardinal-number", "linear-functional", "infinite-dimensional"],
    ["vector-space-cardinality-lemma", "strongly-independent-existence-lemma", "basis-of-vector-space"],
    "Theorem 2: If R is a vector space of infinite dimension b over Delta of cardinality d, then dim(R*) = d^b, the cardinal number of all functions from a set of cardinality b to a set of cardinality d."
))
write_file(os.path.join(d, "theorem.tex"), r"""If $\mathfrak{R}$ is a vector space of infinite dimensionality $b$ over a division ring $\Delta$ whose cardinal number is $d$, then the dimensionality $b^*$ of the dual space $\mathfrak{R}^*$ is $d^b$, the cardinal number of the set of mappings of a set of cardinal number $b$ into one of cardinal number $d$.
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Dimensionality of the Dual Space (Theorem 2)",
    "This theorem computes the dimension of the dual space of an infinite-dimensional vector space. Unlike the finite-dimensional case where the dual has the same dimension, for infinite-dimensional spaces the dual is always strictly larger: dim(R*) = d^b > b = dim(R). This result shows that a vector space cannot be identified with its double dual in the infinite-dimensional setting."
))
write_file(os.path.join(d, f"proof_{BOOK_INFO['book_id']}_{BOOK_INFO['chapter']}.{BOOK_INFO['section']}.en.md"), proof_md(
    slug, BOOK_INFO["chapter"], BOOK_INFO["section"], r"""The relation $b^* = d^b$ implies, of course, that $b^* > b$. Moreover, if $b^{**} \equiv \dim \mathfrak{R}^{**}$, then $b^{**} > b^* > b$. This result shows that $\mathfrak{R}$ cannot be identified with the space of linear functions on $\mathfrak{R}^*$.

The proof uses Lemma 1 to determine the cardinality of $\mathfrak{R}$ as $bd$, and Lemma 2 to construct a sufficiently large linearly independent set in $\mathfrak{R}^*$. Specifically, Lemma 2 provides a strongly independent collection of cardinality at least $d$, which yields $d^b$ linearly independent linear functionals on $\mathfrak{R}$.
"""))

# ============================================================
# CONCEPT 22: topological-space (definition recalled in Section 6)
# ============================================================
slug = "topological-space"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Topological Space", "definition",
    "topology", "general-topology", "basic",
    ["topological-space", "open-set", "topology"],
    [],
    "A topological space is a set E together with a collection of subsets (called open sets) such that arbitrary unions and finite intersections of open sets are open, and E and the empty set are open."
))
write_file(os.path.join(d, "theorem.tex"), r"""A \textit{topological space} consists of a set $E$ and a collection of subsets of $E$, called \textit{open sets}, such that:
\begin{enumerate}
\item[1.] The logical sum (arbitrary union) of any collection of open sets is open.
\item[2.] The intersection of any finite number of open sets is open.
\item[3.] The set $E$ and the vacuous set $\emptyset$ are open.
\end{enumerate}
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Topological Space",
    "A topological space provides the minimal structure needed to define continuity and convergence. The definition through open sets (axioms of arbitrary unions, finite intersections, and containment of the whole space and empty set) is the standard formulation. This definition is recalled in the context of introducing the finite topology on the space of linear transformations."
))

# ============================================================
# CONCEPT 23: basis-of-topology
# ============================================================
slug = "basis-of-topology"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Basis of a Topology", "definition",
    "topology", "general-topology", "basic",
    ["basis", "topology", "open-set"],
    ["topological-space"],
    "A subcollection B of open sets is a basis if every open set is a union of members of B. Equivalently, the intersection of any two basis elements is a union of basis elements."
))
write_file(os.path.join(d, "theorem.tex"), r"""A subcollection $\mathfrak{B}$ of the set of open sets is called a \textit{basis} for the topology if every open set is a logical sum of members of $\mathfrak{B}$. If $\mathfrak{B}$ is a basis, then the intersection of any two elements of $\mathfrak{B}$ is a logical sum of elements of $\mathfrak{B}$. Conversely, if $E$ is any set and $\mathfrak{B}$ is a collection of its subsets such that their logical sum is $E$ and the intersection of any two elements of $\mathfrak{B}$ is a logical sum of elements of $\mathfrak{B}$, then $\mathfrak{B}$ is a basis for a topology on $E$.
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Basis of a Topology",
    "A basis for a topology is a convenient tool for specifying a topology: instead of describing all open sets, it suffices to specify a basis whose elements generate all open sets via arbitrary unions. The defining condition ensures consistency of the generated topology."
))

# ============================================================
# CONCEPT 24: finite-topology-linear-transformations
# ============================================================
slug = "finite-topology-linear-transformations"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Finite Topology on Linear Transformations", "definition",
    "topology", "functional-analysis", "intermediate",
    ["finite-topology", "linear-transformations", "topology-on-operators", "pointwise-convergence"],
    ["topological-space", "basis-of-topology", "linear-transformation"],
    "The finite topology on L(R,S) has as basis the sets O(x_i; y_i) = {A : x_i A = y_i, i=1,...,m} for finite collections of vectors x_i in R and y_i in S."
))
write_file(os.path.join(d, "theorem.tex"), r"""The \textit{finite topology} of $\mathfrak{L}(\mathfrak{R}, \mathfrak{S})$ is defined by taking as a basis the collection of sets
$$O(x_1, \cdots, x_m; y_1, \cdots, y_m) = \{ A \in \mathfrak{L}(\mathfrak{R}, \mathfrak{S}) : x_i A = y_i, \; i = 1, \cdots, m \}$$
for arbitrary finite collections $x_1, \cdots, x_m \in \mathfrak{R}$ and $y_1, \cdots, y_m \in \mathfrak{S}$. Moreover, any such open set is either vacuous or coincides with an open set $O(x_j; y_j)$ where the $x_j$ are linearly independent. Thus the sets $O(x_j; y_j)$ with $x_j$ linearly independent constitute a basis for this topology.
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Finite Topology on Linear Transformations",
    "The finite topology (also known as the topology of pointwise convergence or the strong operator topology in some contexts) on the space of linear transformations has as basic open neighborhoods those transformations that agree on a prescribed finite set of vectors. This topology is discrete precisely when the domain is finite-dimensional, providing a sharp contrast between finite and infinite-dimensional theories. It also makes composition continuous."
))

# ============================================================
# CONCEPT 25: finite-topology-discrete-iff-finite-dimensional
# ============================================================
slug = "finite-topology-discrete-iff-finite-dim"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Finite Topology Is Discrete If and Only If Finite Dimensional", "proposition",
    "topology", "functional-analysis", "intermediate",
    ["finite-topology", "discrete-topology", "finite-dimensional", "infinite-dimensional"],
    ["finite-topology-linear-transformations", "basis-of-vector-space"],
    "The topological space L(R,S) with the finite topology is discrete (every subset is open) if and only if R is finite dimensional."
))
write_file(os.path.join(d, "theorem.tex"), r"""The topological space $\mathfrak{L}(\mathfrak{R}, \mathfrak{S})$ endowed with the finite topology is discrete in the sense that every subset is open, if and only if $\mathfrak{R}$ is finite dimensional.
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Finite Topology Is Discrete If and Only If Finite Dimensional",
    "This proposition characterizes when the finite topology on the space of linear transformations is trivial (discrete). For finite-dimensional domains, fixing the images of a basis yields a singleton open set. For infinite-dimensional domains, no finite set of vectors can pin down a transformation uniquely, so the topology is non-discrete."
))
write_file(os.path.join(d, f"proof_{BOOK_INFO['book_id']}_{BOOK_INFO['chapter']}.{BOOK_INFO['section']}.en.md"), proof_md(
    slug, BOOK_INFO["chapter"], BOOK_INFO["section"], r"""First, let $\mathfrak{R}$ have the finite basis $e_1, e_2, \cdots, e_n$ and let $A \in \mathfrak{L}(\mathfrak{R}, \mathfrak{S})$. Then $O(e_i; e_i A) = \{A\}$ so that $\{A\}$ is an open set. It follows from the axiom that arbitrary unions of open sets are open that every subset of $\mathfrak{L}(\mathfrak{R}, \mathfrak{S})$ is open. Next let $\dim \mathfrak{R}$ be infinite. Then if $x_1, x_2, \cdots, x_r$ is a linearly independent set, $O(x_j; y_j)$ contains more than one element since there exist many linear transformations taking the given values on a finite linearly independent set and extending arbitrarily on the rest of a basis. Hence the topology is not discrete.
"""))

# ============================================================
# CONCEPT 26: closed-set
# ============================================================
slug = "closed-set"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Closed Set in a Topological Space", "definition",
    "topology", "general-topology", "basic",
    ["closed-set", "topology", "complement"],
    ["topological-space"],
    "A subset of a topological space is closed if its complement is open. Closed sets satisfy: arbitrary intersections and finite unions of closed sets are closed, and E and the empty set are closed."
))
write_file(os.path.join(d, "theorem.tex"), r"""A subset of a topological space $E$ is called \textit{closed} if its complement is open. The closed sets satisfy conditions dual to those of open sets: the intersection of any number of closed sets is closed, and the union of any finite number of closed sets is closed. The whole space $E$ and the vacuous set $\emptyset$ are closed.
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Closed Set in a Topological Space",
    "A closed set is the complement of an open set. The closed sets form a dual structure to the open sets, satisfying the dual axioms (closure under arbitrary intersections and finite unions). This concept is essential for defining the closure of a set."
))

# ============================================================
# CONCEPT 27: closure-of-set
# ============================================================
slug = "closure-of-set"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Closure of a Set in a Topological Space", "definition",
    "topology", "general-topology", "basic",
    ["closure", "topology", "closed-set", "limit-point"],
    ["topological-space", "closed-set"],
    "The closure Cl S of a subset S is the intersection of all closed sets containing S, equivalently the set of points p such that every neighborhood of p has non-empty intersection with S."
))
write_file(os.path.join(d, "theorem.tex"), r"""The \textit{closure} $\text{Cl}\, S$ of a subset $S$ of a topological space $E$ is defined to be the intersection of all the closed sets containing $S$. Equivalently, $\text{Cl}\, S$ is the totality of points $p \in E$ with the property that every neighborhood of $p$ has non-vacuous intersection with $S$.
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Closure of a Set in a Topological Space",
    "The closure of a set is the smallest closed set containing it. The equivalent neighborhood characterization states that a point belongs to the closure precisely when it cannot be separated from the set by any open set. This is a fundamental concept in topology."
))

# ============================================================
# CONCEPT 28: exercise-1-mackey
# ============================================================
slug = "mackey-linear-independence-geometric-sequences"
d = os.path.join(BASE, slug)
write_file(os.path.join(d, "concept.yaml"), concept_yaml(
    slug, "Mackey's Linear Independence of Geometric Sequences (Exercise 1)", "proposition",
    "algebra", "linear-algebra", "intermediate",
    ["linear-independence", "geometric-progression", "dual-space", "mackey"],
    ["linear-independence", "dual-space-dimension-theorem"],
    "Exercise 1 (Mackey): The collection of sequences xi_gamma = (gamma, gamma^2, gamma^3, ...) for gamma != 0 in a field Phi is linearly independent. This gives an elementary proof of Theorem 2 for the commutative case."
))
write_file(os.path.join(d, "theorem.tex"), r"""Let $\mathfrak{R}$ be a vector space over a field $\Phi$. Prove that the collection of sequences $\xi_\gamma = (\gamma, \gamma^2, \gamma^3, \cdots)$, $\gamma \neq 0$ in $\Phi$, is linearly independent.
""")
write_file(os.path.join(d, "introduce.en.md"), introduce_en(
    "Mackey's Linear Independence of Geometric Sequences (Exercise 1)",
    "This exercise, attributed to Mackey, asks to prove that the geometric progression sequences form a linearly independent set in the space of all sequences over a field. This provides an elementary proof of the dual space dimension theorem (Theorem 2) for the commutative case, avoiding the more involved construction via strongly independent collections."
))
write_file(os.path.join(d, f"exercise_{BOOK_INFO['book_id']}_{BOOK_INFO['chapter']}.{BOOK_INFO['section']}.1.en.md"), exercise_md(
    BOOK_INFO["chapter"], BOOK_INFO["section"], 1,
    r"""(Mackey) Let $\mathfrak{R}$ be a vector space over a field $\Phi$. Prove that the collection of sequences $\xi_\gamma = (\gamma, \gamma^2, \gamma^3, \cdots)$, $\gamma \neq 0$ in $\Phi$, is linearly independent. (Note: This leads to an elementary proof of Theorem 2 for the commutative case.)
"""))

# ============================================================
# .done marker
# ============================================================
write_file(os.path.join(BASE, ".done"), "DONE\n")

print(f"Created 28 concept directories in {BASE}")
print("Done.")
