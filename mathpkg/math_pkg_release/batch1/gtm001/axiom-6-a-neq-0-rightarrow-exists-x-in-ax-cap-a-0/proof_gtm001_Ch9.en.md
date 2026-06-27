---
role: proof
locale: en
of_concept: axiom-6-a-neq-0-rightarrow-exists-x-in-ax-cap-a-0
source_book: gtm001
source_chapter: "9"
source_section: ""
---

** If $B = \{\text{rank}(x) | x \in A\}$ and $A \neq 0$, then $B \neq 0$. Thus $B$ is a nonempty class of ordinals, hence, by Proposition 6.26, which was proved using only the weak form of the Axiom of Regularity, $B$

Then all elements of $B_0$ have bounded rank, hence $B_0$ is a set. If $B_n$ is a set then since

$$B_{n+1} = \bigcup_{y \in B_n} \{x \in B | x \ R y \land (\forall z \in B)[z \ R y \rightarrow \text{rank}(x) \leq \text{rank}(z)]\}$$

$B_{n+1}$ is a set. Thus $(\forall n \geq 0)[\mathcal{M}(B_n)]$. If

$$b = \bigcup_{n < \omega} B_n$$

then $b \subseteq B \subseteq A$ and $b \neq 0$.

If $(\forall x \in B)[B \cap (R^{-1}) \text{"}\{x\} \neq 0]$ then in particular

$$x \in b \rightarrow B \cap (R^{-1}) \text{"}\{x\} \neq 0.$$

Furthermore $(\forall x \in b)(\exists n)[x \in B_n]$. Since $B \cap (R^{-1}) \text{"}\{x\}$ is not empty it contains an element of minimal rank, i.e.,

$(\exists y \in B)[y \ R x \land (\forall z \in B)[z \ R x \rightarrow \text{rank}(y) \leq \text{rank}(z)]].$

Since $x \in B_n$, $y \in B_{n+1}$ and hence $y \in b$. But $y \ R x$, that is

$(\forall x \in b)[b \cap (R^{-1}) \text{"}\{x\} \neq 0].$

This contradicts the fact that $R \text{ Fr } A$. $\square$
