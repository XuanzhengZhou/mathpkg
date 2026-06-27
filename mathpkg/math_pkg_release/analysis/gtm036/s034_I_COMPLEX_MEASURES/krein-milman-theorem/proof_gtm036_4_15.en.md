---
role: proof
locale: en
of_concept: krein-milman-theorem
source_book: gtm036
source_chapter: "4"
source_section: "15 (Extreme Points)"
---
The proof proceeds by showing that the family of closed convex proper subsets of $K$ that are "extremal" (closed in the face sense) has minimal elements, and any such minimal closed extremal subset must be a singleton extreme point.

Define a closed extremal subset of $K$ as a non-empty closed convex subset $F \subset K$ such that whenever a line segment with endpoints in $K$ has an interior point in $F$, the endpoints themselves belong to $F$. Let $\mathcal{F}$ be the family of all closed extremal subsets of $K$, partially ordered by inclusion.

Since $K \in \mathcal{F}$, the family is non-empty. For any chain in $\mathcal{F}$, the intersection is non-empty (by compactness of $K$) and is itself a closed extremal subset. By Zorn's lemma, $\mathcal{F}$ contains minimal elements.

Let $M$ be a minimal element of $\mathcal{F}$. If $M$ contained two distinct points $x \neq y$, then by the Hahn-Banach separation theorem, there exists a continuous linear functional $f$ separating $x$ and $y$. The subset $M' = \{z \in M : f(z) = \sup_{z \in M} f(z)\}$ is a proper closed extremal subset of $M$, contradicting minimality. Hence $M = \{x_0\}$ is a singleton, and $x_0$ is an extreme point of $K$.

Thus $\operatorname{ext}(K) \neq \emptyset$. To show $K = \overline{\operatorname{conv}}(\operatorname{ext}(K))$, suppose not. Then there exists a point $x \in K \setminus \overline{\operatorname{conv}}(\operatorname{ext}(K))$. By separation, there exists a continuous linear functional $f$ with $f(x) > \sup f(\operatorname{ext}(K))$. The set $\{z \in K : f(z) = \sup f(K)\}$ is a closed extremal subset disjoint from $\operatorname{ext}(K)$, and contains a minimal closed extremal subset by the same chain argument, which must be an extreme point — contradiction.
