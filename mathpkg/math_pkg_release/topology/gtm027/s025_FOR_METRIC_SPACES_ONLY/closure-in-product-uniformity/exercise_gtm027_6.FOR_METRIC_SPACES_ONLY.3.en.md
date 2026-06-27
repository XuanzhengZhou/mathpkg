---
role: exercise
locale: en
chapter: "6"
section: "FOR METRIC SPACES ONLY"
exercise_number: 3
---

# Exercise B(c): Closure in the Product Uniformity

Let $(X, \mathfrak{u})$ and $(Y, \mathfrak{v})$ be uniform spaces and for each $U \in \mathfrak{u}$ and each $V \in \mathfrak{v}$ let

$$W(U, V) = \{((x, y), (u, v)) : (x, u) \in U \text{ and } (y, v) \in V\}.$$

Show that the closure of a subset $R$ of $X \times Y$ in the product uniform topology is given by

$$R^{-} = \bigcap \{V \circ R \circ U^{-1} : U \in \mathfrak{u} \text{ and } V \in \mathfrak{v}\}.$$

Here $U^{-1} = \{(u, x) : (x, u) \in U\}$ and $V \circ R \circ U^{-1}$ denotes the composition of relations.
