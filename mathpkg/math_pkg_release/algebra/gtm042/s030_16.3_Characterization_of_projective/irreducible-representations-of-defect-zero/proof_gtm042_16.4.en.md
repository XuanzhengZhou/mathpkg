---
role: proof
locale: en
of_concept: irreducible-representations-of-defect-zero
source_book: gtm042
source_chapter: "16"
source_section: "16.4"
---

Assume that $K$ is sufficiently large.

Let $E$ be a simple $K[G]$-module of dimension $N$, and let $P$ be a $G$-stable lattice in $E$. By hypothesis, $p^n \mid N$, where $p^n$ is the largest power of $p$ dividing $g = |G|$.

(a) To show $P$ is projective, it suffices to prove that $\bar{P} = P/\mathfrak{m}P$ is a projective $k[G]$-module. Let $\varphi_P$ be the character of $P$. The defect of the block containing $E$ is zero because the dimension $N$ is divisible by $p^n$; consequently the corresponding primitive idempotent of $k[G]$ lifts to $A[G]$, and $P$ is projective.

(b) The surjectivity of $A[G] \to \operatorname{End}_A(P)$ follows from the fact that $P$ is a projective $A[G]$-module and that $E = P \otimes_A K$ is absolutely irreducible (since the center of $\operatorname{End}_{K[G]}(E)$ is $K$). The kernel is then a direct factor by general properties of separable algebras.

(c) That $\bar{P}$ is simple and projective follows from the defect zero condition: the reduction modulo $\mathfrak{m}$ of an irreducible representation of defect zero remains irreducible and becomes a projective $k[G]$-module.
