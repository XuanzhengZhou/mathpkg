---
role: proof
locale: en
of_concept: cones-family-properties
source_book: gtm036
source_chapter: "3"
source_section: "F FAMILIES OF CONES"
---

The statement is presented without proof in the text. These properties follow directly from the definition of a cone.

\textbf{Intersection:} Let $\{\mathcal{C}_\alpha\}$ be a family of cones. If $x \in \bigcap_\alpha \mathcal{C}_\alpha$ and $\lambda \geq 0$, then $\lambda x \in \mathcal{C}_\alpha$ for each $\alpha$ since each $\mathcal{C}_\alpha$ is a cone. Hence $\lambda x \in \bigcap_\alpha \mathcal{C}_\alpha$, so the intersection is a cone.

\textbf{Directed union:} If the family is directed by $\subset$ (i.e., for any $\alpha, \beta$ there exists $\gamma$ with $\mathcal{C}_\alpha \subset \mathcal{C}_\gamma$ and $\mathcal{C}_\beta \subset \mathcal{C}_\gamma$), then for any $x \in \bigcup_\alpha \mathcal{C}_\alpha$, we have $x \in \mathcal{C}_\alpha$ for some $\alpha$, and $\lambda x \in \mathcal{C}_\alpha \subset \bigcup \mathcal{C}_\alpha$ for $\lambda \geq 0$.

\textbf{Finite linear combinations:} If $\mathcal{C}_1, \ldots, \mathcal{C}_n$ are cones and $a_i$ are scalars, then $a_i \mathcal{C}_i$ is a cone (scalar multiple of a cone), and the sum of cones is a cone, so $a_1 \mathcal{C}_1 + \cdots + a_n \mathcal{C}_n$ is a cone.

\textbf{Conical extension properties:} $C(A) = \bigcup_{a \geq 0} aA$ follows from the definition. The sublinearity $C(aA + bB) \subset a C(A) + b C(B)$ holds because any element of $C(aA + bB)$ is $\lambda(ax + by) = a(\lambda x) + b(\lambda y) \in a C(A) + b C(B)$. The commutation with unions follows from the definition of conical extension.
