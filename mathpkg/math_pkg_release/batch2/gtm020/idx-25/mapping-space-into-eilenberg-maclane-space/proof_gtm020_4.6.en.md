---
locale: en
of_concept: mapping-space-into-eilenberg-maclane-space
role: proof
source_book: gtm020
source_chapter: "4"
source_section: "4.6"
---

We give two proofs of this theorem. The first is by induction on $n$. The case $n = 0$ is clear since $K(\Pi, 0) = \Pi$ is a discrete space. Next we apply the inductive hypothesis for $n - 1$ to describe using (3.5) and (4.2). The connected components of $\text{Map}(X, Y)$ are indexed by $[X, Y]$ the homotopy classes of maps $X \rightarrow Y$

$$\text{Map}(X, K(\Pi, n)) = \prod_{[X, K(\Pi, n)]} B(\text{Map}(X, K(\Pi, n - 1)))$$

where each connected component is the classifying space

$$B(\text{Map}(X, K(\Pi, n - 1)))$$

of the gauge group of the $K(\Pi, n - 1)$ bundles over $X$. Now we use the inductive hypothesis to rewrite this expression for $\text{Map}(X, K(\Pi, n))$

$$\text{Map}(X, K(\Pi, n)) = K(H^n(X, \Pi), 0) \times B\left(\prod_{0 \leq p \leq n-1} K(H^{n-p-1}(X, \Pi), p)\right)$$

$$= \prod_{0 \leq q \leq n} K(H^{n-q}(X, \Pi), q) \quad \text{for } p + 1 = q.$$

This completes the inductive step and proves the theorem.

For another proof we start with the evaluation map $e(f) = f(*)$ at a base point $* \in X$.
