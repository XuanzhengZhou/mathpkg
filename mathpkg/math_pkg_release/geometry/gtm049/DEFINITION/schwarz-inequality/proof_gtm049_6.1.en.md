---
role: proof
locale: en
of_concept: schwarz-inequality
source_book: gtm049
source_chapter: "VI"
source_section: "6.1"
---

**Proof.** The result is clear when $a = 0$. Assume $\|a\| \neq 0$. Consider

$$\|xa - b\|^2 = \sigma(xa - b, xa - b) = \|a\|^2 x^2 - 2\sigma(a, b)x + \|b\|^2.$$

Since the left-hand side is nonnegative for all real $x$, the quadratic polynomial in $x$ has a non-positive discriminant:

$$4\sigma(a, b)^2 - 4\|a\|^2 \|b\|^2 \leq 0,$$

which yields $\sigma(a, b)^2 \leq \|a\|^2 \|b\|^2$, i.e., $|\sigma(a, b)| \leq \|a\| \|b\|$.

Equality holds if and only if the quadratic has a double root, which occurs precisely when there exists $x$ such that $\|xa - b\| = 0$, i.e., $b = xa$.
