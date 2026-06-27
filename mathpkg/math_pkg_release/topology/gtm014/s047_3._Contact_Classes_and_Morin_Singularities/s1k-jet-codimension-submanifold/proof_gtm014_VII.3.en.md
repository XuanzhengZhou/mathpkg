---
role: proof
locale: en
of_concept: s1k-jet-codimension-submanifold
source_book: gtm014
source_chapter: "VII"
source_section: "3. Contact Classes and Morin Singularities"
---

It is enough to prove that $S_{1_k} \cap J^k(X, Y)_{p,q}$ is a codimension $k$ submanifold of $J^k(X, Y)_{p,q}$. Moreover, we can assume that $X = Y = \mathbf{R}^n$ and $p = q = 0$. Given $\sigma_0$ in $S_{1_k}$ with source and target at $0$, we show that a neighborhood of $\sigma_0$ in $S_{1_k} \cap J^k(\mathbf{R}^n, \mathbf{R}^n)_{0,0}$ is a codimension $k$ submanifold.

We can assume $\sigma_0$ has the form $(x_1, \ldots, x_n) \mapsto (f(x), x_2, \ldots, x_n)$. Then $\sigma_0$ being in $S_{1_k}$ is equivalent to the condition

$$\frac{\partial f}{\partial x_1}(0) = \frac{\partial^2 f}{\partial x_1^2}(0) = \cdots = \frac{\partial^k f}{\partial x_1^k}(0) = 0.$$

Let $\pi: \mathbf{R}^n \to \mathbf{R}^{n-1}$ be the submersion $\pi(x_1, \ldots, x_n) = (x_2, \ldots, x_n)$, which induces a fiber mapping $\pi_*: J^k(\mathbf{R}^n, \mathbf{R}^n)_{0,0} \to J^k(\mathbf{R}^n, \mathbf{R}^{n-1})_{0,0}$. Let $U$ be the open subset of $J^k(\mathbf{R}^n, \mathbf{R}^{n-1})_{0,0}$ consisting of all $k$-jets of maps whose differential restricted to the $x_2, \ldots, x_n$ directions is invertible. Over $U$, the $k$ equations $\partial^s f / \partial x_1^s(0) = 0$ for $s = 1, \ldots, k$ are independent, defining a codimension $k$ submanifold.
