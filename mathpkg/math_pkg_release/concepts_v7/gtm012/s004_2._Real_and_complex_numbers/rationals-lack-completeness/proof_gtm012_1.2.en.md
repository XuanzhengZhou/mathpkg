---
role: proof
locale: en
of_concept: rationals-lack-completeness
source_book: gtm012
source_chapter: "1"
source_section: "2. Real and complex numbers"
---

# Proof of Theorem 2.1: The Rational Numbers Do Not Satisfy the Completeness Axiom

Consider the set

$$A = \{ y \in \mathbb{Q} \mid y > 0,\; y^2 < 2 \}.$$

The set $A$ is nonempty (e.g., $1 \in A$ since $1^2 = 1 < 2$) and is bounded above (e.g., $2$ is an upper bound since $y > 2$ implies $y^2 > 4 > 2$). If $\mathbb{Q}$ satisfied the completeness axiom O5, then $A$ would have a least upper bound $x = \operatorname{lub} A$ with $x \in \mathbb{Q}$.

Since $1 \in A$, we have $x \geq 1 > 0$. We consider the three possibilities for $x^2$:

1. **If $x^2 < 2$**, then $x$ would not be an upper bound of $A$. Indeed, one can find a rational number $h > 0$ sufficiently small such that $(x + h)^2 < 2$ (for example, choose $h < \min\left(1, \frac{2 - x^2}{2x + 1}\right)$). Then $x + h \in A$, contradicting that $x$ is an upper bound.

2. **If $x^2 > 2$**, then $x$ would not be the *least* upper bound. One can find $h > 0$ such that $(x - h)^2 > 2$ (choose $h < \frac{x^2 - 2}{2x}$). Then $x - h$ is an upper bound of $A$ that is smaller than $x$, contradicting that $x$ is the least upper bound.

3. **Therefore $x^2 = 2$.** But there is no rational number whose square is $2$ (this is the classic proof: if $x = p/q$ in lowest terms and $(p/q)^2 = 2$, then $p^2 = 2q^2$, so $p$ is even; writing $p = 2r$ gives $4r^2 = 2q^2$, so $q^2 = 2r^2$ and $q$ is also even, contradicting that $p/q$ is in lowest terms).

Thus the assumption that $\mathbb{Q}$ satisfies O5 leads to a contradiction. Hence $\mathbb{Q}$ does not satisfy the completeness axiom. In $\mathbb{R}$, however, $A$ does have a least upper bound $x$ with $x^2 = 2$, which shows that $\mathbb{R}$ contains elements (such as $\sqrt{2}$) that are not in $\mathbb{Q}$.
