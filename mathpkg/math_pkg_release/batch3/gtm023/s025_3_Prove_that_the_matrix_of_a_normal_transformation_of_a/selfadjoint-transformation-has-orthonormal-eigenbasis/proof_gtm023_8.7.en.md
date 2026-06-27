---
role: proof
locale: en
of_concept: selfadjoint-transformation-has-orthonormal-eigenbasis
source_book: gtm023
source_chapter: "VIII"
source_section: "8.7"
---

Define the Rayleigh quotient $F$ by
$$F(x) = \frac{(x, \varphi x)}{(x, x)} \quad (x \neq 0).$$
$F$ is continuous as a quotient of continuous functions and is homogeneous of degree zero: $F(\lambda x) = F(x)$ for $\lambda \neq 0$.

Since the unit sphere $\{x \in E : |x| = 1\}$ is compact (in the finite-dimensional case), $F$ attains its minimum at some unit vector $e_1$. Thus $F(e_1) \leq F(x)$ for all $x \neq 0$.

To show $e_1$ is an eigenvector, let $y$ be arbitrary and define
$$f(t) = F(e_1 + ty) = \frac{(e_1 + ty, \varphi e_1 + t\varphi y)}{(e_1 + ty, e_1 + ty)}.$$
Since $f$ attains a minimum at $t = 0$, we have $f'(0) = 0$. Differentiating at $t = 0$:
$$f'(0) = (e_1, \varphi y) + (y, \varphi e_1) - 2(e_1, \varphi e_1)(e_1, y).$$
Using selfadjointness, $(e_1, \varphi y) = (\varphi e_1, y)$, so
$$f'(0) = 2(\varphi e_1, y) - 2(e_1, \varphi e_1)(e_1, y) = 2(\varphi e_1 - (e_1, \varphi e_1)e_1, y).$$
Setting $f'(0) = 0$ for all $y$ yields
$$\varphi e_1 = (e_1, \varphi e_1)e_1,$$
so $e_1$ is an eigenvector with eigenvalue $\lambda_1 = (e_1, \varphi e_1)$.

Now restrict $\varphi$ to the orthogonal complement $E_1 = \{e_1\}^\perp$. Since $\varphi$ is selfadjoint and $\{e_1\}$ is stable, $E_1$ is also stable under $\varphi$ (by the stability theorem). The restriction is again selfadjoint. Applying the same construction to $E_1$ yields an eigenvector $e_2$ orthogonal to $e_1$. Continuing inductively, we obtain $n$ mutually orthogonal eigenvectors $e_v$ ($v = 1, \ldots, n$) satisfying $(e_v, e_\mu) = \delta_{v\mu}$ and $\varphi e_v = \lambda_v e_v$. These form an orthonormal basis of $E$, and the matrix of $\varphi$ in this basis is diagonal.
