---
role: proof
locale: en
of_concept: lowenheim-skolem-theorem
source_book: gtm053
source_chapter: "I"
source_section: "7"
---

The corollary follows from Proposition 7.3. Since the alphabet of $L$ is countable, the set of all formulas of $L$ is also countable. Let $\mathcal{E}$ be the set of all formulas of $L$. Choose $M_0$ to be any countable subset of $N$, for example the empty set or the interpretations of the finitely many or countably many constant symbols.

Apply Proposition 7.3 to $\mathcal{E}$, $\psi$ (the interpretation of $L$ in $N$), and $M_0$. This yields a set $M$ with $M_0 \subset M \subset N$ and

$$\operatorname{card} M \leqslant \operatorname{card} M_0 + \operatorname{card} \mathcal{E} + \aleph_0 \leqslant \aleph_0 + \aleph_0 + \aleph_0 = \aleph_0.$$

Thus $M$ is countable. Moreover, by Proposition 7.3, all formulas in $\mathcal{E}$ (i.e., all formulas of $L$) are $(M,N)$-absolute. In particular, for any formula $P \in \mathcal{E}$ and any $\xi \in \overline{M}$, $|P|_M(\xi) = |P|_N(\xi)$. Therefore, if $N$ is a model for some set of sentences, $M$ is also a model for those same sentences. The restriction of $\psi$ to $M$ gives the required countable submodel.
