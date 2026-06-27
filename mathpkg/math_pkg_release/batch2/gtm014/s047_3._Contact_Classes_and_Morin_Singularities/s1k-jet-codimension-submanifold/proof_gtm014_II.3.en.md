---
role: proof
locale: en
of_concept: s1k-jet-codimension-submanifold
source_book: gtm014
source_chapter: "II"
source_section: "3"
---

It is enough to prove that $S_{1^k} \cap J^k(X, Y)_{p,q}$ is a codimension $k$ submanifold of $J^k(X, Y)_{p,q}$. Moreover, we can assume that $X = Y = \mathbf{R}^n$ and $p = q = 0$. Given $\sigma_0 \in S_{1^k}$ with source and target at $0$, we will show that a neighborhood of $\sigma_0$ in $S_{1^k} \cap J^k(\mathbf{R}^n, \mathbf{R}^n)_{0,0}$ is a codimension $k$ submanifold.

Clearly, we can assume $\sigma_0$ has the form $(x_1, \ldots, x_n) \mapsto (f(x), x_2, \ldots, x_n)$. Then $\sigma_0 \in S_{1^k}$ is equivalent to the condition
$$
\frac{\partial f}{\partial x_1}(0) = \frac{\partial^2 f}{\partial x_1^2}(0) = \cdots = \frac{\partial^k f}{\partial x_1^k}(0) = 0.
$$

Now let $\pi: \mathbf{R}^n \to \mathbf{R}^{n-1}$ be the submersion $\pi(x_1, \ldots, x_n) = (x_2, \ldots, x_n)$, which induces a fiber mapping $\pi_*: J^k(\mathbf{R}^n, \mathbf{R}^n)_{0,0} \to J^k(\mathbf{R}^n, \mathbf{R}^{n-1})_{0,0}$. Let $U$ be the open subset of $J^k(\mathbf{R}^n, \mathbf{R}^{n-1})_{0,0}$ consisting of all $k$-jets of maps of the form $(x_1, \ldots, x_n) \mapsto (f_2(x), \ldots, f_n(x))$ having the property that $dx_2 \wedge \cdots \wedge dx_n \neq 0$.

The map $\pi_*^{-1}(U) \to U \times \mathbf{R}^k$ given by extracting the $k$ partial derivatives $\partial^s f / \partial x_1^s(0)$ for $s = 1, \ldots, k$ is a diffeomorphism (after a suitable choice of coordinates). Under this identification, $S_{1^k} \cap \pi_*^{-1}(U)$ corresponds to $U \times \{0\}$, where $\{0\} \subset \mathbf{R}^k$ is the origin. Since $\{0\}$ is a codimension $k$ submanifold of $\mathbf{R}^k$, the result follows.

(Note: The original OCR text at lines 63-67 provides the core of the proof but has some gaps. The reconstruction above fills in the standard argument from Thom-Boardman theory. The statement of Proposition 3.13 is not explicitly numbered in the surviving OCR text but is identified by the heading "Proof of Proposition 3.13" at line 63.)
