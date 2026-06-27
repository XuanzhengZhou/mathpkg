---
role: proof
locale: en
of_concept: comma-category-projection-preserves-monics
source_book: gtm005
source_chapter: "V. Limits"
source_section: "7. Subobjects and Generators"
---

Consider the projection functor $P: (x \downarrow G) \to A$ sending $\langle f: x \to Ga, a \rangle$ to $a$.

An arrow $h: \langle f', a' \rangle \to \langle f, a \rangle$ in $(x \downarrow G)$ is monic if and only if the underlying arrow $h: a' \to a$ in $A$ is monic. This is because the comma category inherits monics from $A$: the projection $P$ is faithful and reflects monics.

Alternatively, one can argue that the projection $P$ preserves all kernel pairs. For an arrow $u$ in $(x \downarrow G)$, its kernel pair is computed as the pullback of $u$ with itself. Since $G$ is continuous (it preserves, in particular, pullbacks), the projection $P$ preserves pullbacks (limits in $(x \downarrow G)$ are computed componentwise in $A$, with the structural arrow from $x$ induced by the universal property). In particular, the kernel pair of the identity $1_a$, which is just $(1_a, 1_a)$, is preserved by $P$, and this property implies that $P$ carries monics in $(x \downarrow G)$ to monics in $A$.

Thus the monics in $(x \downarrow G)$ correspond precisely to monics in $A$ under the projection $P$.
