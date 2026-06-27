---
role: proof
locale: en
of_concept: cstar-quotient-is-cstar
source_book: gtm003
source_chapter: "VI"
source_section: "2"
---

Using the approximate unit $(e_n)$ for the closed ideal $J$ (Theorem 2.3, the approximate unit lemma), one shows $J^* = J$: for $x \in J$, $x^* = \lim (e_n x)^* = \lim x^* e_n \in J$.

For the quotient norm, one proves $\|\hat{x}\| = \inf_{u \in J_1} \|x(e - u)\|$ where $\hat{x} = x + J$:

Lower bound: $\|\hat{x}\| = \inf_{y \in J} \|x - y\| \leq \inf_{n} \|x - x e_n\| = \lim \|x(e - e_n)\|$.

Upper bound: $\|x - y\| \geq \|(x - y)(e - e_n)\| \geq \|x(e - e_n)\| - \|y(e - e_n)\|$. Taking $\inf$ over $y \in J$ and limits gives the equality.

For the C*-identity in the quotient: $\|\hat{x}\|^2 = \inf \|x(e - u)\|^2 = \inf \|(e - u)x^* x(e - u)\| \leq \inf \|x^* x(e - u)\| = \|\hat{x}^*\hat{x}\|$, and the reverse inequality $\|\hat{x}^*\hat{x}\| \leq \|\hat{x}^*\|\|\hat{x}\| \leq \|\hat{x}\|^2$ (since the quotient map is contractive) completes the proof that the C*-identity holds. Thus $A/J$ is a C*-algebra.
