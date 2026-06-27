---
role: proof
locale: en
of_concept: fixed-points-equal-fixed-lines
source_book: gtm006
source_chapter: "XIII"
source_section: "2"
---

Let $\mathcal{P}$ be a finite projective plane and let $A$ be an incidence matrix for $\mathcal{P}$. By Lemma 13.2, any collineation $\alpha$ can be represented by two permutation matrices $P = (p_{ij})$ and $Q = (q_{jk})$ with $PA = AQ$.

The entry $p_{ii} = 1$ if and only if $P_i^{\alpha} = P_i$, i.e., $P_i$ is a fixed point of $\alpha$. Therefore the number of fixed points of $\alpha$ is the trace of $P$:
$$
\operatorname{tr}(P) = \sum_i p_{ii}.
$$

Similarly, by the definition of $Q$, the number of fixed lines of $\alpha$ is the trace of $Q$:
$$
\operatorname{tr}(Q) = \sum_j q_{jj}.
$$

Since $PA = AQ$ and, by Theorem 3.14, the incidence matrix $A$ of a finite projective plane is non-singular, we can write $P = AQA^{-1}$. Therefore $P$ and $Q$ are conjugate matrices, so their traces are equal:
$$
\operatorname{tr}(P) = \operatorname{tr}(AQA^{-1}) = \operatorname{tr}(Q).
$$

Thus $\alpha$ has equally many fixed points and fixed lines.
