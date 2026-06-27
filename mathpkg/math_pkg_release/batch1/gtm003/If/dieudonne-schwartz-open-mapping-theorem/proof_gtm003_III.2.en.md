---
role: proof
locale: en
of_concept: dieudonne-schwartz-open-mapping-theorem
source_book: gtm003
source_chapter: "III"
source_section: "2"
---

Let $E = \varinjlim_n E_n$ be an (LF)-space (strict inductive limit of Fréchet spaces $E_n$) and let $F = \varinjlim_n F_n$ be an (LF)-space. The case where $F$ is a Fréchet space is subsumed by letting $F_n = F$ for all $n \in \mathbb{N}$.

For all $m, n \in \mathbb{N}$, set $G_{m,n} = E_m \cap u^{-1}(F_n)$. As a closed subspace of the Fréchet space $E_m$, each $G_{m,n}$ is complete and metrizable.

Since $u(E) = F$, for each $n$ there exists $m$ such that $u(E_m) \supset F_n$. The restriction $u|_{G_{m,n}}: G_{m,n} \to F_n$ is a continuous linear map between complete metrizable spaces with dense range (in a suitable topology). By Theorem 2.1, either the range is meager or the map is a topological homomorphism.

By a Baire category argument on the inductive limit, one shows that $u$ must be a topological homomorphism: if it were not open, its restriction would have meager range for some $m, n$, contradicting the surjectivity condition and the Baire property of $F$.
