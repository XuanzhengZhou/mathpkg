---
role: proof
locale: en
of_concept: immersion-local-submanifold
source_book: gtm014
source_chapter: "I"
source_section: "2"
---

Given $p$ in $X$, there exist open neighborhoods $U$ of $p$ in $X$ and $V$ of $\phi(p)$ in $Y$ with $\phi(U) \subset V$, charts $\rho: U \to \mathbf{R}^n$ and $\tau: V \to \mathbf{R}^m$, and a linear map $\lambda: \mathbf{R}^n \to \mathbf{R}^m$ of rank $n$ so that the diagram

$$
\begin{array}{ccc}
U & \xrightarrow{\phi} & V \\
{\scriptstyle\rho}\downarrow & & \downarrow{\scriptstyle\tau} \\
\mathbf{R}^n & \xrightarrow{\lambda} & \mathbf{R}^m
\end{array}
$$

commutes. This is possible by Corollary 2.5.

Now (1) follows since $\lambda: \mathbf{R}^n \to \mathbf{R}^m$ is a homeomorphism onto its image. For $\tau(\phi(U))$ is homeomorphic to $\lambda(\mathbf{R}^n)$, and $\tau$ is a homeomorphism.

For (2), observe that $\tau(\phi(U)) = \lambda(\mathbf{R}^n)$ is the image of $\mathbf{R}^n$ under a linear injection of rank $n$, which is a linear subspace of $\mathbf{R}^m$ and thus satisfies the submanifold condition in $\mathbf{R}^m$. Pulling back via the chart $\tau$ shows $\phi(U)$ is a submanifold of $Y$.

**Note:** The image of an immersion need not be a submanifold even if the immersion is 1:1. For example, consider a figure-eight curve $\phi: \mathbf{R} \to \mathbf{R}^2$ where $P = \lim_{t \to \infty} \phi(t)$. The induced topology on $\phi(\mathbf{R})$ from $\mathbf{R}^2$ is not the same (near $P$) as the induced manifold topology on $\phi(\mathbf{R})$.
