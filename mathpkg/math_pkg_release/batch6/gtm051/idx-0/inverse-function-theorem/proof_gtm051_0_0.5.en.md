---
role: proof
locale: en
of_concept: inverse-function-theorem
source_book: gtm051
source_chapter: "0"
source_section: "0.5"
---

Since $dF_0$ is bijective, the implicit function theorem (or the fixed point / contraction mapping principle) guarantees that $F$ is a local diffeomorphism near $0$. More concretely:

Consider the auxiliary map $G: U \to \mathbb{R}^n$ defined by $G(x) = x - (dF_0)^{-1}(F(x) - dF_0(x))$. Then $dG_0 = 0$. For a sufficiently small neighborhood $U'$ of $0$, the map $y \mapsto G(x)$ is a contraction in $x$ for each fixed $y$ near $0$. By the Banach fixed point theorem, for each $y$ close enough to $0$, there exists a unique $x \in U'$ such that $F(x) = y$. The inverse function $F^{-1}$ thus exists locally, and by the inverse function theorem for $C^\infty$ maps, it is differentiable with $d(F^{-1})_{F(x)} = (dF_x)^{-1}$.

Alternatively, more directly: since $dF_0$ is an isomorphism, by continuity $dF_x$ remains invertible for $x$ in a small neighborhood $U'$ of $0$. The map $F$ is then a local diffeomorphism by the inverse function theorem (a standard result in advanced calculus, proved via the contraction mapping principle).
