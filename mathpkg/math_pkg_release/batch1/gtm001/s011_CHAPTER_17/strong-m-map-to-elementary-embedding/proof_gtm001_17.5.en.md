---
role: proof
locale: en
of_concept: strong-m-map-to-elementary-embedding
source_book: gtm001
source_chapter: "17"
source_section: "17.5"
---

For any term $t$ of $\mathcal{L}$, define $h(D(t)) = D(\pi(t))$. Then $h$ is well-defined and for all $\alpha \in \text{On}$, $h(\alpha) = h(D(\check{\alpha})) = D(\pi(\check{\alpha})) = D(\pi(\alpha)) = \pi(\alpha)$.

Let $\psi(x_0, \ldots, x_n)$ be a bounded formula and let $t_0, \ldots, t_n \in T_\alpha$. Let $\psi^\alpha(x_0, \ldots, x_n)$ be the formula obtained from $\psi$ by replacing each bounded quantifier $\exists x \in y(\ldots)$ by $\exists^\alpha x (x \in y \wedge \ldots)$. Then

$$L \models \psi(D(t_0), \ldots, D(t_n)) \leftrightarrow T(\langle \psi^\alpha(t_0, \ldots, t_n) \rangle) = 1$$
$$\leftrightarrow T(\langle \psi^{\pi(\alpha)}(\pi(t_0), \ldots, \pi(t_n)) \rangle) = 1$$
$$\leftrightarrow L \models \psi(D(\pi(t_0)), \ldots, D(\pi(t_n))).$$

For $\Sigma_1$ formulas $\varphi(x_1, \ldots, x_n) = (\exists x_0)\psi(x_0, x_1, \ldots, x_n)$, upward absoluteness follows from the bounded case together with the fact that $\pi$ is cofinal (as a strong $M$-map on On). The downward direction uses the term model to find a witness.
