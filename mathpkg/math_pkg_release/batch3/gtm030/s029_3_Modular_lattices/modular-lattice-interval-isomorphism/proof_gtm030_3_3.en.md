---
role: proof
locale: en
of_concept: modular-lattice-interval-isomorphism
source_book: gtm030
source_chapter: "3"
source_section: "3"
---

Let $x$ be in the interval $I[a \cup b, a]$, so that $a \cup b \geq x \geq a$. Then applying the meet with $b$, we obtain $b \geq x \cap b \geq a \cap b$, so $x \cap b$ lies in the interval $I[b, a \cap b]$. Similarly, if $y$ is in $I[b, a \cap b]$, then $b \geq y \geq a \cap b$, and applying the join with $a$ gives $a \cup b \geq y \cup a \geq a$, so $y \cup a$ lies in $I[a \cup b, a]$. Thus we have mappings

$$x \mapsto x \cap b : I[a \cup b, a] \to I[b, a \cap b],$$
$$y \mapsto y \cup a : I[b, a \cap b] \to I[a \cup b, a].$$

We show these are inverses. Let $x \in I[a \cup b, a]$. Since $x \geq a$, the modular law $L_5$ gives

$$(x \cap b) \cup a = x \cap (a \cup b).$$

Since $x \leq a \cup b$, we have $x \cap (a \cup b) = x$, hence $(x \cap b) \cup a = x$. Dually, if $y \in I[b, a \cap b]$, then $(y \cup a) \cap b = y$. Therefore the two mappings are mutually inverse bijections and preserve the order, establishing the isomorphism of the intervals.
