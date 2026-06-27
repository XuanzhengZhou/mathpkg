#!/usr/bin/env python3
"""Batch fill missing concept files for GTM005 concepts (s004 section)."""
import os, yaml

BASE = "/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch1/gtm005"
P = "s004_4_Natural_Transformations"

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

# ─── determinant-as-natural-transformation ───
write_concept(
    f"{P}/determinant-as-natural-transformation",
    {"id": "determinant-as-natural-transformation",
     "title_en": "Determinant as a Natural Transformation",
     "title_zh": "", "type": "theorem", "domain": "foundations",
     "subdomain": "category-theory", "difficulty": "basic",
     "tags": ["natural-transformation", "determinant", "general-linear-group", "units"],
     "depends_on": {"required": ["natural-transformation", "functor"], "recommended": [], "suggested": []},
     "source_books": [{"book_id": "gtm005", "author": "Saunders Mac Lane",
        "title": "Categories for the Working Mathematician",
        "chapter": "I", "section": "4", "pages": "",
        "role_in_book": "Example of a natural transformation: determinant maps GL_n to units"}],
     "content_hash": "", "extraction_date": "2026-06-27", "extraction_agent": "v8-full-extract"},
    r"""For each commutative ring $K$, let $\det_K M$ be the determinant of an $n \times n$ matrix $M$ with entries in $K$, and let $K^*$ denote the group of units of $K$. Then $\det_K$ is a natural transformation between the functors $\mathrm{GL}_n$ and $(-)^*$:
$$\det: \mathrm{GL}_n \Rightarrow (-)^*$$
where $\mathrm{GL}_n: \mathbf{CRng} \to \mathbf{Grp}$ sends a ring $K$ to $\mathrm{GL}_n(K)$ and $(-)^*: \mathbf{CRng} \to \mathbf{Grp}$ sends $K$ to its group of units $K^*$.
""",
    r"""The determinant provides a classic example of a natural transformation. For each commutative ring $K$, the determinant $\det_K: \mathrm{GL}_n(K) \to K^*$ maps an invertible matrix to its determinant, which is a unit in $K$. These maps are natural in $K$: for any ring homomorphism $f: K \to K'$, the determinant commutes with the induced maps, making $\det$ a natural transformation from the general linear group functor to the group-of-units functor."""
)

# ─── double-character-group-natural-transformation ───
write_concept(
    f"{P}/double-character-group-natural-transformation",
    {"id": "double-character-group-natural-transformation",
     "title_en": "Double Character Group Natural Transformation",
     "title_zh": "", "type": "theorem", "domain": "foundations",
     "subdomain": "category-theory", "difficulty": "intermediate",
     "tags": ["natural-transformation", "character-group", "double-dual"],
     "depends_on": {"required": ["natural-transformation", "abelian-group"], "recommended": [], "suggested": []},
     "source_books": [{"book_id": "gtm005", "author": "Saunders Mac Lane",
        "title": "Categories for the Working Mathematician",
        "chapter": "I", "section": "4", "pages": "",
        "role_in_book": "Example: natural map from a group to its double character group"}],
     "content_hash": "", "extraction_date": "2026-06-27", "extraction_agent": "v8-full-extract"},
    r"""For each abelian group $G$, let $D(G) = \hom(G, \mathbb{R}/\mathbb{Z})$ be the character group of $G$. The twice-iterated character group $G \mapsto D(DG)$ and the identity $I(G) = G$ are both functors $\mathbf{Ab} \to \mathbf{Ab}$. For each group $G$ there is a natural transformation
$$\tau: I \Rightarrow D \circ D$$
given by $\tau_G: G \to D(DG)$, where $(\tau_G g)(t) = t(g)$ for each $g \in G$ and character $t \in DG$.
""",
    r"""For an abelian group $G$, the double character group $D(DG)$ consists of homomorphisms from the character group $DG = \hom(G, \mathbb{R}/\mathbb{Z})$ to $\mathbb{R}/\mathbb{Z}$. Mac Lane observes that the canonical map $\tau_G: G \to D(DG)$ sending $g$ to evaluation at $g$ is a natural transformation from the identity functor to the twice-iterated character group functor, analogous to the natural embedding of a vector space into its double dual."""
)

