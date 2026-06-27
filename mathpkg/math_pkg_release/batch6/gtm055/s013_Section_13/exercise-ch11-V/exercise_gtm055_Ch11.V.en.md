---
role: exercise
locale: en
chapter: "11"
section: "Problems"
exercise_number: "V"
---

Let $U$ be a nonempty open subset of Euclidean space $\mathbb{R}^n$ and let $m$ be a nonnegative integer. We denote by $\mathcal{C}^{(m)}(U)$ the linear space of all $m$ times continuously differentiable complex-valued functions on $U$ and by $\mathcal{C}^{(\infty)}(U)$ the space of infinitely differentiable functions on $U$, i.e., $\mathcal{C}^{(\infty)}(U) = \bigcap_{m=0}^{\infty} \mathcal{C}^{(m)}(U)$. If $k_1, \ldots, k_n$ are nonnegative integers such that $k_1 + \cdots + k_n \leq m$, and if $f \in \mathcal{C}^{(m)}(U)$, we write $D^{k_1, \ldots, k_n}f$ for the (continuous) partial derivative

$$\frac{\partial^{k_1 + \cdots + k_n}f}{\partial x_1^{k_1} \cdots \partial x_n^{k_n}}$$

obtained by differentiating $k_i$ times with respect to the variable $x_i$, $i = 1, \ldots, n$. Show that there exist test functions on $\mathbb{R}^n$ that are positive on the interior of any closed cell, have that cell as support, and possess the property that all positive powers are also test functions. Show similarly that if $x_0$ is a point in $\mathbb{R}^n$ and $r$ is a positive radius, then there exist test functions $\varphi_r$ on $\mathbb{R}^n$ having for support the closed ball $D_r(x_0)^-$ and possessing the property that $\int_{\mathbb{R}^n} \varphi_r \, d\mu_n = 1$, where $\mu_n$ denotes Lebesgue-Borel measure on $\mathbb{R}^n$.
