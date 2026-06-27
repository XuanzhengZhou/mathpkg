---
role: proof
locale: en
of_concept: generating-cone-direction-equivalence
source_book: gtm036
source_chapter: "23"
source_section: "ORDERED LINEAR SPACES"
---

The equivalence is obtained by a simple translation argument from the previous characterization $C - C = E \iff \forall x \exists u \geq 0 : u \geq x$.

If $C$ generates $E$, then for any $x, y \in E$, let $u \geq x$ with $u \geq 0$ (by the previous characterization applied to $x$). Let $v \geq u$ and $v \geq y$ (by applying the characterization to the element $y$ after replacing $x$ by something larger than both, or more directly: first find $w \geq x$ and then increase to also dominate $y$). A cleaner argument: find $u_1 \geq x, u_1 \geq 0$ and $u_2 \geq y, u_2 \geq 0$. Let $z = u_1 + u_2 \in C$. Then $z - x = (u_1 - x) + u_2 \in C + C \subseteq C$, so $z \geq x$. Similarly $z \geq y$.

Conversely, if the ordering directs $E$, then for any $x \in E$, take $y = 0$: there exists $z \in C$ with $z \geq x$ and $z \geq 0$. Thus every $x$ has a positive upper bound, so $C$ generates $E$ by the previous equivalence.
