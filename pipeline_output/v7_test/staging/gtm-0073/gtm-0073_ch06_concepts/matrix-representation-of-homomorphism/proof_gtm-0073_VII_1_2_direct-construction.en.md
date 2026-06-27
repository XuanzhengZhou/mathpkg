---
role: proof
source_book: gtm-0073
chapter: VII
section: "VII.1"
proof_technique: direct-construction
locale: en
content_hash: ""
written_against: ""
---
Let $\{u_1, \ldots, u_n\}$ be a basis of $E$, $\{v_1, \ldots, v_m\}$ a basis of $F$ and $f \in \operatorname{Hom}_R(E,F)$. There are elements $r_{ij}$ of $R$ such that
\[
f(u_i) = \sum_{j=1}^{m} r_{ij} v_j \quad (i = 1, \ldots, n).
\]
The $r_{ij}$ are uniquely determined since $\{v_1, \ldots, v_m\}$ is a basis of $F$. Define $\beta : \operatorname{Hom}_R(E,F) \to M$ by $f \mapsto (r_{ij})$. Verification: $\beta$ is an additive homomorphism. If $\beta(f) = 0$, then $f(u_i) = 0$ for every basis element $u_i$, whence $f = 0$; thus $\beta$ is a monomorphism. Given a matrix $(r_{ij}) \in M$, define $f: E \to F$ by $f(u_i) = \sum_{j=1}^{m} r_{ij} v_j$ and extend linearly. Then $\beta(f) = (r_{ij})$, so $\beta$ is surjective. If $R$ is commutative, $\beta$ respects scalar multiplication.
