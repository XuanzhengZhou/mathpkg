---
role: proof
locale: en
of_concept: disjoint-disk-pair-isotopy
source_book: gtm033
source_chapter: "8"
source_section: "3"
---

# Proof of Theorem 3.2 (Isotopy of Disjoint Disk Embeddings)

Let $M$ be a connected $n$-manifold without boundary. Suppose that $f_i, g_i: D^n \rightarrow M$ ($i = 1, 2$) are embeddings such that

$$f_1(D^n) \cap f_2(D^n) = \varnothing = g_1(D^n) \cap g_2(D^n).$$

If $M$ is orientable suppose further that $f_i$ and $g_i$ both preserve, or both reverse, orientation. Then there is an isotopy of $M$ carrying $f_1, f_2$ to $g_1, g_2$ respectively.

**Proof.** An argument similar to the proof of Theorem 3.1 applies to embeddings of a disjoint union of disks. One first isotops the centers of the disks to agree (using ambient isotopy from Theorem 1.3 and the connectedness of $M$ minus the image of one disk). Then one uses the standard linear isotopy in coordinate charts around each center, taking care that the disks remain disjoint throughout — this is possible because the disks can be shrunk radially to sufficiently small neighborhoods of their centers. The orientation condition ensures the linear parts lie in the same component of $\mathrm{GL}(n)$, and a smooth path in $\mathrm{GL}(n)$ completes the isotopy. $\square$
