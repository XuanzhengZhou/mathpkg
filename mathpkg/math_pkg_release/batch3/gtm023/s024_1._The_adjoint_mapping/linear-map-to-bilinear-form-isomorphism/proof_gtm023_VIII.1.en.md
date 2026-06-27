---
role: proof
locale: en
of_concept: linear-map-to-bilinear-form-isomorphism
source_book: gtm023
source_chapter: "VIII"
source_section: "§1. The adjoint mapping"
---

**Injectivity:** Suppose $\varphi$ determines the zero bilinear function, i.e., $(\varphi x, y) = 0$ for all $x, y \in E$. For fixed $x$, take $y = \varphi x$; then $(\varphi x, \varphi x) = 0$, which implies $\varphi x = 0$ by positive definiteness of the inner product. Since this holds for all $x$, we have $\varphi = 0$. Thus $\varrho$ is injective.

**Surjectivity:** Let $\Phi \in B(E, E)$ be an arbitrary bilinear function. For each fixed $y \in E$, the map $x \mapsto \Phi(x, y)$ is a linear functional on $E$. By the Riesz representation theorem, there exists a unique vector $x' \in E$ such that $\Phi(x, y) = (x, x')$ for all $x \in E$. Define $\varphi: E \rightarrow E$ by $\varphi y = x'$. The uniqueness of $x'$ ensures $\varphi$ is well-defined and linear. Then $\Phi(x, y) = (x, \varphi y)$ for all $x, y$. By symmetry of the inner product, $\Phi(x, y) = (\varphi y, x)$, so $\varrho$ is surjective.

Since $\varrho$ is clearly linear, it is an isomorphism.
