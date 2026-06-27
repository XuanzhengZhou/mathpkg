---
role: proof
locale: en
of_concept: lemma-3-1-quadrangle-lines-form-quadrilateral
source_book: gtm006
source_chapter: "3"
source_section: "2. Basic Concepts"
---

Let $A, B, C, D$ be a quadrangle in the projective plane $\mathcal{P}$, so that no three of $A, B, C, D$ are collinear. Consider the four lines $AB, BC, CD, DA$. We must show that no three of these lines are concurrent.

Suppose, for contradiction, that three of these lines pass through a common point $T$. By symmetry, it suffices to consider the case where $AB, BC, CD$ are concurrent at $T$, or the case where $AB, AD, BC$ are concurrent at $T$.

**Case 1:** $AB$, $BC$, $CD$ are concurrent at $T$.

Since $T$ is on both $AB$ and $BC$, and any two distinct lines intersect in a unique point (axiom (ii)), we have $T = AB \cap BC = B$. Thus $T = B$. But then $B$ lies on $CD$, which means $B, C, D$ are collinear, contradicting the assumption that $A, B, C, D$ is a quadrangle (no three collinear).

**Case 2:** $AB$, $AD$, $BC$ are concurrent at $T$.

Since $T$ is on both $AB$ and $AD$, we have $T = AB \cap AD = A$, so $T = A$. But then $A$ lies on $BC$, meaning $A, B, C$ are collinear, again contradicting the quadrangle property.

The remaining cases are symmetric. Therefore, no three of the lines $AB, BC, CD, DA$ can be concurrent. Hence they form a quadrilateral. $\square$
