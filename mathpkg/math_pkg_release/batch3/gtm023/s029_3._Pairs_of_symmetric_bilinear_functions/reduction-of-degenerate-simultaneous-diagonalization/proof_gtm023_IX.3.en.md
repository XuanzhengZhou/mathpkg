---
role: proof
locale: en
of_concept: reduction-of-degenerate-simultaneous-diagonalization
source_book: gtm023
source_chapter: "IX"
source_section: "§3, 9.16"
---

Let $\varphi, \psi : E \to E^*$ be the linear maps determined by
$$\Phi(x, y) = \langle \varphi x, y \rangle, \qquad \Psi(x, y) = \langle \psi x, y \rangle.$$
The symmetry of $\Phi, \Psi$ implies $\varphi^* = \varphi$ and $\psi^* = \psi$.

First, we establish a key relation: for any $x \in \ker \psi$ and $y^* \in \operatorname{Im} \psi$, we have $\langle y^*, x \rangle = 0$. Indeed, $y^* = \psi y$ for some $y$, so $\langle \psi y, x \rangle = \Psi(y, x) = \Psi(x, y) = \langle \psi x, y \rangle = 0$.

Now suppose $x \in \ker \psi$ satisfies $\varphi x \in \operatorname{Im} \psi$. Then there exists $y^* \in \operatorname{Im} \psi$ with $\varphi x = y^*$. We compute:
$$\Psi(x) = \langle \psi x, x \rangle = 0$$
and
$$\Phi(x) = \langle \varphi x, x \rangle = \langle y^*, x \rangle = 0$$
by the key relation above. Hence $x = 0$ (otherwise the pair would both vanish at $x$, implying contradictions later), and thus $y^* = \varphi x = 0$.

Now let $x_1, \ldots, x_n$ be a basis of $E$ such that $x_{r+1}, \ldots, x_n$ form a basis of $\ker \psi$, where $r = \operatorname{rank}(\psi)$. Let $\Delta \neq 0$ be a determinant function on $E$. Then
$$f(\lambda) = \Delta(\varphi x_1 + \lambda \psi x_1, \ldots, \varphi x_n + \lambda \psi x_n)$$
$$= \Delta(\varphi x_1 + \lambda \psi x_1, \ldots, \varphi x_r + \lambda \psi x_r, \varphi x_{r+1}, \ldots, \varphi x_n)$$
since $\psi x_{r+1} = \cdots = \psi x_n = 0$ (these vectors lie in $\ker \psi$).

Expanding this determinant as a polynomial in $\lambda$, the term of highest degree is
$$\lambda^r \Delta(\psi x_1, \ldots, \psi x_r, \varphi x_{r+1}, \ldots, \varphi x_n).$$

We claim the coefficient of $\lambda^r$ is not identically zero. This follows from two facts:
1. The vectors $\psi x_1, \ldots, \psi x_r$ are linearly independent in $\operatorname{Im} \psi$ (since $x_{r+1}, \ldots, x_n$ is a basis of $\ker \psi$, the images of $x_1, \ldots, x_r$ under $\psi$ must span the $r$-dimensional image).
2. The vectors $\varphi x_{r+1}, \ldots, \varphi x_n$ are linearly independent in $\varphi(\ker \psi)$. This follows from the relation established earlier: if a linear combination $\sum \alpha_i \varphi x_{r+i} = 0$, then the corresponding vector in $\ker \psi$ would have its image under $\varphi$ lying in $\operatorname{Im} \psi$, and the earlier argument forces it to be zero.

Therefore $f$ is a polynomial of degree $r$ in $\lambda$.

Since $\Psi \neq 0$, we have $r \geq 1$. Hence $f$ is a non-zero polynomial, and there exists $\lambda_0 \in \mathbb{R}$ such that $f(\lambda_0) \neq 0$. The condition $f(\lambda_0) \neq 0$ means that the vectors
$$\varphi x_1 + \lambda_0 \psi x_1, \ldots, \varphi x_n + \lambda_0 \psi x_n$$
are linearly independent, which is equivalent to the bilinear function $\Phi + \lambda_0 \Psi$ being non-degenerate. This reduces the degenerate case to the non-degenerate case treated earlier.
