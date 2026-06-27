---
role: proof
locale: en
of_concept: indecomposable-serial-ring-structure
source_book: gtm013
source_chapter: "8"
source_section: "23"
---

The proof relies on the structure theory of serial rings developed by Nakayama, Kupisch, and others. For an indecomposable serial ring $R$ with basic set of primitive idempotents $e_1, \ldots, e_n$, one considers the Cartan invariants $c_{ij}$ which count the composition factors. The key observation is that the basic ring of $R$ is isomorphic to a factor of a block upper triangular matrix ring $\mathbb{UTM}_{(m_1,\ldots,m_n)}(D)$ where $D \cong e_i R e_i / e_i J e_i$ is the common division ring of $R$ (since $R$ is indecomposable serial, all simple modules have the same endomorphism division ring).

When $c_1 = 1$, the epimorphism from the block upper triangular matrix ring onto $R$ has a nontrivial kernel, giving a proper homomorphic image. When $c_1 = i$, the kernel vanishes and the map is an isomorphism. The mapping is constructed by sending the matrix units of the block upper triangular matrix ring to the appropriate homomorphisms between indecomposable projective modules $R e_i$, using the Kupisch series structure of serial rings.
