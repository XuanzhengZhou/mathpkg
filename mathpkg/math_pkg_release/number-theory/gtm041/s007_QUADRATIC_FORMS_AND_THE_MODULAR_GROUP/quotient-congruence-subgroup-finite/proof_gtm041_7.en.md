---
role: proof
locale: en
of_concept: quotient-congruence-subgroup-finite
source_book: gtm041
source_chapter: ""
source_section: "Quadratic Forms and the Modular Group"
---

Consider the natural reduction map $\phi: \Gamma \to \text{SL}(2, \mathbb{Z}/n\mathbb{Z})$ defined by reducing each matrix entry modulo $n$. The kernel of $\phi$ is precisely $\Gamma^{(n)}$, since $A \in \ker(\phi)$ if and only if $A \equiv I \pmod{n}$.

By the first isomorphism theorem for groups,
$$\Gamma/\Gamma^{(n)} = \Gamma/\ker(\phi) \cong \text{im}(\phi) \subseteq \text{SL}(2, \mathbb{Z}/n\mathbb{Z}).$$

Since $\mathbb{Z}/n\mathbb{Z}$ is a finite ring with $n$ elements, the group $\text{SL}(2, \mathbb{Z}/n\mathbb{Z})$ is finite (there are only finitely many $2 \times 2$ matrices over $\mathbb{Z}/n\mathbb{Z}$ with determinant $1$). Therefore its subgroup $\text{im}(\phi)$ is also finite, and consequently $\Gamma/\Gamma^{(n)}$ is finite.

Since the quotient is finite, there exist finitely many coset representatives $A_1, \ldots, A_k$ such that every $B \in \Gamma$ can be written uniquely as $B = A_i B^{(n)}$ for some $B^{(n)} \in \Gamma^{(n)}$.
