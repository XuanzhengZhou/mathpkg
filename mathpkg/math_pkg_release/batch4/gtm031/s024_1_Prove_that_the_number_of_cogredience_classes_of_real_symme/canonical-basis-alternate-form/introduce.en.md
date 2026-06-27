---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Every non-degenerate alternate scalar product on a finite-dimensional vector space admits a canonical symplectic basis. The proof constructs pairs of vectors $(u_i, v_i)$ iteratively using a projection method: given $k$ pairs already found, define $E_k(x) = \sum_1^k g(x, v_i)u_i - \sum_1^k g(x, u_i)v_i$, which is a projection onto the span of the first $k$ pairs. One then restricts to the complementary subspace $(1 - E_k)\mathfrak{R}$ to find the next pair, continuing until the restricted form vanishes identically.
