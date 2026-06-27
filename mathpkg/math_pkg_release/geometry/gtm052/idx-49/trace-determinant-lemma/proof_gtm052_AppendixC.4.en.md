---
role: proof
locale: en
of_concept: trace-determinant-lemma
source_book: gtm052
source_chapter: "Appendix C"
source_section: "4"
---

If $\dim V = 1$, then $arphi$ is multiplication by a scalar $\lambda \in K$, and it says

$$\exp \left( \sum_{r=1}^{\infty} \lambda^r rac{t^r}{r} ight) = rac{1}{1 - \lambda t}.$$

This is an elementary calculation, which we already did in computing the zeta function of $\mathbf{P}^1$. For the general case, we use induction on $\dim V$. Furthermore, we may clearly assume that $K$ is algebraically closed. Hence $arphi$ has an eigenvector, so we have an invariant subspace $V' \subseteq V$. We use the exact sequence

$$0 ightarrow V' ightarrow V ightarrow V/V' ightarrow 0$$

and the fact that both sides of the above equation are multiplicative for short exact sequences of vector spaces. By induction, this gives the result.