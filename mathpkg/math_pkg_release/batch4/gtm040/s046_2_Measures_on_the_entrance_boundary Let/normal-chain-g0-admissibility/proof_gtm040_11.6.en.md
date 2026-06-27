---
role: proof
locale: en
of_concept: normal-chain-g0-admissibility
source_book: gtm040
source_chapter: "11"
source_section: "3"
---

**Proof of Lemma 11-6.** From the definition of the potential matrix, we have $G_{0j} \geq 0$ for all $j$ and $G_{00} = 0$, which verify conditions (1) and (2).

For condition (3), multiply the definition $G_{0\cdot} = \delta_0 + \delta_0 P + \delta_0 P^2 + \cdots$ on the right by $P$:
$$G_{0\cdot} P = \delta_0 P + \delta_0 P^2 + \delta_0 P^3 + \cdots.$$
Since all terms are non-negative, Fatou's Theorem (or monotone convergence) yields
$$G_{0\cdot} P = G_{0\cdot} - \delta_0 \leq G_{0\cdot} + \delta_0,$$
which is precisely condition (3): $\nu P \leq \nu + \delta_0$.

For the second formula, form the $K$-matrix of Definition 9-80 with respect to the distinguished state $0$. By Lemma 9-81, $K_{0j} = G_{0j}$. The $0$th row of the formula of Corollary 9-86 then yields
$$\nu_E (I - P^E) = \lambda^E_E - \delta_0,$$
as required.
