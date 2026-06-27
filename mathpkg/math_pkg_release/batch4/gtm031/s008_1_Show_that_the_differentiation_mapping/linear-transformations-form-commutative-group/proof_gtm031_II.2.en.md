---
role: proof
locale: en
of_concept: linear-transformations-form-commutative-group
source_book: gtm031
source_chapter: "II"
source_section: "2"
---

Since $A$ and $B$ are linear, for any $x, y \in \mathfrak{R}_1$ and $\alpha \in \Delta$,

$$(x + y)(A + B) = (x + y)A + (x + y)B = xA + yA + xB + yB$$
$$= xA + xB + yA + yB = x(A + B) + y(A + B)$$

and

$$(\alpha x)(A + B) = (\alpha x)A + (\alpha x)B = \alpha(xA) + \alpha(xB) = \alpha(xA + xB) = \alpha\,x(A + B).$$

Thus $A + B$ is a linear transformation.

**Associativity**: For any $x \in \mathfrak{R}_1$,
$$x[(A + B) + C] = x(A + B) + xC = xA + xB + xC,$$
$$x[A + (B + C)] = xA + x(B + C) = xA + xB + xC.$$
Hence $(A + B) + C = A + (B + C)$.

**Commutativity**: For any $x \in \mathfrak{R}_1$,
$$x(A + B) = xA + xB = xB + xA = x(B + A).$$
Hence $A + B = B + A$.

**Identity**: Define the mapping $0$ by $x0 = 0$, the zero vector in $\mathfrak{R}_2$. This mapping is clearly linear: $(x+y)0 = 0 = 0+0 = x0 + y0$ and $(\alpha x)0 = 0 = \alpha \cdot 0 = \alpha(x0)$. Moreover $x(A + 0) = xA + x0 = xA + 0 = xA$, so $A + 0 = A = 0 + A$ for all $A \in \mathfrak{L}(\mathfrak{R}_1, \mathfrak{R}_2)$.

**Inverse**: For any $A \in \mathfrak{L}(\mathfrak{R}_1, \mathfrak{R}_2)$, define $-A$ by $x(-A) = -xA$. Then $(-A)$ is linear since
$$(x+y)(-A) = -(x+y)A = -(xA + yA) = -xA - yA = x(-A) + y(-A),$$
$$(\alpha x)(-A) = -(\alpha x)A = -\alpha(xA) = \alpha(-xA) = \alpha\,x(-A).$$
Moreover $x(A + (-A)) = xA + x(-A) = xA - xA = 0 = x0$ for all $x$, so $A + (-A) = 0$.

All group axioms are satisfied, so $\mathfrak{L}(\mathfrak{R}_1, \mathfrak{R}_2)$ is a commutative group under $+$.
