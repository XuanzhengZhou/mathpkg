---
role: exercise
locale: en
chapter: "6"
section: "FOR METRIC SPACES ONLY"
exercise_number: 2
---

# Exercise B(b): Action of Product Entourage on a Relation

Let $(X, \mathfrak{u})$ and $(Y, \mathfrak{v})$ be uniform spaces and for each $U \in \mathfrak{u}$ and each $V \in \mathfrak{v}$ let

$$W(U, V) = \{((x, y), (u, v)) : (x, u) \in U \text{ and } (y, v) \in V\}.$$

If $R$ is a subset of $X \times Y$, show that

$$W(U, V)[R] = V \circ R \circ U^{-1} = \bigcup \{U[x] \times V[y] : (x, y) \in R\}.$$

Here $U^{-1} = \{(u, x) : (x, u) \in U\}$ and $V \circ R \circ U^{-1}$ denotes the composition of relations.