# ─── epimorphism ───
write_concept(
    f"{P}/epimorphism",
    {"id": "epimorphism", "title_en": "Epimorphism", "title_zh": "",
     "type": "definition", "domain": "foundations", "subdomain": "category-theory",
     "difficulty": "basic", "tags": ["epimorphism", "epi", "category-theory"],
     "depends_on": {"required": ["category"], "recommended": [], "suggested": ["monomorphism"]},
     "source_books": [{"book_id": "gtm005", "author": "Saunders Mac Lane",
        "title": "Categories for the Working Mathematician",
        "chapter": "I", "section": "5", "pages": "",
        "role_in_book": "Definition of epimorphism (right-cancellative arrow)"}],
     "content_hash": "", "extraction_date": "2026-06-27", "extraction_agent": "v8-full-extract"},
    r"""An arrow $f: a \to b$ in a category $C$ is \emph{epi} (or an \emph{epimorphism}) if for any two arrows $g_1, g_2: b \to c$, the equality $g_1 \circ f = g_2 \circ f$ implies $g_1 = g_2$.
""",
    r"""An epimorphism (or epi) in a category is the categorical abstraction of a surjective function. An arrow $f: a \to b$ is epi if it can be cancelled on the right: $g_1 \circ f = g_2 \circ f$ implies $g_1 = g_2$. In concrete categories such as $\mathbf{Set}$ and $\mathbf{Grp}$, epis correspond to surjective functions, but there are important exceptions -- the inclusion $\mathbb{Z} \hookrightarrow \mathbb{Q}$ is epi in the category of rings."""
)

# ─── monomorphism ───
write_concept(
    f"{P}/monomorphism",
    {"id": "monomorphism", "title_en": "Monomorphism", "title_zh": "",
     "type": "definition", "domain": "foundations", "subdomain": "category-theory",
     "difficulty": "basic", "tags": ["monomorphism", "monic", "category-theory"],
     "depends_on": {"required": ["category"], "recommended": [], "suggested": ["epimorphism"]},
     "source_books": [{"book_id": "gtm005", "author": "Saunders Mac Lane",
        "title": "Categories for the Working Mathematician",
        "chapter": "I", "section": "5", "pages": "",
        "role_in_book": "Definition of monomorphism (left-cancellative arrow)"}],
     "content_hash": "", "extraction_date": "2026-06-27", "extraction_agent": "v8-full-extract"},
    r"""An arrow $f: a \to b$ in a category $C$ is \emph{monic} (or a \emph{monomorphism}) if for any two arrows $g_1, g_2: c \to a$, the equality $f \circ g_1 = f \circ g_2$ implies $g_1 = g_2$.
""",
    r"""A monomorphism (or monic) in a category is the categorical abstraction of an injective function. An arrow $f: a \to b$ is monic if it can be cancelled on the left: $f \circ g_1 = f \circ g_2$ implies $g_1 = g_2$. In most concrete categories, monics correspond to injective functions, though the categorical definition is purely in terms of arrows and composition."""
)

# ─── left-inverse-coretraction ───
write_concept(
    f"{P}/left-inverse-coretraction",
    {"id": "left-inverse-coretraction", "title_en": "Left Inverse / Coretraction",
     "title_zh": "", "type": "definition", "domain": "foundations",
     "subdomain": "category-theory", "difficulty": "basic",
     "tags": ["left-inverse", "coretraction", "section", "category-theory"],
     "depends_on": {"required": ["category", "invertible-arrow"], "recommended": [], "suggested": []},
     "source_books": [{"book_id": "gtm005", "author": "Saunders Mac Lane",
        "title": "Categories for the Working Mathematician",
        "chapter": "I", "section": "5", "pages": "",
        "role_in_book": "Relationship between monics/epis and invertibility"}],
     "content_hash": "", "extraction_date": "2026-06-27", "extraction_agent": "v8-full-extract"},
    r"""An arrow $f: a \to b$ has a \emph{left inverse} (or is a \emph{coretraction}, or a \emph{section}) if there exists an arrow $g: b \to a$ with $g \circ f = 1_a$. An arrow with a left inverse is necessarily monic.
""",
    r"""An arrow with a left inverse is called a coretraction or section; it is necessarily monic. Dually, an arrow with a right inverse is called a retraction and is necessarily epi. An arrow that is both a section and a retraction is invertible."""
)

