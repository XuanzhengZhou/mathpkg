---
role: proof
locale: en
of_concept: decomposition-nonalternating-bilinear-forms
source_book: gtm049
source_chapter: "5"
source_section: "5.3"
---

As in Theorem 3 we argue by induction on $\dim V$.

Because $\sigma$ is not alternating, there must exist a vector $a \in V$ such that $\sigma(a, a) 
eq 0$. By Proposition 5, $V = [a] \oplus [a]^\perp$. If the restriction of $\sigma$ to $[a]^\perp$ is either zero or is not alternating, the theorem follows by induction.

Suppose then that the restriction of $\sigma$ to $[a]^\perp$ is alternating and not zero. Our task is to find a vector $b \in V$ so that $[a+b]$ is non-degenerate and $\sigma$ is not alternating on $[a+b]^\perp$. We may find vectors $b, c \in [a]^\perp$ such that $\sigma(b, c) 
eq 0$. Let $v = xa + c$.

If $\sigma(b, a) = 0$, choose $x = -\sigma(b, c)/\sigma(a, a)$. Then $v \in [a+b]^\perp$ and $\sigma(v, v) 
eq 0$, completing the induction step.

If $\sigma(c, a) = 0$, a symmetric argument applies.

If neither $\sigma(b, a)$ nor $\sigma(c, a)$ is zero, set $b' = b + yc$ with $y = -\sigma(b, a)/\sigma(c, a)$ so that $\sigma(b', a) = 0$. Then $\sigma(b', c) = \sigma(b, c) 
eq 0$, and we may argue as in the first case with $b$ replaced by $b'$. This completes the proof.
