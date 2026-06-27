---
role: proof
locale: en
of_concept: torsion-free-group-ring
source_book: gtm059
source_chapter: "3"
source_section: "3. Cyclotomic Units as a Universal Distribution"
---

The embedding of $V_k$ into $V_k^*$ corresponds to an embedding of group rings $\mathbb{Z}[Z_k] \hookrightarrow \mathbb{Z}[Z_k^*]$, which sends an element corresponding to $e_k \in Z_k$ to the sum over all $w_k \in Z_k^*$ that project onto $e_k$ under the canonical map $w_k \mapsto w_k^*$.

Suppose an element
$$
\sum a_{w_k} [w_k] \in \mathbb{Z}[Z_k]
$$
is a torsion element. Under the embedding and projection, the coefficients $a_{w_k}$ for different $w_k$ projecting to the same element must be equal. Hence the element already lies in the image of $\mathbb{Z}[Z_k]$, which is torsion-free. Therefore $\mathbb{Z}[Z_k]$ itself has no torsion.
