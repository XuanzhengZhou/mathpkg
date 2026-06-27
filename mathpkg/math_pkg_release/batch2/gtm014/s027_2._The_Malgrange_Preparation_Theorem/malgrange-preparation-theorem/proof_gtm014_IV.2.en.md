---
role: proof
locale: en
of_concept: malgrange-preparation-theorem
source_book: gtm014
source_chapter: "IV"
source_section: "§2. The Malgrange Preparation Theorem"
---

The proof that Theorem 2.2 $\Rightarrow$ Theorem 2.1 (Mather Division Theorem) is word-for-word the same as the proof that Theorem 1.4 $\Rightarrow$ Theorem 1.2 (Weierstrass Division Theorem), substituting "smooth" for "holomorphic" throughout.

Then the Malgrange Preparation Theorem follows from the Mather Division Theorem: let $G(t, x) = t^k$ and apply Theorem 2.1. Setting $\lambda_i = r_i$ proves the desired representation $(qF)(t, x) = t^k + \sum \lambda_i(x)t^i$. To show $q(0) \neq 0$, consider the equality at $x=0$:
$$t^k = q(t,0)F(t,0) + r(t,0) = q(t,0)t^k g(t) + \sum r_i(0)t^i.$$
Since both sides are smooth, a power series argument gives $q(0)g(0) = 1$, hence $q(0) \neq 0$.
