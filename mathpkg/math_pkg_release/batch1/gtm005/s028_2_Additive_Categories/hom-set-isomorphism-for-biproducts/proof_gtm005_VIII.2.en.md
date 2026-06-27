---
role: proof
locale: en
of_concept: hom-set-isomorphism-for-biproducts
source_book: gtm005
source_chapter: "VIII. Abelian Categories"
source_section: "2. Additive Categories"
---

The isomorphism follows by iterating the binary case. For binary biproducts, the proof in the biproduct characterization theorem established the isomorphism $A(d, c) \cong A(d, a) \oplus A(d, b)$ via the map $h \mapsto \langle p_1 h, p_2 h \rangle$.

For the general case, given objects $c_1, \ldots, c_m$ and $a_1, \ldots, a_n$, each arrow $f : \bigoplus_k c_k \to \bigoplus_j a_j$ determines components $f_{jk} = p_j f i_k : c_k \to a_j$. Conversely, given a family of arrows $g_{jk} : c_k \to a_j$, one defines $g : \bigoplus_k c_k \to \bigoplus_j a_j$ by
$$
g = \sum_{j,k} i'_j \, g_{jk} \, p'_k,
$$
where $i'_j, p'_k$ are the injections and projections of the respective biproducts. The equations $p_j i'_j = 1$, $p_j i'_\ell = 0$ for $j \neq \ell$, and $\sum_j i'_j p'_j = 1$ guarantee that these constructions are mutually inverse, yielding the stated isomorphism of abelian groups. Composition then corresponds to matrix multiplication because
$$
(p_j (g \circ f) i_k) = \sum_\ell (p_j g i'_\ell)(p'_\ell f i_k).
$$
