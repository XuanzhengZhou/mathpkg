---
role: proof
locale: en
of_concept: mather-division-theorem
source_book: gtm014
source_chapter: "IV"
source_section: "2"
---

The proof that Theorem 2.2 (Polynomial Division Theorem) implies Theorem 2.1 (Mather Division Theorem) is word-for-word the same as the proof that Theorem 1.4 implies Theorem 1.2 (in the Weierstrass context), with the single exception that "smooth" is substituted for "holomorphic" throughout.

In outline, given $F$ satisfying $F(t, 0) = g(t)t^k$ with $g(0) \neq 0$, one considers the polynomial
$$P_k(t, \lambda) = t^k + \sum_{i=0}^{k-1} \lambda_i t^i$$
and applies the Polynomial Division Theorem (2.2) to divide $G$ by $P_k$. The condition $F(t, 0) = g(t)t^k$ allows one to relate division by $F$ to division by $P_k$ through an invertible change of the smooth factor, yielding the required $q$ and $r$ with $r(t, x) = \sum_{i=0}^{k-1} r_i(x) t^i$.