# ─── right-inverse-retraction ───
write_concept(
    f"{P}/right-inverse-retraction",
    {"id": "right-inverse-retraction", "title_en": "Right Inverse / Retraction",
     "title_zh": "", "type": "definition", "domain": "foundations",
     "subdomain": "category-theory", "difficulty": "basic",
     "tags": ["right-inverse", "retraction", "category-theory"],
     "depends_on": {"required": ["category", "invertible-arrow"], "recommended": [], "suggested": ["left-inverse-coretraction"]},
     "source_books": [{"book_id": "gtm005", "author": "Saunders Mac Lane",
        "title": "Categories for the Working Mathematician",
        "chapter": "I", "section": "5", "pages": "",
        "role_in_book": "Dual notion to left inverse / coretraction"}],
     "content_hash": "", "extraction_date": "2026-06-27", "extraction_agent": "v8-full-extract"},
    r"""An arrow $f: a \to b$ has a \emph{right inverse} (or is a \emph{retraction}) if there exists an arrow $h: b \to a$ with $f \circ h = 1_b$. An arrow with a right inverse is necessarily epi.
""",
    r"""An arrow with a right inverse is called a retraction; it is necessarily epimorphic. This is the dual notion to a coretraction. An arrow that admits both a left and right inverse is invertible, and the two inverses coincide."""
)

# ─── inverse-of-natural-isomorphism ───
write_concept(
    f"{P}/inverse-of-natural-isomorphism",
    {"id": "inverse-of-natural-isomorphism",
     "title_en": "Inverse of a Natural Isomorphism", "title_zh": "",
     "type": "proposition", "domain": "foundations", "subdomain": "category-theory",
     "difficulty": "basic",
     "tags": ["natural-isomorphism", "natural-transformation", "functor"],
     "depends_on": {"required": ["natural-transformation", "natural-isomorphism"], "recommended": [], "suggested": []},
     "source_books": [{"book_id": "gtm005", "author": "Saunders Mac Lane",
        "title": "Categories for the Working Mathematician",
        "chapter": "I", "section": "4", "pages": "",
        "role_in_book": "Componentwise inverses form a natural isomorphism"}],
     "content_hash": "", "extraction_date": "2026-06-27", "extraction_agent": "v8-full-extract"},
    r"""If $\tau: S \Rightarrow T$ is a natural isomorphism (a natural transformation where each component $\tau_c: Sc \to Tc$ is invertible in $B$), then the inverses $(\tau_c)^{-1}$ in $B$ are the components of a natural isomorphism $\tau^{-1}: T \Rightarrow S$.
""",
    r"""When a natural transformation has every component invertible, it is called a natural isomorphism. Mac Lane notes that the componentwise inverses automatically assemble into a natural isomorphism in the opposite direction, making natural isomorphism a symmetric relation between functors."""
)

# ─── ordinal-finite-set-equivalence ───
write_concept(
    f"{P}/ordinal-finite-set-equivalence",
    {"id": "ordinal-finite-set-equivalence",
     "title_en": "Equivalence Between Finite Sets and Finite Ordinals",
     "title_zh": "", "type": "theorem", "domain": "foundations",
     "subdomain": "category-theory", "difficulty": "intermediate",
     "tags": ["equivalence-of-categories", "finite-sets", "finite-ordinals"],
     "depends_on": {"required": ["equivalence-of-categories", "category-of-finite-sets"], "recommended": [], "suggested": []},
     "source_books": [{"book_id": "gtm005", "author": "Saunders Mac Lane",
        "title": "Categories for the Working Mathematician",
        "chapter": "I", "section": "4", "pages": "",
        "role_in_book": "Example of an equivalence of categories"}],
     "content_hash": "", "extraction_date": "2026-06-27", "extraction_agent": "v8-full-extract"},
    r"""Let $\mathbf{Set}_f$ be the category of all finite sets and $\mathbf{Finord}$ the category of finite ordinal numbers. The inclusion $S: \mathbf{Finord} \to \mathbf{Set}_f$ is a functor. For each finite set $X$, choose a bijection $\theta_X: X \to \#X$ where $\#X = n$ is the ordinal number of elements in $X$. This defines a functor $\#: \mathbf{Set}_f \to \mathbf{Finord}$ with $\#f = \theta_Y f \theta_X^{-1}$.
Then $I_{\mathbf{Finord}} = \# \circ S$ and $\theta: I_{\mathbf{Set}_f} \cong S \circ \#$ is a natural isomorphism, establishing an equivalence of categories.
""",
    r"""Mac Lane illustrates equivalence of categories with finite sets and finite ordinal numbers. The category $\mathbf{Finord}$ is a skeleton of $\mathbf{Set}_f$: the inclusion $S$ and cardinality functor $\#$ form an equivalence with $I \cong S \circ \#$ and $I' = \# \circ S$. This shows equivalent categories need not be isomorphic."""
)

