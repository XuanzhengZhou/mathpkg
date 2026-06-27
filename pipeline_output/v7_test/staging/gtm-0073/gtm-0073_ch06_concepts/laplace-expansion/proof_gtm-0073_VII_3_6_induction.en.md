---
role: proof
source_book: gtm-0073
chapter: VII
section: "VII.3"
proof_technique: induction
locale: en
content_hash: ""
written_against: ""
---
Fix $j$ and prove the column expansion. It suffices to show that the map $\phi : \operatorname{Mat}_n R \to R$ given by $\phi(A) = \sum_{i=1}^{n} (-1)^{i+j} a_{ij} |A_{ij}|$ is an alternating $R$-multilinear form with $\phi(I_n) = 1_R$, then uniqueness (Theorem 3.3) gives $\phi = d$.

To verify the alternating property: if rows $k$ and $t$ are equal ($k < t$), then $|A_{ij}| = 0$ for $i \neq k, t$ (determinant with repeated rows). The remaining two terms are $(-1)^{k+j}|A_{kj}| + (-1)^{t+j}|A_{tj}|$. Since $A_{kj}$ is obtained from $A_{tj}$ by successively interchanging row $t$ with rows $t-1, \ldots, k+1$, we have $|A_{kj}| = (-1)^{t-k-1}|A_{tj}|$. Thus the sum vanishes. Multilinearity follows similarly from multilinearity of the minors. The row expansion is proved analogously.
