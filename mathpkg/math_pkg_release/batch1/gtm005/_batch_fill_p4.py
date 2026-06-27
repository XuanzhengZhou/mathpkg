#!/usr/bin/env python3
"""Batch fill phase 4: From_two_given_categories (41 concepts)."""
import os, yaml

BASE = "/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch1/gtm005"
P = "From_two_given_categories"

def wc(slug, ydata, tex, intro):
    d = os.path.join(BASE, P, slug)
    os.makedirs(d, exist_ok=True)
    for fp, content in [(os.path.join(d,"concept.yaml"), yaml.dump(ydata, default_flow_style=False, allow_unicode=True, sort_keys=False)),
                        (os.path.join(d,"theorem.tex"), tex.strip()+"\n"),
                        (os.path.join(d,"introduce.en.md"), "---\nrole: introduce\nlocale: en\ncontent_hash: \"\"\nwritten_against: \"\"\n---\n"+intro+"\n")]:
        if not os.path.exists(fp):
            with open(fp, 'w') as f: f.write(content)
    print("  OK:", slug)

src = lambda ch,sec: [{"book_id": "gtm005", "author": "Saunders Mac Lane",
    "title": "Categories for the Working Mathematician", "chapter": ch, "section": sec, "pages": "", "role_in_book": ""}]

