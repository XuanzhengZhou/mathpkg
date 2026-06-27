---
role: proof
locale: en
of_concept: universal-quantifier-implication-distribution
source_book: gtm037
source_chapter: ""
source_section: ""
---

We proceed by induction on $m$. The case $m = 0$ is trivial, since $(\varphi \rightarrow \psi) \rightarrow (\varphi \rightarrow \psi)$ is a tautology. Now assume the result for $m$, and suppose that $\alpha \in {}^{m+1}\text{Rng } v$. Then

$$\vdash \forall \alpha_1 \cdots \forall \alpha_m (\varphi \rightarrow \psi) \rightarrow (\forall \alpha_1 \cdots \forall \alpha_m \varphi \rightarrow \forall \alpha_1 \cdots \forall \alpha_m \psi)$$

by the induction hypothesis. Generalizing on $\alpha_0$, noticing an instance of the axioms 10.23(2), and applying detachment yields the desired result.
