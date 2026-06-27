---
role: proof
locale: en
of_concept: pl-approximation-of-paths-in-r3
source_book: gtm047
source_chapter: "14"
source_section: "14"
---

**Proof.** Given a continuous path $p: [0,1] \to U$, one constructs a sufficiently fine simplicial approximation. Since $U$ is open in $\mathbb{R}^3$, the image $p([0,1])$ is compact and has positive distance from the complement $\mathbb{R}^3 \setminus U$. Choose a triangulation of $[0,1]$ fine enough so that the image of each subinterval under $p$ has diameter less than this distance. Construct a PL path $p'$ by linearly interpolating between the images of the subdivision points within $U$. The straight-line homotopy between $p$ and $p'$ stays within $U$ by the choice of subdivision, providing a based homotopy $p \cong p'$.
