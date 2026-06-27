---
role: proof
locale: en
of_concept: "let-be-a-signed-measure-on-a-measurable"
source_book: gtm025
source_chapter: "Complex Analysis"
source_section: "19.3"
---

To prove (i), observe that $v(E) = v(F) + v(E \cap F')$. In order that $v(E)$ be finite, it is necessary and sufficient that both summands on the right side be finite. Conclusions (ii) and (iii) are proved by repeating verbatim the proofs of (10.13) and (10

$F_2 \in \mathcal{A}$ such that $F_2 \subset E \cap F_1'$ and $\nu(F_2) < -\frac{1}{n_2}$. Then

$$\nu(E \cap (F_1 \cup F_2')) = \nu(E) - \nu(F_1) - \nu(F_2) > 0,$$

and so $E \cap (F_1 \cup F_2')$ is not a nonnegative set for $\nu$. Continuing this process, we obtain a sequence $(n_k)_{k=1}^{\infty}$ of minimal positive integers and a corresponding pairwise disjoint sequence $(F_k)_{k=1}^{\infty}$ of sets in $\mathcal{A}$ such that $\nu(F_k) < -\frac{1}{n_k}$ for each $k \in N$. Let $F = \bigcup_{k=1}^{\infty} F_k$. Then we have

$$\infty > \nu(E \cap F') = \nu(E) - \nu(F) = \nu(E) - \sum_{k=1}^{\infty} \nu(F_k) > \nu(E) + \sum_{k=1}^{\infty} \frac{1}{n_k} > 0.$$

Thus $\sum_{k=1}^{\infty} \frac{1}{n_k} < \infty$ and $E \cap F'$ is not a nonnegative set for $\nu$. Choose $A \in \mathcal{A}$ such that $A \subset E \cap F'$ and $\nu(A) < 0$, and then choose $k$ so large that $\nu(A) < -\frac{1}{n_k}$ and $n_k > 2$. Now

$$A \cup F_k \subset E \cap \bigcup_{j=1}^{k-1} F_j'$$

and

$$\nu(A \cup F_k) = \nu(A) + \nu(F_k) < -\frac{1}{n_k} - \frac{1}{n_k} < -\frac{1}{n_k-1}.$$

This contradicts the minimality of $n_k$. We conclude that a set $S$ of the required sort exists. $\square$

(19

To prove our uniqueness assertion, suppose that $(P_1, P_1')$ and $(P_2, P_2')$ are two Hahn decompositions of $X$ for $\nu$, and select $E \in \mathcal{A}$. Since $E \cap P_1 \cap P_2'$ is a subset of both $P_1$ and $P_2'$, we have $\nu(E \cap P_1 \cap P_2') = 0$; similarly $\nu(E \cap P_1' \cap P_2) = 0$. Thus we have $\nu(E \cap P_1) = \nu(E \cap (P_1 \cup P_2)) = \nu(E \cap P_2)$ and $\nu(E \cap P_1') = \nu(E \cap (P_1' \cup P_2')) = \nu(E \cap P_2')$.
