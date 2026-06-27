---
role: proof
locale: en
of_concept: "$C"
source_book: gtm007
source_chapter: "I"
source_section: "3.1"
---
Case (a): $p = 2$. The map $x \mapsto x^2$ is an automorphism of $\mathbb{F}_q$ (since it is injective on a finite set), so all elements are squares.

Case (b): $p \neq 2$. Let $\Omega$ be an algebraic closure of $\mathbb{F}_q$; if $x \in \mathbb{F}_q^*$, let $y \in \Omega$ satisfy $y^2 = x$. We have $y^{q-1} = x^{(q-1)/2} = \pm 1$ since $x^{q-1} = 1$. For $x$ to be a square in $\mathbb{F}_q$, we need $y \in \mathbb{F}_q^*$, i.e., $y^{q-1} = 1$. Hence $\mathbb{F}_q^{*2}$ is the kernel of $x \mapsto x^{(q-1)/2}$. Since $\mathbb{F}_q^*$ is cyclic of order $q-1$ (Theorem 2), the index of $\mathbb{F}_q^{*2}$ is $2$.
