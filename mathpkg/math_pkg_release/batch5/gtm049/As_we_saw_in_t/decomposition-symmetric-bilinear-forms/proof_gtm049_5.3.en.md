---
role: proof
locale: en
of_concept: decomposition-symmetric-bilinear-forms
source_book: gtm049
source_chapter: "5"
source_section: "5.3"
---

The last assertion of Theorem 3 follows from the corollary to Proposition 4. The direct sum decomposition is proved by induction on $\dim V$.

Since $\sigma$ is not alternating, there exists $a \in V$ such that $\sigma(a, a) 
eq 0$. Then $A = [a]$ is a non-degenerate subspace and hence $V = A \oplus A^\perp$ by Proposition 5. If the restriction of $\sigma$ to $A^\perp$ is either zero or is not alternating, the theorem follows by induction. (By the remark above, the proof ends here if $F$ is not of characteristic 2.)

Suppose then that the restriction of $\sigma$ to $A^\perp$ is alternating and not zero. Thus we can find vectors $b, c \in A^\perp$ such that $\sigma(b, c) 
eq 0$. We note that $\sigma(a + b, a + b) = \sigma(a, a) 
eq 0$, so $[a + b]$ is non-degenerate.

Consider the vector $v = xa + c$. Then

$$\sigma(v, v) = x^2 \sigma(a, a)$$

and

$$\sigma(a + b, v) = x\sigma(a, a) + \sigma(b, c).$$

If $x = -\sigma(b, c)/\sigma(a, a)$, the vector $v$ lies in $[a + b]^\perp$ and $\sigma(v, v) 
eq 0$. Thus $V = [a + b] \oplus [a + b]^\perp$ where $[a + b]$ is non-degenerate and $\sigma$ is not alternating on $[a + b]^\perp$. The proof can now be completed by induction.
