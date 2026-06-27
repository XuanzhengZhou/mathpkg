---
role: proof
locale: en
of_concept: matrix-of-composition
source_book: gtm049
source_chapter: "IV"
source_section: "4.3"
---

If $u_i f = \sum_{j=1}^{n} a_{ij} v_j$ and $v_j g = \sum_{k=1}^{p} b_{jk} w_k$, then
$$
u_i(fg) = (u_i f)g = \left(\sum_{j=1}^{n} a_{ij} v_j\right) g = \sum_{j=1}^{n} a_{ij} (v_j g) = \sum_{j=1}^{n} a_{ij} \sum_{k=1}^{p} b_{jk} w_k = \sum_{k=1}^{p} \left(\sum_{j=1}^{n} a_{ij} b_{jk}\right) w_k = \sum_{k=1}^{p} c_{ik} w_k,
$$
where $c_{ik} = \sum_{j=1}^{n} a_{ij} b_{jk}$. Thus $(c_{ik})$ is precisely the matrix product of $(a_{ij})$ and $(b_{jk})$, and it equals the matrix of $fg$.
