#!/usr/bin/env python3
"""Generate all concept files for GTM073 Chapter IV: Modules."""
import os

BASE = "/home/a123/文档/mathpkg/pipeline_output/v7_test/staging/gtm-0073/gtm-0073_ch03_concepts"
DATE = "2026-06-24"
AGENT = "v7-gtm073"
BOOK_ID = "gtm-0073"
AUTHOR = "Hungerford, Thomas W."
BOOK_TITLE = "Algebra"
CHAPTER = "IV"

def write_yaml(dirname, id_, title_en, title_zh, typ, subdomain, difficulty, section, role):
    d = os.path.join(BASE, dirname)
    os.makedirs(d, exist_ok=True)
    content = f"""id: {id_}
title_en: "{title_en}"
title_zh: "{title_zh}"
type: {typ}
domain: algebra
subdomain: {subdomain}
difficulty: {difficulty}
tags: []
depends_on:
  required: []
  recommended: []
  suggested: []
proof_deps: {{}}
source_books:
  - book_id: {BOOK_ID}
    author: "{AUTHOR}"
    title: "{BOOK_TITLE}"
    chapter: {CHAPTER}
    section: "{section}"
    pages: ""
    role_in_book: "{role}"
content_hash: ""
extraction_date: "{DATE}"
extraction_agent: "{AGENT}"
"""
    with open(os.path.join(d, "concept.yaml"), "w") as f:
        f.write(content)

def write_tex(dirname, content):
    with open(os.path.join(BASE, dirname, "theorem.tex"), "w") as f:
        f.write(content)

def write_intro(dirname, content):
    header = """---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
"""
    with open(os.path.join(BASE, dirname, "introduce.en.md"), "w") as f:
        f.write(header + content)

def write_proof(dirname, section, technique, content):
    sec_safe = section.replace(".", "_")
    fname = f"proof_{BOOK_ID}_IV_{sec_safe}_{technique}.en.md"
    header = f"""---
role: proof
source_book: {BOOK_ID}
chapter: {CHAPTER}
section: "{section}"
proof_technique: {technique}
locale: en
content_hash: ""
written_against: ""
---
"""
    with open(os.path.join(BASE, dirname, fname), "w") as f:
        f.write(header + content)

# ============================================================
# SECTION 1: MODULES, HOMOMORPHISMS AND EXACT SEQUENCES
# ============================================================

# Def 1.1
write_yaml("left-r-module", "left-r-module", "Left R-Module", "左R-模",
           "definition", "module-theory", "basic", "IV.1", "Definition 1.1")
write_tex("left-r-module", r"""Let $R$ be a ring. A (left) $R$-module is an additive abelian group $A$ together with a function $R \times A \to A$ (the image of $(r,a)$ being denoted by $ra$) such that for all $r,s \in R$ and $a,b \in A$:
\begin{enumerate}
\item[(i)] $r(a + b) = ra + rb$.
\item[(ii)] $(r + s)a = ra + sa$.
\item[(iii)] $r(sa) = (rs)a$.
\end{enumerate}
If $R$ has an identity element $1_R$ and
\begin{enumerate}
\item[(iv)] $1_R a = a$ for all $a \in A$,
\end{enumerate}
then $A$ is said to be a \emph{unitary} $R$-module. If $R$ is a division ring, then a unitary $R$-module is called a (left) \emph{vector space}.
""")
write_intro("left-r-module", "An $R$-module generalizes the notion of an abelian group (which is a $\\mathbb{Z}$-module) by allowing the scalars to come from an arbitrary ring $R$. The definition requires the additive abelian group structure plus a scalar multiplication satisfying distributivity and associativity axioms. When $R$ has identity and the module is unitary, the identity acts as expected; when $R$ is a division ring, we recover the definition of a vector space.\n")

# Def 1.2
write_yaml("r-module-homomorphism", "r-module-homomorphism", "R-Module Homomorphism", "R-模同态",
           "definition", "module-theory", "basic", "IV.1", "Definition 1.2")
