---
role: proof
locale: en
of_concept: maclane-planarity-equivalence
source_book: gtm054
source_chapter: "E"
source_section: "11"
---

We give a heuristic proof, as presented in the text.

Consider first the case where $\Gamma$ is an arbitrary biconnected multigraph and, by our definition, planar. Let $Z_1, \ldots, Z_k$ be the regions of a planar imbedding of $\Gamma$. By B3 and E9, $Z_1, \ldots, Z_k$ are all elementary. Hence $\Gamma_i$, defined to be $\Gamma_{Z_i}$, is an elementary circuit of $\Gamma$. Let $D_i$ be a topological disk whose boundary is a topological realization of $\Gamma_i$. Identifying these disks along common boundary segments yields a topological realization of $\Gamma$ as a graph embedded in the plane (or sphere). This shows that combinatorial planarity implies topological planarity.

The converse direction — that a topologically planar multigraph admits a combinatorial planar imbedding — follows by taking the boundaries of the topological regions to obtain the cycles $Z_1, \ldots, Z_k$ that form a planar imbedding. The sum of all region boundaries equals the empty set (each edge appears twice with opposite orientations), and every edge not on the outer boundary appears in exactly two regions. These properties verify the axioms of a combinatorial planar imbedding.
