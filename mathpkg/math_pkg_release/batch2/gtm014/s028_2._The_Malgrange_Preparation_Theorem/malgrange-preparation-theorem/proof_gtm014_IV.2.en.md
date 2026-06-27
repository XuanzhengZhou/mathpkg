---
role: proof
locale: en
of_concept: malgrange-preparation-theorem
source_book: gtm014
source_chapter: "IV"
source_section: "2"
---

The Malgrange Preparation Theorem follows from the Mather Division Theorem (Theorem 2.1) in precisely the same way that the Weierstrass Preparation Theorem (Theorem 1.1) follows from the Weierstrass Division Theorem (Theorem 1.2).

**Proof sketch.** Given $F$ with $F(t, 0) = g(t)t^k$ and $g(0) \neq 0$, apply the Division Theorem (2.1) with $G(t, x) = t^k$. There exist smooth $q$ and $r$ such that
$$t^k = q(t, x)F(t, x) + r(t, x)$$
with $r(t, x) = \sum_{i=0}^{k-1} r_i(x)t^i$. Evaluating at $x = 0$:
$$t^k = q(t, 0)F(t, 0) + r(t, 0) = q(t, 0)g(t)t^k + \sum_{i=0}^{k-1} r_i(0)t^i.$$
Since $g(0) \neq 0$, comparing coefficients of $t^k$ yields $q(0, 0)g(0) = 1$, so $q(0) \neq 0$. Rearranging:
$$q(t, x)F(t, x) = t^k - r(t, x) = t^k - \sum_{i=0}^{k-1} r_i(x)t^i.$$
Setting $\lambda_i(x) = -r_i(x)$ gives the desired form.
