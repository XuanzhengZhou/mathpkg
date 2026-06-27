---
role: proof
locale: en
of_concept: real-numbers-cogenerator-metric-spaces
source_book: gtm026
source_chapter: "1"
source_section: "Exercise 20"
---

Let $(X, d)$ be a metric space and let $y, z \in X$ with $y \neq z$. Then $d(y, z) > 0$. Consider the distance-decreasing map $d(y, -): X \to \mathbb{R}$. We have
$$d(y, y) = 0, \qquad d(y, z) = d(y, z) > 0,$$
so $d(y, -)$ separates $y$ and $z$. More generally, for any pair of distinct morphisms $f, g: (Y, d') \to (X, d)$, there exists some $t \in Y$ with $f(t) \neq g(t)$. Setting $x = f(t)$ and applying $d(x, -)$ yields a map $h = d(x, -) \circ (-): X \to \mathbb{R}$ that is distance decreasing (as a composition of the distance-decreasing map $d(x, -)$ with the identity on $X$) and satisfies $f \circ h \neq g \circ h$.

Thus $\mathbb{R}$ is a cogenerator in the category of metric spaces and distance-decreasing maps.
