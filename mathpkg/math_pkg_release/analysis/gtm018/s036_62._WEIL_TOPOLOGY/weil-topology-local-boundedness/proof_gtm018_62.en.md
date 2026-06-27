---
role: proof
locale: en
of_concept: weil-topology-local-boundedness
source_book: gtm018
source_chapter: "62"
source_section: "Weil Topology"
---

**Theorem F.** Let $N_0$ be an arbitrary set of finite measure in $\mathbf{N}$ (such a set exists by Theorem C), and let $M_0$ be a set in $\mathbf{N}$ such that $M_0M_0^{-1} \subset N_0$ (such a set exists by Theorem A). We shall prove that $M_0$ is bounded. 

For any $x \in X$, $xM_0$ is a neighborhood of $x$. Since $M_0M_0^{-1} \subset N_0$ and $\mu(N_0) < \infty$, any finite union of translates of $M_0$ has finite measure. This establishes local boundedness.

If a measurable set $E$ has nonempty interior, then $E$ contains a translate of some $N \in \mathbf{N}$. By Theorem C, $\mu(N) > 0$, hence $\mu(E) > 0$.

If a measurable set $E$ is bounded, then by definition it may be covered by a finite number of left translations of any set in $\mathbf{N}$. Choosing $M \in \mathbf{N}$ with $\mu(M) < \infty$ (by Theorem C), the finite union of translates of $M$ covering $E$ has finite measure, so $\mu(E) < \infty$. $\blacksquare$
