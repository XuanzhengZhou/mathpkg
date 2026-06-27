---
role: proof
locale: en
of_concept: lemma-1-5-smooth-approximation
source_book: gtm033
source_chapter: "5"
source_section: "1. Degrees of Maps"
---

# Proof of Lemma 1.5 (Smooth Approximation of Continuous Maps)

By Theorem 4.6.3, $N$ can be embedded as a $C^\infty$ retract of an open subset $W \subset \mathbb{R}_+^n$ (the closed upper half-space); let $r: W \to N$ be a $C^\infty$ retraction.

By standard approximation theory, there exists a $C^\infty$ map $g: M \to N$ that approximates $f$ so closely (in the $C^0$ sense on compact subsets) that the straight-line homotopy

$$h: M \times I \to \mathbb{R}_+^n, \qquad h(x, t) = (1 - t)f(x) + t g(x)$$

takes values in $W$. (Here we regard $f$ and $g$ as maps into $\mathbb{R}_+^n$ via the embedding $N \subset W \subset \mathbb{R}_+^n$.)

Then the composition $r \circ h: M \times I \to N$ is a $C^\infty$ homotopy from $r \circ h(\cdot, 0) = r \circ f = f$ (since $r$ is a retraction) to $r \circ h(\cdot, 1) = r \circ g = g$. Thus $f$ is homotopic to the $C^\infty$ map $g$, which approximates $f$ arbitrarily closely.
