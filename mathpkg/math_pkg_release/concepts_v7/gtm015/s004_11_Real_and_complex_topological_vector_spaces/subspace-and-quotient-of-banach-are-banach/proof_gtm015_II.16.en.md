---
role: proof
locale: en
of_concept: subspace-and-quotient-of-banach-are-banach
source_book: gtm015
source_chapter: "Chapter 2 – Topological Vector Spaces"
source_section: "16. Normed spaces, Banach spaces"
---

# Proof that Closed Subspace and Quotient of a Banach Space are Banach

**Theorem (16.11).** If $E$ is a Banach space and $M$ is a closed linear subspace of $E$, then $M$ and $E/M$ are also Banach spaces (for the relative norm and the quotient norm, respectively). Moreover, the norm topologies on $M$ and $E/M$ coincide with the relative topology and the quotient topology, respectively.

*Proof.* The assertion about $M$ is straightforward: a closed subset of a complete metric space is complete. Since $M$ is a closed linear subspace of the Banach space $E$, the restriction of the norm to $M$ makes $M$ a normed space whose metric is the restriction of the complete metric on $E$. Hence $M$ is complete.

The quotient norm on $E/M$ yields the quotient topology by (16.7). For the completeness of $E/M$: let $(u_n)$ be a Cauchy sequence in $E/M$ with respect to the metric $\|u - v\|$. Choose a subsequence $(u_{n_k})$ such that $\|u_{n_{k+1}} - u_{n_k}\| < 2^{-k}$. Inductively select representatives $x_{n_k} \in u_{n_k}$ with $\|x_{n_{k+1}} - x_{n_k}\| < 2^{-k+1}$. Then $(x_{n_k})$ is Cauchy in $E$, hence converges to some $x \in E$ by completeness. Setting $u = [x]$, we have $u_{n_k} \to u$ in $E/M$, and since the original sequence is Cauchy, $u_n \to u$. Thus $E/M$ is complete. $\square$
