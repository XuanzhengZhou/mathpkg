---
role: proof
locale: en
of_concept: deformation-germ-infinitesimally-stable-finite-set
source_book: gtm014
source_chapter: "IV"
source_section: "4"
---

In the case that $S$ is a single point, this is just Proposition 4.3.

For the general case where $S = \{p_1, \ldots, p_k\}$ is a finite set, the proof proceeds precisely as the proof of Proposition 4.3 with the following modifications:

Replace the module $A_F^p$ at a single point with the direct sum
$$A_F^S = A_F^{p_1} \oplus \cdots \oplus A_F^{p_k},$$
where $A_F^{p_i}$ denotes the module associated to the germ of $F$ at $(p_i, 0)$.

In the proof of Proposition 4.3, the claim that $A$ is a finitely generated module over $C^\infty_{(q,0)}(Y \times \mathbf{R}^k)$ is proved using the Malgrange Preparation Theorem (IV, Theorem 3.6). For the generalization to a finite set, Lemma 1.4 is used instead to handle the direct sum decomposition of $A_F^S$.

The remaining steps — constructing the vector fields $\zeta$ on $X \times \mathbf{R}^k$ and $\eta$ on $Y \times \mathbf{R}^k$, verifying that their $\mathbf{R}^k$-components vanish, and establishing the equation $\tau_F = (dF)(\zeta) + F^*\eta$ — carry over verbatim from the proof of Proposition 4.3, applied simultaneously at each point $p_i \in S$ in a neighborhood of $S \times \{0\}$.
