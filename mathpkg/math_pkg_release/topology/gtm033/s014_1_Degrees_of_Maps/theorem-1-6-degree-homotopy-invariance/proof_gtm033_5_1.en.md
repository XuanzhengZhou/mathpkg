---
role: proof
locale: en
of_concept: theorem-1-6-degree-homotopy-invariance
source_book: gtm033
source_chapter: "5"
source_section: "1. Degrees of Maps"
---

# Proof of Theorem 1.6 (Homotopy Invariance and Boundary Extension Property of Degree)

**(a) Homotopy invariance.** Let $f, g: M \to N$ be homotopic maps. By Lemma 1.5, we may assume both $f$ and $g$ are $C^\infty$ (approximating continuous maps by smooth ones without changing degree). Let $H: M \times I \to N$ be a $C^\infty$ homotopy from $f$ to $g$.

Since $M$ and $N$ are compact without boundary and $N$ is connected, Lemma 1.4 ensures that $\deg f$ (or $\deg_2 f$) does not depend on the choice of regular value. Choose a regular value $y \in N$ for both $f$ and $g$ (such values exist by Sard's theorem). Then Lemma 1.4 gives $\deg(f, y) = \deg(g, y)$, so $\deg f = \deg g$. The same argument works with mod 2 degree when $M$ and $N$ are not oriented.

**(b) Boundary extension.** Suppose $M = \partial W$ with $W$ compact and $f = \tilde{f}|_{\partial W}$ for some $\tilde{f}: W \to N$. If $W$ and $N$ are orientable, give them orientations. Choose a regular value $y \in N$ for both $\tilde{f}$ and $\tilde{f}|_{\partial W}$ (again possible by Sard). By Lemma 1.2, $\deg(\tilde{f}|_{\partial W}, y) = \deg(f, y) = 0$. Hence $\deg f = 0$. The same reasoning using mod 2 degree yields $\deg_2 f = 0$ in the nonorientable case.
