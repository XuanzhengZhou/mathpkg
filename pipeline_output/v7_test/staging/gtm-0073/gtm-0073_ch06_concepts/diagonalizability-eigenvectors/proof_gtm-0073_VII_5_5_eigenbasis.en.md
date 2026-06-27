---
role: proof
source_book: gtm-0073
chapter: VII
section: "VII.5"
proof_technique: eigenbasis
locale: en
content_hash: ""
written_against: ""
---
By Theorem IV.2.5, the eigenvectors of $\phi$ span $E$ if and only if $E$ has a basis consisting of eigenvectors. Clearly $U = \{u_1, \ldots, u_n\}$ is a basis of eigenvectors with corresponding eigenvalues $k_1, \ldots, k_n \in K$ if and only if the matrix of $\phi$ relative to $U$ is the diagonal matrix $D$ with main diagonal $k_1, k_2, \ldots, k_n$.

For the multiplicity claim: suppose $v = \sum_i r_i u_i$ is an eigenvector with $\phi(v) = kv$. Since $U$ is linearly independent and $\sum_i k r_i u_i = kv = \phi(v) = \sum_i r_i \phi(u_i) = \sum_i r_i k_i u_i$, we have $k r_i = r_i k_i$ for all $i$. Thus for each $i$ with $r_i \neq 0$, $k = k_i$. Therefore each eigenvalue appears on the diagonal exactly $\dim_K C(\phi, k)$ times (the number of basis vectors with that eigenvalue).
