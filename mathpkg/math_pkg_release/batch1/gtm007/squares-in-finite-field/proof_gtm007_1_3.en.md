---
role: proof
locale: en
of_concept: squares-in-finite-field
source_book: gtm007
source_chapter: "I"
source_section: "3"
---

(a) If $p = 2$, the Frobenius map $x \mapsto x^2$ is an automorphism of $\mathbb{F}_q$ (it is additive since $(x+y)^2 = x^2 + y^2$ in characteristic 2, and injective), so every element is a square.

(b) Assume $p \neq 2$. Let $\Omega$ be an algebraic closure of $\mathbb{F}_q$. If $x \in \mathbb{F}_q^*$, choose $y \in \Omega$ with $y^2 = x$. Then $y^{q-1} = x^{(q-1)/2}$. Since $x^{q-1} = 1$, we have $(x^{(q-1)/2})^2 = 1$, so $x^{(q-1)/2} = \pm 1$. For $x$ to be a square in $\mathbb{F}_q$, we need $y \in \mathbb{F}_q^*$, i.e., $y^{q-1} = 1$, which means $x^{(q-1)/2} = 1$. Thus $\mathbb{F}_q^{*2}$ is exactly the kernel of $x \mapsto x^{(q-1)/2}$. Since $\mathbb{F}_q^*$ is cyclic of order $q-1$, the map $x \mapsto x^{(q-1)/2}$ is surjective onto $\{\pm 1\}$, so the kernel has index $2$.
