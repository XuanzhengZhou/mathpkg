---
role: proof
locale: en
of_concept: bounded-formula-subalgebra-invariance
source_book: gtm008
source_chapter: "13"
source_section: "13. Boolean-Valued Set Theory"
---

(By induction on the number of logical symbols in $\varphi$.) If $\varphi$ is atomic, the result follows from Theorem 13.15. The only nontrivial case is the bounded existential quantifier:

$$\varphi(u, u_1, \ldots, u_n) \equiv (\exists x \in u) \psi(x, u, u_1, \ldots, u_n).$$

Then by Theorem 13.13,
$$[\![\varphi(u, u_1, \ldots, u_n)]\!]^{(B)} = \sum_{x \in \mathcal{D}(u)} u(x) \cdot [\![\psi(x, u, u_1, \ldots, u_n)]\!]^{(B)}$$
$$= \sum_{x \in \mathcal{D}(u)} u(x) \cdot [\![\psi(x, u, u_1, \ldots, u_n)]\!]^{(B')}$$
by the induction hypothesis. By Theorem 13.13 again, this equals $[\![\varphi(u, u_1, \ldots, u_n)]\!]^{(B')}$, since $\mathcal{D}(u) \subseteq V^{(B)}$ by assumption. The cases of negation, conjunction, and bounded universal quantification are handled similarly.
