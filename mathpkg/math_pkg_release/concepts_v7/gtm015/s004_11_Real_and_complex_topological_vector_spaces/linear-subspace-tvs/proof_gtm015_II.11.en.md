---
role: proof
locale: en
of_concept: linear-subspace-tvs
source_book: gtm015
source_chapter: "Chapter 2 – Topological Vector Spaces"
source_section: "11. Real and complex topological vector spaces"
---

# Proof of Linear Subspace Inherits TVS Structure

**Theorem (11.6).** If $E$ is a TVS over $\mathbb{K}$ and $M$ is a linear subspace of $E$, then $M$, with the relative topology, is also a TVS over $\mathbb{K}$.

*Proof.* The restrictions of the continuous mappings $(x, y) \mapsto x + y$ and $(\lambda, x) \mapsto \lambda x$, to $M \times M$ and $\mathbb{K} \times M$, respectively, are continuous for the relative topology of $M$. Indeed, a mapping into a subspace is continuous for the relative topology if and only if it is continuous as a mapping into the ambient space; the restrictions coincide, as mappings into $E$, with the original operations composed with the inclusion $M \hookrightarrow E$, hence are continuous. $\square$
