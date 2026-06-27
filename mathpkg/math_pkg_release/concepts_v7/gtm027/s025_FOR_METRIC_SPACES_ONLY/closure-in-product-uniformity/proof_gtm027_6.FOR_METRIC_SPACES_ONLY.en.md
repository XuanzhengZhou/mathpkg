---
role: proof
locale: en
of_concept: closure-in-product-uniformity
source_book: gtm027
source_chapter: "6"
source_section: "FOR METRIC_SPACES ONLY"
---

# Proof of Closure in Product Uniformity

**Proposition (Exercise B(c)).** Let $(X, \mathfrak{u})$ and $(Y, \mathfrak{v})$ be uniform spaces and let $W(U, V)$ be the product entourage as defined in part (a). The closure of a subset $R$ of $X \times Y$ in the product uniform topology is

$$R^{-} = \bigcap \{V \circ R \circ U^{-1} : U \in \mathfrak{u} \text{ and } V \in \mathfrak{v}\}.$$

**Proof.** In a uniform space, a point $z$ belongs to the closure of a set $R$ if and only if every entourage-neighborhood of $z$ intersects $R$. Since the family $\{W(U, V) : U \in \mathfrak{u}, V \in \mathfrak{v}\}$ is a base for the product uniformity, we have

$$z \in R^{-} \iff \forall U \in \mathfrak{u}, \forall V \in \mathfrak{v} : W(U, V)[z] \cap R \neq \emptyset.$$

Let $z = (u, v)$. Then $W(U, V)[(u, v)] = U[u] \times V[v]$, so the condition becomes

$$\forall U \in \mathfrak{u}, \forall V \in \mathfrak{v}, \exists (x, y) \in R : x \in U[u] \text{ and } y \in V[v].$$

Now $x \in U[u] \iff (u, x) \in U \iff (x, u) \in U^{-1}$. And $y \in V[v] \iff (y, v) \in V$. Therefore,

\begin{align*}
(u, v) \in R^{-}
&\iff \forall U \in \mathfrak{u}, \forall V \in \mathfrak{v}, \exists (x, y) \in R : (x, u) \in U^{-1} \text{ and } (y, v) \in V \\
&\iff \forall U \in \mathfrak{u}, \forall V \in \mathfrak{v}, (u, v) \in V \circ R \circ U^{-1} \\
&\iff (u, v) \in \bigcap \{V \circ R \circ U^{-1} : U \in \mathfrak{u}, V \in \mathfrak{v}\}.
\end{align*}

This establishes the formula. Note that by part (b), $W(U, V)[R] = V \circ R \circ U^{-1}$, so the closure can also be expressed as

$$R^{-} = \bigcap \{W(U, V)[R] : U \in \mathfrak{u}, V \in \mathfrak{v}\}.$$

The result is a natural generalization of the fact that in a metric space, the closure of a set is the intersection of all open $\varepsilon$-enlargements of the set.
