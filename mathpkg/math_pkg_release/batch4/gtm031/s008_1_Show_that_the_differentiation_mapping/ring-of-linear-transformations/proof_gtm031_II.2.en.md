---
role: proof
locale: en
of_concept: ring-of-linear-transformations
source_book: gtm031
source_chapter: "II"
source_section: "2"
---

We verify the ring axioms:

1. $\mathfrak{L}(\mathfrak{R}, \mathfrak{R})$ with $+$ is a commutative group (previously established).

2. $\mathfrak{L}(\mathfrak{R}, \mathfrak{R})$ is closed under composition $\cdot$: If $A, B \in \mathfrak{L}(\mathfrak{R}, \mathfrak{R})$, then $AB$ maps $\mathfrak{R}$ into $\mathfrak{R}$ and is linear (being the resultant of two linear transformations).

3. Composition is associative: For any $x \in \mathfrak{R}$, $x((AB)C) = (x(AB))C = ((xA)B)C$, and $x(A(BC)) = (xA)(BC) = ((xA)B)C$. Thus $(AB)C = A(BC)$.

4. Distributive laws hold (previously established):
   $$A(B + C) = AB + AC, \quad (B + C)D = BD + CD.$$

5. The identity mapping $1: x \mapsto x$ is clearly linear: $(x+y)1 = x+y = x1 + y1$ and $(\alpha x)1 = \alpha x = \alpha(x1)$. For any $A \in \mathfrak{L}$, $x(A1) = (xA)1 = xA$ and $x(1A) = (x1)A = xA$, so $A1 = A = 1A$.

All ring axioms are satisfied.
