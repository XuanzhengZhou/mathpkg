---
role: proof
locale: en
of_concept: sylvesters-law-of-inertia
source_book: gtm023
source_chapter: "9"
source_section: "2. The decomposition of E"
---

Suppose $\Phi(x) = \sum_v \lambda_v (\xi^v)^2$ with $\lambda_v > 0$ for $v = 1, \ldots, p$ and $\lambda_v \leq 0$ for $v = p+1, \ldots, n$.

The vectors $x_1, \ldots, x_p$ (corresponding to the first $p$ coordinates) span a subspace of dimension $p$ on which $\Phi$ is positive definite: for any nonzero linear combination $x = \sum_{v=1}^p \xi^v x_v$, we have $\Phi(x) = \sum_{v=1}^p \lambda_v (\xi^v)^2 > 0$.

On the other hand, any subspace $F$ on which $\Phi$ is positive definite can have dimension at most $p$. Indeed, if $\dim F > p$, then by dimension considerations $F$ would have nontrivial intersection with the subspace spanned by $x_{p+1}, \ldots, x_n$. Any nonzero vector in this intersection would satisfy $\Phi(x) \leq 0$ (since all $\lambda_v \leq 0$ for $v > p$), contradicting positive definiteness on $F$.

Therefore $p$ is the maximal dimension of a positive definite subspace, i.e., $p$ is the index of $\Phi$. By the uniqueness of the index (proved above), $p$ is independent of the particular diagonal representation chosen.
