---
role: proof
locale: en
of_concept: decomposition-of-symmetric-nonalternating-bilinear-form
source_book: gtm049
source_chapter: "5"
source_section: "5.3"
---

**PROOF.** The equality $r = \operatorname{rank} \sigma$ follows from the corollary to Proposition 4. The direct sum decomposition is proved by induction on $\dim V$.

Since $\sigma$ is not alternating, there exists $a \in V$ such that $\sigma(a,a) \neq 0$. Then $A = [a]$ is a non-degenerate subspace, and by Proposition 5, $V = A \oplus A^\perp$. If the restriction of $\sigma$ to $A^\perp$ is either zero or not alternating, the theorem follows by induction. (Over fields of characteristic $\neq 2$, the proof ends here.)

Suppose the restriction of $\sigma$ to $A^\perp$ is alternating and not zero. Then we can find vectors $b,c \in A^\perp$ such that $\sigma(b,c) \neq 0$. Note $\sigma(a+b, a+b) = \sigma(a,a) \neq 0$, so $[a+b]$ is non-degenerate.

Consider $v = xa + c$. Then $\sigma(v,v) = x^2\sigma(a,a)$ and $\sigma(a+b, v) = x\sigma(a,a) + \sigma(b,c)$. Choosing $x = -\sigma(b,c)/\sigma(a,a)$ gives $v \in [a+b]^\perp$ with $\sigma(v,v) \neq 0$. Thus $V = [a+b] \oplus [a+b]^\perp$ where $[a+b]$ is non-degenerate and $\sigma$ is not alternating on $[a+b]^\perp$. The proof is completed by induction.