# ─── small-category-via-hom-sets ───
write_concept(
    f"{P}/small-category-via-hom-sets",
    {"id": "small-category-via-hom-sets",
     "title_en": "Small Category Defined via Hom-Sets", "title_zh": "",
     "type": "definition", "domain": "foundations", "subdomain": "category-theory",
     "difficulty": "basic", "tags": ["small-category", "hom-set", "foundations"],
     "depends_on": {"required": ["category", "hom-set"], "recommended": [], "suggested": []},
     "source_books": [{"book_id": "gtm005", "author": "Saunders Mac Lane",
        "title": "Categories for the Working Mathematician",
        "chapter": "I", "section": "8", "pages": "",
        "role_in_book": "Alternative definition of a category using hom-sets with disjointness axiom"}],
     "content_hash": "", "extraction_date": "2026-06-27", "extraction_agent": "v8-full-extract"},
    r"""A \emph{small category} is given by:
\begin{enumerate}
\item A set of objects $a, b, c, \ldots$;
\item A function assigning to each ordered pair $\langle a, b \rangle$ a set $\hom(a, b)$;
\item For each ordered triple $\langle a, b, c \rangle$, a composition function $\hom(b, c) \times \hom(a, b) \to \hom(a, c)$, written $\langle g, f \rangle \mapsto g \circ f$;
\item For each object $b$, an identity $1_b \in \hom(b, b)$.
\end{enumerate}
These satisfy associativity, unit laws, and the disjointness axiom: if $\langle a, b \rangle \neq \langle a', b' \rangle$, then $\hom(a, b) \cap \hom(a', b') = \emptyset$.
""",
    r"""Mac Lane provides an alternative definition of a small category entirely in terms of hom-sets. One specifies for each ordered pair of objects a set $\hom(a, b)$ of arrows with a composition operation. The disjointness axiom ensures each arrow has a unique domain and codomain. This formulation is particularly convenient for enriched categories where hom-sets carry additional structure."""
)

# ─── Exercise concepts ───
for ex_num in ["4-4", "4-5", "4-6"]:
    ex_slug = f"{P}/exercise-{ex_num}"
    ex_id = "exercise-" + ex_num
    write_concept(ex_slug,
        {"id": ex_id, "title_en": "Exercise " + ex_num + " (Chapter I, Section 4)",
         "title_zh": "", "type": "exercise", "domain": "foundations",
         "subdomain": "category-theory", "difficulty": "basic",
         "tags": ["exercise", "natural-transformation"],
         "depends_on": {"required": ["natural-transformation", "functor", "category"], "recommended": [], "suggested": []},
         "source_books": [{"book_id": "gtm005", "author": "Saunders Mac Lane",
            "title": "Categories for the Working Mathematician",
            "chapter": "I", "section": "4", "pages": "",
            "role_in_book": "Exercise on natural transformations"}],
         "content_hash": "", "extraction_date": "2026-06-27", "extraction_agent": "v8-full-extract"},
        r"See Mac Lane, \emph{Categories for the Working Mathematician}, Chapter I, Section 4, Exercise " + ex_num + "." + "\n",
        "Exercise " + ex_num + " from Chapter I, Section 4 of Mac Lane's Categories for the Working Mathematician, covering natural transformations and related concepts."
    )

for ex_num in ["5-1", "5-2", "5-3", "5-4", "5-5", "5-6", "5-7", "5-8"]:
    ex_slug = f"{P}/exercise-{ex_num}"
    ex_id = "exercise-" + ex_num
    write_concept(ex_slug,
        {"id": ex_id, "title_en": "Exercise " + ex_num + " (Chapter I, Section 5)",
         "title_zh": "", "type": "exercise", "domain": "foundations",
         "subdomain": "category-theory", "difficulty": "basic",
         "tags": ["exercise", "monic", "epi"],
         "depends_on": {"required": ["monomorphism", "epimorphism", "category"], "recommended": [], "suggested": []},
         "source_books": [{"book_id": "gtm005", "author": "Saunders Mac Lane",
            "title": "Categories for the Working Mathematician",
            "chapter": "I", "section": "5", "pages": "",
            "role_in_book": "Exercise on monics, epis, and related concepts"}],
         "content_hash": "", "extraction_date": "2026-06-27", "extraction_agent": "v8-full-extract"},
        r"See Mac Lane, \emph{Categories for the Working Mathematician}, Chapter I, Section 5, Exercise " + ex_num + "." + "\n",
        "Exercise " + ex_num + " from Chapter I, Section 5 of Mac Lane's Categories for the Working Mathematician, covering monomorphisms, epimorphisms, and related categorical notions."
    )

print("Done with s004 concepts.")
