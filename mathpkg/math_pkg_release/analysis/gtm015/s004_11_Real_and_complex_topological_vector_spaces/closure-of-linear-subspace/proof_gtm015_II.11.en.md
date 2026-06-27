---
role: proof
locale: en
of_concept: closure-of-linear-subspace
source_book: gtm015
source_chapter: "Chapter 2 – Topological Vector Spaces"
source_section: "11. Real and complex topological vector spaces"
---

# Proof of Closure of a Linear Subspace is a Linear Subspace

**Theorem (11.7).** In a TVS, the closure of a linear subspace is a linear subspace.

*Proof.* If $M$ is a linear subspace of a TVS $E$ over $\mathbb{K}$, then the continuous mapping $(x, y) \mapsto x + y$, which maps $M \times M$ into $M$, also maps $(M \times M)^{-} = \overline{M} \times \overline{M}$ into $\overline{M}$, thus $x + y \in \overline{M}$ whenever $x, y \in \overline{M}$. Similarly, the continuous mapping $(\lambda, x) \mapsto \lambda x$, which maps $\mathbb{K} \times M$ into $M$, also maps $(\mathbb{K} \times M)^{-} = \mathbb{K} \times \overline{M}$ into $\overline{M}$; that is, $\lambda x \in \overline{M}$ for all $\lambda \in \mathbb{K}$ and $x \in \overline{M}$. Hence $\overline{M}$ is a linear subspace. $\square$
