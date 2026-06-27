---
role: proof
locale: en
of_concept: isbell-example-no-adjoint
source_book: gtm026
source_chapter: "2"
source_section: "2.28"
---

Let $I$ be the proper class of all cardinals and consider the functor $U$ defined as follows. For each group $G$, let $U(G)$ be the set of all families $(H_i)_{i \in I}$ where each $H_i$ is a subgroup of $G$. For a group homomorphism $f: G \to G'$, define $U(f)$ by sending $(H_i)$ to $(f(H_i))$. One verifies that $U$ preserves all limits (essentially because limits in the category of groups are computed on underlying sets, and $U$ is defined via image operations that commute with limits).

However, $U$ does not satisfy the solution set condition. If $U$ had a left adjoint $F$, then for the singleton set $1$, the free group $F(1)$ would need to encode a universal family of subgroups, which would require bounding the cardinality of subgroups uniformly across all groups — an impossibility since there exist groups of arbitrarily large cardinality with arbitrarily large systems of subgroups. Therefore the solution set condition fails, and $U$ has no left adjoint despite preserving all limits.
