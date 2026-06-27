---
role: proof
source_book: gtm-0073
chapter: VII
section: "VII.4"
proof_technique: block-concatenation
locale: en
content_hash: ""
written_against: ""
---
($\Rightarrow$) For each $i$, let $V_i$ be an ordered basis of $E_i$ such that $\phi|_{E_i}$ has matrix $M_i$ relative to $V_i$. Since $E = E_1 \oplus \cdots \oplus E_t$, the concatenation $V = \bigcup_{i=1}^{t} V_i$ (ordered with elements of $V_1$ first, then $V_2$, etc.) is a basis of $E$. The matrix of $\phi$ relative to $V$ is the block diagonal matrix $M$.

($\Leftarrow$) Suppose $U = \{u_1, \ldots, u_n\}$ is a basis of $E$ and $M$ is the matrix of $\phi$ relative to $U$, with diagonal blocks of sizes $n_1, \ldots, n_t$. Let $E_1$ be the span of $\{u_1, \ldots, u_{n_1}\}$, $E_2$ the span of $\{u_{n_1+1}, \ldots, u_{n_1+n_2}\}$, etc. Then $E = E_1 \oplus \cdots \oplus E_t$, each $E_i$ is $\phi$-invariant (since off-diagonal blocks are zero), and $M_i$ is the matrix of $\phi|_{E_i}$.
