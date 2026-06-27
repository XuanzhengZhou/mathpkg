---
role: proof
locale: en
of_concept: reduction-to-pairwise-coprime
source_book: gtm050
source_chapter: "2"
source_section: "2.2"
---

Assume $x^3 + y^3 = z^3$ with $x, y, z$ positive integers. Let $d$ be a prime dividing two of $\{x, y, z\}$. We show $d$ divides the third.

- If $d \mid x$ and $d \mid y$, then $d \mid (x^3 + y^3) = z^3$, so $d \mid z$.
- If $d \mid x$ and $d \mid z$, then $d \mid (z^3 - x^3) = y^3$, so $d \mid y$.
- If $d \mid y$ and $d \mid z$, then $d \mid (z^3 - y^3) = x^3$, so $d \mid x$.

In all cases, any common prime factor of two variables also divides the third. Therefore, letting $g = \gcd(x, y, z)$, we can define $x' = x/g$, $y' = y/g$, $z' = z/g$, which yields $x'^3 + y'^3 = z'^3$ with $\gcd(x', y') = \gcd(x', z') = \gcd(y', z') = 1$. Thus we may assume without loss of generality that $x, y, z$ are pairwise relatively prime.
