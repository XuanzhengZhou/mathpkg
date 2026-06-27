---
role: proof
locale: en
of_concept: serre-cohomology-finiteness
source_book: gtm052
source_chapter: "III"
source_section: "5"
---

Since $\mathcal{O}_X(1)$ is a very ample sheaf on $X$ over $\operatorname{Spec} A$, there is a closed immersion $i : X \rightarrow \mathbf{P}_A^r$ of schemes over $A$, for some $r$, such that $\mathcal{O}_X(1) = i^*\mathcal{O}_{\mathbf{P}^r}(1)$ — cf. (II, 5.16.1). If $\mathcal{F}$ is coherent on $X$, then $i_*\mathcal{F}$ is coherent on $\mathbf{P}_A^r$ (II, Ex. 5.5), and the cohomology is the same (2.10). Thus we reduce to the case $X = \mathbf{P}_A^r$.

For $X = \mathbf{P}_A^r$, we observe that (a) and (b) are true for any sheaf of the form $\mathcal{O}_X(q)$, $q \in \mathbf{Z}$. This follows immediately from the explicit calculations (5.1). Hence the same is true for any finite direct sum of such sheaves.

To prove the theorem for arbitrary coherent $\mathcal{F}$ on $\mathbf{P}_A^r$, we use descending induction on the dimension of the support of $\mathcal{F}$, together with the fact that any coherent sheaf on $\mathbf{P}_A^r$ admits a surjection from a finite direct sum of sheaves $\mathcal{O}(q_i)$. Writing $\mathcal{F}$ as a quotient of such a sum $\mathcal{E}$, we obtain an exact sequence

$$0 \rightarrow \mathcal{R} \rightarrow \mathcal{E} \rightarrow \mathcal{F} \rightarrow 0.$$

The kernel $\mathcal{R}$ has strictly smaller support, so by induction (a) and (b) hold for $\mathcal{R}$. Since they hold for $\mathcal{E}$, the long exact cohomology sequence yields the result for $\mathcal{F}$.
