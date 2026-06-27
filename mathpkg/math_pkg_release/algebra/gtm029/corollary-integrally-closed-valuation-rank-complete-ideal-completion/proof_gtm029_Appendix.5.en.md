---
role: proof
locale: en
of_concept: corollary-integrally-closed-valuation-rank-complete-ideal-completion
source_book: gtm029
source_chapter: "Appendix"
source_section: "5"
---

We first establish a lemma on complete $o$-modules, where $o$ is not necessarily noetherian.

Lemma. Let $K$ be a field containing $o$, let $M$ be a finite $o$-module contained in $K$ and let $\{x_i\}$ be a finite $o$-basis of $M$. For each $i$ let $o_i$ denote the ring generated over $o$ by the quotients $x_j/x_i$, $j \neq i$, and let $o_i$ be the integral closure of $o_i$ in $K$. If $M'$ is the completion of $M$ in $K$ then

$$M' = \bigcap_i o_i x_i.$$

PROOF OF THE LEMMA. If $y \in M'$ and $v$ is any valuation of $K$ which is non-negative on $o_i$, then $v \in S$ and $v(x_j) \geq v(x_i)$ for all $j$. Thus $R_v M = R_v x_i$, $v(y) \geq v(x_i)$ for all such $v$, and hence $y \in o_i x_i$.

Conversely, let $y$ be an element of the intersection of the $o_i x_i$ and let $v \in S$. If $i$ is an index such that $v(x_j) \geq v(x_i)$ for all $j$, then $v$ is non-negative on $o_i$ and hence $v(y) \geq v(x_i)$. Thus $y \in R_v x_i = R_v M$, and this shows that $y \in M'$. The lemma is proved.

The proof of the theorem is now immediate. We identify the ideal $B$ of the theorem with the module $M$ of the lemma

valuation ideals in $\bar{o}$, of which $\mathfrak{A}$ is the intersection, are primary ideals. Those which are associated with the same prime ideal in $\mathfrak{o}$ yield a partial intersection which is a primary complete ideal.

One often deals with complete fractional $\mathfrak{o}$-ideals, i.e., with finite complete $\mathfrak{o}$-modules contained in the quotient field of $\mathfrak{o}$. It is clear that any such complete fractional $\mathfrak{o}$-ideal is of the form $\frac{1}{z} \cdot \mathfrak{A}$, where $\mathfrak{A}$ is a complete (integral) ideal in $\mathfrak{o}$ (use property (f) of Proposition 1).

4. We shall now discuss briefly the axiomatic aspects of the properties (a)–(g) (see Proposition 1) of the 'operation. The operation of completion of $\mathfrak{o}$-modules $M$, in $K$, is not the only 'operation on $\mathfrak{o}$-modules which satisfies properties (a)–(g) of Proposition 1. If we examine the proof of that proposition we see that we have not used the fact that the set $S$ consists of all the valuations $v$ of $K$ which are non-negative on $\mathfrak{o}$, but only the fact that the intersection of all the valuation rings $R_v, v \in S$, is the integral closure of $\mathfrak{o}$ in $K$. Therefore, if we choose any subset $S_1$ of $S$ with the property

$$\bigcap_{v \in S_1} R_v = \bar{o}$$

and define for any module $M$ in $K$ its completion $M'$ by

$$M' = \bigcap_{v \in S_1} R_v M,$$

we obtain another 'operation which satisfies conditions (a)–(g). An important special case is the one in which $\mathfrak{o}$ is a noetherian integrally closed domain, $K$ the quotient field of $\mathfrak{o}$ and $S_1$ the set of all essential valuations of $\mathfrak
