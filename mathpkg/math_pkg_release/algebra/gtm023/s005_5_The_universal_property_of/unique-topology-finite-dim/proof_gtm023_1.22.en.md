---
role: proof
locale: en
of_concept: unique-topology-finite-dim
source_book: gtm023
source_chapter: "1"
source_section: "1.22"
---

**Existence:** Let $e_v$ ($v=1,\ldots,n$) be a fixed basis of $E$ and consider the linear isomorphism $\varphi: \mathbb{R}^n \to E$ given by $(\xi^1,\ldots,\xi^n) \mapsto \sum_v \xi^v e_v$. Define the open sets in $E$ as $\varphi(U)$ where $U$ is open in $\mathbb{R}^n$. Then $\varphi$ becomes a homeomorphism and the linear operations in $E$ are continuous (by continuity of operations in $\mathbb{R}^n$). For any linear function $f$ in $E$,
$$f(x) - f(x_0) = f(x - x_0) = \sum_v (\xi^v - \xi^v_0) f(e_v),$$
so $f$ is continuous (it is a linear combination of coordinate functions).

**Uniqueness:** Let $e_v$ be a basis of $E$ and define $\varphi: \mathbb{R}^n \to E$ by $\varphi(\xi^1,\ldots,\xi^n) = \sum_v \xi^v e_v$, and $\psi: E \to \mathbb{R}^n$ by $\psi x = (\xi^1(x),\ldots,\xi^n(x))$ where $x = \sum_v \xi^v(x) e_v$. $T_1$ implies $\varphi$ is continuous. The coordinate functions $x \mapsto \xi^v(x)$ are linear, so $T_2$ implies $\psi$ is continuous. Since $\psi \circ \varphi = \iota_{\mathbb{R}^n}$ and $\varphi \circ \psi = \iota_E$, $\varphi$ is a homeomorphism. Hence the topology of $E$ is uniquely determined by $T_1$ and $T_2$.
