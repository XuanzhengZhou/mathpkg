---
role: proof
source_book: gtm-0073
chapter: VII
section: "VII.3"
proof_technique: adjugate
locale: en
content_hash: ""
written_against: ""
---
The system $AX = B$ (where $X = (x_1, \ldots, x_n)^t$, $B = (b_1, \ldots, b_n)^t$) has a unique solution $X = A^{-1}B$ when $|A| \neq 0$ (Proposition 3.7). Substitute $A^{-1} = |A|^{-1} A^0$ to obtain $X = |A|^{-1} A^0 B$. The $j$th component is $x_j = |A|^{-1} \sum_{i=1}^{n} (A^0)_{ji} b_i = |A|^{-1} \sum_{i=1}^{n} (-1)^{i+j} b_i |A_{ij}|$.
