---
role: proof
locale: en
of_concept: matrix-transpose-is-anti-isomorphism
source_book: gtm030
source_chapter: "III"
source_section: "9"
---

*Proof.* Let $(a) = (a_{ij})$ and $(b) = (b_{ij})$ be elements of $\Re_n$. Clearly $(a) + (b) = (a_{ij} + b_{ij})$, and $[(a) + (b)]'$ has the element $a_{ji} + b_{ji}$ in its $(i,j)$-position. Hence
$$[(a) + (b)]' = (a)' + (b)'.$$

Next, let $(p) = (a)(b)$ be the matrix product. The $(i,j)$-element of $(p)$ is
$$p_{ij} = \sum_{k} a_{ik} b_{kj},$$
so the $(i,j)$-element of $(p)'$ is
$$p_{ji} = \sum_{k} a_{jk} b_{ki}.$$

On the other hand, the $(i,j)$-element of $(b)'(a)'$ is
$$\sum_{k} b_{ki} a_{jk}.$$

Since $\Re$ is commutative, $a_{jk} b_{ki} = b_{ki} a_{jk}$, and therefore
$$[(a)(b)]' = (b)'(a)'.$$

The mapping is clearly 1-1 and onto, hence it is an anti-isomorphism of $\Re_n$ onto itself.
