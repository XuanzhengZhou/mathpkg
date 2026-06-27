---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Theorem 16.19 states that for any uniform Boolean-valued set $u$, the supremum $\sup(u)$ is always attained at some element $x \in \mathcal{D}(u)$. The proof is a clever partition-of-unity argument: enumerate $\mathcal{D}(u) = \{x_\xi\}$ and define $b_\xi = u(x_\xi) \cdot \prod_{\eta < \xi} \neg u(x_\eta)$. The $b_\xi$ are disjoint and their sum is $\sup(u)$. Using the completeness of $\mathcal{D}(u)$ and the partition-of-unity, one constructs an element $x$ that "mixes" the $x_\xi$ with weights $b_\xi$, and shows $u(x) = \sup(u)$. This theorem is a key step toward the decomposition theorem.
