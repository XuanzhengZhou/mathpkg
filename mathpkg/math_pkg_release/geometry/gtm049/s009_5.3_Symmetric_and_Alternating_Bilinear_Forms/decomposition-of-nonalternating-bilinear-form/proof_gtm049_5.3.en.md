---
role: proof
locale: en
of_concept: decomposition-of-nonalternating-bilinear-form
source_book: gtm049
source_chapter: "5"
source_section: "5.3"
---

**PROOF.** We argue by induction on $\dim V$.

Since $\sigma$ is not alternating, there exists $a \in V$ such that $\sigma(a,a) \neq 0$. By Proposition 5, $V = [a] \oplus [a]^\perp$. If the restriction of $\sigma$ to $[a]^\perp$ is either zero or not alternating, the theorem follows by induction.

Suppose the restriction of $\sigma$ to $[a]^\perp$ is alternating and non-zero. We must find $b \in V$ such that $[a+b]$ is non-degenerate and $\sigma$ is not alternating on $[a+b]^\perp$. Find $b, c \in [a]^\perp$ with $\sigma(b,c) \neq 0$. Let $v = xa + c$ and try to satisfy three conditions so that $v \in [a+b]^\perp$ with $\sigma(v,v) \neq 0$.

If neither $\sigma(b,a)$ nor $\sigma(c,a)$ is zero, set $b' = b + yc$ with $y = -\sigma(b,a)/\sigma(c,a)$ so that $\sigma(b',a) = 0$ while $\sigma(b',c) = \sigma(b,c) \neq 0$. Then we may proceed with $b$ replaced by $b'$, reducing to the case where one of $\sigma(b,a)$, $\sigma(c,a)$ is zero, which is handled similarly. This completes the proof.
