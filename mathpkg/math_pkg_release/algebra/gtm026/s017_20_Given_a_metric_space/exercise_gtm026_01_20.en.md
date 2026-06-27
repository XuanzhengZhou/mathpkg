---
role: exercise
locale: en
chapter: "1"
section: "Exercise 20"
exercise_number: 20
---

Given a metric space $(X, d)$ and an element $x$ of $X$:

(a) Show that $d(x, -): (X, d) \longrightarrow \mathbb{R}$ (where $\mathbb{R}$ has the usual metric) is distance decreasing.

(b) Conclude that $\mathbb{R}$ is a cogenerator in the category (1.9) of metric spaces.

(c) An object $K$ of (any category) $\mathcal{K}$ is **injective** if $K$ is projective in $\mathcal{K}^{\text{op}}$ (as defined in exercise 17); that is, if for every $f: A \longrightarrow K$ and mono $i: A \longrightarrow B$ there exists an extension $g: B \longrightarrow K$ with $g \circ i = f$.

Prove McShane's theorem ([McShane '34, Theorem 1]): $\mathbb{R}$ is injective in the category of metric spaces.

[Hint: if $f$ is defined and distance decreasing on a subset $A$, then
$$g(x) = \sup\{\, f(a) - d(x, a) : a \in A \,\}$$
is a suitable extension.]
