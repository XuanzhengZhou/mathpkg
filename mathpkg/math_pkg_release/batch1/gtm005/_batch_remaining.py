#!/usr/bin/env python3
"""Batch create concept files for remaining GTM005 sections."""
import os, json, hashlib, datetime

OUT = "/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch1/gtm005"
date = "2026-06-27"
agent = "v8-full-extract"

def h(s):
    return hashlib.md5(s.encode()).hexdigest()[:16]

def write_concept(base_dir, slug, data):
    d = os.path.join(base_dir, slug)
    os.makedirs(d, exist_ok=True)

    # concept.yaml
    y = {
        "id": slug,
        "title_en": data["title_en"],
        "title_zh": "",
        "type": data["type"],
        "domain": data.get("domain","foundations"),
        "subdomain": data.get("subdomain","category-theory"),
        "difficulty": data.get("difficulty","basic"),
        "tags": data.get("tags",[]),
        "depends_on": data.get("depends_on",{"required":[],"recommended":[],"suggested":[]}),
        "source_books": [{
            "book_id": "gtm005",
            "author": "Saunders Mac Lane",
            "title": "Categories for the Working Mathematician",
            "chapter": data.get("chapter",""),
            "section": data.get("section",""),
            "pages": data.get("pages",""),
            "role_in_book": data.get("role_in_book","")
        }],
        "content_hash": h(data.get("theorem","") + data.get("intro","")),
        "extraction_date": date,
        "extraction_agent": agent
    }
    with open(os.path.join(d,"concept.yaml"),"w") as f:
        json.dump(y, f, indent=2)

    # theorem.tex
    with open(os.path.join(d,"theorem.tex"),"w") as f:
        f.write(data.get("theorem",""))

    # introduce.en.md
    intro = f"""---
role: introduce
locale: en
content_hash: "{h(data.get('intro',''))}"
written_against: "{h(data.get('theorem',''))}"
---
{data.get('intro','')}"""
    with open(os.path.join(d,"introduce.en.md"),"w") as f:
        f.write(intro)

    # proof file (for theorem/proposition/lemma/corollary)
    if data["type"] in ("theorem","proposition","lemma","corollary") and data.get("proof"):
        pfn = f"proof_gtm005_{data.get('chapter','X')}.{data.get('section','X')}.en.md"
        proof_md = f"""---
role: proof
locale: en
of_concept: {slug}
source_book: gtm005
source_chapter: "{data.get('chapter','')}"
source_section: "{data.get('section','')}"
---
{data['proof']}"""
        with open(os.path.join(d, pfn), "w") as f:
            f.write(proof_md)

    # exercise files
    for i, ex in enumerate(data.get("exercises",[])):
        efn = f"exercise_gtm005_{data.get('chapter','X')}.{data.get('section','X')}.{i+1}.en.md"
        ex_md = f"""---
role: exercise
locale: en
chapter: "{data.get('chapter','')}"
section: "{data.get('section','')}"
exercise_number: {i+1}
---
{ex}"""
        with open(os.path.join(d, efn), "w") as f:
            f.write(ex_md)


# ═══════════════════════════════════════════════════
# SECTION: s004 Natural Transformations (I.4-I.5)
# ═══════════════════════════════════════════════════
s004 = os.path.join(OUT, "s004_4_Natural_Transformations")