# Functor category
wc("functor-category",
   {"id":"functor-category","title_en":"Functor Category","title_zh":"","type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
    "tags":["functor-category","exponential","natural-transformation"],
    "depends_on":{"required":["functor","natural-transformation","category"],"recommended":[],"suggested":[]},
    "source_books":src("II","5"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""For categories $C$ and $B$, the \emph{functor category} $B^C$ (or $[C, B]$) has as objects all functors $T: C \to B$ and as arrows all natural transformations $\tau: S \Rightarrow T$ between such functors. Composition is the vertical composition of natural transformations.
""",
   "The functor category $[C, B]$ has functors $C \to B$ as objects and natural transformations between them as morphisms. It is the exponential object in the category of small categories, making $\mathbf{Cat}$ cartesian closed. Functor categories are fundamental: presheaf categories are functor categories $[C^{\mathrm{op}}, \mathbf{Set}]$, and many categorical constructions are expressed as functors between functor categories.")

# 2-category
wc("2-category",
   {"id":"2-category","title_en":"2-Category","title_zh":"","type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
    "tags":["2-category","two-category","bicategory","strict-2-category"],
    "depends_on":{"required":["category","natural-transformation","functor-category"],"recommended":[],"suggested":["bicategory"]},
    "source_books":src("II","5"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""A (strict) \emph{2-category} is a category enriched over $\mathbf{Cat}$. Concretely, it consists of objects, 1-cells (arrows) between objects, and 2-cells between parallel 1-cells, with two composition operations (horizontal and vertical) satisfying the interchange law.
""",
   "A 2-category has objects, arrows (1-cells), and arrows between arrows (2-cells), with two compatible composition operations. The prototypical example is $\mathbf{Cat}$ itself: objects are categories, 1-cells are functors, and 2-cells are natural transformations. 2-categories provide the framework for adjunctions, monads, and Kan extensions at the 2-categorical level.")

wc("cat-is-2-category",
   {"id":"cat-is-2-category","title_en":"Cat is a 2-Category","title_zh":"","type":"theorem","domain":"foundations","subdomain":"category-theory","difficulty":"basic",
    "tags":["cat","2-category","functor","natural-transformation"],
    "depends_on":{"required":["2-category","functor","natural-transformation"],"recommended":[],"suggested":[]},
    "source_books":src("II","5"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""The category $\mathbf{Cat}$ of all small categories is a 2-category. The objects are small categories, the 1-cells are functors, and the 2-cells are natural transformations. Horizontal composition is the Godement product of natural transformations, and vertical composition is the usual composition of natural transformations componentwise.
""",
   "$\mathbf{Cat}$ is the fundamental example of a 2-category: categories as objects, functors as 1-cells, and natural transformations as 2-cells. The two composition laws for natural transformations (vertical and horizontal, or Godement product) satisfy the interchange law, giving $\mathbf{Cat}$ its 2-categorical structure.")

# Duplicate "cat-is-a-two-category" vs "cat-is-2-category"
wc("cat-is-a-two-category",
   {"id":"cat-is-a-two-category","title_en":"Small Categories Form a 2-Category","title_zh":"","type":"theorem","domain":"foundations","subdomain":"category-theory","difficulty":"basic",
    "tags":["2-category","cat","small-category"],
    "depends_on":{"required":["category","2-category"],"recommended":[],"suggested":[]},
    "source_books":src("II","5"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""The collection of all small categories, functors, and natural transformations forms a 2-category $\mathbf{Cat}$ with horizontal composition given by the Godement product $(\sigma \circ \tau)_c = \sigma_{Tc} \circ S'\tau_c$ for natural transformations $\sigma: S \Rightarrow S'$ and $\tau: T \Rightarrow T'$ between composable functors.
""",
   "Mac Lane observes that small categories, functors, and natural transformations organize into a 2-category, denoted $\mathbf{Cat}$. Horizontal composition is the Godement product, and the interchange law holds. This is the canonical example of a 2-category.")

# Comma category
wc("comma-category",
   {"id":"comma-category","title_en":"Comma Category","title_zh":"","type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
    "tags":["comma-category","slice-category","universal-arrow"],
    "depends_on":{"required":["functor","category"],"recommended":[],"suggested":["universal-arrow"]},
    "source_books":src("II","6"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""For functors $S: A \to C$ and $T: B \to C$, the \emph{comma category} $(S \downarrow T)$ has as objects triples $\langle a, b, f: Sa \to Tb \rangle$, and as arrows $\langle a, b, f \rangle \to \langle a', b', f' \rangle$ pairs $\langle h: a \to a', k: b \to b' \rangle$ such that $Tk \circ f = f' \circ Sh$.
""",
   "The comma category $(S \downarrow T)$ is a fundamental construction that generalizes slice categories and arrow categories. Its objects are pairs of objects from the domains of $S$ and $T$ together with an arrow between their images. Comma categories are essential in the theory of Kan extensions, where pointwise Kan extensions are computed as limits over comma categories.")

wc("arrow-category-as-comma-category",
   {"id":"arrow-category-as-comma-category","title_en":"Arrow Category as Comma Category","title_zh":"","type":"proposition","domain":"foundations","subdomain":"category-theory","difficulty":"basic",
    "tags":["arrow-category","comma-category","functor-category"],
    "depends_on":{"required":["arrow-category","comma-category"],"recommended":[],"suggested":[]},
    "source_books":src("II","6"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""The arrow category $C^{\mathbf{2}}$ of a category $C$ is isomorphic to the comma category $(I_C \downarrow I_C)$, where $I_C: C \to C$ is the identity functor.
""",
   "The arrow category $C^{\mathbf{2}}$ (functors from $\mathbf{2} = \{0 \to 1\}$ to $C$) is a special case of the comma category construction: it is precisely $(I_C \downarrow I_C)$. This identification shows how comma categories generalize the idea of 'arrows as objects.'")

wc("category-of-objects-under",
   {"id":"category-of-objects-under","title_en":"Category of Objects Under","title_zh":"","type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"basic",
    "tags":["coslice-category","comma-category","objects-under"],
    "depends_on":{"required":["category","comma-category"],"recommended":[],"suggested":[]},
    "source_books":src("II","6"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""For an object $c \in C$, the \emph{category of objects under $c$} (or \emph{coslice category}), denoted $(c \downarrow C)$, has as objects arrows $f: c \to a$ and as arrows commutative triangles.
""",
   "The coslice category $(c \downarrow C)$ has objects 'under $c$': arrows from $c$ to any object. It is the comma category $(c \downarrow I_C)$ where $c$ is regarded as a functor from the terminal category. Objects under are used to define universal arrows and to construct limits and colimits.")

wc("category-of-objects-under-b",
   {"id":"category-of-objects-under-b","title_en":"Category of Objects Under an Object","title_zh":"","type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"basic",
    "tags":["coslice","comma-category"],
    "depends_on":{"required":["category","comma-category"],"recommended":[],"suggested":["category-of-objects-under"]},
    "source_books":src("II","6"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""For a fixed object $b$ in a category $C$, the category $(b \downarrow C)$ of objects under $b$ has as objects all arrows $f: b \to c$ with domain $b$, and arrows $h: \langle c, f \rangle \to \langle c', f' \rangle$ are arrows $h: c \to c'$ with $h \circ f = f'$.
""",
   "The category $(b \downarrow C)$ of objects under $b$ is the comma category obtained by regarding $b$ as a functor $\mathbf{1} \to C$. This construction is dual to the slice category and is used in defining sifted colimits and in the study of pro-objects.")

wc("category-of-objects-s-under-b",
   {"id":"category-of-objects-s-under-b","title_en":"Category of Objects Under $b$ via Functor $S$","title_zh":"","type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
    "tags":["comma-category","coslice"],
    "depends_on":{"required":["comma-category","functor"],"recommended":[],"suggested":[]},
    "source_books":src("II","6"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""For a functor $S: D \to C$ and an object $b \in C$, the comma category $(b \downarrow S)$ generalizes the slice under $b$. Its objects are pairs $\langle d, f: b \to Sd \rangle$.
""",
   "The comma category $(b \downarrow S)$ captures the category of factorizations of arrows from $b$ through the functor $S$. This general construction is the setting for the definition of universal arrows from $b$ to $S$ and appears throughout Mac Lane's treatment of universals and limits.")

# Bifunctor
wc("contravariant-covariant-bifunctor",
   {"id":"contravariant-covariant-bifunctor","title_en":"Contravariant-Covariant Bifunctor","title_zh":"","type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
    "tags":["bifunctor","contravariant","covariant"],
    "depends_on":{"required":["bifunctor","functor"],"recommended":[],"suggested":[]},
    "source_books":src("II","3"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""A \emph{bifunctor} contravariant in its first argument and covariant in its second is a functor $H: C^{\mathrm{op}} \times D \to E$. Equivalently, it is a family of functors $H(-, d): C^{\mathrm{op}} \to E$ for each $d$ and $H(c, -): D \to E$ for each $c$, agreeing on objects.
""",
   "A bifunctor that is contravariant in one argument and covariant in the other (a 'profunctor-like' bifunctor) is a functor from $C^{\mathrm{op}} \times D$ to $E$. The hom-functor $\hom_C: C^{\mathrm{op}} \times C \to \mathbf{Set}$ is the canonical example. Such mixed-variance bifunctors are the basis for the calculus of ends and coends.")

# Interchange laws
wc("interchange-law-for-bifunctors",
   {"id":"interchange-law-for-bifunctors","title_en":"Interchange Law for Bifunctors","title_zh":"","type":"proposition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
    "tags":["interchange-law","bifunctor","horizontal-composition"],
    "depends_on":{"required":["bifunctor","natural-transformation"],"recommended":[],"suggested":[]},
    "source_books":src("II","5"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""For a bifunctor $F: A \times B \to C$ and natural transformations $\sigma: S \Rightarrow S': A \to A'$ and $\tau: T \Rightarrow T': B \to C$, the interchange law $(F \circ (S' \times T')) \circ (F \circ (\sigma \times \tau)) = F \circ ((S' \circ \sigma) \times (T' \circ \tau))$ holds.
""",
   "The interchange law governs how horizontal and vertical compositions of natural transformations interact. It states that the Godement product respects vertical composition: one can 'interchange' the order of composing horizontally then vertically. This law is what makes $\mathbf{Cat}$ a 2-category.")

wc("interchange-law-for-natural-transformations",
   {"id":"interchange-law-for-natural-transformations","title_en":"Interchange Law for Natural Transformations","title_zh":"","type":"proposition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
    "tags":["interchange-law","natural-transformation","2-category"],
    "depends_on":{"required":["natural-transformation","horizontal-composition","vertical-composition"],"recommended":[],"suggested":[]},
    "source_books":src("II","5"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""For natural transformations $\sigma, \sigma', \tau, \tau'$ with appropriate domains and codomains, the interchange law states:
$$(\tau' \circ \tau) * (\sigma' \circ \sigma) = (\tau' * \sigma') \circ (\tau * \sigma)$$
where $*$ denotes horizontal composition and $\circ$ denotes vertical composition.
""",
   "The interchange law for natural transformations is the fundamental identity of 2-category theory. It states that in a diagram of functors and natural transformations, composing horizontally first and then vertically yields the same result as composing vertically first and then horizontally.")

wc("interchange-law-natural-transformations",
   {"id":"interchange-law-natural-transformations","title_en":"Interchange Law","title_zh":"","type":"proposition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
    "tags":["interchange-law","natural-transformation","2-category"],
    "depends_on":{"required":["natural-transformation","functor-category"],"recommended":[],"suggested":[]},
    "source_books":src("II","5"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""In the 2-category $\mathbf{Cat}$, horizontal and vertical composition of natural transformations satisfy the interchange law: for any composable diagram of functors and natural transformations, $(\beta * \alpha') \circ (\alpha * \beta') = (\beta \circ \alpha) * (\beta' \circ \alpha')$ whenever both sides are defined.
""",
   "The interchange law is the key identity that makes $\mathbf{Cat}$ a 2-category. It relates the two ways to compose natural transformations—vertical (componentwise) and horizontal (Godement product)—and ensures the coherence of the 2-categorical structure.")

# Horizontal and vertical composition
wc("horizontal-composition-of-natural-transformations",
   {"id":"horizontal-composition-of-natural-transformations","title_en":"Horizontal Composition of Natural Transformations","title_zh":"","type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
    "tags":["horizontal-composition","godement-product","natural-transformation"],
    "depends_on":{"required":["natural-transformation","functor"],"recommended":[],"suggested":[]},
    "source_books":src("II","5"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""Given natural transformations $\sigma: S \Rightarrow S': A \to B$ and $\tau: T \Rightarrow T': B \to C$, their \emph{horizontal composition} (or \emph{Godement product}) $\tau * \sigma: T \circ S \Rightarrow T' \circ S'$ is defined by
$$(\tau * \sigma)_a = \tau_{S'a} \circ T(\sigma_a) = T'(\sigma_a) \circ \tau_{Sa}.$$
These two expressions are equal by the naturality of $\tau$.
""",
   "Horizontal composition (the Godement product) combines natural transformations along functors: given $\sigma: S \Rightarrow S'$ and $\tau: T \Rightarrow T'$, the horizontal composite $\tau * \sigma$ goes from $T \circ S$ to $T' \circ S'$. The two possible definitions coincide by naturality, and this operation is associative and has identities.")

wc("horizontal-composition-natural-transformations",
   {"id":"horizontal-composition-natural-transformations","title_en":"Horizontal Composition (Godement Product)","title_zh":"","type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
    "tags":["horizontal-composition","godement-product","natural-transformation","2-category"],
    "depends_on":{"required":["natural-transformation","functor"],"recommended":[],"suggested":[]},
    "source_books":src("II","5"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""The \emph{Godement product} (horizontal composition) $\tau \circ \sigma$ of natural transformations $\sigma: S \Rightarrow S': A \to B$ and $\tau: T \Rightarrow T': B \to C$ yields a natural transformation $T \circ S \Rightarrow T' \circ S'$ with $(\tau \circ \sigma)_a$ given by either path in the naturality square of $\tau$.
""",
   "The Godement product is the horizontal composition operation in the 2-category $\mathbf{Cat}$. It combines natural transformations by 'pasting' them side by side. Together with vertical composition, it satisfies the interchange law, making $\mathbf{Cat}$ the prototypical 2-category.")

wc("vertical-composition-of-natural-transformations",
   {"id":"vertical-composition-of-natural-transformations","title_en":"Vertical Composition of Natural Transformations","title_zh":"","type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"basic",
    "tags":["vertical-composition","natural-transformation"],
    "depends_on":{"required":["natural-transformation","functor"],"recommended":[],"suggested":[]},
    "source_books":src("II","5"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""Given natural transformations $\sigma: S \Rightarrow T$ and $\tau: T \Rightarrow U$ between functors $S, T, U: C \to B$, their \emph{vertical composition} $\tau \circ \sigma: S \Rightarrow U$ is defined componentwise: $(\tau \circ \sigma)_c = \tau_c \circ \sigma_c$.
""",
   "Vertical composition of natural transformations is defined componentwise: if $\sigma: S \Rightarrow T$ and $\tau: T \Rightarrow U$, then $(\tau \circ \sigma)_c = \tau_c \circ \sigma_c$. This is the composition in the functor category $[C, B]$, giving it the structure of a category with functors as objects and natural transformations as arrows.")

# Double category
wc("double-category",
   {"id":"double-category","title_en":"Double Category","title_zh":"","type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"advanced",
    "tags":["double-category","internal-category","2-category"],
    "depends_on":{"required":["category","internal-category"],"recommended":[],"suggested":["2-category"]},
    "source_books":src("II","5"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""A \emph{double category} consists of a set of objects, two sorts of arrows ("horizontal" and "vertical"), and 2-cells (squares) with boundaries, admitting both horizontal and vertical composition of both arrows and 2-cells, satisfying interchange.
""",
   "A double category has both horizontal and vertical 1-cells, plus 2-cells that fill squares, with composition in both directions. It generalizes 2-categories (which have only one sort of 1-cell, with 2-cells going between them). Double categories arise naturally in the study of rings, modules, and profunctors.")

wc("two-category",
   {"id":"two-category","title_en":"Two-Category (2-Category)","title_zh":"","type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
    "tags":["2-category","bicategory","enriched-category"],
    "depends_on":{"required":["category","enriched-category"],"recommended":[],"suggested":[]},
    "source_books":src("II","5"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""A (strict) \emph{2-category} is a $\mathbf{Cat}$-enriched category. It has objects, hom-categories between objects, and composition functors on hom-categories that are strictly associative and unital.
""",
   "A strict 2-category is a category enriched over $\mathbf{Cat}$. Between any two objects there is a hom-category (not just a hom-set), and composition is a functor. This is the setting for adjunctions, monads, and other 2-categorical structures that Mac Lane develops.")

# Hom-set in functor category
wc("hom-set-in-functor-category",
   {"id":"hom-set-in-functor-category","title_en":"Hom-Set in a Functor Category","title_zh":"","type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"basic",
    "tags":["functor-category","hom-set","natural-transformation"],
    "depends_on":{"required":["functor-category","hom-set","natural-transformation"],"recommended":[],"suggested":[]},
    "source_books":src("II","5"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""In the functor category $[C, B]$, the hom-set $[C, B](S, T)$ consists of all natural transformations $\tau: S \Rightarrow T$ between functors $S, T: C \to B$.
""",
   "The hom-set in the functor category $[C, B]$ between two functors $S$ and $T$ is precisely the set $\mathrm{Nat}(S, T)$ of natural transformations from $S$ to $T$. This is consistent with the definition of the functor category where objects are functors and arrows are natural transformations.")

# Functor category as bifunctor
wc("functor-category-as-a-bifunctor",
   {"id":"functor-category-as-a-bifunctor","title_en":"Functor Category as a Bifunctor","title_zh":"","type":"proposition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
    "tags":["functor-category","bifunctor","exponential"],
    "depends_on":{"required":["functor-category","bifunctor"],"recommended":[],"suggested":[]},
    "source_books":src("II","5"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""The assignment $(C, B) \mapsto B^C$ is a bifunctor $\mathbf{Cat}^{\mathrm{op}} \times \mathbf{Cat} \to \mathbf{Cat}$, contravariant in the exponent and covariant in the base.
""",
   "The functor category construction is functorial in both arguments: given functors $F: C' \to C$ and $G: B \to B'$, there is an induced functor $G^F: B^C \to B'^{C'}$. This makes the assignment $(C, B) \mapsto [C, B]$ a bifunctor from $\mathbf{Cat}^{\mathrm{op}} \times \mathbf{Cat}$ to $\mathbf{Cat}$.")

# Product of categories
wc("product-of-categories-as-bifunctor",
   {"id":"product-of-categories-as-bifunctor","title_en":"Product of Categories as a Bifunctor","title_zh":"","type":"proposition","domain":"foundations","subdomain":"category-theory","difficulty":"basic",
    "tags":["product-category","bifunctor","cat"],
    "depends_on":{"required":["product-category","bifunctor"],"recommended":[],"suggested":[]},
    "source_books":src("II","3"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""The product of categories is a bifunctor $\times: \mathbf{Cat} \times \mathbf{Cat} \to \mathbf{Cat}$ sending a pair of categories $(C, D)$ to $C \times D$ and a pair of functors $(F, G)$ to $F \times G: C \times D \to C' \times D'$.
""",
   "The product of categories extends to a bifunctor on $\mathbf{Cat}$: the assignment $(C, D) \mapsto C \times D$ and $(F, G) \mapsto F \times G$ is a functor from $\mathbf{Cat} \times \mathbf{Cat}$ to $\mathbf{Cat}$, making $\mathbf{Cat}$ a monoidal category under the Cartesian product.")

# Universal natural transformation
wc("universal-natural-transformation",
   {"id":"universal-natural-transformation","title_en":"Universal Natural Transformation","title_zh":"","type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
    "tags":["universal-natural-transformation","representable-functor","adjunction"],
    "depends_on":{"required":["natural-transformation","universal-arrow","representable-functor"],"recommended":[],"suggested":[]},
    "source_books":src("II","5"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""A natural transformation $\nu: H \Rightarrow F$ is \emph{universal} from $H$ to $F$ if composition with $\nu$ induces a bijection between natural transformations $F \Rightarrow G$ and natural transformations $H \Rightarrow G$ for any functor $G$.
""",
   "A universal natural transformation formalizes the notion of a 'best approximation' at the level of functors and natural transformations. This concept unifies the treatment of adjunctions, Kan extensions, and representable functors within the 2-categorical framework of $\mathbf{Cat}$.")

wc("universal-natural-transformation-for-product-with-two",
   {"id":"universal-natural-transformation-for-product-with-two","title_en":"Universal Natural Transformation for Product with $\mathbf{2}$","title_zh":"","type":"proposition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
    "tags":["universal-natural-transformation","arrow-category","interval-category"],
    "depends_on":{"required":["universal-natural-transformation","arrow-category"],"recommended":[],"suggested":[]},
    "source_books":src("II","5"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""The projection functors $\pi_0, \pi_1: C \times \mathbf{2} \to C$ exhibit $C \times \mathbf{2}$ as the representing object for a universal natural transformation. Namely, for any functor $T: C \to B$, the arrow category $B^{\mathbf{2}}$ classifies natural transformations into $T$.
""",
   "Mac Lane shows that the product $C \times \mathbf{2}$ (where $\mathbf{2}$ is the interval category $0 \to 1$) serves as a cylinder object: functors $C \times \mathbf{2} \to B$ correspond precisely to natural transformations in $B^C$. This universal property makes the arrow category fundamental in the study of functor categories.")

# Isomorphism opposite-product
wc("isomorphism-opposite-product-category",
   {"id":"isomorphism-opposite-product-category","title_en":"Isomorphism $(C \times D)^{\mathrm{op}} \cong C^{\mathrm{op}} \times D^{\mathrm{op}}$","title_zh":"","type":"proposition","domain":"foundations","subdomain":"category-theory","difficulty":"basic",
    "tags":["opposite-category","product-category","isomorphism"],
    "depends_on":{"required":["opposite-category","product-category"],"recommended":[],"suggested":[]},
    "source_books":src("II","3"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""For categories $C$ and $D$, there is a canonical isomorphism
$$(C \times D)^{\mathrm{op}} \cong C^{\mathrm{op}} \times D^{\mathrm{op}}$$
of categories, given by swapping the order of objects and arrows.
""",
   "The opposite of a product is the product of opposites: $(C \times D)^{\mathrm{op}} \cong C^{\mathrm{op}} \times D^{\mathrm{op}}$. This basic isomorphism is used repeatedly when dealing with bifunctors of mixed variance and the calculus of ends and coends.")

wc("product-category-with-arrow-category",
   {"id":"product-category-with-arrow-category","title_en":"Product Category with the Arrow Category","title_zh":"","type":"proposition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
    "tags":["product-category","arrow-category","functor-category"],
    "depends_on":{"required":["product-category","arrow-category"],"recommended":[],"suggested":[]},
    "source_books":src("II","5"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""There is an isomorphism of categories $C \times \mathbf{2} \cong C^{\mathbf{2}}$? No: the product $C \times \mathbf{2}$ and the arrow category $C^{\mathbf{2}}$ are generally different. However, functors $C \times \mathbf{2} \to D$ correspond to natural transformations in $D^C$.
""",
   "The product $C \times \mathbf{2}$ (where $\mathbf{2} = \{0 \to 1\}$) and the functor category $C^{\mathbf{2}}$ are distinct but related: natural transformations in a functor category correspond to functors from $C \times \mathbf{2}$ to the target category, providing the 'cylinder' interpretation of natural transformations.")

wc("product-category-with-interval",
   {"id":"product-category-with-interval","title_en":"Product Category with the Interval Category","title_zh":"","type":"proposition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
    "tags":["interval-category","product-category","natural-transformation"],
    "depends_on":{"required":["category","natural-transformation"],"recommended":[],"suggested":[]},
    "source_books":src("II","4"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""A functor $H: C \times \mathbf{2} \to B$ (where $\mathbf{2}$ is the category $\{0 \to 1\}$) determines a natural transformation between the restrictions $H(-, 0)$ and $H(-, 1)$, and every natural transformation arises uniquely in this way.
""",
   "The interval category $\mathbf{2} = \{0 \to 1\}$ acts as a 'cylinder' for natural transformations: a functor $C \times \mathbf{2} \to B$ is the same thing as a natural transformation between two functors $C \to B$. This provides the geometric intuition of natural transformations as homotopies between functors.")

# Projection functors
wc("projection-functors",
   {"id":"projection-functors","title_en":"Projection Functors","title_zh":"","type":"definition","domain":"foundations","subdomain":"category-theory","difficulty":"basic",
    "tags":["projection","product-category","functor"],
    "depends_on":{"required":["product-category","functor"],"recommended":[],"suggested":[]},
    "source_books":src("II","3"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""The \emph{projection functors} $P: C \times D \to C$ and $Q: C \times D \to D$ are defined by $P(c, d) = c$, $P(f, g) = f$, and $Q(c, d) = d$, $Q(f, g) = g$.
""",
   "Projection functors from a product category to its factors are the universal maps: they satisfy the universal property that a pair of functors into $C$ and $D$ factors uniquely through $C \times D$. They are the categorical product structure in $\mathbf{Cat}$.")

# Embedding into product
wc("embedding-functors-into-product-with-two",
   {"id":"embedding-functors-into-product-with-two","title_en":"Embedding Functors into Product with $\mathbf{2}$","title_zh":"","type":"proposition","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
    "tags":["embedding","arrow-category","product-category"],
    "depends_on":{"required":["product-category","arrow-category"],"recommended":[],"suggested":[]},
    "source_books":src("II","5"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
   r"""There are natural embedding functors $\langle -, 0 \rangle, \langle -, 1 \rangle: C \to C \times \mathbf{2}$ sending each object $c$ to $(c, 0)$ and $(c, 1)$ respectively. These play the role of the domain and codomain embeddings for the cylinder object.
""",
   "The embeddings $C \hookrightarrow C \times \mathbf{2}$ sending $c$ to $(c, 0)$ or $(c, 1)$ correspond to the two endpoints of the 'cylinder' or 'interval' $\mathbf{2}$. These are used to extract the domain and codomain functors from a natural transformation regarded as a functor on the cylinder.")

# Exercises
exercises = [
    ("exercise-arrow-functions-as-natural-transformation", "Exercise: Arrow Functions as Natural Transformation",
     "Exercise from Chapter II, Section 4 of Mac Lane's Categories for the Working Mathematician."),
    ("exercise-functors-to-arrow-category", "Exercise: Functors to Arrow Category",
     "Exercise exploring the relationship between functors to the arrow category and natural transformations."),
    ("exercise-fundamental-group-of-topological-group-is-abelian", "Exercise: Fundamental Group of Topological Group is Abelian",
     "Exercise proving that the fundamental group of a topological group is abelian, using the Eckmann-Hilton argument."),
    ("exercise-hilton-eckmann-argument", "Exercise: Eckmann-Hilton Argument",
     "Exercise on the Eckmann-Hilton argument: two compatible monoid structures on a set coincide and are commutative."),
    ("exercise-horizontal-composition-as-functor", "Exercise: Horizontal Composition as Functor",
     "Exercise showing that horizontal composition of natural transformations is a functor."),
    ("exercise-interchange-for-paths-in-topological-group", "Exercise: Interchange for Paths in Topological Group",
     "Exercise verifying the interchange law for path composition in a topological group."),
    ("exercise-matrices-in-functor-categories", "Exercise: Matrices in Functor Categories",
     "Exercise relating matrices and functor categories."),
    ("exercise-natural-endomorphisms-of-identity-functor", "Exercise: Natural Endomorphisms of Identity Functor",
     "Exercise on the monoid of natural endomorphisms of the identity functor."),
    ("exercise-opposite-of-matrk-category", "Exercise: Opposite of Matrix Category",
     "Exercise showing that $\mathbf{Matr}_K^{\mathrm{op}}$ is equivalent to $\mathbf{Matr}_{K^{\mathrm{op}}}$."),
    ("exercise-permutation-representation-category", "Exercise: Permutation Representation Category",
     "Exercise on the category of permutation representations."),
    ("exercise-product-of-family-of-categories", "Exercise: Product of a Family of Categories",
     "Exercise on products of families of categories."),
    ("exercise-relate-exercise-7-to-product-functor", "Exercise: Relate Exercise 7 to Product Functor",
     "Exercise connecting an earlier exercise to the product functor construction."),
    ("exercise-ring-of-continuous-functions-functor", "Exercise: Ring of Continuous Functions Functor",
     "Exercise on the functor sending a space to its ring of continuous functions."),
]
for slug, title, intro in exercises:
    wc(slug,
       {"id":slug,"title_en":title,"title_zh":"","type":"exercise","domain":"foundations","subdomain":"category-theory","difficulty":"intermediate",
        "tags":["exercise","functor-category","natural-transformation"],
        "depends_on":{"required":["functor-category","natural-transformation"],"recommended":[],"suggested":[]},
        "source_books":src("II","3-7"),"content_hash":"","extraction_date":"2026-06-27","extraction_agent":"v8-full-extract"},
       "See Mac Lane, Categories for the Working Mathematician, Chapter II, Exercise.\n",
       intro)

print("\nPhase 4 done!")
