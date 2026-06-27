---
role: proof
locale: en
of_concept: locally-compact-hausdorff-tvs-is-finite-dimensional
source_book: gtm003
source_chapter: "1"
source_section: "3.6"
---

By (3.1) every one-dimensional subspace of $L$ is complete, hence closed in $L$ and therefore locally compact; it follows that $K$ is locally compact.

Now let $V$ be a compact, circled $0$-neighborhood in $L$, and let $\{\lambda_n\}$ be a null sequence in $K$ consisting of non-zero terms. We show first that $\{\lambda_n V: n \in \mathbb{N}\}$ is a neighborhood base of $0$ in $L$.

Given a $0$-neighborhood $U$, choose a circled $0$-neighborhood $W$ such that $W + W \subset U$. Since $V$ is compact, there exist elements $x_i \in V$ ($i = 1, \ldots, k$) satisfying
$$V \subset \bigcup_{i=1}^{k} (x_i + W),$$
and there exists $\lambda \in K$, $\lambda \neq 0$, such that $\lambda x_i \in W$ for all $i$, and $|\lambda| \leq 1$. There exists $n \in \mathbb{N}$ for which $|\lambda_n| \leq |\lambda|$, and
$$\lambda_n V \subset \lambda V \subset \bigcup_{i=1}^{k} (\lambda x_i + \lambda W) \subset W + W \subset U.$$

This shows that $\{\lambda_n V\}$ is a neighborhood base at $0$ in $L$. Since $V$ is compact, it is precompact; thus for any $0$-neighborhood $U$, there exists a finite set $F \subset L$ such that $V \subset F + U$. Consequently, $L = \bigcup_{n} \lambda_n^{-1} V$ can be covered by finitely many translates of any given $0$-neighborhood. Hence $L$ is precompact, and since $L$ is complete (being locally compact and Hausdorff), $L$ must be finite-dimensional. More precisely, if $L$ were infinite-dimensional, one could construct an infinite linearly independent set and the precompactness would be contradicted via Riesz's lemma.