s004_concepts = [
    {"slug":"natural-transformation","title_en":"Natural Transformation","type":"definition",
     "chapter":"I","section":"4","difficulty":"intermediate",
     "tags":["natural-transformation","functor","morphism-of-functors"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""Given two functors $S, T: C \rightarrow B$, a \textbf{natural transformation} $\tau: S \xrightarrow{\cdot} T$ is a function which assigns to each object $c$ of $C$ an arrow $\tau_c = \tau c: Sc \rightarrow Tc$ of $B$ in such a way that for every arrow $f: c \rightarrow c'$ in $C$, the following diagram commutes:
\[
\begin{array}{ccc}
Sc & \xrightarrow{\tau_c} & Tc \\
{\scriptstyle Sf}\downarrow & & \downarrow{\scriptstyle Tf} \\
Sc' & \xrightarrow{\tau_{c'}} & Tc'
\end{array}
\]
When this holds, we say that $\tau_c: Sc \rightarrow Tc$ is \textbf{natural} in $c$.""",
     "intro":"A natural transformation between two functors $S, T: C \\rightarrow B$ provides a way of 'translating' the image of $C$ under $S$ into its image under $T$, while respecting all the arrows of $C$. For each object $c$, a component $\\tau_c: Sc \\to Tc$ is given, and the naturality condition ensures these components commute with the images of every morphism. This is the central concept of category theory, formalizing the intuitive notion of a 'natural' construction.",
     "depends_on":{"required":["functor","category"],"recommended":[],"suggested":[]},
     "role_in_book":"The fundamental definition upon which all of category theory is built."
    },
    {"slug":"natural-isomorphism","title_en":"Natural Isomorphism (Natural Equivalence)","type":"definition",
     "chapter":"I","section":"4","difficulty":"intermediate",
     "tags":["natural-isomorphism","natural-equivalence","invertible"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""A natural transformation $\tau: S \xrightarrow{\cdot} T$ is a \textbf{natural isomorphism} (or \textbf{natural equivalence}), written $\tau: S \cong T$, if every component $\tau_c: Sc \rightarrow Tc$ is invertible in $B$. In this case, the inverses $(\tau_c)^{-1}$ in $B$ are the components of a natural isomorphism $\tau^{-1}: T \xrightarrow{\cdot} S$.""",
     "intro":"A natural isomorphism is the categorical notion of two functors being 'essentially the same'. When every component of a natural transformation is invertible, the functors $S$ and $T$ are naturally isomorphic, meaning they differ only by a coherent choice of isomorphisms.",
     "depends_on":{"required":["natural-transformation","invertible-arrow"],"recommended":[],"suggested":[]},
     "role_in_book":"Used throughout the text to define equivalences of categories, adjunctions, and all universal properties."
    },
    {"slug":"determinant-as-natural-transformation","title_en":"Determinant as a Natural Transformation","type":"definition",
     "chapter":"I","section":"4","difficulty":"intermediate",
     "tags":["determinant","natural-transformation","general-linear-group"],
     "domain":"algebra","subdomain":"linear-algebra",
     "theorem":r"""Let $\det_K M$ be the determinant of an $n \times n$ matrix $M$ with entries in the commutative ring $K$, and let $K^*$ denote the group of units of $K$. For each $n$, the general linear group $\operatorname{GL}_n K$ is the group of all $n \times n$ matrices $M$ with $\det_K M \in K^*$. The determinant is a natural transformation $\det: \operatorname{GL}_n \xrightarrow{\cdot} (-)^*$ between the functors $\operatorname{GL}_n: \mathbf{CRng} \rightarrow \mathbf{Grp}$ and $(-)^*: \mathbf{CRng} \rightarrow \mathbf{Grp}$.""",
     "intro":"The determinant provides a classic example of a natural transformation. For each commutative ring $K$, the determinant maps the general linear group $\\operatorname{GL}_n K$ to the group of units $K^*$, and this map commutes with ring homomorphisms. This naturality captures the fact that the determinant is defined by a universal polynomial formula independent of the particular ring.",
     "depends_on":{"required":["natural-transformation","functor"],"recommended":[],"suggested":[]},
    },
    {"slug":"factor-commutator-natural-transformation","title_en":"Factor-Commutator Natural Transformation","type":"definition",
     "chapter":"I","section":"4","difficulty":"intermediate",
     "tags":["commutator-subgroup","abelianization","natural-transformation"],
     "domain":"algebra","subdomain":"group-theory",
     "theorem":r"""For each group $G$, the projection $p_G: G \rightarrow G/[G,G]$ to the factor-commutator group defines a natural transformation $p: I \xrightarrow{\cdot} F$ from the identity functor on $\mathbf{Grp}$ to the factor-commutator functor $\mathbf{Grp} \rightarrow \mathbf{Ab} \rightarrow \mathbf{Grp}$. For each group homomorphism $f: G \rightarrow H$, the following diagram commutes:
\[
\begin{array}{ccc}
G & \xrightarrow{p_G} & G/[G,G] \\
{\scriptstyle f}\downarrow & & \downarrow{\scriptstyle f'} \\
H & \xrightarrow{p_H} & H/[H,H]
\end{array}
\]""",
     "intro":"The abelianization of a group, sending each group to its factor-commutator group, is a natural transformation. Every group homomorphism induces a homomorphism between the corresponding abelianizations, and the projection maps commute with these induced maps. This is a fundamental example of a natural transformation arising from a universal construction.",
     "depends_on":{"required":["natural-transformation","commutator-subgroup"],"recommended":[],"suggested":[]},
    },
    {"slug":"double-character-group-natural-transformation","title_en":"Double Character Group Natural Transformation","type":"definition",
     "chapter":"I","section":"4","difficulty":"intermediate",
     "tags":["character-group","pontryagin-duality","natural-transformation"],
     "domain":"algebra","subdomain":"group-theory",
     "theorem":r"""In the category $\mathbf{Ab}$ of abelian groups, let $D(G) = \hom(G, \mathbb{R}/\mathbb{Z})$ denote the character group of $G$. For each $G$, there is a homomorphism $\tau_G: G \rightarrow D(DG)$ defined by $(\tau_G g)(t) = t(g)$ for $g \in G$, $t \in DG$. This defines a natural transformation $\tau: I \xrightarrow{\cdot} D \circ D$ from the identity functor to the twice-iterated character group functor.""",
     "intro":"The double dual map in the category of abelian groups (using the circle group $\\mathbb{R}/\\mathbb{Z}$ as the dualizing object) is a natural transformation from the identity functor to the double character group functor. This is the abelian group analog of the double dual in vector spaces and foreshadows Pontryagin duality.",
     "depends_on":{"required":["natural-transformation","character-group"],"recommended":[],"suggested":[]},
    },
    {"slug":"ordinal-finite-set-equivalence","title_en":"Equivalence Between Finite Ordinals and Finite Sets","type":"definition",
     "chapter":"I","section":"4","difficulty":"intermediate",
     "tags":["equivalence-of-categories","finite-ordinals","finite-sets","skeleton"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""Let $\mathbf{Finord}$ be the category of finite ordinal numbers $n = \{0,1,\ldots,n-1\}$ with all functions between them, and $\mathbf{Set}_f$ the category of all finite sets. The inclusion functor $S: \mathbf{Finord} \rightarrow \mathbf{Set}_f$ and the cardinality functor $\#: \mathbf{Set}_f \rightarrow \mathbf{Finord}$ (taking each finite set $X$ to $\#X$, the number of elements) yield natural isomorphisms $I_{\mathbf{Set}_f} \cong S \circ \#$ and $I_{\mathbf{Finord}} = \# \circ S$. Thus these categories are equivalent.""",
     "intro":"The categories of finite ordinal numbers and finite sets are equivalent. The cardinality functor selects a skeleton (the finite ordinals) of the category of finite sets, while the inclusion provides the inverse equivalence up to natural isomorphism. This is a prototypical example of an equivalence of categories.",
     "depends_on":{"required":["natural-isomorphism","functor","category"],"recommended":["equivalence-of-categories"],"suggested":[]},
    },
    {"slug":"equivalence-of-categories","title_en":"Equivalence of Categories","type":"definition",
     "chapter":"I","section":"4","difficulty":"intermediate",
     "tags":["equivalence","functor","natural-isomorphism"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""An \textbf{equivalence} between categories $C$ and $D$ is a pair of functors $S: C \rightarrow D$, $T: D \rightarrow C$ together with natural isomorphisms $I_C \cong T \circ S$ and $I_D \cong S \circ T$. We then say that $C$ and $D$ are \textbf{equivalent} categories.""",
     "intro":"An equivalence of categories is the correct notion of 'sameness' for categories. Unlike isomorphism of categories (which requires the functors to be strict inverses), an equivalence allows the composites to be only naturally isomorphic to the identity functors. This captures the idea that categories are the same 'up to isomorphism of objects.'",
     "depends_on":{"required":["functor","natural-isomorphism"],"recommended":[],"suggested":[]},
     "role_in_book":"The fundamental notion of sameness for categories, used throughout."
    },
    {"slug":"monomorphism","title_en":"Monomorphism (Monic Arrow)","type":"definition",
     "chapter":"I","section":"5","difficulty":"basic",
     "tags":["monomorphism","monic","arrow-property"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""An arrow $f: a \rightarrow b$ in a category $C$ is \textbf{monic} (or is a \textbf{monomorphism}) if for any two parallel arrows $g, h: c \rightarrow a$, the equality $f \circ g = f \circ h$ implies $g = h$. In other words, $f$ is left-cancellable.""",
     "intro":"A monomorphism is the categorical generalization of an injective function. Rather than referring to elements, the definition uses only the composition of arrows: an arrow is monic if it can be canceled on the left. In concrete categories like Set, Grp, and R-Mod, monomorphisms correspond exactly to injective functions.",
     "depends_on":{"required":["category","arrow"],"recommended":[],"suggested":["epimorphism"]},
    },
    {"slug":"epimorphism","title_en":"Epimorphism (Epic Arrow)","type":"definition",
     "chapter":"I","section":"5","difficulty":"basic",
     "tags":["epimorphism","epic","arrow-property"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""An arrow $f: a \rightarrow b$ in a category $C$ is \textbf{epi} (or is an \textbf{epimorphism}) if for any two parallel arrows $g, h: b \rightarrow c$, the equality $g \circ f = h \circ f$ implies $g = h$. In other words, $f$ is right-cancellable.""",
     "intro":"An epimorphism is the categorical dual of a monomorphism, generalizing the notion of a surjective function. An arrow is epic if it can be canceled on the right. In Set and Grp, epimorphisms are surjective, but in other categories (e.g., Rng), there exist epimorphisms that are not surjective (such as the inclusion $\\mathbb{Z} \\hookrightarrow \\mathbb{Q}$).",
     "depends_on":{"required":["category","arrow"],"recommended":["monomorphism"],"suggested":[]},
    },
    {"slug":"invertible-arrow","title_en":"Invertible Arrow (Isomorphism)","type":"definition",
     "chapter":"I","section":"5","difficulty":"basic",
     "tags":["isomorphism","invertible","arrow"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""An arrow $e: a \rightarrow b$ is \textbf{invertible} in $C$ if there exists an arrow $e': b \rightarrow a$ with $e' \circ e = 1_a$ and $e \circ e' = 1_b$. If such an $e'$ exists, it is unique and is written $e' = e^{-1}$. Furthermore, $(e_1 e_2)^{-1} = e_2^{-1} e_1^{-1}$ whenever the composite $e_1 e_2$ is defined and both factors are invertible.""",
     "intro":"An invertible arrow (isomorphism) in a category is an arrow that has a two-sided inverse. Isomorphisms identify objects that are 'the same' within the category. In concrete categories, isomorphisms correspond to bijections that preserve structure in both directions.",
     "depends_on":{"required":["category","arrow","identity-arrow"],"recommended":[],"suggested":[]},
    },
    {"slug":"idempotent-arrow","title_en":"Idempotent Arrow","type":"definition",
     "chapter":"I","section":"5","difficulty":"basic",
     "tags":["idempotent","split-idempotent"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""An arrow $f: b \rightarrow b$ is called \textbf{idempotent} when $f \circ f = f$. An idempotent is said to \textbf{split} when there exist arrows $g: b \rightarrow c$ and $h: c \rightarrow b$ such that $f = h \circ g$ and $g \circ h = 1_c$.""",
     "intro":"An idempotent arrow is an endomorphism that equals its own square. A split idempotent factors as a retraction followed by its section. In Set, all idempotents split, but in general categories this need not hold. The splitting of idempotents is an important completeness condition.",
     "depends_on":{"required":["category","endomorphism"],"recommended":[],"suggested":[]},
    },
    {"slug":"split-idempotent","title_en":"Split Idempotent","type":"definition",
     "chapter":"I","section":"5","difficulty":"basic",
     "tags":["idempotent","split","retraction","section"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""An idempotent $f: b \rightarrow b$ is said to \textbf{split} when there exist arrows $g: b \rightarrow c$ and $h: c \rightarrow b$ such that $f = h \circ g$ and $g \circ h = 1_c$. The object $c$ is called a \textbf{retract} of $b$.""",
     "intro":"A split idempotent decomposes the endomorphism into a retraction-section pair. When an idempotent splits, the object $b$ is a retract of $c$ and the idempotent 'selects' the subobject $c$. Splitting idempotents is analogous to taking the image of a projection operator.",
     "depends_on":{"required":["idempotent-arrow"],"recommended":[],"suggested":[]},
    },
    {"slug":"terminal-object","title_en":"Terminal Object","type":"definition",
     "chapter":"I","section":"5","difficulty":"basic",
     "tags":["terminal-object","universal-property"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""An object $t$ is \textbf{terminal} in $C$ if to each object $a$ in $C$ there is exactly one arrow $a \rightarrow t$. If $t$ is terminal, the only arrow $t \rightarrow t$ is the identity, and any two terminal objects of $C$ are isomorphic in $C$.""",
     "intro":"A terminal object is the categorical formulation of a one-point set. It is an object to which every object has a unique arrow. Terminal objects are unique up to unique isomorphism and serve as the basis for defining elements of an object (as arrows from the terminal object) in categories without a concrete underlying set.",
     "depends_on":{"required":["category","isomorphism"],"recommended":["initial-object"],"suggested":[]},
    },
    {"slug":"initial-object","title_en":"Initial Object","type":"definition",
     "chapter":"I","section":"5","difficulty":"basic",
     "tags":["initial-object","universal-property"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""An object $s$ is \textbf{initial} in $C$ if to each object $a$ in $C$ there is exactly one arrow $s \rightarrow a$. Any two initial objects of $C$ are isomorphic.""",
     "intro":"An initial object is the categorical dual of a terminal object. It is an object from which every object receives a unique arrow. In Set, the empty set is initial; in Grp, the trivial group is initial; in Rng, $\\mathbb{Z}$ is initial. Initial objects are fundamental to the definition of universal arrows and adjunctions.",
     "depends_on":{"required":["category","isomorphism"],"recommended":["terminal-object"],"suggested":[]},
    },
    {"slug":"null-object","title_en":"Null Object (Zero Object)","type":"definition",
     "chapter":"I","section":"5","difficulty":"basic",
     "tags":["null-object","zero-object","initial","terminal"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""A \textbf{null object} $z$ in $C$ is an object which is both initial and terminal. If $C$ has a null object, that object is unique up to isomorphism, and for any two objects $a$ and $b$ of $C$ there is a unique arrow $a \rightarrow z \rightarrow b$ (the composite through $z$), called the \textbf{zero arrow} from $a$ to $b$. Any composite with a zero arrow is itself a zero arrow.""",
     "intro":"A null object (or zero object) is simultaneously initial and terminal. It provides a canonical 'zero' arrow between any two objects. Categories with null objects (such as Ab, R-Mod, and Set$_*$) admit a rich theory of kernels and cokernels, forming the foundation for abelian categories.",
     "depends_on":{"required":["initial-object","terminal-object"],"recommended":["zero-arrow"],"suggested":[]},
    },
    {"slug":"zero-arrow","title_en":"Zero Arrow","type":"definition",
     "chapter":"I","section":"5","difficulty":"basic",
     "tags":["zero-arrow","null-object"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""In a category $C$ with a null object $z$, the \textbf{zero arrow} $0_{a,b}: a \rightarrow b$ is the unique arrow $a \rightarrow z \rightarrow b$ factoring through $z$. Any composite with a zero arrow is itself a zero arrow.""",
     "intro":"The zero arrow is the arrow that factors through the null object. It provides a canonical trivial morphism between any two objects and satisfies $0 \\circ f = 0$ and $g \\circ 0 = 0$ for any composable arrows $f, g$. Zero arrows are essential for defining kernels, cokernels, and exactness.",
     "depends_on":{"required":["null-object"],"recommended":[],"suggested":[]},
    },
    {"slug":"groupoid","title_en":"Groupoid","type":"definition",
     "chapter":"I","section":"5","difficulty":"intermediate",
     "tags":["groupoid","invertible","group"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""A \textbf{groupoid} is a category in which every arrow is invertible. A group is then a groupoid with exactly one object.""",
     "intro":"A groupoid is a category where every morphism is an isomorphism. Groupoids generalize groups: a group is a one-object groupoid. They naturally arise in topology (the fundamental groupoid of a space), in the study of symmetries, and in algebraic geometry (stacks).",
     "depends_on":{"required":["category","invertible-arrow"],"recommended":["group"],"suggested":[]},
    },
    {"slug":"fundamental-groupoid","title_en":"Fundamental Groupoid","type":"definition",
     "chapter":"I","section":"5","difficulty":"intermediate",
     "tags":["fundamental-groupoid","homotopy","topology"],
     "domain":"topology","subdomain":"algebraic-topology",
     "theorem":r"""The \textbf{fundamental groupoid} $\pi(X)$ of a topological space $X$ has as objects the points $x$ of $X$, and as arrows $x \rightarrow x'$ the homotopy classes of paths $f: I \rightarrow X$ from $x$ to $x'$, where $I = [0,1]$, $f(0) = x$, $f(1) = x'$. Composition is given by concatenation of paths; identities are constant paths.""",
     "intro":"The fundamental groupoid is a refinement of the fundamental group that does not require choosing a basepoint. Its objects are all points of the space, and its arrows are homotopy classes of paths. The automorphism group of a point is the fundamental group $\\pi_1(X, x)$. The fundamental groupoid provides a convenient language for the Seifert-van Kampen theorem.",
     "depends_on":{"required":["groupoid"],"recommended":[],"suggested":["homotopy"]},
    },
    {"slug":"small-set","title_en":"Small Set (Relative to a Universe)","type":"definition",
     "chapter":"I","section":"5","difficulty":"advanced",
     "tags":["universe","small-set","foundations"],
     "domain":"foundations","subdomain":"set-theory",
     "theorem":r"""Fix a universe $U$. A set $u$ is called \textbf{small} if $u \in U$. The universe $U$ itself is the set of all small sets. A function $f: u \rightarrow v$ is small when $u$ and $v$ are small sets. A category $C$ is \textbf{small} if the set of objects of $C$ and the set of arrows of $C$ are both small sets.""",
     "intro":"The notion of a small set (relative to a chosen Grothendieck universe) provides a foundation for category theory that avoids the set-theoretic paradoxes of 'the category of all sets'. By choosing a universe $U$, 'small' means 'member of $U$', and 'large' categories like Set (the category of all small sets) can be safely discussed.",
     "depends_on":{"required":["universe"],"recommended":[],"suggested":[]},
    },
    {"slug":"universe","title_en":"Grothendieck Universe","type":"definition",
     "chapter":"I","section":"5","difficulty":"advanced",
     "tags":["universe","foundations","set-theory","grothendieck"],
     "domain":"foundations","subdomain":"set-theory",
     "theorem":r"""A \textbf{universe} is a set $U$ with the following properties:
\begin{enumerate}
\item[(i)] $x \in u \in U$ implies $x \in U$ (transitivity);
\item[(ii)] $u, v \in U$ implies $\{u,v\}, \langle u,v\rangle, u \times v \in U$;
\item[(iii)] $x \in U$ implies $\mathcal{P}x \in U$ and $\bigcup x \in U$;
\item[(iv)] $\omega \in U$ (where $\omega = \{0,1,2,\ldots\}$ is the set of finite ordinals);
\item[(v)] if $f: a \rightarrow b$ is a surjective function with $a \in U$ and $b \subset U$, then $b \in U$ (replacement).
\end{enumerate}""",
     "intro":"A Grothendieck universe is a set $U$ closed under the basic operations of set theory, serving as a model of ZFC. The assumption of a universe allows category theory to be developed within standard set theory: one fixes a universe $U$, calls its members 'small sets', and constructs the category of all small sets as a legitimate object.",
     "depends_on":{"required":[],"recommended":["small-set"],"suggested":[]},
    },
    {"slug":"small-category","title_en":"Small Category","type":"definition",
     "chapter":"I","section":"5","difficulty":"basic",
     "tags":["small-category","universe"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""Fix a universe $U$. A category $C$ is \textbf{small} if both the set of objects $\operatorname{Ob}(C)$ and the set of arrows $\operatorname{Arr}(C)$ are small sets (i.e., belong to $U$). A category is \textbf{locally small} if each hom-set $C(a,b)$ is a small set.""",
     "intro":"A small category is one whose objects and arrows form sets (relative to a fixed universe). Most familiar categories (Set, Grp, Top) are NOT small, because their objects form proper classes. They are, however, locally small: each hom-set is a genuine set. Small categories are the objects of the category Cat.",
     "depends_on":{"required":["category","small-set","universe"],"recommended":[],"suggested":[]},
    },
    {"slug":"small-category-via-hom-sets","title_en":"Small Category Defined via Hom-Sets","type":"definition",
     "chapter":"I","section":"8","difficulty":"basic",
     "tags":["small-category","hom-set","disjointness"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""A \textbf{small category} is given by:
\begin{enumerate}
\item A set of objects $a, b, c, \ldots$;
\item A function assigning to each ordered pair $\langle a, b\rangle$ of objects a set $\hom(a, b)$;
\item For each ordered triple $\langle a, b, c\rangle$ of objects, a composition function $\hom(b,c) \times \hom(a,b) \rightarrow \hom(a,c)$, written $\langle g, f\rangle \mapsto g \circ f$;
\item For each object $b$, an identity element $1_b \in \hom(b, b)$.
\end{enumerate}
These data must satisfy the associativity and unit axioms, plus the \textbf{disjointness} axiom:
\begin{enumerate}
\item[(v)] If $\langle a, b\rangle \neq \langle a', b'\rangle$, then $\hom(a, b) \cap \hom(a', b') = \emptyset$.
\end{enumerate}""",
     "intro":"This definition reformulates a small category purely in terms of its hom-sets, with the disjointness condition ensuring each arrow has a unique domain and codomain. This hom-set formulation is the starting point for enriched category theory, where hom-sets are replaced by objects of a monoidal category.",
     "depends_on":{"required":["category","hom-set"],"recommended":["small-category"],"suggested":["enriched-category"]},
    },
    {"slug":"hom-set","title_en":"Hom-Set","type":"definition",
     "chapter":"I","section":"8","difficulty":"basic",
     "tags":["hom-set","arrow"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""For objects $a$ and $b$ in a category $C$, the \textbf{hom-set}
\[
\hom_C(a, b) = \{ f \mid f \text{ is an arrow } f: a \rightarrow b \text{ in } C \}
\]
consists of all arrows of the category with domain $a$ and codomain $b$. Common notations include $\hom_C(a,b) = C(a,b) = \hom(a,b) = (a,b) = (a,b)_C$.""",
     "intro":"The hom-set collects all arrows between two objects. In locally small categories, each hom-set is a genuine set. The structure of hom-sets encodes the essential information of the category: functors are assignments on hom-sets, natural transformations correspond to families of elements of hom-sets, and enriched categories generalize by replacing hom-sets with objects of a monoidal category.",
     "depends_on":{"required":["category","arrow"],"recommended":[],"suggested":[]},
    },
    {"slug":"ab-category","title_en":"Ab-Category (Preadditive Category)","type":"definition",
     "chapter":"I","section":"8","difficulty":"intermediate",
     "tags":["ab-category","preadditive","enriched-category","bilinear-composition"],
     "domain":"algebra","subdomain":"homological-algebra",
     "theorem":r"""An \textbf{Ab-category} (also called a \textbf{preadditive category}) is a category $A$ in which each hom-set $A(a, b)$ is an additive abelian group and for which composition is bilinear: for arrows $f, f': a \rightarrow b$ and $g, g': b \rightarrow c$,
\[
(g + g') \circ (f + f') = g \circ f + g \circ f' + g' \circ f + g' \circ f'.
\]""",
     "intro":"An Ab-category is a category enriched over the monoidal category of abelian groups. The hom-sets carry an abelian group structure, and composition distributes over addition. Categories of modules (R-Mod), abelian groups (Ab), and chain complexes are Ab-categories. This structure is the first step toward abelian categories.",
     "depends_on":{"required":["category","hom-set"],"recommended":["additive-functor"],"suggested":["abelian-category"]},
    },
    {"slug":"additive-functor","title_en":"Additive Functor Between Ab-Categories","type":"definition",
     "chapter":"I","section":"8","difficulty":"intermediate",
     "tags":["additive-functor","ab-category","homomorphism"],
     "domain":"algebra","subdomain":"homological-algebra",
     "theorem":r"""If $A$ and $B$ are Ab-categories, a functor $T: A \rightarrow B$ is \textbf{additive} when every function $T: A(a, a') \rightarrow B(Ta, Ta')$ is a homomorphism of abelian groups; that is, $T(f + f') = Tf + Tf'$ for all parallel pairs $f, f': a \rightarrow a'$.""",
     "intro":"An additive functor between Ab-categories preserves the additive structure on hom-sets. Additive functors are the appropriate morphisms for Ab-categories and are essential for homological algebra, where derived functors and Ext/Tor are additive functors.",
     "depends_on":{"required":["functor","ab-category"],"recommended":[],"suggested":[]},
    },
]

# Write s004 concepts
for c in s004_concepts:
    write_concept(s004, c["slug"], c)

# Exercises for s004
s004_exercises = [
    {"slug":"exercise-4-4","title_en":"Exercise I.4.4: Natural transformation between functors to a preorder","type":"exercise",
     "chapter":"I","section":"4","difficulty":"basic",
     "tags":["exercise","preorder","natural-transformation"],
     "theorem":r"""For functors $S, T: C \rightarrow P$ where $C$ is a category and $P$ a preorder, show that there is a natural transformation $S \xrightarrow{\cdot} T$ (which is then unique) if and only if $Sc \leq Tc$ for every object $c \in C$.""",
     "intro":"This exercise demonstrates that natural transformations between functors into a preorder category are trivial: they exist exactly when a pointwise inequality holds, reflecting the fact that preorders have at most one arrow between any two objects."},
    {"slug":"exercise-4-5","title_en":"Exercise I.4.5: Arrows-only description of a natural transformation","type":"exercise",
     "chapter":"I","section":"4","difficulty":"intermediate",
     "tags":["exercise","arrows-only","natural-transformation"],
     "theorem":r"""Show that every natural transformation $\tau: S \xrightarrow{\cdot} T$ defines a function (also called $\tau$) which sends each arrow $f: c \rightarrow c'$ of $C$ to an arrow $\tau f: Sc \rightarrow Tc'$ of $B$ in such a way that $Tg \circ \tau f = \tau(gf) = \tau g \circ Sf$ for each composable pair $\langle g, f\rangle$. Conversely, show that every such function $\tau$ comes from a unique natural transformation with $\tau_c = \tau(1_c)$.""",
     "intro":"This exercise provides an 'arrows-only' characterization of natural transformations, paralleling the arrows-only definition of categories. It shows that a natural transformation is equivalently a map from arrows of $C$ to arrows of $B$ satisfying a twisted composition law."},
    {"slug":"exercise-4-6","title_en":"Exercise I.4.6: Equivalence to Matr_F","type":"exercise",
     "chapter":"I","section":"4","difficulty":"intermediate",
     "tags":["exercise","equivalence","matrices","vector-spaces"],
     "theorem":r"""Let $F$ be a field. Show that the category of all finite-dimensional vector spaces over $F$ (with morphisms all linear transformations) is equivalent to the category $\mathbf{Matr}_F$ described in \S 2.""",
     "intro":"This exercise establishes the equivalence between the category of finite-dimensional vector spaces and the matrix category. This is the prototypical example of a skeleton: $\mathbf{Matr}_F$ is a skeleton of the category of finite-dimensional vector spaces."},
    {"slug":"exercise-5-1","title_en":"Exercise I.5.1: Arrow both epi and monic but not invertible","type":"exercise",
     "chapter":"I","section":"5","difficulty":"intermediate",
     "tags":["exercise","epimorphism","monomorphism","non-invertible"],
     "theorem":r"""Find a category with an arrow which is both epi and monic, but not invertible (e.g., a dense subset of a topological space).""",
     "intro":"This exercise shows that 'monic + epic' does not imply 'isomorphic' in a general category, unlike in balanced categories such as Set, Grp, and R-Mod."},
    {"slug":"exercise-5-2","title_en":"Exercise I.5.2: Composite of monics/epis","type":"exercise",
     "chapter":"I","section":"5","difficulty":"basic",
     "tags":["exercise","monomorphism","epimorphism","composition"],
     "theorem":r"""Prove that the composite of monics is monic, and likewise for epis.""",
     "intro":"A straightforward verification that the classes of monomorphisms and epimorphisms are closed under composition."},
    {"slug":"exercise-5-3","title_en":"Exercise I.5.3: Monic composite implies first factor monic","type":"exercise",
     "chapter":"I","section":"5","difficulty":"basic",
     "tags":["exercise","monomorphism","composition"],
     "theorem":r"""If a composite $g \circ f$ is monic, so is $f$. Is this true of $g$?""",
     "intro":"This exercise explores cancellation properties: if a composite is monic, the first factor must be monic, but the second factor need not be."},
    {"slug":"exercise-5-4","title_en":"Exercise I.5.4: Inclusion Z→Q is epi in Rng","type":"exercise",
     "chapter":"I","section":"5","difficulty":"intermediate",
     "tags":["exercise","epimorphism","rings","rational-numbers"],
     "theorem":r"""Show that the inclusion $\mathbb{Z} \rightarrow \mathbb{Q}$ is epi in the category $\mathbf{Rng}$ of rings.""",
     "intro":"A classic example of an epimorphism that is not surjective. In the category of rings, the inclusion of the integers into the rationals is epic because any ring homomorphism from $\\mathbb{Q}$ is determined by its values on $\\mathbb{Z}$."},
    {"slug":"exercise-5-5","title_en":"Exercise I.5.5: Every epi in Grp is surjective","type":"exercise",
     "chapter":"I","section":"5","difficulty":"challenge",
     "tags":["exercise","epimorphism","groups","surjective"],
     "theorem":r"""In $\mathbf{Grp}$, prove that every epi is surjective. (Hint: If $\varphi: G \rightarrow H$ has image $M$ not $H$, use the factor group $H/M$ if $M$ has index 2. Otherwise, let $\operatorname{Perm} H$ be the group of all permutations of the set $H$, choose three different cosets $M, Mu$ and $Mv$ of $M$, define $\sigma \in \operatorname{Perm} H$ by $\sigma(xu) = xv$, $\sigma(xv) = xu$ for $x \in M$, and $\sigma$ otherwise identity. Let $\psi: H \rightarrow \operatorname{Perm} H$ send each $h$ to left multiplication $\psi_h$ by $h$, while $\psi'_h = \sigma^{-1}\psi_h\sigma$. Then $\psi\varphi = \psi'\varphi$, but $\psi \neq \psi'$.)""",
     "intro":"A non-trivial theorem: in the category of groups, epimorphisms are precisely the surjective homomorphisms. This is not true in all concrete categories (see Exercise I.5.4)."},

    {"slug":"exercise-5-6","title_en":"Exercise I.5.6: All idempotents split in Set","type":"exercise",
     "chapter":"I","section":"5","difficulty":"basic",
     "tags":["exercise","idempotent","split","set"],
     "theorem":r"""In $\mathbf{Set}$, show that all idempotents split.""",
     "intro":"Every idempotent function $f: X \\to X$ ($f \\circ f = f$) factors through its image. The image is a retract of $X$."},
    {"slug":"exercise-5-7","title_en":"Exercise I.5.7: Regular arrows","type":"exercise",
     "chapter":"I","section":"5","difficulty":"intermediate",
     "tags":["exercise","regular-arrow","left-inverse","right-inverse"],
     "theorem":r"""An arrow $f: a \rightarrow b$ in a category $C$ is \textbf{regular} when there exists an arrow $g: b \rightarrow a$ such that $fgf = f$. Show that $f$ is regular if it has either a left or a right inverse, and prove that every arrow in $\mathbf{Set}$ with $a \neq \emptyset$ is regular.""",
     "intro":"Regular arrows generalize the idea of having a pseudo-inverse. In Set, every non-empty function admits a section-like map (using the axiom of choice), making it regular."},
    {"slug":"exercise-5-8","title_en":"Exercise I.5.8: Peano-Lawvere axiom for natural numbers object","type":"exercise",
     "chapter":"I","section":"5","difficulty":"challenge",
     "tags":["exercise","natural-numbers-object","categorical-logic"],
     "theorem":r"""Consider the category with objects $\langle X, e, t\rangle$, where $X$ is a set, $e \in X$, and $t: X \rightarrow X$, and with arrows $f: \langle X, e, t\rangle \rightarrow \langle X', e', t'\rangle$ the functions $f$ on $X$ to $X'$ with $fe = e'$ and $ft = t'f$. Prove that this category has an initial object, which is essentially the natural numbers with the successor function.""",
     "intro":"A categorical characterization of the natural numbers as the initial object in the category of pointed sets with an endofunction. This is the Lawvere formulation of the Peano axioms."},
]

for c in s004_exercises:
    write_concept(s004, c["slug"], c)

print(f"s004: wrote {len(s004_concepts)} concepts + {len(s004_exercises)} exercises")

# ═══════════════════════════════════
# s008: Graphs and Free Categories
# ═══════════════════════════════════
s008 = os.path.join(OUT, "s008_7_Graphs_and_Free_Categories")

s008_concepts = [
    {"slug":"graph","title_en":"(Directed) Graph","type":"definition",
     "chapter":"I","section":"7","difficulty":"basic",
     "tags":["graph","directed-graph","objects","arrows"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""A \textbf{(directed) graph} $G$ consists of a set $O$ of objects (vertices), a set $A$ of arrows $f$ (edges), and a pair of functions $\partial_0, \partial_1: A \rightrightarrows O$:
\[
A \xrightarrow{\partial_0}_{\partial_1} O, \quad \partial_0 f = \text{domain } f, \quad \partial_1 f = \text{codomain } f.
\]""",
     "intro":"A directed graph is the underlying data of a category without the composition and identity structure. Every category has an underlying graph (its objects and arrows), and the free category construction produces a category from any graph by freely adding composite arrows (paths)."
    },
    {"slug":"morphism-of-graphs","title_en":"Morphism of Graphs","type":"definition",
     "chapter":"I","section":"7","difficulty":"basic",
     "tags":["graph","morphism","graph-homomorphism"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""A \textbf{morphism} $D: G \rightarrow G'$ of graphs is a pair of functions $D_O: O \rightarrow O'$ and $D_A: A \rightarrow A'$ such that $\partial_i \circ D_A = D_O \circ \partial_i$ for $i = 0, 1$.""",
     "intro":"A graph morphism maps vertices to vertices and edges to edges, preserving the domain and codomain assignments. This makes graphs into a category Grph."
    },
    {"slug":"o-graph","title_en":"O-Graph","type":"definition",
     "chapter":"I","section":"7","difficulty":"intermediate",
     "tags":["o-graph","graph","fixed-objects"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""An \textbf{$O$-graph} for a fixed set $O$ is a graph $A$ whose set of objects is exactly $O$. If $A$ and $B$ are two $O$-graphs, the product over $O$ is
\[
A \times_O B = \{ \langle g, f\rangle \mid \partial_0 g = \partial_1 f,\; g \in A,\; f \in B \},
\]
the set of composable pairs of arrows. The definitions $\partial_0\langle g, f\rangle = \partial_0 f$, $\partial_1\langle g, f\rangle = \partial_1 g$ make this an $O$-graph.""",
     "intro":"An $O$-graph fixes the set of objects and varies only the arrows. This structure allows the definition of a category as an $O$-graph equipped with associative composition and identity operations, generalizing monoids."
    },
    {"slug":"free-category-on-a-graph","title_en":"Free Category Generated by a Graph","type":"theorem",
     "chapter":"I","section":"7","difficulty":"intermediate",
     "tags":["free-category","free-construction","graph","adjunction"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""Let $G$ be a small graph. There exists a small category $C_G$ and a morphism $P: G \rightarrow UC_G$ of graphs such that for any category $B$ and any morphism $D: G \rightarrow UB$ of graphs, there is a unique functor $D': C_G \rightarrow B$ with $D = UD' \circ P$. The category $C_G$ is called the \textbf{free category generated by the graph} $G$.""",
     "proof":r"""Take the objects of $C_G$ to be those of $G$ and the arrows of $C_G$ to be the finite strings (paths)
\[
a_1 \xrightarrow{f_1} a_2 \xrightarrow{f_2} a_3 \longrightarrow \cdots \xrightarrow{f_{n-1}} a_n
\]
composed of $n$ objects $a_1, \ldots, a_n$ connected by $n-1$ arrows $f_i: a_i \rightarrow a_{i+1}$ of $G$. Regard each such string as an arrow $\langle a_1, f_1, \ldots, f_{n-1}, a_n\rangle: a_1 \rightarrow a_n$. Define composition by concatenation, identifying the common end. This is associative, and strings of length 1 are identities.

Every string of length $n > 1$ decomposes uniquely as a composite of strings of length 2:
\[
\langle a_1, f_1, a_2, \ldots, a_{n-1}, f_{n-1}, a_n\rangle = \langle a_{n-1}, f_{n-1}, a_n\rangle \circ \cdots \circ \langle a_1, f_1, a_2\rangle.
\]

The morphism $P: G \rightarrow UC_G$ sends each arrow $f$ to the string $\langle a_1, f, a_2\rangle$ of length 2. For any graph morphism $D: G \rightarrow UB$, define $D'$ on strings by
\[
D'\langle a_1, f_1, \ldots, f_{n-1}, a_n\rangle = D f_{n-1} \circ \cdots \circ D f_1,
\]
taking identity strings to identity arrows. This gives the required unique factorization.""",
     "intro":"The free category on a graph is the category whose arrows are formal paths in the graph, with composition by concatenation. This construction is the left adjoint to the forgetful functor from categories to graphs, giving the bijection $\operatorname{Cat}(C_G, B) \cong \operatorname{Grph}(G, UB)$, natural in $G$ and $B$."
    },
    {"slug":"diagram-of-shape-g","title_en":"Diagram of Shape G","type":"definition",
     "chapter":"I","section":"7","difficulty":"intermediate",
     "tags":["diagram","graph","functor","free-category"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""If $G$ is any graph, a \textbf{diagram of shape $G$} in a category $B$ is a morphism $D: G \rightarrow UB$ of graphs. By the free category theorem, such morphisms correspond exactly to functors $D': C_G \rightarrow B$ via the natural bijection $\operatorname{Cat}(C_G, B) \cong \operatorname{Grph}(G, UB)$.""",
     "intro":"A diagram in a category is simply a graph morphism into the underlying graph of the category. The free category theorem shows this is equivalent to a functor from the free category on the graph. This formalizes the notion of 'commutative diagrams' in category theory."
    },
    {"slug":"free-monoid","title_en":"Free Monoid Generated by a Set","type":"definition",
     "chapter":"I","section":"7","difficulty":"basic",
     "tags":["free-monoid","free-construction","monoid"],
     "domain":"algebra","subdomain":"semigroup-theory",
     "theorem":r"""The \textbf{free monoid} $FX$ generated by a set $X$ consists of all finite strings $x_1 x_2 \cdots x_n$ of elements $x_i \in X$. Multiplication is juxtaposition, and the empty string is the unit. For any monoid $M$, any function $f: X \rightarrow UM$ (where $UM$ is the underlying set) extends uniquely to a monoid morphism $g: FX \rightarrow M$.""",
     "intro":"The free monoid on a set is the monoid of words, directly analogous to the free category on a graph. Both are instances of the same universal property: a left adjoint to a forgetful functor."
    },
    {"slug":"free-groupoid","title_en":"Free Groupoid Generated by a Graph","type":"definition",
     "chapter":"I","section":"7","difficulty":"intermediate",
     "tags":["free-groupoid","groupoid","free-construction"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""Each graph $G$ generates a \textbf{free groupoid} $F$, satisfying the universal property analogous to Theorem 1 with "category" replaced by "groupoid". As a corollary, every set $X$ generates a free group.""",
     "intro":"Just as a graph freely generates a category (by paths), it also freely generates a groupoid (by paths with formal inverses). When the graph has one vertex, this gives the free group on the set of edges."
    },
    {"slug":"quotient-category","title_en":"Quotient Category by a Congruence","type":"proposition",
     "chapter":"I","section":"8","difficulty":"intermediate",
     "tags":["quotient-category","congruence","generators-and-relations"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""For a category $C$, let $R$ be a function assigning to each pair of objects $a, b$ a binary relation $R_{a,b}$ on $\hom_C(a,b)$. There exists a \textbf{quotient category} $C/R$ and a functor $Q: C \rightarrow C/R$, bijective on objects, such that:
\begin{enumerate}
\item If $f R f'$ then $Qf = Qf'$;
\item If $H: C \rightarrow D$ is any functor with $Hf = Hf'$ whenever $f R f'$, then $H = H' \circ Q$ for a unique functor $H': C/R \rightarrow D$.
\end{enumerate}""",
     "proof":r"""Call $R$ a \textbf{congruence} on $C$ if: (i) each $R_{a,b}$ is an equivalence relation; (ii) if $f R_{a,b} f'$, then for all $g: a' \rightarrow a$ and $h: b \rightarrow b'$, one has $(h f g) R_{a',b'} (h f' g)$. Given any $R$, take the least congruence $R'$ containing $R$. Define the objects of $C/R$ to be those of $C$, and $\hom_{C/R}(a,b) = \hom_C(a,b)/R'_{a,b}$. Because $R'$ is a congruence, composition descends to the quotient, and the projection $Q: C \rightarrow C/R$ satisfies the universal property.""",
     "intro":"Quotient categories allow categories to be presented by generators and relations, analogous to presentations of groups or monoids. The free category on a graph modulo a congruence gives a category presented by generators and relations."
    },
]

for c in s008_concepts:
    write_concept(s008, c["slug"], c)

s008_exercises = [
    {"slug":"exercise-7-1","title_en":"Exercise I.7.1: Opposite graph and product of graphs","type":"exercise",
     "chapter":"I","section":"7","difficulty":"basic",
     "tags":["exercise","opposite-graph","product-graph"],
     "theorem":r"""Define "opposite graph" and "product of two graphs" to agree with the corresponding definitions for categories (i.e., so that the underlying graph functor $U$ preserves opposites and products).""",
     "intro":"Extending the definitions of opposite category and product category to the level of graphs, ensuring the forgetful functor from categories to graphs preserves these constructions."},
    {"slug":"exercise-7-2","title_en":"Exercise I.7.2: Finite ordinals are free categories","type":"exercise",
     "chapter":"I","section":"7","difficulty":"intermediate",
     "tags":["exercise","free-category","ordinal"],
     "theorem":r"""Show that every finite ordinal number is a free category.""",
     "intro":"Each finite ordinal (as a poset category) is the free category on a linear graph, generalizing the observation that a chain is the free category on a directed path."},
]

for c in s008_exercises:
    write_concept(s008, c["slug"], c)

print(f"s008: wrote {len(s008_concepts)} concepts + {len(s008_exercises)} exercises")

# ═══════════════════════════════════
# s009: Universals and Limits intro
# ═══════════════════════════════════
s009 = os.path.join(OUT, "s009_III_Universals_and_Limits")

s009_concepts = [
    {"slug":"universal-arrow","title_en":"Universal Arrow","type":"definition",
     "chapter":"III","section":"1","difficulty":"intermediate",
     "tags":["universal-arrow","universal-property","adjunction"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""Given a functor $S: D \rightarrow C$ and an object $c \in C$, a \textbf{universal arrow} from $c$ to $S$ is a pair $\langle r, u\rangle$ consisting of an object $r \in D$ and an arrow $u: c \rightarrow Sr$ of $C$ such that for every pair $\langle d, f\rangle$ with $d \in D$ and $f: c \rightarrow Sd$, there is a unique arrow $f': r \rightarrow d$ of $D$ with $Sf' \circ u = f$.
\[
\begin{array}{ccc}
c & \xrightarrow{u} & Sr & r \\
{\scriptstyle f}\downarrow & {\scriptstyle Sf'}\swarrow & & {\scriptstyle f'}\downarrow \\
Sd & & & d
\end{array}
\]""",
     "intro":"A universal arrow from an object to a functor formalizes the idea of a 'best' or 'most efficient' construction. Every adjunction, limit, colimit, and free construction can be expressed as a universal arrow. This is the unifying concept behind all universal properties in category theory."
    },
    {"slug":"universal-arrow-from-functor","title_en":"Universal Arrow from a Functor to an Object","type":"definition",
     "chapter":"III","section":"1","difficulty":"intermediate",
     "tags":["universal-arrow","dual","co-universal"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""Given a functor $S: D \rightarrow C$ and an object $c \in C$, a \textbf{universal arrow} from $S$ to $c$ is a pair $\langle r, v\rangle$ consisting of an object $r \in D$ and an arrow $v: Sr \rightarrow c$ of $C$ such that for every pair $\langle d, f\rangle$ with $d \in D$ and $f: Sd \rightarrow c$, there is a unique arrow $f': d \rightarrow r$ of $D$ with $v \circ Sf' = f$.""",
     "intro":"The dual notion of a universal arrow from an object to a functor. Together, these two types of universal arrow encompass all universal constructions in category theory."
    },
    {"slug":"universal-property-defines-object-up-to-isomorphism","title_en":"Universal Property Determines Object up to Isomorphism","type":"proposition",
     "chapter":"III","section":"1","difficulty":"basic",
     "tags":["universal-property","isomorphism","uniqueness"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""If $\langle r, u: c \rightarrow Sr\rangle$ is a universal arrow from $c$ to $S$, then the object $r$ is uniquely determined up to (unique) isomorphism in $D$. More precisely, if $\langle r', u': c \rightarrow Sr'\rangle$ is another such universal arrow, there is a unique isomorphism $\varphi: r \rightarrow r'$ such that $S\varphi \circ u = u'$.""",
     "proof":r"""Apply the universal property of $\langle r, u\rangle$ to the pair $\langle r', u'\rangle$ to obtain a unique $f: r \rightarrow r'$ with $Sf \circ u = u'$. Symmetrically, obtain $g: r' \rightarrow r$ with $Sg \circ u' = u$. Then $g \circ f: r \rightarrow r$ satisfies $S(g \circ f) \circ u = Sg \circ Sf \circ u = Sg \circ u' = u = S(1_r) \circ u$. By uniqueness, $g \circ f = 1_r$. Similarly $f \circ g = 1_{r'}$.""",
     "intro":"Universal properties determine objects up to unique isomorphism. This is a fundamental principle: any two objects satisfying the same universal property are canonically isomorphic. This justifies the common phrase 'the' universal object."
    },
    {"slug":"comma-category","title_en":"Comma Category","type":"definition",
     "chapter":"III","section":"1","difficulty":"intermediate",
     "tags":["comma-category","slice-category","coslice-category"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""Given functors $T: E \rightarrow C$ and $S: D \rightarrow C$, the \textbf{comma category} $(T \downarrow S)$ has as objects all triples $\langle e, d, f\rangle$ with $e \in E$, $d \in D$, and $f: Te \rightarrow Sd$ in $C$. An arrow $\langle e, d, f\rangle \rightarrow \langle e', d', f'\rangle$ is a pair of arrows $k: e \rightarrow e'$ in $E$ and $h: d \rightarrow d'$ in $D$ such that $f' \circ Tk = Sh \circ f$.""",
     "intro":"The comma category construction generalizes slice and coslice categories. A universal arrow from $c$ to $S$ is precisely an initial object in the comma category $(c \downarrow S)$, where $c$ is regarded as a functor from the one-object category. This unifies the treatment of all universal constructions."
    },
    {"slug":"universal-element","title_en":"Universal Element of a Functor","type":"definition",
     "chapter":"III","section":"1","difficulty":"intermediate",
     "tags":["universal-element","representable-functor","yoneda"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""Given a functor $H: C \rightarrow \mathbf{Set}$, a \textbf{universal element} of $H$ is a pair $\langle r, e\rangle$ where $r \in C$ and $e \in Hr$ such that for every pair $\langle c, x\rangle$ with $x \in Hc$, there is a unique arrow $f: r \rightarrow c$ with $(Hf)e = x$. Equivalently, the natural transformation $\hom_C(r, -) \xrightarrow{\cdot} H$ determined by $e$ is a natural isomorphism.""",
     "intro":"A universal element of a set-valued functor is an element that represents the functor. The Yoneda lemma guarantees that giving a universal element of $H$ is equivalent to giving a natural isomorphism $\\hom(r, -) \\cong H$, i.e., a representation of $H$."
    },
    {"slug":"representable-functor","title_en":"Representable Functor","type":"definition",
     "chapter":"III","section":"1","difficulty":"intermediate",
     "tags":["representable-functor","yoneda","hom-functor"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""A functor $H: C \rightarrow \mathbf{Set}$ is \textbf{representable} if there exists an object $r \in C$ and a natural isomorphism $\hom_C(r, -) \cong H$. Dually, a contravariant functor $K: C^{\text{op}} \rightarrow \mathbf{Set}$ is representable if $\hom_C(-, r) \cong K$ for some $r$.""",
     "intro":"A representable functor is one that is naturally isomorphic to a hom-functor. The representing object $r$ serves as a 'classifying object' for the functor. The Yoneda Lemma is the fundamental theorem about representable functors, establishing that natural transformations from a representable functor correspond to elements of the represented set."
    },
]

for c in s009_concepts:
    write_concept(s009, c["slug"], c)
print(f"s009: wrote {len(s009_concepts)} concepts")

# ═══════════════════════════════════
# s040: Perspectives on Braided Categories
# ═══════════════════════════════════
s040 = os.path.join(OUT, "s040_6_Perspectives")
os.makedirs(s040, exist_ok=True)

s040_concepts = [
    {"slug":"braided-monoidal-category-applications","title_en":"Applications of Braided Monoidal Categories","type":"definition",
     "chapter":"XI","section":"6","difficulty":"advanced",
     "tags":["braided-category","knot-theory","quantum-groups","tangle"],
     "domain":"topology","subdomain":"quantum-topology",
     "theorem":r"""Braided monoidal categories provide the algebraic framework for:
\begin{itemize}
\item \textbf{Knot theory}: Braidings model the crossing of strands; the Yang-Baxter equation corresponds to the Reidemeister III move.
\item \textbf{Quantum groups}: The category of representations of a quantum group is braided monoidal.
\item \textbf{Tangled categories}: Freyd-Yetter categories provide a universal braided monoidal category generated by a category.
\end{itemize}""",
     "intro":"The study of braided monoidal categories connects category theory to low-dimensional topology (knots, links, tangles) and quantum algebra. The braiding axioms (hexagons) encode the algebraic essence of geometric braiding operations."
    },
    {"slug":"symmetric-vs-braided","title_en":"Symmetric vs. Braided Monoidal Categories","type":"definition",
     "chapter":"XI","section":"6","difficulty":"advanced",
     "tags":["braided","symmetric","monoidal-category"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""A \textbf{symmetric} monoidal category is a braided monoidal category in which the braiding is its own inverse: $c_{Y,X} \circ c_{X,Y} = 1_{X \otimes Y}$. In a general braided category, the double braiding $c_{Y,X} \circ c_{X,Y}$ need not be the identity; this is the essential difference between symmetric and braided structures.""",
     "intro":"Symmetric monoidal categories (like Set, Vect) have 'untwisted' braidings where swapping twice returns to the original. In genuinely braided categories, swapping twice may yield a non-trivial automorphism, leading to representations of the braid group rather than the symmetric group."
    },
]

for c in s040_concepts:
    write_concept(s040, c["slug"], c)
os.system(f"echo DONE > {s040}/.done")
print(f"s040: wrote {len(s040_concepts)} concepts")

# ═══════════════════════════════════
# s042: Simplicial Identities
# ═══════════════════════════════════
s042 = os.path.join(OUT, "s042_1_Verify_the_face_and_degeneracy_identities_for_the_operatio")
os.makedirs(s042, exist_ok=True)

s042_concepts = [
    {"slug":"simplicial-category","title_en":"Simplicial Category (Delta)","type":"definition",
     "chapter":"XII","section":"1","difficulty":"intermediate",
     "tags":["simplicial-category","delta","simplicial-set"],
     "domain":"topology","subdomain":"algebraic-topology",
     "theorem":r"""The \textbf{simplicial category} $\Delta$ has as objects the finite ordinal numbers $[n] = \{0, 1, \ldots, n\}$, and as arrows $[n] \rightarrow [m]$ all (weakly) order-preserving functions. A \textbf{simplicial object} in a category $C$ is a functor $\Delta^{\text{op}} \rightarrow C$.""",
     "intro":"The simplicial category $\\Delta$ is the fundamental shape category for combinatorial topology. Its opposite is used for simplicial sets (presheaves on $\\Delta$), which model topological spaces combinatorially."
    },
    {"slug":"face-and-degeneracy-maps","title_en":"Face and Degeneracy Maps","type":"definition",
     "chapter":"XII","section":"1","difficulty":"intermediate",
     "tags":["simplicial","face-map","degeneracy-map"],
     "domain":"topology","subdomain":"algebraic-topology",
     "theorem":r"""Every arrow in $\Delta$ can be expressed as a composite of \textbf{face maps} $\delta_i^n: [n-1] \rightarrow [n]$ ($0 \leq i \leq n$), the injective map skipping $i$, and \textbf{degeneracy maps} $\sigma_i^n: [n+1] \rightarrow [n]$ ($0 \leq i \leq n$), the surjective map repeating $i$. These generate $\Delta$ subject to the simplicial identities:
\begin{align*}
\delta_j^{n+1} \circ \delta_i^n &= \delta_i^{n+1} \circ \delta_{j-1}^n \quad (i < j), \\
\sigma_j^n \circ \sigma_i^{n+1} &= \sigma_i^n \circ \sigma_{j+1}^{n+1} \quad (i \leq j), \\
\sigma_j^{n-1} \circ \delta_i^n &= \begin{cases}
\delta_i^{n-1} \circ \sigma_{j-1}^{n-2} & (i < j) \\
1_{[n-1]} & (i = j \text{ or } i = j+1) \\
\delta_{i-1}^{n-1} \circ \sigma_j^{n-2} & (i > j+1).
\end{cases}
\end{align*}""",
     "intro":"The face and degeneracy maps generate all order-preserving maps between ordinals. The simplicial identities encode all relations among them, providing the algebraic structure underlying simplicial sets and simplicial homology."
    },
    {"slug":"simplicial-set","title_en":"Simplicial Set","type":"definition",
     "chapter":"XII","section":"1","difficulty":"intermediate",
     "tags":["simplicial-set","presheaf","delta"],
     "domain":"topology","subdomain":"algebraic-topology",
     "theorem":r"""A \textbf{simplicial set} $X$ is a contravariant functor $X: \Delta^{\text{op}} \rightarrow \mathbf{Set}$. Equivalently, it consists of sets $X_n$ ($n \geq 0$) together with face operators $d_i: X_n \rightarrow X_{n-1}$ ($0 \leq i \leq n$) and degeneracy operators $s_i: X_n \rightarrow X_{n+1}$ ($0 \leq i \leq n$) satisfying the dual simplicial identities.""",
     "intro":"Simplicial sets are the combinatorial models of topological spaces, forming the foundation of modern homotopy theory. The category of simplicial sets, $\\mathbf{sSet}$, is a presheaf topos and supports a Quillen model structure equivalent to the homotopy theory of topological spaces."
    },
]

for c in s042_concepts:
    write_concept(s042, c["slug"], c)
os.system(f"echo DONE > {s042}/.done")
print(f"s042: wrote {len(s042_concepts)} concepts")

# ═══════════════════════════════════
# s043: Operations in Monoidal Categories
# ═══════════════════════════════════
s043_path = os.path.join(OUT, "s043_4_Operations_in")
os.makedirs(s043_path, exist_ok=True)

s043_concepts = [
    {"slug":"internal-hom","title_en":"Internal Hom in a Monoidal Category","type":"definition",
     "chapter":"XII","section":"4","difficulty":"advanced",
     "tags":["internal-hom","monoidal-category","closed-category"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""In a monoidal category $V$, an \textbf{internal hom} is a functor $[-,-]: V^{\text{op}} \times V \rightarrow V$ together with a natural isomorphism
\[
V(a \otimes b, c) \cong V(a, [b, c]).
\]
A monoidal category with an internal hom is called a \textbf{closed} monoidal category.""",
     "intro":"The internal hom makes a monoidal category closed, meaning the tensor product has a right adjoint in each variable. This structure is essential for enriched category theory, where hom-objects take values in a closed monoidal category."
    },
    {"slug":"monoidal-category-internal-operations","title_en":"Operations in a Monoidal Category","type":"definition",
     "chapter":"XII","section":"4","difficulty":"intermediate",
     "tags":["monoidal-category","operations","composition"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""In any monoidal category $(V, \otimes, I, a, \ell, r)$, one can define the following internal operations:
\begin{itemize}
\item For objects $X, Y$, the tensor product $X \otimes Y$;
\item The unit object $I$;
\item If $V$ is symmetric, the symmetry $c_{X,Y}: X \otimes Y \xrightarrow{\cong} Y \otimes X$.
\end{itemize}
These operations can be used to define monoids, comonoids, and other algebraic structures internal to $V$.""",
     "intro":"A monoidal category provides the environment for defining algebraic structures (monoids, groups, rings, modules) internally. For example, a monoid in $(V, \\otimes, I)$ is an object $M$ with multiplication $M \\otimes M \\to M$ and unit $I \\to M$ satisfying associativity and unit laws."
    },
]

for c in s043_concepts:
    write_concept(s043_path, c["slug"], c)
os.system(f"echo DONE > {s043_path}/.done")
print(f"s043: wrote {len(s043_concepts)} concepts")

# ═══════════════════════════════════
# s044: Bicategories
# ═══════════════════════════════════
s044 = os.path.join(OUT, "s044_6_Bicategories")
os.makedirs(s044, exist_ok=True)

s044_concepts = [
    {"slug":"bicategory","title_en":"Bicategory","type":"definition",
     "chapter":"XII","section":"6","difficulty":"advanced",
     "tags":["bicategory","2-category","weak-2-category"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""A \textbf{bicategory} $B$ consists of:
\begin{itemize}
\item A set of objects (0-cells) $A, B, C, \ldots$;
\item For each pair $A, B$, a category $B(A, B)$ whose objects are 1-cells (arrows) $f: A \rightarrow B$ and whose arrows are 2-cells $\alpha: f \Rightarrow g$;
\item For each triple $A, B, C$, a composition functor $c_{A,B,C}: B(B, C) \times B(A, B) \rightarrow B(A, C)$;
\item For each $A$, an identity 1-cell $1_A \in B(A, A)$;
\item Natural isomorphisms for associativity ($a$) and left/right unit ($\ell, r$) satisfying coherence axioms (the pentagon and triangle identities).
\end{itemize}""",
     "intro":"A bicategory is a weak 2-category, where composition of 1-cells is associative only up to coherent isomorphism rather than strictly. Bicategories naturally arise in many contexts: the bicategory of spans, of bimodules (profunctors), and of categories with functors and natural transformations (Cat)."
    },
    {"slug":"hom-category-in-bicategory","title_en":"Hom-Category in a Bicategory","type":"definition",
     "chapter":"XII","section":"6","difficulty":"advanced",
     "tags":["bicategory","hom-category","2-cell"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""For objects $A, B$ in a bicategory $B$, the hom-category $B(A, B)$ has as objects the 1-cells $f, g: A \rightarrow B$ and as arrows the 2-cells $\alpha: f \Rightarrow g$, with vertical composition given by composition within the hom-category. Horizontal composition is given by the composition functors $c_{A,B,C}$.""",
     "intro":"Unlike ordinary categories where homs are sets, in a bicategory the homs are themselves categories. The 2-cells can be composed both 'vertically' (within a hom-category) and 'horizontally' (across 1-cells), with an interchange law ensuring compatibility."
    },
]

for c in s044_concepts:
    write_concept(s044, c["slug"], c)
os.system(f"echo DONE > {s044}/.done")
print(f"s044: wrote {len(s044_concepts)} concepts")

# ═══════════════════════════════════
# s045: Examples of Bicategories
# ═══════════════════════════════════
s045 = os.path.join(OUT, "s045_7_Examples_of_Bicategories")
os.makedirs(s045, exist_ok=True)

s045_concepts = [
    {"slug":"bicategory-of-spans","title_en":"Bicategory of Spans","type":"definition",
     "chapter":"XII","section":"7","difficulty":"advanced",
     "tags":["bicategory","span","pullback"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""In a category $C$ with pullbacks, the \textbf{bicategory of spans} $\mathbf{Span}(C)$ has objects those of $C$, 1-cells $A \rightarrow B$ given by spans $A \leftarrow S \rightarrow B$, and 2-cells given by morphisms of spans. Composition of spans is by pullback.""",
     "intro":"The bicategory of spans is a fundamental example of a bicategory that is not strict. Spans model relations categorically: a span represents a 'generalized arrow' from $A$ to $B$ that may be many-valued, and 2-cells compare different such representations."
    },
    {"slug":"profunctors-as-bicategory","title_en":"Bicategory of Profunctors (Distributors)","type":"definition",
     "chapter":"XII","section":"7","difficulty":"advanced",
     "tags":["bicategory","profunctor","distributor","bimodule"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""The \textbf{bicategory of profunctors} $\mathbf{Prof}$ has small categories as objects, profunctors $F: C^{\text{op}} \times D \rightarrow \mathbf{Set}$ as 1-cells $C \rightarrow D$, and natural transformations as 2-cells. Composition is given by the coend formula.""",
     "intro":"Profunctors generalize both functors and relations between categories. The bicategory Prof is a universal receptacle for formal category theory: adjunctions, Kan extensions, and the Yoneda embedding all have elegant formulations in terms of profunctors."
    },
    {"slug":"bicategory-cat","title_en":"The Bicategory Cat of Categories","type":"definition",
     "chapter":"XII","section":"7","difficulty":"intermediate",
     "tags":["bicategory","cat","2-category"],
     "domain":"foundations","subdomain":"category-theory",
     "theorem":r"""The collection of all small categories, functors, and natural transformations forms a 2-category (strict bicategory) $\mathbf{Cat}$. Objects are small categories, 1-cells are functors, and 2-cells are natural transformations, with strict composition of functors.""",
     "intro":"Cat is the prototypical 2-category. Unlike Span and Prof, Cat is a strict 2-category: composition of 1-cells (functors) is strictly associative. This makes Cat the natural setting for studying adjunctions, monads, and other categorical structures at the 2-dimensional level."
    },
]

for c in s045_concepts:
    write_concept(s045, c["slug"], c)
os.system(f"echo DONE > {s045}/.done")
print(f"s045: wrote {len(s045_concepts)} concepts")

# ═══════════════════════════════════
# s046: Crossed Modules
# ═══════════════════════════════════
s046 = os.path.join(OUT, "s046_8_Crossed_Modules_and_Categories_in_Grp")
os.makedirs(s046, exist_ok=True)

s046_concepts = [
    {"slug":"crossed-module","title_en":"Crossed Module","type":"definition",
     "chapter":"XII","section":"8","difficulty":"advanced",
     "tags":["crossed-module","group-theory","homotopy-type"],
     "domain":"algebra","subdomain":"group-theory",
     "theorem":r"""A \textbf{crossed module} consists of two groups $G$ and $H$, a group homomorphism $\partial: H \rightarrow G$, and an action of $G$ on $H$, denoted $(g, h) \mapsto {}^{g}h$, such that for all $g \in G$, $h, h' \in H$:
\begin{enumerate}
\item $\partial({}^{g}h) = g(\partial h)g^{-1}$ (equivariance);
\item ${}^{\partial h}h' = h h' h^{-1}$ (Peiffer identity).
\end{enumerate}""",
     "intro":"A crossed module is an algebraic model for connected homotopy 2-types. They arise naturally from the boundary map of a second relative homotopy group $\\partial: \\pi_2(X, A) \\to \\pi_1(A)$, where the action is by conjugation of loops. Crossed modules are equivalent to internal categories in the category of groups."
    },
    {"slug":"category-internal-to-grp","title_en":"Internal Category in the Category of Groups","type":"definition",
     "chapter":"XII","section":"8","difficulty":"advanced",
     "tags":["internal-category","groups","category-object"],
     "domain":"algebra","subdomain":"group-theory",
     "theorem":r"""A \textbf{category internal to Grp} (or \textbf{$G$-groupoid}) consists of two groups $C_1$ (arrows) and $C_0$ (objects), with domain, codomain, identity, and composition maps that are group homomorphisms satisfying the usual category axioms. Such an internal category is equivalent to a crossed module.""",
     "intro":"An internal category in Grp is precisely a crossed module. The group of objects corresponds to $G$, the group of arrows to the semidirect product $G \\ltimes H$, and the domain/codomain maps encode the boundary homomorphism $\\partial$ and the Peiffer identity."
    },
    {"slug":"crossed-module-from-relative-homotopy","title_en":"Crossed Module from Relative Homotopy Groups","type":"definition",
     "chapter":"XII","section":"8","difficulty":"advanced",
     "tags":["crossed-module","homotopy","relative-homotopy-group"],
     "domain":"topology","subdomain":"algebraic-topology",
     "theorem":r"""For a pair of spaces $(X, A)$ with basepoint, the boundary homomorphism $\partial: \pi_2(X, A) \rightarrow \pi_1(A)$ together with the natural action of $\pi_1(A)$ on $\pi_2(X, A)$ forms a crossed module. This is the fundamental crossed module of the pair $(X, A)$.""",
     "intro":"The motivating example of a crossed module comes from algebraic topology: the second relative homotopy group mapping to the fundamental group of the subspace, with the Whitehead product action. This crossed module captures the homotopy 2-type of the pair."
    },
    {"slug":"strict-2-group","title_en":"Strict 2-Group","type":"definition",
     "chapter":"XII","section":"8","difficulty":"advanced",
     "tags":["2-group","crossed-module","internal-category"],
     "domain":"algebra","subdomain":"group-theory",
     "theorem":r"""A \textbf{strict 2-group} is a group object in the category of groupoids. Equivalently, it is a crossed module, or an internal category in Grp where every arrow is invertible. The correspondence is given by: $G = C_0$ (objects), $H = \ker d_0$ (arrows with codomain identity), and $\partial = d_1|_{H}$.""",
     "intro":"Strict 2-groups provide a categorification of groups: they are 2-categories with one object and all 1- and 2-cells invertible. The equivalence between strict 2-groups and crossed modules (and internal groupoids in Grp) is a fundamental result connecting higher category theory to classical algebra."
    },
]

for c in s046_concepts:
    write_concept(s046, c["slug"], c)
os.system(f"echo DONE > {s046}/.done")
print(f"s046: wrote {len(s046_concepts)} concepts")

print("\n=== BATCH COMPLETE ===")
print("s004: Natural Transformations (20 concepts + 11 exercises)")
print("s008: Graphs and Free Categories (8 concepts + 2 exercises)")
print("s009: Universals and Limits (6 concepts)")
print("s040: Perspectives (2 concepts)")
print("s042: Simplicial Identities (3 concepts)")
print("s043: Operations in (2 concepts)")
print("s044: Bicategories (2 concepts)")
print("s045: Examples of Bicategories (3 concepts)")
print("s046: Crossed Modules (4 concepts)")
