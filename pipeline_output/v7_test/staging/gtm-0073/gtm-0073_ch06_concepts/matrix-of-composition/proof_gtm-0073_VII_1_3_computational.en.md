---
role: proof
source_book: gtm-0073
chapter: VII
section: "VII.1"
proof_technique: computational
locale: en
content_hash: ""
written_against: ""
---
Let $A = (r_{ij})$ and $B = (s_{kj})$. For each $i = 1,2,\ldots,n$:
\[
gf(u_i) = g\left( \sum_{k=1}^{m} r_{ik} v_k \right) = \sum_{k=1}^{m} r_{ik} \left( \sum_{j=1}^{p} s_{kj} w_j \right) = \sum_{j=1}^{p} \left( \sum_{k=1}^{m} r_{ik} s_{kj} \right) w_j.
\]
The $i$-$j$th entry of the matrix of $gf$ is $\sum_{k=1}^{m} r_{ik} s_{kj}$, which is precisely the $i$-$j$th entry of the matrix product $AB$.
