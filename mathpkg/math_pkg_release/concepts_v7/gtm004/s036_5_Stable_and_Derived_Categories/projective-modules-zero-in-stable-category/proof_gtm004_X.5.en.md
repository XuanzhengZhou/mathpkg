---
role: proof
locale: en
of_concept: projective-modules-zero-in-stable-category
source_book: gtm004
source_chapter: "X"
source_section: "5. Stable and Derived Categories"
---

# Proof of Projective Modules Are Zero in the Stable Category

Let $R$ be a ring and let $\mathfrak{StM}_R$ be the stable category of left $R$-modules. Recall that a homomorphism $f: A \to B$ is called *projective* if it factors through a projective module, i.e., there exists a projective module $P$ and homomorphisms $g: A \to P$, $h: P \to B$ such that $f = h \circ g$. The set of projective homomorphisms from $A$ to $B$ is denoted $\operatorname{Phom}_R(A, B)$, which forms a subgroup of $\operatorname{Hom}_R(A, B)$. The morphism set in $\mathfrak{StM}_R$ is

$$\underline{\operatorname{Hom}}_R(A, B) = \operatorname{Hom}_R(A, B) / \operatorname{Phom}_R(A, B).$$

Let $P$ be a projective $R$-module. Consider the identity morphism $\operatorname{id}_P: P \to P$. Since $P$ is projective, we may factor $\operatorname{id}_P$ as

$$\operatorname{id}_P = \operatorname{id}_P \circ \operatorname{id}_P,$$

where $\operatorname{id}_P: P \to P$ and $\operatorname{id}_P: P \to P$ are both homomorphisms. More concretely, taking $g = \operatorname{id}_P: P \to P$ (with codomain the projective module $P$) and $h = \operatorname{id}_P: P \to P$, we obtain $\operatorname{id}_P = h \circ g$. Hence $\operatorname{id}_P \in \operatorname{Phom}_R(P, P)$, and therefore $\operatorname{id}_P$ represents the zero element in $\underline{\operatorname{Hom}}_R(P, P)$.

Consequently, the zero morphism $0: P \to 0$ and the zero morphism $0: 0 \to P$ provide mutual inverses in $\mathfrak{StM}_R$: the composition $0 \to P \xrightarrow{\operatorname{id}_P} P \to 0$ equals the zero endomorphism of $0$, and the composition $P \to 0 \to P$ equals $\operatorname{id}_P = 0$ in $\underline{\operatorname{Hom}}_R(P, P)$. Hence $P \cong 0$ in $\mathfrak{StM}_R$.

Thus every projective $R$-module is isomorphic to the zero object in the stable category $\mathfrak{StM}_R$. $\square$
