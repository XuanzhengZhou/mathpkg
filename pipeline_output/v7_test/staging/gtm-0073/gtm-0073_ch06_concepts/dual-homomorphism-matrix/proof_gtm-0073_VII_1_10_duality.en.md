---
role: proof
source_book: gtm-0073
chapter: VII
section: "VII.1"
proof_technique: duality
locale: en
content_hash: ""
written_against: ""
---
Recall that the dual basis $V^* = \{v_1^*, \ldots, v_m^*\}$ of $F^* = \operatorname{Hom}_R(F,R)$ is determined by $v_i^*(v_j) = \delta_{ij}$. If $f(u_i) = \sum_k r_{ik} v_k$, then $\bar{f}(v_j^*)(u_i) = v_j^*(f(u_i)) = r_{ij}$, so $\bar{f}(v_j^*) = \sum_i r_{ij} u_i^*$. Thus the matrix of $\bar{f}$ relative to $V^*$ and $U^*$ has $(j,i)$-entry $r_{ij}$, which is precisely the same matrix $A$ (using the right-module convention where coefficients of $f(u_j)$ form the $j$th column).
