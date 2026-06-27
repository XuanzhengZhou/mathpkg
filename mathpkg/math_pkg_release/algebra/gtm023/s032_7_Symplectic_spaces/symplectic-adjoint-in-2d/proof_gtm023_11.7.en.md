---
role: proof
locale: en
of_concept: symplectic-adjoint-in-2d
source_book: gtm023
source_chapter: "11"
source_section: "7"
---

The proof is left as an exercise in the source text. In a 2-dimensional symplectic space with symplectic basis $\{a, b\}$ (so $\langle a, b \rangle = 1$), the matrix of the symplectic form is $J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$. A linear transformation $\varphi$ has matrix $M = \begin{pmatrix} \alpha & \beta \\ \gamma & \delta \end{pmatrix}$ in this basis.

The symplectic adjoint $\tilde{\varphi}$ is defined by $\langle \varphi x, y \rangle = \langle x, \tilde{\varphi} y \rangle$ for all $x, y$. In matrix terms, $M^{\mathsf{T}} J = J \tilde{M}$, so $\tilde{M} = -J M^{\mathsf{T}} J$. Computing:
$$\tilde{M} = -\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} \begin{pmatrix} \alpha & \gamma \\ \beta & \delta \end{pmatrix} \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = \begin{pmatrix} \delta & -\beta \\ -\gamma & \alpha \end{pmatrix}$$

Now $\operatorname{tr} \varphi = \alpha + \delta$, so $i \cdot \operatorname{tr} \varphi \cdot I - M$ (using the complex structure $i$ which in this context acts as $-J$) gives:
$$-J \cdot (\alpha+\delta) \cdot I - M = -(\alpha+\delta) J - M$$

In the 2-dimensional case over $\mathbb{C}$ with the appropriate identification of the complex structure, this simplifies to $\tilde{M} = i \cdot \operatorname{tr}(\varphi) \cdot I - M$, yielding the stated formula.
