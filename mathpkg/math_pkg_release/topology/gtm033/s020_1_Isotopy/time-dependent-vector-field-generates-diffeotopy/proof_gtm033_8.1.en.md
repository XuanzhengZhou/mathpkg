---
role: proof
locale: en
of_concept: time-dependent-vector-field-generates-diffeotopy
source_book: gtm033
source_chapter: "8"
source_section: "1. Isotopy"
---

# Proof of Time-Dependent Vector Field Generates Diffeotopy

**Theorem 1.1.** Let $G$ be a time-dependent vector field on $M$ having bounded velocity. Then $G$ generates a diffeotopy of $M$. That is, there is a unique diffeotopy $F: M \times I \rightarrow M$ such that

$$\frac{\partial F}{\partial t}(x,t) = G(F(x,t),t).$$

*Proof.* Let $X: M \times I \rightarrow T(M \times I)$ be the vector field $X(x,t) = (G(x,t),1)$. The projection into $I$ of a solution curve of $X$ is a curve of the form $y \mapsto y + t$. Therefore all solution curves are defined on intervals of length $\leqslant 1$.

The condition of bounded velocity implies that $M$ has a complete Riemannian metric in which all solution curves have finite length. Completeness then implies that each solution curve lies in a compact set. This means solution curves are defined on closed finite intervals, the endpoints of which map into $M \times 0$ and $M \times 1$. It follows that for $x \in M$ there is a solution curve of $X$ having the form

$$t \mapsto (F(x,t),t), \quad 0 \leqslant t \leqslant 1.$$

This defines the diffeotopy $F$. Uniqueness of $F$ follows from uniqueness of solutions of Lipschitz differential equations. $\square$
