---
role: proof
locale: en
of_concept: explicit-reciprocity-symbol-identity
source_book: gtm059
source_chapter: "9"
source_section: "§6"
---

**Proof.** For $x, y \in v_w$ we have

$$x + [y] x = x + y \bmod xy, \qquad x - [-] y = x - y \bmod xy.$$

This will be applied when $\operatorname{ord}_x, \operatorname{ord}_y \ge 2$, so that $\operatorname{ord}_x, \operatorname{ord}_y \ge n + 3$. In that case, addition on the formal group $A$ and addition on the multiplicative group $\mathbb{G}_m$ are interchangeable on the left of the symbol.

We compute:

$$0 = (\operatorname{ord}_x(-1), \operatorname{ord}_x(-1))$$
$$= (\operatorname{ord}_x^2(-1) - \operatorname{ord}_x^2(-1)) + [\operatorname{ord}_x^2(-1) - \operatorname{ord}_x^2(-1)]$$
$$= (\operatorname{ord}_x^2(-1), \operatorname{ord}_x^2(-1)) + [\operatorname{ord}_x^2(-1) - [\operatorname{ord}_x(-1) - 1]].$$

Hence

$$(\operatorname{ord}_x(-1), \operatorname{ord}_x(-1)) = (\operatorname{ord}_x^2(-1), \operatorname{ord}_x^2(-1)) + [\operatorname{ord}_x^2(-1), \operatorname{ord}_x^2(-1)].$$

Note that $(\operatorname{ord}_x, \operatorname{ord}_y) = 0$ for all $x \in v_w$. Recursively we obtain

$$\operatorname{ord}_x(-1) = 1 + \sum_{i=1}^{n-1} (\operatorname{ord}_x^{i+1})^{2-i+1} = \sum_{i=1}^{n-1} (\operatorname{ord}_x^{i})^{2-i+1},$$

which yields the claimed formula.