write_tex("r-module-homomorphism", r"""Let $A$ and $B$ be modules over a ring $R$. A function $f : A \to B$ is an \emph{$R$-module homomorphism} provided that for all $a, c \in A$ and $r \in R$:
\[
f(a + c) = f(a) + f(c) \quad \text{and} \quad f(ra) = rf(a).
\]
If $R$ is a division ring, then an $R$-module homomorphism is called a \emph{linear transformation}.
""")
write_intro("r-module-homomorphism", "An $R$-module homomorphism is a structure-preserving map between $R$-modules: it respects both the additive group structure (as a group homomorphism) and the scalar multiplication. The kernel and image of a module homomorphism are submodules. When $R$ is a division ring, module homomorphisms coincide with linear transformations of vector spaces.\n")

# Def 1.3
write_yaml("submodule", "submodule", "Submodule", "子模",
           "definition", "module-theory", "basic", "IV.1", "Definition 1.3")
write_tex("submodule", r"""Let $R$ be a ring, $A$ an $R$-module and $B$ a nonempty subset of $A$. $B$ is a \emph{submodule} of $A$ provided that $B$ is an additive subgroup of $A$ and $rb \in B$ for all $r \in R$, $b \in B$. A submodule of a vector space over a division ring is called a \emph{subspace}.
""")
write_intro("submodule", "A submodule is a subset of a module that is itself a module under the same operations. The condition requires closure under addition and under scalar multiplication by elements of the ring. The kernel and image of any module homomorphism are submodules, and intersections of submodules are again submodules.\n")

# Def 1.4
write_yaml("submodule-generated-by-subset", "submodule-generated-by-subset", "Submodule Generated by a Subset", "子集生成的子模",
           "definition", "module-theory", "basic", "IV.1", "Definition 1.4")
write_tex("submodule-generated-by-subset", r"""If $X$ is a subset of a module $A$ over a ring $R$, then the intersection of all submodules of $A$ containing $X$ is called the \emph{submodule generated by $X$} (or \emph{spanned by $X$}). If $X$ is finite and generates the module $B$, $B$ is said to be \emph{finitely generated}. If $X = \emptyset$, then the submodule generated by $X$ is the zero submodule.
""")
write_intro("submodule-generated-by-subset", "The submodule generated by a subset $X$ is the smallest submodule containing $X$, obtained as the intersection of all submodules containing $X$. When $X$ is finite, the resulting module is called finitely generated. If the ring has identity and the module is unitary, the generated submodule consists of all finite linear combinations of elements of $X$ with coefficients in $R$.\n")

# Thm 1.6
write_yaml("quotient-module", "quotient-module", "Quotient Module", "商模",
           "theorem", "module-theory", "basic", "IV.1", "Theorem 1.6")
write_tex("quotient-module", r"""Let $B$ be a submodule of a module $A$ over a ring $R$. Then the quotient group $A/B$ is an $R$-module with the action of $R$ on $A/B$ given by:
\[
r(a + B) = ra + B \quad \text{for all } r \in R, a \in A.
\]
The map $\pi : A \to A/B$ given by $a \mapsto a + B$ is an $R$-module epimorphism with kernel $B$.
""")
write_intro("quotient-module", "The quotient module $A/B$ generalizes quotient groups to the module setting. The scalar multiplication is well-defined because $B$ is a submodule, guaranteeing that the coset $ra + B$ depends only on the coset $a + B$. The canonical projection $\\pi$ is a surjective module homomorphism with kernel exactly $B$.\n")
write_proof("quotient-module", "IV.1", "direct-verification", """Since $A$ is an additive abelian group, $B$ is a normal subgroup, and $A/B$ is a well-defined abelian group. If $a + B = a' + B$, then $a - a' \\in B$. Since $B$ is a submodule, $ra - ra' = r(a - a') \\in B$ for all $r \\in R$. Thus $ra + B = ra' + B$ by Corollary I.4.3 and the action of $R$ on $A/B$ is well defined. The remainder of the proof verifies the module axioms and that $\\pi$ is an epimorphism with kernel $B$.
""")

print("Section 1 done...")
