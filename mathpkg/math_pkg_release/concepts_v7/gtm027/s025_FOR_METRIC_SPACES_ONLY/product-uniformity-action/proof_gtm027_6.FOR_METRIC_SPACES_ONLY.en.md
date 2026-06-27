---
role: proof
locale: en
of_concept: product-uniformity-action-on-subset
source_book: gtm027
source_chapter: "6"
source_section: "FOR METRIC_SPACES ONLY"
---

# Proof of Product Uniformity Action on Subsets

**Proposition (Exercise B(b)).** Let $(X, \mathfrak{u})$ and $(Y, \mathfrak{v})$ be uniform spaces and for each $U \in \mathfrak{u}$ and $V \in \mathfrak{v}$ let

$$W(U, V) = \{((x, y), (u, v)) : (x, u) \in U \text{ and } (y, v) \in V\}.$$

If $R$ is a subset of $X \times Y$, then

$$W(U, V)[R] = V \circ R \circ U^{-1} = \bigcup \{U[x] \times V[y] : (x, y) \in R\}.$$

**Proof.** Recall that for an entourage $W$ and a subset $R$, the action is defined by

$$W[R] = \{z : \exists w \in R \text{ such that } (w, z) \in W\}.$$

For $W = W(U, V)$, we have

$$W(U, V)[R] = \{(u, v) \in X \times Y : \exists (x, y) \in R \text{ with } ((x, y), (u, v)) \in W(U, V)\}.$$

By definition of $W(U, V)$, the condition $((x, y), (u, v)) \in W(U, V)$ means $(x, u) \in U$ and $(y, v) \in V$.

**First equality:** $W(U, V)[R] = V \circ R \circ U^{-1}$.

Recall that $U^{-1} = \{(u, x) : (x, u) \in U\}$. Then

\begin{align*}
(u, v) \in V \circ R \circ U^{-1}
&\iff \exists (x, y) \in R : (u, x) \in U^{-1} \text{ and } (y, v) \in V \\
&\iff \exists (x, y) \in R : (x, u) \in U \text{ and } (y, v) \in V \\
&\iff (u, v) \in W(U, V)[R].
\end{align*}

**Second equality:** $V \circ R \circ U^{-1} = \bigcup \{U[x] \times V[y] : (x, y) \in R\}$.

For a fixed $(x, y) \in R$, we have

$$U[x] \times V[y] = \{(u, v) : (x, u) \in U \text{ and } (y, v) \in V\}.$$

Thus a pair $(u, v)$ belongs to $\bigcup_{(x,y) \in R} U[x] \times V[y]$ if and only if there exists $(x, y) \in R$ such that $(x, u) \in U$ and $(y, v) \in V$, which is exactly the characterization of $W(U, V)[R]$. This establishes the second equality and completes the proof.
