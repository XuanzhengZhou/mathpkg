---
role: exercise
locale: en
chapter: "25"
section: "25.5"
exercise_number: 2
---
# Exercise 25.2

Let $X$ be a compact orientable $k$-dimensional manifold in $\mathbb{C}^n$. Browder's theorem (Chapter 15, Theorem 15.8) shows that when $k = n$, the polynomial hull $\hat{X}$ is always strictly larger than $X$. Explain why this result is true in the special case $k = n = 1$.

**Hint:** When $k = n = 1$, $X$ is a compact orientable 1-dimensional manifold in $\mathbb{C}$, i.e., a finite disjoint union of simple closed curves (Jordan curves). Use the fact that a compact set in $\mathbb{C}$ is polynomially convex if and only if its complement is connected (apply Runge's theorem, or equivalently, the rational approximation theorem). Since each Jordan curve separates the plane into an interior and an exterior region, $\mathbb{C} \setminus X$ is disconnected, so $X$ cannot be polynomially convex. Hence $\hat{X} \supsetneq X$, and in fact $\hat{X}$ contains the bounded components of $\mathbb{C} \setminus X$.
