---
role: proof
locale: en
of_concept: compactification-partial-order
source_book: gtm027
source_chapter: "5"
source_section: "Compactification"
---

# Proof of Partial Ordering of Compactifications

**Theorem 22.** The collection of all compactifications of a topological space is partially ordered by $\geq$. If $(f, Y)$ and $(g, Z)$ are Hausdorff compactifications of a space and $(f, Y) \geq (g, Z) \geq (f, Y)$, then $(f, Y)$ and $(g, Z)$ are topologically equivalent.

Recall from the definition: a compactification of $X$ is a pair $(f, Y)$ where $Y$ is compact and $f$ is a homeomorphism of $X$ onto a dense subspace of $Y$. The relation $(f, Y) \geq (g, Z)$ holds iff there exists a continuous map $h: Y \to Z$ such that $h \circ f = g$ (equivalently, $g \circ f^{-1}$ on $f[X]$ extends continuously to $h$ carrying $Y$ onto $Z$).

*Proof.* We first verify the three properties of a partial order.

**Reflexivity.** For any compactification $(f, Y)$, the identity map $\mathrm{id}_Y: Y \to Y$ is continuous and satisfies $\mathrm{id}_Y \circ f = f$. Hence $(f, Y) \geq (f, Y)$.

**Transitivity.** If $(f, Y) \geq (g, Z)$ and $(g, Z) \geq (h, U)$, then there exist continuous maps $h_1: Y \to Z$ onto $Z$ with $h_1 \circ f = g$, and $h_2: Z \to U$ onto $U$ with $h_2 \circ g = h$. The composition $h_2 \circ h_1: Y \to U$ is continuous and onto $U$, and $(h_2 \circ h_1) \circ f = h_2 \circ (h_1 \circ f) = h_2 \circ g = h$. Hence $(f, Y) \geq (h, U)$.

**Antisymmetry (for Hausdorff compactifications).** Suppose $(f, Y)$ and $(g, Z)$ are Hausdorff compactifications with $(f, Y) \geq (g, Z)$ and $(g, Z) \geq (f, Y)$. Then there exist continuous surjections $h: Y \to Z$ with $h \circ f = g$ and $k: Z \to Y$ with $k \circ g = f$. Consider $k \circ h: Y \to Y$. This is continuous and satisfies $(k \circ h) \circ f = k \circ g = f$. Hence $k \circ h$ agrees with the identity on the dense subspace $f[X]$ of $Y$. Since $Y$ is Hausdorff, the set of points where two continuous functions agree is closed; thus $k \circ h = \mathrm{id}_Y$ on all of $Y$. Similarly, $h \circ k = \mathrm{id}_Z$ on $Z$. Therefore $h$ is a bijection with continuous inverse $k$, i.e., $h$ is a homeomorphism, and $(f, Y)$ and $(g, Z)$ are topologically equivalent.

*Remark.* The antisymmetry argument uses that $f[X]$ is dense in $Y$ and $Y$ is Hausdorff. For non-Hausdorff compactifications, antisymmetry may fail, so $\geq$ is only a preorder on the full collection. $\square$
