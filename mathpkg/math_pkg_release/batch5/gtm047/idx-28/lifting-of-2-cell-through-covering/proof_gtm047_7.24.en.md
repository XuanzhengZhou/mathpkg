---
role: proof
locale: en
of_concept: lifting-of-2-cell-through-covering
source_book: gtm047
source_chapter: "7"
source_section: "24"
---

**Proof.** (1) Let $U$ and $\{\tilde{U}_i\}$ be as in the definition of a covering, and let $\hat{U}_k$ be the set $\tilde{U}_i$ that contains $\tilde{P}_0$. Suppose that $f(\Delta) \subset U$. Then the desired $\tilde{f}$ exists: we use $f$ followed by $(g | \tilde{U}_k)^{-1}$. Since $\tilde{f}(\Delta)$ must be connected, $\tilde{f}$ is unique.

(2) We shall show that the theorem reduces to the case described in (1). Let $K$ be a triangulation of $\Delta$, sufficiently fine so that if $\sigma^2 \in K$, then $f(\sigma^2)$ lies in a single set $U$ as in Case (1). Let $\sigma_0^2$ be a simplex of $K$ that contains $P_0 = f(Q_0)$. If $\sigma_0^2 = |K|$, we have Case (1). If not, it follows by Theorem 17.2 that $K$ has a free 2-simplex $\sigma_1^2 \neq \sigma_0^2$. (Or see the proof of Theorem 3.3.) Suppose that $f| \text{Cl} (\Delta - \sigma_1^2)$ has a unique lifting $\tilde{f}_1$ of the desired sort. Let $A = \sigma_1^2 \cap \text{Cl} (\Delta - \sigma_1^2)$, so that $A$ is connected. Then $\tilde{f}_1 | A$ is defined, and $\tilde{f}_1(A) \subset \tilde{U}_k$ for some $k$. Since $f(\sigma_1^2) \subset U$, the lifting can be extended over $\sigma_1^2$, uniquely, by the method of Case (1). Repeating the process, we get a lifting defined on all of $\Delta$.
