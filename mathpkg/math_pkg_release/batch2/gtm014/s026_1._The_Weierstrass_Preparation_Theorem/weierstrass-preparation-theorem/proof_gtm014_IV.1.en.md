---
role: proof
locale: en
of_concept: weierstrass-preparation-theorem
source_book: gtm014
source_chapter: "IV"
source_section: "§1. The Weierstrass Preparation Theorem"
---

Let $G(w, z) = w^k$ and apply the Weierstrass Division Theorem (Theorem 1.2). Setting $\lambda_i$ equal to $r_i$ proves (i). To show that $q(0) \neq 0$, consider

$$w^k = q(w, 0) F(w, 0) + r(w, 0)$$

$$= q(w, 0) w^k g(w) + \sum_{i=0}^{k-1} r_i(0) w^i.$$

Since both sides are analytic functions of $w$, we may use power series techniques to conclude that $q(0) g(0) = 1$ and thus $q(0) \neq 0$.
