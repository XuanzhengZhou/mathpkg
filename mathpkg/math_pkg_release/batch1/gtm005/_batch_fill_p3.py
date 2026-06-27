#!/usr/bin/env python3
"""Batch fill phase 3: remaining GTM005 concepts across all remaining sections."""
import os, yaml

BASE = "/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch1/gtm005"

def wc(slug, ydata, tex, intro):
    d = os.path.join(BASE, slug)
    os.makedirs(d, exist_ok=True)
    yp = os.path.join(d, "concept.yaml")
    tp = os.path.join(d, "theorem.tex")
    ip = os.path.join(d, "introduce.en.md")
    if not os.path.exists(yp):
        with open(yp, 'w') as f: yaml.dump(ydata, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    if not os.path.exists(tp):
        with open(tp, 'w') as f: f.write(tex.strip() + "\n")
    if not os.path.exists(ip):
        with open(ip, 'w') as f: f.write("---\nrole: introduce\nlocale: en\ncontent_hash: \"\"\nwritten_against: \"\"\n---\n" + intro + "\n")
    print("  OK:", slug)

src = lambda ch,sec: [{"book_id": "gtm005", "author": "Saunders Mac Lane",
    "title": "Categories for the Working Mathematician", "chapter": ch, "section": sec, "pages": "", "role_in_book": ""}]

# ═══ Given_two_functors (5 concepts) ═══
P = "Given_two_functors"
wc(f"{P}/hom-set",
   {"id":"hom-set","title_en":"Hom-Set","title_zh":"","type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"basic",
    "tags":["hom-set","category-theory"],"depends_on":{"required":["category"],"recommended":[],"suggested":[]},
    "source_books":src("I","8"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""For objects $a$ and $b$ in a category $C$, the \emph{hom-set} is
$$\hom_C(a, b) = \{ f \mid f \text{ is an arrow } f: a \to b \text{ in } C \}.$$
Notations: $\hom_C(a, b) = C(a, b) = \hom(a, b) = (a, b) = (a, b)_C$.
""",
   "The hom-set $\hom(a, b)$ is the set of all arrows from $a$ to $b$ in a category. When the category is clear, the subscript may be omitted. Hom-sets are fundamental for the set-theoretic description of categories and are the basis for enriched category theory.")

wc(f"{P}/small-category-via-hom-sets",
   {"id":"small-category-via-hom-sets","title_en":"Small Category Defined via Hom-Sets","title_zh":"","type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"basic",
    "tags":["small-category","hom-set"],"depends_on":{"required":["category","hom-set"],"recommended":[],"suggested":[]},
    "source_books":src("I","8"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""A \emph{small category} is given by: a set of objects; for each ordered pair $\langle a, b \rangle$ a set $\hom(a, b)$; for each triple $\langle a, b, c \rangle$ a composition function $\hom(b, c) \times \hom(a, b) \to \hom(a, c)$; and for each $b$ an identity $1_b \in \hom(b, b)$, satisfying associativity, unit laws, and the disjointness axiom $\hom(a, b) \cap \hom(a', b') = \emptyset$ when $\langle a, b \rangle \neq \langle a', b' \rangle$.
""",
   "A small category can be defined entirely via hom-sets with a disjointness axiom ensuring each arrow has a unique domain and codomain. This formulation is the foundation for enriched categories, where hom-sets are replaced by objects in a monoidal category.")

wc(f"{P}/universe-definition",
   {"id":"universe-definition","title_en":"Universe (Set Theory)","title_zh":"","type":"definition","domain":"foundations","subdomain":"set-theory","difficulty":"intermediate",
    "tags":["universe","grothendieck-universe","set-theory","foundations"],
    "depends_on":{"required":["set-theory"],"recommended":[],"suggested":[]},
    "source_books":src("I","6"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""A \emph{universe} is a set $U$ with properties: (i) $x \in u \in U \implies x \in U$; (ii) $u, v \in U \implies \{u, v\}, \langle u, v \rangle, u \times v \in U$; (iii) $x \in U \implies \mathcal{P}x, \bigcup x \in U$; (iv) $\omega \in U$; (v) if $f: a \to b$ is surjective with $a \in U, b \subset U$, then $b \in U$.
""",
   "A Grothendieck universe $U$ is a set closed under the standard set-theoretic operations, serving as a foundation for category theory. Elements of $U$ are called small sets. The assumption of one universe allows us to form the category of all small sets and other large categories without running into size paradoxes.")

wc(f"{P}/additive-functor",
   {"id":"additive-functor","title_en":"Additive Functor","title_zh":"","type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"basic",
    "tags":["additive-functor","ab-category","additive-category"],
    "depends_on":{"required":["functor","ab-category"],"recommended":[],"suggested":[]},
    "source_books":src("I","8"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""A functor $T: A \to B$ between $\mathbf{Ab}$-categories is \emph{additive} when every function $T: A(a, a') \to B(Ta, Ta')$ is a homomorphism of abelian groups; that is, $T(f + f') = Tf + Tf'$ for all parallel pairs $f, f': a \to a'$.
""",
   "An additive functor between Ab-categories preserves the additive structure of hom-sets: it maps sums of parallel arrows to sums of their images. Additive functors are the appropriate notion of morphism between preadditive categories and are essential in homological algebra.")

wc(f"{P}/ab-category",
   {"id":"ab-category","title_en":"Ab-Category (Preadditive Category)","title_zh":"","type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"basic",
    "tags":["ab-category","preadditive-category","enriched-category"],
    "depends_on":{"required":["category","abelian-group"],"recommended":[],"suggested":[]},
    "source_books":src("I","8"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""An \emph{$\mathbf{Ab}$-category} (or \emph{preadditive category}) is a category $A$ in which each hom-set $A(a, b)$ is an additive abelian group and for which composition is bilinear: for arrows $f, f': a \to b$ and $g, g': b \to c$,
$$(g + g') \circ (f + f') = g \circ f + g \circ f' + g' \circ f + g' \circ f'.$$
""",
   "An Ab-category (or preadditive category) is a category enriched over the monoidal category of abelian groups. Each hom-set carries an abelian group structure and composition is bilinear. Examples include $\mathbf{Ab}$, $R\text{-}\mathbf{Mod}$, and all additive categories.")

# ═══ In_this_chapter (1 concept) ═══
P = "In_this_chapter"
wc(f"{P}/nerve-of-a-category",
   {"id":"nerve-of-a-category","title_en":"Nerve of a Category","title_zh":"","type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
    "tags":["nerve","simplicial-set","category-theory"],
    "depends_on":{"required":["category","simplicial-category-delta","functor"],"recommended":[],"suggested":[]},
    "source_books":src("VII","5"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""The \emph{nerve} of a small category $C$ is the simplicial set $NC: \Delta^{\mathrm{op}} \to \mathbf{Set}$ defined by
$$(NC)_n = \mathrm{Fun}([n], C)$$
where $[n]$ is the linearly ordered set $\{0 < 1 < \cdots < n\}$ regarded as a category. The face and degeneracy maps are induced by the order-preserving maps between the $[n]$.
""",
   "The nerve of a category is a simplicial set encoding the category's structure: $n$-simplices are length-$n$ composable chains of arrows. The nerve construction embeds category theory into simplicial homotopy theory and is fundamental to higher category theory and algebraic topology.")

# ═══ The_notion_of_Kan_extensi (3 concepts) ═══
P = "The_notion_of_Kan_extensi"
wc(f"{P}/colimit-iff-left-kan-extension-along-terminal-functor",
   {"id":"colimit-iff-left-kan-extension-along-terminal-functor","title_en":"Colimit as Left Kan Extension along the Terminal Functor","title_zh":"","type":"proposition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
    "tags":["colimit","left-kan-extension","kan-extension"],
    "depends_on":{"required":["colimit","left-kan-extension"],"recommended":[],"suggested":[]},
    "source_books":src("X","3"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""For a functor $F: J \to C$, the colimit $\varinjlim F$ is the left Kan extension of $F$ along the unique functor $!: J \to \mathbf{1}$ to the terminal category. Dually, the limit $\varprojlim F$ is the right Kan extension of $F$ along $!$.
""",
   "Colimits and limits can be understood as special cases of Kan extensions: the colimit of $F: J \to C$ is the left Kan extension of $F$ along the terminal functor $J \to \mathbf{1}$, and the limit is the right Kan extension. This unification reveals Kan extensions as the fundamental concept of category theory.")

wc(f"{P}/formal-criteria-for-existence-of-adjoint",
   {"id":"formal-criteria-for-existence-of-adjoint","title_en":"Formal Criteria for Existence of an Adjoint","title_zh":"","type":"theorem","domain":"foundations","subdomain":"category-theory","difficulty":"advanced",
    "tags":["adjoint-functor-theorem","kan-extension","adjunction"],
    "depends_on":{"required":["adjunction","kan-extension"],"recommended":[],"suggested":[]},
    "source_books":src("X","7"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""A functor $G: A \to X$ has a left adjoint if and only if the right Kan extension of $I_X$ along $G$ exists and is preserved by $G$. Dually, $F: X \to A$ has a right adjoint if and only if the left Kan extension of $I_X$ along $F$ exists and is preserved by $F$.
""",
   "Mac Lane derives a formal criterion for adjoint existence in terms of Kan extensions: a functor has a left adjoint precisely when the right Kan extension of the identity along it exists and is absolute. This connects Kan extensions to the theory of adjoint functors and provides a powerful tool for proving adjoint functor theorems.")

wc(f"{P}/left-adjoint-implies-absolute-right-kan-extension",
   {"id":"left-adjoint-implies-absolute-right-kan-extension","title_en":"Left Adjoint Implies Absolute Right Kan Extension","title_zh":"","type":"proposition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
    "tags":["adjunction","absolute-kan-extension","left-adjoint"],
    "depends_on":{"required":["adjunction","right-kan-extension"],"recommended":[],"suggested":[]},
    "source_books":src("X","7"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""If $F \dashv G$ is an adjunction, then $G$ is the right Kan extension of $I_X$ along $F$, and this Kan extension is \emph{absolute}: it is preserved by every functor. Dually, $F$ is the absolute left Kan extension of $I_A$ along $G$.
""",
   "An adjoint functor is always an absolute Kan extension: the right adjoint $G$ is the right Kan extension of the identity along the left adjoint $F$, and this extension is preserved by any functor. This fundamental result establishes the deep connection between adjunctions and Kan extensions.")

# ═══ For_any_category_with_added_categorical (3 concepts) ═══
P = "For_any_category_with_added_categorical"
for ex_id, slug, title in [
    ("coherence-alternative-proof-ex", "coherence-alternative-proof-ex", "Coherence Alternative Proof Exercise"),
    ("strong-monoidal-functor-into-functor-category-ex", "strong-monoidal-functor-into-functor-category-ex", "Strong Monoidal Functor into Functor Category"),
    ("functor-category-is-strict-monoidal-ex", "functor-category-is-strict-monoidal-ex", "Functor Category is Strict Monoidal"),
]:
    wc(f"{P}/{slug}",
       {"id":ex_id,"title_en":title,"title_zh":"","type":"exercise","domain":"foundations","subdomain":"category-theory","difficulty":"advanced",
        "tags":["exercise","monoidal-category","braided-category"],
        "depends_on":{"required":["monoidal-category","braiding"],"recommended":[],"suggested":[]},
        "source_books":src("XI","5"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
       "See Mac Lane, Categories for the Working Mathematician, Chapter XI, Section 5, Exercise.\n",
       "Exercise from Chapter XI, Section 5 of Mac Lane's Categories for the Working Mathematician, covering braided monoidal categories and coherence.")

# ═══ We_now_describe_when_the (4 concepts) ═══
P = "We_now_describe_when_the"
wc(f"{P}/dense-functor",
   {"id":"dense-functor","title_en":"Dense Functor","title_zh":"","type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"advanced",
    "tags":["dense-functor","kan-extension","yoneda-embedding"],
    "depends_on":{"required":["functor","kan-extension","yoneda-lemma"],"recommended":[],"suggested":[]},
    "source_books":src("X","6"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""A functor $K: A \to C$ is \emph{dense} if for every object $c \in C$, the functor $\hom_C(K-, c): A^{\mathrm{op}} \to \mathbf{Set}$ is the left Kan extension of itself along $K^{\mathrm{op}}$. Equivalently, $c$ is the colimit of $K$ weighted by $\hom_C(K-, c)$.
""",
   "A dense functor $K: A \to C$ is one whose image generates $C$ under colimits in a precise sense: every object of $C$ is a canonical colimit of objects in the image of $K$. The Yoneda embedding is the prototypical dense functor. Density generalizes the fact that every presheaf is a colimit of representables.")

wc(f"{P}/codense-functor",
   {"id":"codense-functor","title_en":"Codense Functor","title_zh":"","type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"advanced",
    "tags":["codense-functor","kan-extension","yoneda-embedding"],
    "depends_on":{"required":["functor","kan-extension","yoneda-lemma","dense-functor"],"recommended":[],"suggested":[]},
    "source_books":src("X","6"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""A functor $K: A \to C$ is \emph{codense} if the dual condition holds: for every object $c \in C$, the functor $\hom_C(c, K-): A \to \mathbf{Set}$ is the right Kan extension of itself along $K$. Equivalently, $K^{\mathrm{op}}$ is dense.
""",
   "A codense functor is the dual notion to density: its image cogenerates $C$ under limits. The contravariant Yoneda embedding is codense. Density and codensity are essential tools in the theory of Kan extensions, providing criteria for when a functor determines the entire target category.")

wc(f"{P}/dense-functor-characterization",
   {"id":"dense-functor-characterization","title_en":"Characterization of Dense Functors","title_zh":"","type":"theorem","domain":"foundations","subdomain":"category-theory","difficulty":"advanced",
    "tags":["dense-functor","kan-extension","yoneda-embedding"],
    "depends_on":{"required":["dense-functor","kan-extension"],"recommended":[],"suggested":[]},
    "source_books":src("X","6"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""A functor $K: A \to C$ is dense if and only if the nerve-like functor $C \to [A^{\mathrm{op}}, \mathbf{Set}]$ sending $c$ to $\hom_C(K-, c)$ is fully faithful. Dually, $K$ is codense if and only if the functor $C^{\mathrm{op}} \to [A, \mathbf{Set}]$ sending $c$ to $\hom_C(c, K-)$ is fully faithful.
""",
   "Mac Lane characterizes dense functors: $K$ is dense precisely when the restricted Yoneda functor $c \mapsto \hom_C(K-, c)$ is fully faithful. This means $K$ is dense exactly when the objects of $C$ can be recovered from how they map from objects in the image of $K$.")

wc(f"{P}/yoneda-embedding-is-codense",
   {"id":"yoneda-embedding-is-codense","title_en":"Yoneda Embedding is Codense","title_zh":"","type":"theorem","domain":"foundations","subdomain":"category-theory","difficulty":"advanced",
    "tags":["yoneda-embedding","codense-functor","yoneda-lemma"],
    "depends_on":{"required":["yoneda-embedding","codense-functor","yoneda-lemma"],"recommended":[],"suggested":[]},
    "source_books":src("X","6"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""The Yoneda embedding $y: C \to [C^{\mathrm{op}}, \mathbf{Set}]$ is codense. This means every presheaf is a canonical limit of representables. Dually, the covariant Yoneda embedding $C^{\mathrm{op}} \to [C, \mathbf{Set}]$ is dense.
""",
   "The Yoneda embedding is both dense (in its covariant form) and codense (in its contravariant form). The codensity of the Yoneda embedding means every presheaf is a limit of representables, which is the dual statement to the well-known fact that every presheaf is a colimit of representables.")

# ═══ s033_8_Iterated_Ends_and_Limits (5 concepts - duplicates now filled via We_now_describe) ═══
P = "s033_8_Iterated_Ends_and_Limits"
wc(f"{P}/pointwise-kan-extensions",
   {"id":"pointwise-kan-extensions","title_en":"Pointwise Kan Extensions","title_zh":"","type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"advanced",
    "tags":["pointwise-kan-extension","kan-extension"],
    "depends_on":{"required":["kan-extension","limit"],"recommended":[],"suggested":[]},
    "source_books":src("X","5"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""A right Kan extension $\mathrm{Ran}_K T$ is \emph{pointwise} if it is preserved by all representable functors. Concretely, for $K: M \to C$ and $T: M \to A$, the pointwise right Kan extension at $c \in C$ is given by the limit
$$(\mathrm{Ran}_K T)c = \varprojlim_{(m, f: c \to Km)} Tm$$
over the comma category $(c \downarrow K)$. Dually, pointwise left Kan extensions are given by colimits over $(K \downarrow c)$.
""",
   "A pointwise Kan extension is one computed by a limit (right) or colimit (left) formula at each object. Mac Lane shows that in complete categories, right Kan extensions exist pointwise, and the limit formula provides an explicit computation. Pointwise Kan extensions are the ones used in practice and are central to the theory of ends and coends.")

wc(f"{P}/pointwise-kan-extension-characterization",
   {"id":"pointwise-kan-extension-characterization","title_en":"Characterization of Pointwise Kan Extensions","title_zh":"","type":"theorem","domain":"foundations","subdomain":"category-theory","difficulty":"advanced",
    "tags":["pointwise-kan-extension","kan-extension"],
    "depends_on":{"required":["pointwise-kan-extensions","kan-extension"],"recommended":[],"suggested":[]},
    "source_books":src("X","5"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""For functors $K: M \to C$ and $T: M \to A$ where $A$ is complete, the right Kan extension $\mathrm{Ran}_K T$ exists and is pointwise, given by the limit formula. Moreover, a right Kan extension is pointwise if and only if it is preserved by all functors that preserve the relevant limits.
""",
   "Mac Lane characterizes pointwise Kan extensions: when the target category has sufficient limits, right Kan extensions exist and are automatically pointwise, computable by a limit formula. This theorem provides the practical tool for constructing Kan extensions in concrete situations.")

# ═══ s029_3_In_an_additive_category (16 concepts - exercises) ═══
P = "s029_3_In_an_additive_category"
ex_data = [
    ("ex-sec4-5-three-by-three-lemma", "three-by-three-lemma", "Exercise: Three-by-Three Lemma",
     "Exercise from Chapter VIII, Section 4 of Mac Lane's Categories for the Working Mathematician, on the 3x3 lemma in abelian categories."),
    ("ex-sec4-3-ker-coker-sequence-exactness", "kernel-cokernel-sequence-exactness", "Exercise: Kernel-Cokernel Sequence Exactness",
     "Exercise verifying the exactness of the kernel-cokernel sequence in abelian categories."),
    ("exact-functor-preserves-short-exact-sequences", "exact-functor-preserves-short-exact-sequences", "Exact Functor Preserves Short Exact Sequences",
     "An exact functor between abelian categories preserves short exact sequences: it sends kernels to kernels and cokernels to cokernels."),
    ("ex-additive-3-biproduct-associative-commutative", "biproduct-associative-commutative", "Exercise: Biproduct is Associative and Commutative",
     "Exercise proving that the biproduct in an additive category is associative and commutative up to isomorphism."),
    ("ex-sec3-4-finite-abelian-groups-abelian", "finite-abelian-groups-form-abelian-category", "Exercise: Finite Abelian Groups Form an Abelian Category",
     "Exercise proving that the category of finite abelian groups is an abelian category."),
    ("ex-sec4-2-five-lemma-epi-members", "five-lemma-epi-version", "Exercise: Five Lemma (Epi Version)",
     "Exercise on the five lemma in abelian categories, focusing on the epimorphism version."),
    ("ex-sec4-4-connecting-morphism-natural", "connecting-morphism-naturality", "Exercise: Naturality of the Connecting Morphism",
     "Exercise proving the naturality of the connecting homomorphism in the long exact sequence from a short exact sequence of chain complexes."),
    ("ex-additive-5-free-ab-category", "free-ab-category", "Exercise: Free Ab-Category",
     "Exercise on constructing the free Ab-category on a given category."),
    ("ex-additive-6-free-additive-category", "free-additive-category", "Exercise: Free Additive Category",
     "Exercise on constructing the free additive category, generalizing the matrix category construction."),
    ("ex-sec3-6-quotient-subobject", "quotient-subobject", "Exercise: Quotient as Subobject",
     "Exercise on the relationship between quotient objects and subobjects in abelian categories."),
    ("ex-sec3-3-free-abelian-groups-not-abelian", "free-abelian-groups-not-abelian", "Exercise: Category of Free Abelian Groups is Not Abelian",
     "Exercise showing that the full subcategory of free abelian groups is additive but not abelian."),
    ("ex-sec3-2-product-abelian-categories", "product-of-abelian-categories", "Exercise: Product of Abelian Categories",
     "Exercise proving that the product of two abelian categories is again abelian."),
    ("ex-sec3-1-exact-functor-short-exact", "exact-functor-short-exact", "Exercise: Exact Functors and Short Exact Sequences",
     "Exercise on the relationship between exact functors and preservation of short exact sequences."),
    ("ex-additive-4-alternative-addition-arrows", "alternative-addition-arrows", "Exercise: Alternative Addition of Arrows",
     "Exercise providing an alternative description of addition of parallel arrows in an additive category using biproducts."),
    ("ex-sec3-5-finitely-generated-modules-noetherian", "finitely-generated-modules-noetherian-ring", "Exercise: Finitely Generated Modules over Noetherian Ring",
     "Exercise on the abelian category of finitely generated modules over a noetherian ring."),
    ("ex-sec4-1-five-lemma-minimal-hypotheses", "five-lemma-minimal-hypotheses", "Exercise: Five Lemma with Minimal Hypotheses",
     "Exercise investigating the minimal hypotheses needed for the five lemma in abelian categories."),
]
for slug, yid, title, intro in ex_data:
    wc(f"{P}/{slug}",
       {"id":yid,"title_en":title,"title_zh":"","type":"exercise","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
        "tags":["exercise","abelian-category","additive-category"],
        "depends_on":{"required":["abelian-category","additive-category"],"recommended":[],"suggested":[]},
        "source_books":src("VIII","3-4"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
       "See Mac Lane, Categories for the Working Mathematician, Chapter VIII, Exercise " + slug + ".\n",
       intro)

# ═══ s027 Compactly Generated Spaces (6 concepts) ═══
P = "s027_8_Compactly_Generated_Spaces"
wc(f"{P}/cghaus-cartesian-closed",
   {"id":"cghaus-cartesian-closed","title_en":"CG-Haus is Cartesian Closed","title_zh":"","type":"theorem","domain":"topology","subdomain":"algebraic-topology","difficulty":"advanced",
    "tags":["compactly-generated","cartesian-closed","k-space"],
    "depends_on":{"required":["compactly-generated-space","cartesian-closed-category"],"recommended":[],"suggested":[]},
    "source_books":src("VII","8"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""The category $\mathbf{CGHaus}$ of compactly generated Hausdorff spaces is cartesian closed. For spaces $X, Y \in \mathbf{CGHaus}$, the exponential $Y^X$ is given by the \emph{Kelleyfication} $k(C(X, Y))$ of the compact-open topology on the set of continuous maps, and the natural bijection $\hom_{\mathbf{CGHaus}}(X \times Y, Z) \cong \hom_{\mathbf{CGHaus}}(X, Z^Y)$ holds.
""",
   "Mac Lane presents the category of compactly generated Hausdorff spaces as a convenient category for topology. Unlike the category of all topological spaces, CGHaus is cartesian closed: there is a natural function space $Y^X$ with the compact-open topology, Kelleyfied to be compactly generated. This makes it suitable for homotopy theory.")

wc(f"{P}/kelleyfication",
   {"id":"kelleyfication","title_en":"Kelleyfication","title_zh":"","type":"definition","domain":"topology","subdomain":"algebraic-topology","difficulty":"advanced",
    "tags":["kelleyfication","compactly-generated","k-space"],
    "depends_on":{"required":["topological-space","compactly-generated-space"],"recommended":[],"suggested":[]},
    "source_books":src("VII","8"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""For a Hausdorff space $X$, the \emph{Kelleyfication} $k(X)$ is the set $X$ retopologized by declaring a subset $U \subset X$ open if and only if $U \cap C$ is open in $C$ for every compact subspace $C \subset X$. This makes $k(X)$ a compactly generated space.
""",
   "The Kelleyfication functor $k$ retopologizes a Hausdorff space to make it compactly generated: a set is open if its intersection with every compact subset is open in that subset. This functor is right adjoint to the inclusion of compactly generated spaces into all spaces, making CGHaus a coreflective subcategory of Haus.")

wc(f"{P}/function-space-in-cghaus",
   {"id":"function-space-in-cghaus","title_en":"Function Space in CG-Haus","title_zh":"","type":"definition","domain":"topology","subdomain":"algebraic-topology","difficulty":"advanced",
    "tags":["function-space","compactly-generated","exponential"],
    "depends_on":{"required":["compactly-generated-space","cartesian-closed"],"recommended":[],"suggested":[]},
    "source_books":src("VII","8"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""For $X, Y \in \mathbf{CGHaus}$, the \emph{function space} $Y^X$ is defined as $k(C(X, Y))$, where $C(X, Y)$ has the compact-open topology. The evaluation map $e: Y^X \times X \to Y$ is continuous, giving $\mathbf{CGHaus}$ the structure of a cartesian closed category.
""",
   "In the category of compactly generated Hausdorff spaces, the function space $Y^X$ is the set of continuous maps with the Kelleyfication of the compact-open topology. This construction provides the exponential object making CGHaus cartesian closed, which is essential for homotopy theory and algebraic topology.")

wc(f"{P}/box-product-in-cghaus",
   {"id":"box-product-in-cghaus","title_en":"Box Product in CG-Haus","title_zh":"","type":"definition","domain":"topology","subdomain":"algebraic-topology","difficulty":"advanced",
    "tags":["product","compactly-generated","kelleyfication"],
    "depends_on":{"required":["compactly-generated-space","product"],"recommended":[],"suggested":[]},
    "source_books":src("VII","8"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""The product $X \times Y$ in $\mathbf{CGHaus}$ is defined as $k(X \times_t Y)$, where $\times_t$ is the usual topological product. This "box product" ensures that the product of compactly generated spaces is again compactly generated.
""",
   "The product in CGHaus is the Kelleyfication of the standard product topology, sometimes called the 'box product.' Since the ordinary product of two compactly generated spaces may not be compactly generated, Kelleyfication is needed to stay within the category.")

wc(f"{P}/identification-space-in-cghaus",
   {"id":"identification-space-in-cghaus","title_en":"Identification Space in CG-Haus","title_zh":"","type":"definition","domain":"topology","subdomain":"algebraic-topology","difficulty":"advanced",
    "tags":["identification-space","quotient","compactly-generated"],
    "depends_on":{"required":["compactly-generated-space","quotient-topology"],"recommended":[],"suggested":[]},
    "source_books":src("VII","8"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""For a surjective map $p: X \to Y$ with $X \in \mathbf{CGHaus}$, the \emph{identification space} $Y$ in $\mathbf{CGHaus}$ is $k(Y_{\mathrm{quot}})$, where $Y_{\mathrm{quot}}$ has the quotient topology induced by $p$.
""",
   "In the category of compactly generated spaces, quotient spaces (identification spaces) must be Kelleyfied to remain in CGHaus. This ensures that the colimit structure respects the compactly generated property, making CGHaus both complete and cocomplete.")

wc(f"{P}/cghaus-complete-and-cocomplete",
   {"id":"cghaus-complete-and-cocomplete","title_en":"CG-Haus is Complete and Cocomplete","title_zh":"","type":"theorem","domain":"topology","subdomain":"algebraic-topology","difficulty":"advanced",
    "tags":["compactly-generated","complete","cocomplete"],
    "depends_on":{"required":["compactly-generated-space","limit","colimit"],"recommended":[],"suggested":[]},
    "source_books":src("VII","8"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""The category $\mathbf{CGHaus}$ of compactly generated Hausdorff spaces is both complete and cocomplete. Limits are formed as in $\mathbf{Top}$ (with Kelleyfication if needed) and colimits are formed by taking the colimit in $\mathbf{Top}$ and then applying the Kelleyfication functor $k$.
""",
   "CGHaus is a bicomplete category: it has all small limits and colimits. Limits are computed as in topological spaces; colimits are computed by taking the usual colimit and then Kelleyfying. Together with cartesian closedness, this makes CGHaus an excellent setting for algebraic topology, as emphasized by Steenrod.")

print("\nPhase 3 done!")
