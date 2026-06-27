---
role: proof
locale: en
of_concept: levi-form-under-change-of-defining-function
source_book: gtm038
source_chapter: "II"
source_section: "2. Pseudoconvexity"
---

We only need to show that for each $\zeta_0 \in U \cap \partial G$ there is a neighborhood $V(\zeta_0) \subset U$ and in $V$ exactly one differentiable function $h$ with $\varphi|V = h \cdot (\psi|V)$. Therefore let $\zeta_0 \in U \cap \partial G$ and $W(\zeta_0) \subset U$ be chosen so that there is a $C^2$-diffeomorphism $\Phi: W \rightarrow B \subset \mathbb{C}^n$ with $\Phi(W \cap G) = \{z \in B: x_1 < 0\}$, $\Phi(W \cap \partial G) = \{z \in B: x_1 = 0\}$. Then $\tilde{\varphi} := \varphi \circ \Phi^{-1}$, $\tilde{\psi} := \psi \circ \Phi^{-1}$ are twice differentiable in $B$. Without loss of generality $\Phi(\zeta_0) = 0$ and $B$ is convex. Define

$$h_1(x_1, \ldots, x_n, y_1, \ldots, y_n) := \int_0^1 \frac{\partial \tilde{\varphi}}{\partial x_1}(t x_1, x_2, \ldots, y_n) \, dt,$$
$$h_2(x_1, \ldots, x_n, y_1, \ldots, y_n) := \int_0^1 \frac{\partial \tilde{\psi}}{\partial x_1}(t x_1, x_2, \ldots, y_n) \, dt.$$

Then $\tilde{\varphi} = h_1 \cdot x_1$ and $\tilde{\psi} = h_2 \cdot x_1$. Since $(d\varphi)_{\zeta_0} \neq 0$ and $(d\psi)_{\zeta_0} \neq 0$, near $0$ we have $\partial \tilde{\varphi}/\partial x_1 \neq 0$ and $\partial \tilde{\psi}/\partial x_1 \neq 0$. Hence $h_1$ and $h_2$ are non-vanishing near $0$, and $\tilde{\varphi} = (h_1/h_2) \cdot \tilde{\psi}$. Setting $h := (h_1/h_2) \circ \Phi$ gives $\varphi = h \cdot \psi$ near $\zeta_0$, with $h > 0$.

Now compute the Levi form:

$$L_{\psi}(\mathfrak{w}) = \sum_{i,j=1}^{n} \psi_{z_i \bar{z}_j} w_i \bar{w}_j = h \cdot L_{\varphi}(\mathfrak{w}) + \sum_i (\sum_j \overline{\varphi_{z_j} w_j}) h_{z_i} w_i + \sum_j (\sum_i \varphi_{z_i} w_i) h_{\bar{z}_j} \bar{w}_j.$$

The last two terms vanish since $\sum \varphi_{z_j} w_j = 0$ for $\mathfrak{w} \in T_{\zeta_0}^{1,0}(\partial G)$. Since $h$ is positive, the proposition follows.
