---
role: proof
locale: en
of_concept: polynomial-pencil-nonvanishing
source_book: gtm023
source_chapter: "9"
source_section: "3. Pairs of symmetric bilinear functions"
---

Let $\psi: E \to E$ be the self-adjoint linear transformation defined by $\Psi(x,y) = \langle \psi x, y \rangle$ with respect to a fixed positive definite inner product. Similarly, define $\varphi$ by $\Phi(x,y) = \langle \varphi x, y \rangle$.

First note that if $y^* = \varphi x$ for some $x \in \ker \psi$, then for any $x \in \ker \psi$,
$$\Psi(x) = \langle x, \psi x \rangle = 0$$
and
$$\Phi(x) = \langle \varphi x, x \rangle = \langle y^*, x \rangle = 0$$
since $y^* \in \operatorname{Im} \psi$ (this follows from the relation between $\varphi$ and $\psi$, which can be established from the general theory). These equations imply $x = 0$ and hence $y^* = 0$.

Now choose a basis $\{x_1, \ldots, x_n\}$ of $E$ such that $\{x_{r+1}, \ldots, x_n\}$ is a basis of $\ker \psi$, where $r = \operatorname{rank}(\psi)$. Let $\Delta \neq 0$ be a determinant function on $E$. Consider
$$f(\lambda) = \Delta(\varphi x_1 + \lambda \psi x_1, \ldots, \varphi x_n + \lambda \psi x_n).$$

For $v > r$, $x_v \in \ker \psi$, so $\psi x_v = 0$ and $\varphi x_v + \lambda \psi x_v = \varphi x_v$. Therefore
$$f(\lambda) = \Delta(\varphi x_1 + \lambda \psi x_1, \ldots, \varphi x_r + \lambda \psi x_r, \varphi x_{r+1}, \ldots, \varphi x_n).$$

Expanding by multilinearity, the term with the highest power of $\lambda$ is
$$\lambda^r \Delta(\psi x_1, \ldots, \psi x_r, \varphi x_{r+1}, \ldots, \varphi x_n).$$

The coefficient of $\lambda^r$ is non-zero because the vectors $\psi x_1, \ldots, \psi x_r \in \operatorname{Im} \psi$ are linearly independent (they form a basis of $\operatorname{Im} \psi$) and the vectors $\varphi x_{r+1}, \ldots, \varphi x_n$ are linearly independent in $\varphi(\ker \psi)$. Their independence follows from the relation established at the beginning.

Thus $f$ is a non-zero polynomial of degree $r$. Since $r \geq 1$ (as $\Psi \neq 0$), we can choose $\lambda_0 \in \mathbb{R}$ such that $f(\lambda_0) \neq 0$. The condition $f(\lambda_0) \neq 0$ means that the vectors $(\varphi + \lambda_0\psi)x_1, \ldots, (\varphi + \lambda_0\psi)x_n$ are linearly independent, which is equivalent to the associated bilinear function $\Phi + \lambda_0 \Psi$ being non-degenerate.
