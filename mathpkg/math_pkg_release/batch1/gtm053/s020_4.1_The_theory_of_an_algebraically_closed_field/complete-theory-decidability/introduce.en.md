---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This proposition provides a fundamental link between model-theoretic completeness and computability: if a first-order theory is complete and its axioms can be recursively enumerated, then the theory is decidable. The proof is simple and effective: one enumerates all consequences of the axioms (which is possible because proofs are finite and can be generated algorithmically), and by completeness, for any sentence $P$, eventually either $P$ or $\neg P$ appears in the enumeration. This argument applies directly to $\text{ACF}_p$ and $\text{RCF}$, establishing their decidability.
