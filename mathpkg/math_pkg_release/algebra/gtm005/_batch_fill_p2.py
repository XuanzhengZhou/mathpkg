#!/usr/bin/env python3
"""Batch fill phase 2: remaining GTM005 concept files across all incomplete sections."""
import os, yaml

BASE = "/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch1/gtm005"

def write_concept(slug, ydata, tex, intro):
    d = os.path.join(BASE, slug)
    os.makedirs(d, exist_ok=True)
    yp = os.path.join(d, "concept.yaml")
    tp = os.path.join(d, "theorem.tex")
    ip = os.path.join(d, "introduce.en.md")
    if not os.path.exists(yp):
        with open(yp, 'w') as f:
            yaml.dump(ydata, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    if not os.path.exists(tp):
        with open(tp, 'w') as f:
            f.write(tex.strip() + "\n")
    if not os.path.exists(ip):
        with open(ip, 'w') as f:
            f.write("---\nrole: introduce\nlocale: en\ncontent_hash: \"\"\nwritten_against: \"\"\n---\n" + intro + "\n")
    print("  OK:", slug)

src = lambda ch,sec: [{"book_id": "gtm005", "author": "Saunders Mac Lane",
    "title": "Categories for the Working Mathematician", "chapter": ch, "section": sec,
    "pages": "", "role_in_book": ""}]

# ═══════════════════════════════════════════
# s009 III Universals and Limits (7 concepts)
# ═══════════════════════════════════════════
P = "s009_III_Universals_and_Limits"

write_concept(f"{P}/universal-arrow-from-c-to-s",
    {"id":"universal-arrow-from-c-to-s","title_en":"Universal Arrow from c to S","title_zh":"",
     "type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
     "tags":["universal-arrow","universal-property"],
     "depends_on":{"required":["functor","category"],"recommended":[],"suggested":["yoneda-lemma"]},
     "source_books":src("III","1"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""If $S: D \to C$ is a functor and $c$ an object of $C$, a \emph{universal arrow from $c$ to $S$} is a pair $\langle r, u \rangle$ consisting of an object $r$ of $D$ and an arrow $u: c \to Sr$ of $C$, such that for every pair $\langle d, f \rangle$ with $d$ an object of $D$ and $f: c \to Sd$ an arrow of $C$, there is a unique arrow $f': r \to d$ of $D$ with $Sf' \circ u = f$.
""",
    r"""A universal arrow from an object $c$ to a functor $S: D \to C$ formalizes the idea of a "best approximation" of $c$ by values of $S$. It consists of an object $r \in D$ and an arrow $u: c \to Sr$ such that any other arrow $c \to Sd$ factors uniquely through $u$ via $S$. This is one of the fundamental notions of category theory, unifying free constructions, limits, adjunctions, and representable functors."""
)

write_concept(f"{P}/universal-element-of-functor",
    {"id":"universal-element-of-functor","title_en":"Universal Element of a Functor","title_zh":"",
     "type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
     "tags":["universal-element","representable-functor"],
     "depends_on":{"required":["functor","hom-functor"],"recommended":[],"suggested":["yoneda-lemma"]},
     "source_books":src("III","1"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""If $H: C \to \mathbf{Set}$ is a functor, a \emph{universal element} of $H$ is a pair $\langle r, e \rangle$ consisting of an object $r \in C$ and an element $e \in Hr$ such that for every pair $\langle c, x \rangle$ with $x \in Hc$, there is a unique arrow $f: r \to c$ with $(Hf)e = x$.
""",
    r"""A universal element of a set-valued functor $H: C \to \mathbf{Set}$ is an element $e \in Hr$ from which every other element can be obtained uniquely by applying $H$ to some arrow. Universal elements provide an equivalent formulation of representable functors: $H$ is representable if and only if it has a universal element. This concept bridges the gap between universal arrows and the Yoneda lemma."""
)

write_concept(f"{P}/representation-of-functor",
    {"id":"representation-of-functor","title_en":"Representation of a Functor","title_zh":"",
     "type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
     "tags":["representable-functor","hom-functor","yoneda-lemma"],
     "depends_on":{"required":["functor","hom-functor","natural-isomorphism"],"recommended":[],"suggested":[]},
     "source_books":src("III","1"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""A functor $H: C \to \mathbf{Set}$ is \emph{representable} if there exists an object $r \in C$ and a natural isomorphism
$$\varphi: \hom_C(r, -) \cong H$$
of functors $C \to \mathbf{Set}$. The object $r$ is called the \emph{representing object}. The pair $\langle r, \varphi \rangle$ is a \emph{representation} of $H$.
""",
    r"""A functor $H: C \to \mathbf{Set}$ is representable if it is naturally isomorphic to a hom-functor $\hom(r, -)$ for some object $r$. Representability is a central concept in category theory: many important constructions (products, coproducts, limits, adjoints) are instances of representable functors. The Yoneda lemma establishes that representations are essentially unique when they exist."""
)

write_concept(f"{P}/yoneda-lemma",
    {"id":"yoneda-lemma","title_en":"Yoneda Lemma","title_zh":"",
     "type":"theorem","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
     "tags":["yoneda-lemma","representable-functor","natural-transformation"],
     "depends_on":{"required":["functor","natural-transformation","hom-functor"],"recommended":[],"suggested":["yoneda-embedding"]},
     "source_books":src("III","1"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""For a functor $H: C \to \mathbf{Set}$ and an object $r \in C$, there is a bijection
$$\theta: \mathrm{Nat}(\hom_C(r, -), H) \cong Hr$$
which sends each natural transformation $\alpha: \hom_C(r, -) \Rightarrow H$ to the element $\alpha_r(1_r) \in Hr$. This bijection is natural in both $r$ and $H$.
""",
    r"""The Yoneda lemma is one of the most fundamental results in category theory. It states that natural transformations from a representable functor $\hom(r, -)$ to any set-valued functor $H$ correspond bijectively to elements of $Hr$. A crucial corollary is that the Yoneda embedding $y: C \to [C^{\mathrm{op}}, \mathbf{Set}]$ sending $r$ to $\hom(-, r)$ is fully faithful, meaning every category can be embedded in a functor category."""
)

write_concept(f"{P}/universality-via-hom-sets",
    {"id":"universality-via-hom-sets","title_en":"Universality via Hom-Sets","title_zh":"",
     "type":"proposition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
     "tags":["universal-property","hom-set","representable-functor"],
     "depends_on":{"required":["universal-arrow","representable-functor","yoneda-lemma"],"recommended":[],"suggested":[]},
     "source_books":src("III","1"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""For a functor $S: D \to C$ and an object $c \in C$, a universal arrow $\langle r, u: c \to Sr \rangle$ from $c$ to $S$ determines, for each $d \in D$, a bijection
$$\hom_D(r, d) \cong \hom_C(c, Sd),$$
natural in $d$, sending $f': r \to d$ to $Sf' \circ u$. Conversely, such a natural bijection determines a universal arrow.
""",
    r"""Mac Lane shows that a universal arrow $\langle r, u \rangle$ from $c$ to $S$ is equivalent to a natural isomorphism $\hom_D(r, -) \cong \hom_C(c, S-)$ between hom-functors. This characterization via hom-sets reveals the deep connection between universal properties and representable functors: the functor $\hom_C(c, S-)$ is represented by $r$."""
)

write_concept(f"{P}/natural-transformations-between-hom-functors",
    {"id":"natural-transformations-between-hom-functors","title_en":"Natural Transformations Between Hom-Functors","title_zh":"",
     "type":"proposition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
     "tags":["natural-transformation","hom-functor","yoneda-lemma"],
     "depends_on":{"required":["natural-transformation","hom-functor","yoneda-lemma"],"recommended":[],"suggested":[]},
     "source_books":src("III","1"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""For a category $C$, any natural transformation $\alpha: \hom_C(r, -) \Rightarrow \hom_C(s, -)$ between covariant hom-functors is of the form $\alpha = \hom_C(h, -)$ for a unique arrow $h: s \to r$ in $C$. In particular, the Yoneda embedding is fully faithful.
""",
    r"""A key consequence of the Yoneda lemma is that natural transformations between covariant representable functors $\hom(r, -)$ and $\hom(s, -)$ correspond uniquely to arrows $h: s \to r$ in the opposite direction. This establishes that the Yoneda embedding $y: C^{\mathrm{op}} \to [C, \mathbf{Set}]$ is fully faithful, allowing any category to be faithfully represented as a full subcategory of a functor category."""
)

write_concept(f"{P}/universal-arrow-and-representable-functor",
    {"id":"universal-arrow-and-representable-functor","title_en":"Universal Arrow and Representable Functor","title_zh":"",
     "type":"proposition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
     "tags":["universal-arrow","representable-functor","adjunction"],
     "depends_on":{"required":["universal-arrow","representable-functor"],"recommended":[],"suggested":["adjunction"]},
     "source_books":src("III","1"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""A universal arrow from $c$ to $S: D \to C$ with universal pair $\langle r, u: c \to Sr \rangle$ is equivalent to a representation of the functor $\hom_C(c, S-): D \to \mathbf{Set}$ with representing object $r$. Conversely, a representation $\hom_D(r, -) \cong H$ gives a universal element $1_r \in \hom_D(r, r) \cong Hr$.
""",
    r"""Mac Lane demonstrates the equivalence between three fundamental notions: universal arrows, universal elements, and representable functors. A universal arrow from $c$ to $S$ corresponds to a representation of the functor $\hom_C(c, S-)$, and a universal element of $H$ corresponds to a representation of $H$. These equivalences form the conceptual backbone for understanding adjunctions."""
)

# ═══════════════════════════════════════════
# s011 Adjunctions (9 concepts)
# ═══════════════════════════════════════════
P = "s011_1_Adjunctions"

write_concept(f"{P}/adjunction",
    {"id":"adjunction","title_en":"Adjunction","title_zh":"",
     "type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
     "tags":["adjunction","adjoint-functor","category-theory"],
     "depends_on":{"required":["functor","natural-transformation","universal-arrow"],"recommended":[],"suggested":[]},
     "source_books":src("IV","1"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""An \emph{adjunction} from a category $X$ to a category $A$ consists of two functors $F: X \to A$ and $G: A \to X$ together with a natural transformation $\eta: I_X \Rightarrow GF$ (the \emph{unit}) such that for every pair of objects $x \in X$, $a \in A$ and every arrow $h: x \to Ga$, there is a unique arrow $h^\sharp: Fx \to a$ with $Gh^\sharp \circ \eta_x = h$.
""",
    r"""An adjunction is one of the most important concepts in category theory, introduced by Daniel Kan. It consists of two functors $F \dashv G$ (read "$F$ is left adjoint to $G$") with a universal property: every arrow from $x$ to $Ga$ corresponds uniquely to an arrow from $Fx$ to $a$. Adjunctions unify many mathematical constructions, including free-forgetful pairs, products, limits, and Galois connections."""
)

write_concept(f"{P}/left-adjoint-right-adjoint",
    {"id":"left-adjoint-right-adjoint","title_en":"Left Adjoint and Right Adjoint","title_zh":"",
     "type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
     "tags":["left-adjoint","right-adjoint","adjunction"],
     "depends_on":{"required":["adjunction","functor"],"recommended":[],"suggested":[]},
     "source_books":src("IV","1"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""In an adjunction $\langle F, G, \varphi \rangle: X \rightleftharpoons A$, the functor $F: X \to A$ is called the \emph{left adjoint} and $G: A \to X$ is called the \emph{right adjoint}. The notation $F \dashv G$ denotes "$F$ is left adjoint to $G$."
""",
    r"""In an adjunction $F \dashv G$, the left adjoint $F$ provides the "free" or "most efficient" construction, while the right adjoint $G$ provides the "forgetful" or "underlying" construction. Examples include: the free group functor is left adjoint to the forgetful functor $\mathbf{Set} \to \mathbf{Grp}$; the product functor is right adjoint to the diagonal; and existential quantification is left adjoint to substitution in logic."""
)

write_concept(f"{P}/unit-of-adjunction",
    {"id":"unit-of-adjunction","title_en":"Unit of an Adjunction","title_zh":"",
     "type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
     "tags":["adjunction","unit","natural-transformation"],
     "depends_on":{"required":["adjunction","natural-transformation"],"recommended":[],"suggested":["counit-of-adjunction"]},
     "source_books":src("IV","1"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""For an adjunction $F \dashv G$ with $F: X \to A$ and $G: A \to X$, the \emph{unit} is the natural transformation $\eta: I_X \Rightarrow GF$ whose component at each $x \in X$ is the image $\eta_x: x \to GFx$ of $1_{Fx}$ under the adjunction bijection $\hom_A(Fx, Fx) \cong \hom_X(x, GFx)$.
""",
    r"""The unit of an adjunction $\eta: I_X \Rightarrow GF$ is the natural transformation that embeds each object $x$ into $GFx$. Intuitively, it sends each element to the "free" object it generates. For example, in the free group adjunction, the unit sends each set element to the corresponding generator of the free group. Together with the counit, the unit satisfies the triangle identities that characterize adjunctions."""
)

write_concept(f"{P}/counit-of-adjunction",
    {"id":"counit-of-adjunction","title_en":"Counit of an Adjunction","title_zh":"",
     "type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
     "tags":["adjunction","counit","natural-transformation"],
     "depends_on":{"required":["adjunction","natural-transformation"],"recommended":[],"suggested":["unit-of-adjunction"]},
     "source_books":src("IV","1"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""For an adjunction $F \dashv G$, the \emph{counit} is the natural transformation $\varepsilon: FG \Rightarrow I_A$ whose component at each $a \in A$ is the image $\varepsilon_a: FGa \to a$ of $1_{Ga}$ under the adjunction bijection $\hom_X(Ga, Ga) \cong \hom_A(FGa, a)$.
""",
    r"""The counit of an adjunction $\varepsilon: FG \Rightarrow I_A$ provides the "evaluation" map that collapses the free-forgetful construction back to the original object. For the free group adjunction, the counit sends each formal word in the free group on a group's underlying set to its actual product in the group. The unit and counit together satisfy the triangle identities: $G\varepsilon \circ \eta G = 1_G$ and $\varepsilon F \circ F\eta = 1_F$."""
)

write_concept(f"{P}/adjunction-via-adjuncts",
    {"id":"adjunction-via-adjuncts","title_en":"Adjunction via Adjuncts","title_zh":"",
     "type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
     "tags":["adjunction","adjunct","bijection"],
     "depends_on":{"required":["adjunction","functor"],"recommended":[],"suggested":[]},
     "source_books":src("IV","1"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""An adjunction $F \dashv G$ with $F: X \to A$ and $G: A \to X$ can be given by a natural bijection
$$\varphi = \varphi_{x,a}: \hom_A(Fx, a) \cong \hom_X(x, Ga)$$
for all $x \in X$, $a \in A$. For each arrow $f: Fx \to a$, its \emph{adjunct} is $\varphi f = Gf \circ \eta_x: x \to Ga$. For each $h: x \to Ga$, its adjoint is $\varphi^{-1} h = \varepsilon_a \circ Fh: Fx \to a$.
""",
    r"""Mac Lane presents several equivalent formulations of adjunctions. One of the most practical is via a natural bijection between hom-sets: $\hom(Fx, a) \cong \hom(x, Ga)$. The image of an arrow under this bijection is called its adjunct (or transpose). This hom-set formulation is often the most convenient for constructing specific adjunctions in mathematical practice."""
)

write_concept(f"{P}/adjunction-unit-counit-triangular-identities",
    {"id":"adjunction-unit-counit-triangular-identities","title_en":"Adjunction via Unit-Counit and Triangular Identities","title_zh":"",
     "type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
     "tags":["adjunction","unit","counit","triangle-identities"],
     "depends_on":{"required":["adjunction","unit-of-adjunction","counit-of-adjunction"],"recommended":[],"suggested":[]},
     "source_books":src("IV","1"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""An adjunction $F \dashv G$ can be given equivalently by natural transformations $\eta: I_X \Rightarrow GF$ (the unit) and $\varepsilon: FG \Rightarrow I_A$ (the counit) satisfying the \emph{triangular identities}:
$$G\varepsilon \circ \eta G = 1_G, \qquad \varepsilon F \circ F\eta = 1_F.$$
These are also written as the commutative diagrams requiring $G\varepsilon_a \circ \eta_{Ga} = 1_{Ga}$ and $\varepsilon_{Fx} \circ F\eta_x = 1_{Fx}$.
""",
    r"""An adjunction can be defined purely in terms of the unit $\eta$ and counit $\varepsilon$ satisfying two triangular identities. This elegant formulation, due to Kan, captures the essence of adjointness: the unit embeds $X$ into $GFX$, the counit collapses $FGA$ back to $A$, and the triangle identities ensure these operations compose to identities. This is the most symmetric and category-theoretic formulation of adjunctions."""
)

write_concept(f"{P}/adjunction-characterizations",
    {"id":"adjunction-characterizations","title_en":"Characterizations of Adjunctions","title_zh":"",
     "type":"theorem","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
     "tags":["adjunction","characterization","universal-arrow"],
     "depends_on":{"required":["adjunction","universal-arrow","representable-functor"],"recommended":[],"suggested":[]},
     "source_books":src("IV","1"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""The following data are equivalent for functors $F: X \to A$ and $G: A \to X$:
\begin{enumerate}
\item An adjunction $F \dashv G$ via a natural bijection $\hom_A(Fx, a) \cong \hom_X(x, Ga)$;
\item A universal arrow $\eta_x: x \to GFx$ from each $x$ to $G$ (giving the unit);
\item A universal arrow $\varepsilon_a: FGa \to a$ from $F$ to each $a$ (giving the counit);
\item Natural transformations $\eta: I_X \Rightarrow GF$ and $\varepsilon: FG \Rightarrow I_A$ satisfying the triangle identities.
\end{enumerate}
""",
    r"""Mac Lane proves the equivalence of several formulations of adjunctions: hom-set bijections, universal arrows from each object to the right adjoint, universal arrows from the left adjoint to each object, and the unit-counit with triangle identities. This theorem is fundamental for working with adjunctions in practice, as each formulation is convenient in different contexts."""
)

write_concept(f"{P}/uniqueness-of-left-adjoints",
    {"id":"uniqueness-of-left-adjoints","title_en":"Uniqueness of Left Adjoints","title_zh":"",
     "type":"proposition","domain":"foundations","subdomain":"category-theory","difficulty":"basic",
     "tags":["adjunction","uniqueness","left-adjoint"],
     "depends_on":{"required":["adjunction","natural-isomorphism"],"recommended":[],"suggested":[]},
     "source_books":src("IV","1"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""If $F, F': X \to A$ are both left adjoint to the same functor $G: A \to X$, then $F$ and $F'$ are naturally isomorphic. More precisely, there is a unique natural isomorphism $\theta: F \cong F'$ compatible with the units of the two adjunctions.
""",
    r"""Left adjoints are unique up to unique natural isomorphism. This is a key fact in category theory: if a functor has a left adjoint, that adjoint is essentially unique. This justifies speaking of "the" left adjoint once one is known to exist. The proof follows from the Yoneda lemma and the hom-set characterization of adjunctions."""
)

write_concept(f"{P}/representability-criterion-for-left-adjoint",
    {"id":"representability-criterion-for-left-adjoint","title_en":"Representability Criterion for Left Adjoint","title_zh":"",
     "type":"theorem","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
     "tags":["adjunction","representable-functor","freyd-adjoint-functor-theorem"],
     "depends_on":{"required":["adjunction","representable-functor"],"recommended":[],"suggested":["freyd-adjoint-functor-theorem"]},
     "source_books":src("IV","1"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""A functor $G: A \to X$ has a left adjoint if and only if for each object $x \in X$, the functor $\hom_X(x, G-): A \to \mathbf{Set}$ is representable. The representing object $Fx$ then gives the value of the left adjoint on $x$.
""",
    r"""Mac Lane gives a criterion for the existence of a left adjoint: a functor $G: A \to X$ has a left adjoint precisely when, for each $x$, the composite functor $\hom_X(x, G-)$ is representable. This is the theoretical basis for the General Adjoint Functor Theorem: under suitable completeness and solution-set conditions, the representability of these functors is guaranteed."""
)

# ═══════════════════════════════════════════
# s010 Limits (16 concepts)
# ═══════════════════════════════════════════
P = "s010_1_Let_functors"

write_concept(f"{P}/binary-product",
    {"id":"binary-product","title_en":"Binary Product","title_zh":"",
     "type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"basic",
     "tags":["product","limit","universal-property"],
     "depends_on":{"required":["category","universal-arrow"],"recommended":[],"suggested":[]},
     "source_books":src("III","3"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""A \emph{binary product} of objects $a, b$ in a category $C$ is an object $a \times b$ together with two arrows (projections) $p_1: a \times b \to a$ and $p_2: a \times b \to b$ such that for any object $c$ and arrows $f: c \to a$, $g: c \to b$, there is a unique arrow $h: c \to a \times b$ with $p_1 \circ h = f$ and $p_2 \circ h = g$.
""",
    r"""A binary product $a \times b$ in a category is the categorical formulation of the Cartesian product. It comes with projection maps to each factor, and any pair of maps into the factors factors uniquely through the product. Products are a special case of limits (limits over discrete diagrams with two objects) and are characterized by the universal property $\hom(c, a \times b) \cong \hom(c, a) \times \hom(c, b)$."""
)

write_concept(f"{P}/binary-coproduct",
    {"id":"binary-coproduct","title_en":"Binary Coproduct","title_zh":"",
     "type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"basic",
     "tags":["coproduct","colimit","universal-property"],
     "depends_on":{"required":["category","universal-arrow"],"recommended":[],"suggested":["binary-product"]},
     "source_books":src("III","3"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""A \emph{binary coproduct} of objects $a, b$ in a category $C$ is an object $a + b$ together with two arrows (injections) $i_1: a \to a + b$ and $i_2: b \to a + b$ such that for any object $c$ and arrows $f: a \to c$, $g: b \to c$, there is a unique arrow $h: a + b \to c$ with $h \circ i_1 = f$ and $h \circ i_2 = g$.
""",
    r"""A binary coproduct $a + b$ is the dual notion to a product: it is the "categorical sum." It comes with injections from each summand, and any pair of maps from the summands factors uniquely through the coproduct. In $\mathbf{Set}$, coproducts are disjoint unions; in $\mathbf{Grp}$, they are free products; in $\mathbf{Ab}$, they are direct sums (which coincide with finite products)."""
)

write_concept(f"{P}/equalizer",
    {"id":"equalizer","title_en":"Equalizer","title_zh":"",
     "type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"basic",
     "tags":["equalizer","limit","universal-property"],
     "depends_on":{"required":["category","limit"],"recommended":[],"suggested":[]},
     "source_books":src("III","3"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""An \emph{equalizer} of a parallel pair of arrows $f, g: a \to b$ in a category $C$ is an arrow $e: e \to a$ such that $f \circ e = g \circ e$, and for any arrow $h: c \to a$ with $f \circ h = g \circ h$, there is a unique arrow $k: c \to e$ with $e \circ k = h$.
""",
    r"""An equalizer is the categorical formulation of the solution set of an equation. Given two parallel arrows $f, g: a \to b$, their equalizer is the "largest subobject" of $a$ on which $f$ and $g$ agree. In $\mathbf{Set}$, the equalizer is the subset $\{x \in a \mid f(x) = g(x)\}$ with the inclusion map. Equalizers are always monic."""
)

write_concept(f"{P}/cokernel",
    {"id":"cokernel","title_en":"Cokernel","title_zh":"",
     "type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"basic",
     "tags":["cokernel","coequalizer","colimit"],
     "depends_on":{"required":["category","coequalizer","zero-arrow"],"recommended":[],"suggested":[]},
     "source_books":src("III","3"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""In a category with a zero object, the \emph{cokernel} of an arrow $f: a \to b$ is the coequalizer of $f$ and the zero arrow $0: a \to b$.
""",
    r"""The cokernel is the dual notion to the kernel in a category with zero morphisms. It is the coequalizer of $f$ and the zero arrow, representing the quotient of the codomain by the image of $f$. In abelian categories, the cokernel is a fundamental part of the kernel-cokernel exact sequence."""
)

write_concept(f"{P}/pullback",
    {"id":"pullback","title_en":"Pullback","title_zh":"",
     "type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"basic",
     "tags":["pullback","fiber-product","limit"],
     "depends_on":{"required":["category","limit"],"recommended":[],"suggested":[]},
     "source_books":src("III","3"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""A \emph{pullback} (or \emph{fiber product}) of a pair of arrows $f: a \to c$ and $g: b \to c$ is an object $a \times_c b$ together with arrows $p_1: a \times_c b \to a$ and $p_2: a \times_c b \to b$ such that $f \circ p_1 = g \circ p_2$, and for any $x$ with arrows $u: x \to a$, $v: x \to b$ satisfying $f \circ u = g \circ v$, there is a unique $h: x \to a \times_c b$ with $p_1 \circ h = u$ and $p_2 \circ h = v$.
""",
    r"""A pullback is the categorical formulation of the fiber product. Given two arrows $f: a \to c$ and $g: b \to c$, the pullback $a \times_c b$ is the universal object making the square commute. In $\mathbf{Set}$, it is $\{(x,y) \in a \times b \mid f(x) = g(y)\}$. Pullbacks are fundamental: they generalize inverse images, and many categorical constructions (equalizers, kernels, finite limits) can be built from pullbacks and a terminal object."""
)

write_concept(f"{P}/pushout",
    {"id":"pushout","title_en":"Pushout","title_zh":"",
     "type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"basic",
     "tags":["pushout","fiber-coproduct","colimit"],
     "depends_on":{"required":["category","colimit"],"recommended":[],"suggested":["pullback"]},
     "source_books":src("III","3"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""A \emph{pushout} (or \emph{fiber coproduct}) of a pair of arrows $f: c \to a$ and $g: c \to b$ is an object $a +_c b$ together with arrows $i_1: a \to a +_c b$ and $i_2: b \to a +_c b$ such that $i_1 \circ f = i_2 \circ g$, and it is universal with this property.
""",
    r"""A pushout is the dual notion to a pullback: given two arrows with a common domain, the pushout is the universal object completing the square. In $\mathbf{Set}$, pushouts are given by disjoint union modulo the equivalence generated by $f(c) \sim g(c)$. Pushouts are used to construct adjunction spaces in topology and amalgamated free products in group theory."""
)

write_concept(f"{P}/infinite-product",
    {"id":"infinite-product","title_en":"Infinite Product","title_zh":"",
     "type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
     "tags":["product","limit","infinite-product"],
     "depends_on":{"required":["category","limit"],"recommended":[],"suggested":["binary-product"]},
     "source_books":src("III","3"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""A \emph{product} of a family of objects $\{a_i\}_{i \in I}$ indexed by a set $I$ is an object $\prod_i a_i$ together with projections $p_i: \prod_i a_i \to a_i$ such that for any object $c$ and family of arrows $f_i: c \to a_i$, there is a unique arrow $h: c \to \prod_i a_i$ with $p_i \circ h = f_i$ for all $i$.
""",
    r"""An infinite (or small) product generalizes the binary product to an arbitrary indexed family of objects. It is the limit of a functor from a discrete category with object set $I$. The universal property is $\hom(c, \prod_i a_i) \cong \prod_i \hom(c, a_i)$. Categories with all small products are called complete."""
)

write_concept(f"{P}/infinite-coproduct",
    {"id":"infinite-coproduct","title_en":"Infinite Coproduct","title_zh":"",
     "type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
     "tags":["coproduct","colimit","infinite-coproduct"],
     "depends_on":{"required":["category","colimit"],"recommended":[],"suggested":["binary-coproduct"]},
     "source_books":src("III","3"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""A \emph{coproduct} of a family of objects $\{a_i\}_{i \in I}$ is an object $\coprod_i a_i$ together with injections $i_j: a_j \to \coprod_i a_i$ such that for any object $c$ and family $f_i: a_i \to c$, there is a unique $h: \coprod_i a_i \to c$ with $h \circ i_j = f_j$ for all $j$.
""",
    r"""An infinite coproduct (or small coproduct) is the dual of an infinite product. It is the colimit of a functor from a discrete category. In $\mathbf{Set}$, it is the disjoint union; in $\mathbf{Ab}$, it is the direct sum. Categories with all small coproducts are called cocomplete (when they also have coequalizers)."""
)

write_concept(f"{P}/power",
    {"id":"power","title_en":"Power (Categorical)","title_zh":"",
     "type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
     "tags":["power","cotensor","enriched-category"],
     "depends_on":{"required":["category","product"],"recommended":[],"suggested":[]},
     "source_books":src("III","3"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""For an object $a$ in a category $C$ and a set $J$, the \emph{power} $a^J$ (if it exists) is the object representing the functor $c \mapsto \hom(J, \hom(c, a))$, i.e., there is a natural isomorphism $\hom(c, a^J) \cong \hom(J, \hom(c, a))$.
""",
    r"""The power $a^J$ is the categorical notion of "iterated product of $a$ with itself $J$ times." When $C = \mathbf{Set}$, $a^J$ is exactly the set of functions $J \to a$, the usual exponential. More generally, in any category with products, $a^J$ is the $J$-fold product of copies of $a$."""
)

write_concept(f"{P}/copower",
    {"id":"copower","title_en":"Copower (Categorical)","title_zh":"",
     "type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
     "tags":["copower","tensor","enriched-category"],
     "depends_on":{"required":["category","coproduct"],"recommended":[],"suggested":["power"]},
     "source_books":src("III","3"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""For a set $J$ and an object $a$ in a category $C$, the \emph{copower} $J \cdot a$ (if it exists) is the $J$-fold coproduct of copies of $a$, i.e., $\coprod_{j \in J} a$.
""",
    r"""The copower $J \cdot a$ is the dual notion to the power. It is the $J$-fold coproduct of $a$, also called the tensor of $J$ with $a$ in the enriched category context. In $\mathbf{Set}$, $J \cdot a \cong J \times a$; in $\mathbf{Ab}$, $J \cdot G$ is the direct sum of $|J|$ copies of $G$."""
)

write_concept(f"{P}/colimit",
    {"id":"colimit","title_en":"Colimit","title_zh":"",
     "type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
     "tags":["colimit","limit","kan-extension"],
     "depends_on":{"required":["functor","universal-arrow"],"recommended":[],"suggested":["limit"]},
     "source_books":src("III","3"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""For a functor $F: J \to C$, a \emph{colimit} of $F$ is a universal arrow from $F$ to the diagonal functor $\Delta: C \to C^J$. It consists of an object $\varinjlim F \in C$ and a natural transformation $\lambda: F \Rightarrow \Delta(\varinjlim F)$ which is universal among natural transformations from $F$ to constant functors.
""",
    r"""A colimit is the dual notion to a limit, and generalizes coproducts, coequalizers, pushouts, and direct limits. Given a diagram $F: J \to C$, the colimit $\varinjlim F$ is the "universal cocone" under the diagram. Colimits are constructed by "gluing together" objects according to the shape of $J$. A category with all small colimits is called cocomplete."""
)

write_concept(f"{P}/kernel-pair",
    {"id":"kernel-pair","title_en":"Kernel Pair","title_zh":"",
     "type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
     "tags":["kernel-pair","pullback","equivalence-relation"],
     "depends_on":{"required":["category","pullback"],"recommended":[],"suggested":[]},
     "source_books":src("III","3"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""A \emph{kernel pair} of an arrow $f: a \to b$ is the pullback of $f$ along itself. It is a pair of arrows $p_1, p_2: a \times_b a \to a$ which internalizes the equivalence relation "have the same image under $f$."
""",
    r"""The kernel pair of an arrow $f$ is obtained by pulling back $f$ along itself. In a regular category, the kernel pair of a regular epimorphism is its "kernel congruence," and regular epimorphisms are precisely the coequalizers of their kernel pairs. Kernel pairs generalize the notion of kernel from abelian categories to arbitrary categories."""
)

write_concept(f"{P}/finite-products-from-terminal-and-binary",
    {"id":"finite-products-from-terminal-and-binary","title_en":"Finite Products from Terminal Object and Binary Products","title_zh":"",
     "type":"proposition","domain":"foundations","subdomain":"category-theory","difficulty":"basic",
     "tags":["finite-product","terminal-object","binary-product"],
     "depends_on":{"required":["terminal-object","binary-product"],"recommended":[],"suggested":[]},
     "source_books":src("III","3"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""A category $C$ has all finite products if and only if it has a terminal object and binary products. Any finite product $a_1 \times a_2 \times \cdots \times a_n$ can be constructed by iterating binary products, with the terminal object as the empty product.
""",
    r"""Mac Lane observes that finite products can be built from just two ingredients: a terminal object (the empty product) and binary products. This is because the limit over any finite discrete diagram can be constructed iteratively. This decomposition is a special case of the general fact that all finite limits can be built from pullbacks and a terminal object."""
)

write_concept(f"{P}/group-in-category",
    {"id":"group-in-category","title_en":"Group Object in a Category","title_zh":"",
     "type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
     "tags":["group-object","internal-group","cartesian-category"],
     "depends_on":{"required":["category","finite-products"],"recommended":[],"suggested":["monoid-in-category"]},
     "source_books":src("III","3"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""A \emph{group object} in a category $C$ with finite products is an object $G$ together with arrows:
\begin{itemize}
\item Multiplication $\mu: G \times G \to G$,
\item Unit $e: 1 \to G$,
\item Inverse $\iota: G \to G$,
\end{itemize}
such that the usual group axioms hold when expressed as commutative diagrams (associativity, left/right unit, left/right inverse).
""",
    r"""A group object in a category $C$ with finite products is the internalization of the notion of a group. The group operations are expressed as arrows in $C$, and the axioms as commutative diagrams. Examples include: topological groups in $\mathbf{Top}$, Lie groups in $\mathbf{Diff}$, and group schemes in algebraic geometry. This is a fundamental example of the "categorical algebra" approach."""
)

write_concept(f"{P}/monoid-in-category",
    {"id":"monoid-in-category","title_en":"Monoid Object in a Category","title_zh":"",
     "type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
     "tags":["monoid-object","internal-monoid","cartesian-category"],
     "depends_on":{"required":["category","finite-products"],"recommended":[],"suggested":["group-in-category"]},
     "source_books":src("III","3"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""A \emph{monoid object} in a category $C$ with finite products is an object $M$ together with arrows $\mu: M \times M \to M$ (multiplication) and $e: 1 \to M$ (unit) such that the associativity and unit axioms hold as commutative diagrams.
""",
    r"""A monoid object in a category $C$ with finite products internalizes the notion of a monoid. It consists of an object $M$ with multiplication and unit satisfying the usual axioms diagrammatically. When $C = \mathbf{Set}$, a monoid object is an ordinary monoid. The concept generalizes to monoidal categories, where one uses the monoidal product instead of the categorical product."""
)

write_concept(f"{P}/representable-functors-as-colimits",
    {"id":"representable-functors-as-colimits","title_en":"Representable Functors as Colimits","title_zh":"",
     "type":"theorem","domain":"foundations","subdomain":"category-theory","difficulty":"advanced",
     "tags":["representable-functor","colimit","yoneda-lemma","density"],
     "depends_on":{"required":["representable-functor","colimit","yoneda-lemma"],"recommended":[],"suggested":[]},
     "source_books":src("III","5"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
    r"""Every set-valued functor $H: C^{\mathrm{op}} \to \mathbf{Set}$ is a colimit of representable functors. More precisely, there is a canonical presentation of $H$ as the colimit of the composite
$$\int H \to C \xrightarrow{y} [C^{\mathrm{op}}, \mathbf{Set}]$$
where $\int H$ is the category of elements of $H$ and $y$ is the Yoneda embedding.
""",
    r"""A fundamental result in category theory: every presheaf is a colimit of representables. This "density theorem" means that the representable functors generate the entire presheaf category under colimits. The proof constructs the category of elements of $H$ and shows $H$ is the colimit of representables indexed by this category. This result is used extensively in the theory of Kan extensions and weighted limits."""
)

print("\nPhase 2 done!")
