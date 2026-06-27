---
role: proof
locale: en
of_concept: artinian-radical-nilpotent
source_book: gtm013
source_chapter: "9"
source_section: "15"
---
In view of (15.10), it suffices to prove that for a left artinian ring $R$, its radical $J = J(R)$ is nilpotent. Since
$$J \supseteq J^2 \supseteq J^3 \supseteq \cdots,$$
the left artinian hypothesis implies $J^n = J^{n+1}$ for some $n > 0$. Suppose $J^n \neq 0$. Then the collection of left ideals of $R$ that are not annihilated by $J^n$ is non-empty. By (10.10), there exists a left ideal $I$ of $R$ minimal with respect to the property $J^n I \neq 0$. Let $x \in I$ with $J^n x \neq 0$. Then $Jx \leq Rx \leq I$ and
$$J^n(Jx) = J^{n+1}x = J^n x \neq 0.$$
By the minimality of $I$, we have $Jx = Rx$. But $Jx \leq J(R)x$ contradicts Nakayama's Lemma (15.13) since $J(R) \cdot Rx = Rx \neq 0$ but $Rx$ is finitely generated (being cyclic). Hence $J^n = 0$, so $J$ is nilpotent.
