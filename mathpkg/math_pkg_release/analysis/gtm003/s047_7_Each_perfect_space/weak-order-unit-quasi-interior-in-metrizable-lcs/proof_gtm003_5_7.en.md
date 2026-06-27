---
role: proof
locale: en
of_concept: weak-order-unit-quasi-interior-in-metrizable-lcs
source_book: gtm003
source_chapter: "V: Order Structures"
source_section: "7. Each Perfect Space"
---

Let $x \geq 0$ be a weak order unit of $E$. We show that the linear hull of $[0, x]$ is dense in $E$. If $y \in E$ is such that $\inf(x, |y|) = 0$, then $y = 0$ by the definition of a weak order unit. Since the lattice operations are continuous, it follows that $y = 0$ for any $y$ in the orthogonal complement of the linear hull of $[0, x]$. By the Hahn-Banach theorem in the metrizable separable setting, this implies the linear hull of $[0, x]$ is dense in $E$. Hence $[0, x]$ is a total subset of $E$, i.e., $x$ is a quasi-interior point of the positive cone $C$.

The assumptions that $E$ be metrizable and separable are not dispensable: if $E$ is, for example, either the locally convex direct sum of infinitely many copies of $\mathbb{R}_0$ or the Hilbert direct sum of uncountably many copies of $\ell^2$ (under their respective canonical orderings), then the set of quasi-interior points of $C$ (equivalently, by (7.7), the set of weak order units) is empty.
