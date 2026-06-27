---
role: proof
locale: en
of_concept: definition-by-transfinite-induction
source_book: gtm027
source_chapter: "Appendix"
source_section: "The Classification Axiom Scheme"
---

# Proof of Definition by Transfinite Induction

**Definition by Transfinite Induction (Theorem 128).** Given any function $g$, there exists a unique function $f$ such that domain $f = R$ (the class of ordinal numbers) and $f(x) = g(f|x)$ for each ordinal number $x$.

*Proof.* This is exactly Theorem 128 (Transfinite Induction). The proof proceeds by:
1. Comparability lemma (Theorem 127): any two functions satisfying the recursion equation on ordinal domains are compatible.
2. Let $f$ be the union of all such partial functions.
3. Then $f$ is itself a function with ordinal domain satisfying the equation.
4. If domain $f \neq R$, let $y$ be the first ordinal not in domain $f$. If $g(f)$ is a set, extend $f$ by adding $(y, g(f))$, contradicting maximality. If $g(f) = \mathcal{U}$, then $f(x) = \mathcal{U}$ for all $x \geq$ domain $f$ by Theorem 69, and the equation still holds.

The uniqueness follows directly from the comparability lemma.
