---
role: proof
locale: en
of_concept: absolute-submodel-existence
source_book: gtm053
source_chapter: "I"
source_section: "7"
---

Suppose the set $M_i \subset N$, $i \geqslant 0$, has already been defined. Set

$$M_{i+1} = M_i \cup \{x^{\xi'} \mid \xi' = \xi'(x, P, \xi)\},$$

where $x$ runs through the variables in $L$, $P$ runs through the formulas in $\mathcal{E}$, and $\xi$ runs through the points $\overline{M}_i$. The element $x^{\xi'}$ is chosen so that if $|\exists x P|_N(\xi) = 1$, then $|P|_N(\xi') = 1$ with $\xi'$ a variation of $\xi$ along $x$.

Now define $M = \bigcup_{i=0}^{\infty} M_i$. The cardinality bound follows from the construction: at each stage, at most $\operatorname{card} \mathcal{E} \cdot \operatorname{card} \overline{M}_i$ new elements are added, and $\operatorname{card} \overline{M}_0 \leqslant \operatorname{card} M_0 + \aleph_0$. By induction, $\operatorname{card} M \leqslant \operatorname{card} M_0 + \operatorname{card} \mathcal{E} + \aleph_0$.

To verify absoluteness, one proves by induction on the structure of formulas in $\mathcal{E}$ that for all $P \in \mathcal{E}$ and all $\xi \in \overline{M}$, $|P|_M(\xi) = |P|_N(\xi)$. The key case is $P = \exists x Q$. There exists a variation $\eta$ of the point $\xi$ along variables that do not occur freely in $P$, such that $\eta \in \overline{M}_i$ for some $i$. Then in the case $|\exists x P|_N(\xi) = |\exists x P|_N(\eta) = 1$, there is a $\xi' \in \overline{N}$ with $|P|_N(\xi') = 1$, hence there is an $\eta' \in \overline{M}_{i+1}$ with $|P|_N(\eta') = 1$, where $\eta'$ is a variation of $\eta$ along $x$, by the construction of $M_{i+1}$. This completes the proof.
