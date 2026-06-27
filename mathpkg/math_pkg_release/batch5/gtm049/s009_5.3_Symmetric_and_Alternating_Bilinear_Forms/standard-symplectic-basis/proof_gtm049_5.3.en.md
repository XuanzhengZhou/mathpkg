---
role: proof
locale: en
of_concept: standard-symplectic-basis
source_book: gtm049
source_chapter: "5"
source_section: "5.3"
---

**PROOF.** By Theorem 2, $V = L_1 \oplus \cdots \oplus L_s \oplus V^\perp$ where each $L_i$ is a 2-dimensional non-degenerate alternating subspace. Each $L_i$ has an ordered basis $(b_i, c_i)$ such that $\sigma(b_i, c_i) = x_i \neq 0$. Replacing $c_i$ by $(1/x_i)c_i$, the restriction of $\sigma$ to $L_i$ has matrix $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ with respect to $(b_i, (1/x_i)c_i)$. Choosing any basis for $V^\perp$ (where $\sigma$ is identically zero) and concatenating yields the desired ordered basis. The resulting matrix has $s$ diagonal $2 \times 2$ blocks $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ and zeros elsewhere; the rank is $2s$.
