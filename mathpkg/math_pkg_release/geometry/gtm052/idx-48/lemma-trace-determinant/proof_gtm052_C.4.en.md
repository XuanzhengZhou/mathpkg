---
role: proof
locale: en
of_concept: lemma-trace-determinant
source_book: gtm052
source_chapter: "Appendix C"
source_section: "4"
---

If $\dim V = 1$, then $\varphi$ is multiplication by a scalar $\lambda \in K$, and the identity becomes

$$\exp \left( \sum_{r=1}^{\infty} \lambda^r \frac{t^r}{r} \right) = \frac{1}{1 - \lambda t},$$

which follows from the elementary power series expansion $\sum_{r=1}^{\infty} \lambda^r t^r/r = -\log(1-\lambda t)$. For the general case, we use induction on $\dim V$. We may assume $K$ is algebraically closed. Hence $\varphi$ has an eigenvector, so there is an invariant subspace $V \subseteq V$. From the exact sequence

$$0 \rightarrow V \rightarrow V \rightarrow V/V \rightarrow 0$$

and the fact that both sides of the equation are multiplicative for short exact sequences of vector spaces, the result follows by induction.
