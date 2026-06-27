---
role: proof
locale: en
of_concept: meromorphic-functions-complete-metric-space
source_book: gtm011
source_chapter: "7"
source_section: "3"
---

This corollary follows from the convergence properties established for sequences of meromorphic functions. By Hurwitz's Theorem (2.5), either $\frac{1}{f} \equiv 0$ or $\frac{1}{f}$ has isolated zeros in $B(a; r)$. So if $f \neq \infty$ then $\frac{1}{f} \neq 0$ and $f$ must be meromorphic in $B(a; r)$. Combining this with the first part of the proof we have that $f$ is meromorphic in $G$ if $f$ is not identically infinite.

If each $f_n$ is analytic then $\frac{1}{f_n}$ has no zeros in $B(a; r)$. It follows from Corollary 2.6 to Hurwitz's Theorem that either $\frac{1}{f} \equiv 0$ or $\frac{1}{f}$ never vanishes. But since $f(a) = \infty$ we have that $\frac{1}{f}$ has at least one zero; thus $f \equiv \infty$ in $B(a; r)$. Combining this with the first part of the proof we see that $f \equiv \infty$ or $f$ is analytic.

Since $M(G) \cup \{\infty\} \subset C(G, \mathbb{C}_\infty)$ and the latter is complete under the topology of uniform convergence on compact sets, the completeness follows from showing that limits of sequences in $M(G)$ remain in $M(G) \cup \{\infty\}$.
