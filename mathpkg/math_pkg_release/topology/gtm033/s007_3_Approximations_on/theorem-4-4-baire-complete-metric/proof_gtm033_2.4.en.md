---
role: proof
locale: en
of_concept: theorem-4-4-baire-complete-metric
source_book: gtm033
source_chapter: "2"
source_section: "4. Weak and Strong Topologies on Function Spaces"
---

# Proof of Theorem 4.4: Complete Metric and Baire Property for $C^r$ Function Spaces

**Theorem 4.4.** (a) $C^r_W(M,N)$ has a complete metric;
(b) Every weakly closed subspace of $C^r_S(M,N)$ is a Baire space (in the strong topology).

*Proof.* Recall the $r$-jet prolongation map

$$j^r: C^r(M,N) \rightarrow C^0(M, J^r(M,N)).$$

This map is a homeomorphism onto a weakly closed subspace when $C^r(M,N)$ is given the weak or strong topology and $C^0(M, J^r(M,N))$ the corresponding topology. The result then follows directly from Theorems 4.1, 4.2, and 4.3:

- Theorem 4.1 gives a complete metric on $C^0_W(M, J^r(M,N))$, which restricts to a complete metric on the closed subspace $j^r(C^r_W(M,N)) \cong C^r_W(M,N)$. This proves (a).
- Theorem 4.3 (or the Corollary stated after 4.1) shows that weakly closed subsets of $C^0_S(M, J^r(M,N))$ are Baire spaces. Since $j^r(C^r_S(M,N))$ is weakly closed in $C^0_S(M, J^r(M,N))$, any weakly closed subset of $C^r_S(M,N)$ corresponds to a weakly closed subset and hence is Baire. This proves (b).

QED
