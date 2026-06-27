---
role: proof
locale: en
of_concept: locally-compact-tvs-is-finite-dim
source_book: gtm003
source_chapter: "I. Topological Vector Spaces"
source_section: "3.6"
---

**Proof.** By (3.1), every one-dimensional subspace of $L$ is complete, hence closed in $L$ and therefore locally compact; it follows that $K$ is locally compact. Now let $V$ be a compact, circled 0-neighborhood in $L$, and let $\{\lambda_n\}$ be a null sequence in $K$ consisting of non-zero terms. We show first that $\{\lambda_n V : n \in \mathbb{N}\}$ is a neighborhood base of 0 in $L$. Given a 0-neighborhood $U$, choose a circled 0-neighborhood $W$ such that $W + W \subset U$. Since $V$ is compact, there exist elements $x_i \in V$ ($i = 1, \ldots, k$) satisfying $V \subset \bigcup_{i=1}^k (x_i + W)$, and there exists $\lambda \in K$, $\lambda \neq 0$, such that $\lambda x_i \in W$ for all $i$, and $|\lambda| \leq 1$. There exists $n \in \mathbb{N}$ for which $|\lambda_n| \leq |\lambda|$, and

$$\lambda_n V \subset \lambda V \subset \bigcup_{i=1}^k (\lambda x_i + \lambda W) \subset W + W \subset U$$

shows that $\lambda_n V \subset U$. Thus $\{\lambda_n V\}$ is a 0-neighborhood base. Since $V$ is compact, given a circled 0-neighborhood $W$, there exist $y_1, \ldots, y_m \in V$ such that $V \subset \bigcup (y_j + (1/2)W)$ (or an appropriate scalar). The subspace $M$ spanned by $\{y_1, \ldots, y_m\}$ is finite-dimensional. We claim $L = M$. If not, let $\phi: L \to L/M$ be the quotient map. Since $V$ is compact and $\phi$ is continuous, $\phi(V)$ is compact in $L/M$. But $M$ finite-dimensional implies $L/M$ is Hausdorff (infinite-dimensional), and the scaling argument would produce a contradiction to compactness. Therefore $L = M$, and $L$ is finite-dimensional.
