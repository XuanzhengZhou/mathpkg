---
role: proof
locale: en
of_concept: closure-properties-of-analytic-sets
source_book: gtm038
source_chapter: "III"
source_section: "6. Analytic Sets"
---

**Proof.**

1. $\varnothing = \{\mathfrak{z} \in G: 1 = 0\}$, $G = \{\mathfrak{z} \in G: 0 = 0\}$.

2. Let $\mathfrak{z}_0 \in M := \bigcup_{i=1}^{\ell} M_i$. Then there exists an open neighborhood $U(\mathfrak{z}_0) \subset G$ and holomorphic functions $f_{i,j}, j = 1, \ldots, d_i$ such that
$$M_i \cap U = \{\mathfrak{z} \in U: f_{i,1}(\mathfrak{z}) = \cdots = f_{i,d_i}(\mathfrak{z}) = 0\}.$$
Let $f_{(j_1, \ldots, j_\ell)} := f_{1,j_1} \cdots f_{\ell,j_\ell}$. Then
$$M \cap U = \{\mathfrak{z} \in U: f_{(j_1, \ldots, j_\ell)}(\mathfrak{z}) = 0 \text{ for all indices } (j_1, \ldots, j_\ell)\}.$$

3. Let $\mathfrak{z}_0 \in M' := \bigcap_{i=1}^{\ell} M_i$. Then
$$U \cap M' = \{\mathfrak{z} \in U: f_{i,j}(\mathfrak{z}) = 0 \text{ for } i = 1, \ldots, \ell, j = 1, \ldots, d_i\}.$$

4. For an arbitrary intersection, the local defining functions at each point are the union of the defining functions for each $M_i$, which remains a finite collection due to the local finiteness property of analytic sets.
