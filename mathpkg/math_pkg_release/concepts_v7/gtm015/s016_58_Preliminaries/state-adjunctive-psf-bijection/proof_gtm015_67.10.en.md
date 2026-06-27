---
role: proof
locale: en
of_concept: state-adjunctive-psf-bijection
source_book: gtm015
source_chapter: "67"
source_section: "States and representations"
---

# Proof of Bijection between states and adjunctive PSFs

Proof. (i) Given a state $f$ on $A$, define $\varphi_f(x, y) = f(y^*x)$ for all $x, y \in A$. This is clearly a sesquilinear form; it is positive because $f(x^*x) \geq 0$ for all $x \in A$, and it is adjunctive because $\varphi_f(ax, y) = f(y^*(ax)) = f((a^*y)^*x) = \varphi_f(x, a^*y)$.

(ii) Conversely, if $\varphi$ is an adjunctive PSF on $A$ and $A$ has unity $1$, define $f_\varphi(x) = \varphi(x, 1)$ for all $x \in A$. Then $f_\varphi(1) = \varphi(1, 1) \geq 0$. Moreover, $f_\varphi(x^*x) = \varphi(x^*x, 1) = \varphi(x, x) \geq 0$, so $f_\varphi$ is a state.

The correspondences $f \mapsto \varphi_f$ and $\varphi \mapsto f_\varphi$ are mutually inverse bijections between the set of all states $f$ and the set of all adjunctive PSFs $\varphi$; both sets are convex, and the correspondences preserve convex combinations. There is nothing deeper here than the associativity of multiplication in $A$.
