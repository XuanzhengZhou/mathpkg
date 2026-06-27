---
role: proof
locale: en
of_concept: poincares-recurrence-theorem
source_book: gtm060
source_chapter: "2"
source_section: "B"
---

Consider the images of the neighborhood $U$:

$$U, gU, g^2U, \ldots, g^nU, \ldots$$

Since $g$ is volume-preserving, all of these sets have the same (positive) volume. If they were pairwise disjoint, then $D$ would contain infinitely many disjoint subsets of equal positive volume, implying $D$ has infinite volume -- contradicting the boundedness of $D$.

Therefore, for some $k \geq 0$ and $l \geq 0$ with $k > l$, we must have

$$g^k U \cap g^l U \neq \emptyset.$$

Applying $g^{-l}$ (which preserves intersections since $g$ is one-to-one), we obtain

$$g^{k-l} U \cap U \neq \emptyset.$$

Let $y$ be a point in this intersection. Then $y = g^n x$ for some $x \in U$, where $n = k - l > 0$. Hence $x \in U$ and $g^n x \in U$, proving the theorem.
