---
role: proof
locale: en
of_concept: boolean-algebra-ccc-but-powers-fails
source_book: gtm008
source_chapter: "23"
source_section: "3"
---

To prove Theorem 11.11 we used the partial order structure $P_{\alpha} = \langle P_{\alpha}, \leq \rangle$ where
$$P_{\alpha} = \{p \mid (\exists d)[d \subseteq \alpha \times \omega \wedge d < \omega \wedge p: d \rightarrow 2]\}$$
$$p_1 \leq p_2 \leftrightarrow p_1 \supseteq p_2 \text{ for } p_1, p_2 \in P_{\alpha},$$
to add $\alpha$-many subsets of $\omega$ to $M$, so that $\overline{\mathcal{P}(\omega)} \geq \alpha$ in $M[G]$ (assuming that $\alpha$ is a cardinal in $M$). In terms of Boolean-valued models this means
$$\llbracket \overline{\mathcal{P}(\omega)} \geq \check{\alpha} \rrbracket = 1.$$
Thus $V^{(B)}$ fails to satisfy the Axiom of Powers because the power set of $\omega$ in $V^{(B)}$ can be arbitrarily large.
