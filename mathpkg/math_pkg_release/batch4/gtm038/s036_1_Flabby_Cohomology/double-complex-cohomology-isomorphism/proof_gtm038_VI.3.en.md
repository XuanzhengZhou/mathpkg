---
role: proof
locale: en
of_concept: double-complex-cohomology-isomorphism
source_book: gtm038
source_chapter: "VI"
source_section: "3"
---
**1.** $Z_{0j} = \{\xi \in C_{0j}: d'\xi = 0 \text{ and } d''\xi = 0\}$
$$= \{\xi \in C_{0j}: \text{There is an } \eta \in A^j \text{ with } d'_j\eta = \xi \text{ and } d'_{j+1}(d\eta) = 0\}$$
$$= \{\xi \in C_{0j}: \text{There is an } \eta \in A^j \text{ with } d'_j\eta = \xi \text{ and } d\eta = 0\} = d'_j(Z^j(A^{\bullet})).$$

Since $(A^j, d'_j, C_{\bullet j})$ is an augmented cochain complex, $d'_j$ is injective. Hence $d'_j$ gives an isomorphism $Z^j(A^{\bullet}) \simeq Z_{0j}$.

**2.** $B_{0j} = \{d''\xi: \xi \in C_{0,j-1} \text{ with } d'\xi = 0\}$. Using the augmented complex property, each such $\xi$ is of the form $d'_{j-1}\eta$ with $\eta \in A^{j-1}$. Then $d''\xi = d''d'_{j-1}\eta = d'_j(d\eta)$. Hence $B_{0j} = d'_j(B^j(A^{\bullet}))$.

It follows that $d'_j$ induces an isomorphism $H^j(A^{\bullet}) \xrightarrow{\sim} H_{0j}$. The proof for $H^i(B^{\bullet}) \simeq H_{i0}$ is analogous.
