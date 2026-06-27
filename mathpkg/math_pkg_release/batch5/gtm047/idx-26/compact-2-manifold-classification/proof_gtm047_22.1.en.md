---
role: proof
locale: en
of_concept: compact-2-manifold-classification
source_book: gtm047
source_chapter: "22"
source_section: "1"
---

The proof proceeds by simplifying the $2$-cell with strips representation from Theorem 3.

First, apply the Lemma to arrange all twisted strips so their attachments lie in a single arc on $\operatorname{Bd} D$, disjoint from annular strips.

If there are annular strips, they must come in linked pairs on $\operatorname{Bd} D$. Each linked pair of annular strips, together with part of $D$, forms a handle when a $2$-cell is added (the dotted arcs in Figure 22.9). This produces $h$ handles from $h$ linked pairs of annular strips.

For twisted strips, let $m$ be their number. If $m > 2$, consider the first three twisted strips. By applying Operation $\alpha$ twice and an additional operation $\beta$, two of the three twisted strips become annular (forming a handle), while the third remains twisted. This reduces $m$ by $2$ while increasing $h$ by $1$. Repeating, we can assume $m \leqslant 2$.

After all simplifications, the remaining region $N = \operatorname{Cl}[M - (\bigcup H_i \cup \bigcup B_j)]$ is the union of two $2$-cells whose boundary arcs match in cyclic order, so $N$ is a sphere with holes. Adding the handles $H_i$ (each an annulus) and cross-caps $B_j$ (each a M\"obius band with disk removed) yields a $2$-sphere with $h$ handles and $m$ cross-caps.

The orientability condition follows because handles are orientable and cross-caps are non-orientable; $m=0$ means no cross-caps, hence orientable. $\square$
