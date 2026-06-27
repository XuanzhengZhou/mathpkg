---
role: proof
locale: en
of_concept: conic-canonical-matrix-form
source_book: gtm006
source_chapter: "II"
source_section: "7. Conics"
---

Choose a frame such that $X = \langle(1, 0, 0)\rangle$, $Z = \langle(0, 0, 1)\rangle$, and so $X + Z = \langle(0, 1, 0)\rangle$; hence $Y = \langle(0, 1, 0)\rangle$ is the image of $\langle(0, 1, 0)\rangle$ under $\beta$, while finally $J = \langle(1, 1, 1)\rangle$ is a point on $\mathcal{C}$. Let $A$ be the matrix for $\mathcal{C}$, and write $A = (a_{ij})$, noting that $A$ is symmetric.

Since $X$ is on $\mathcal{C}$, we have $a_{11} = 0$. The fact that $Z$ is on $\mathcal{C}$ forces $a_{33} = 0$.

The image of $\langle(0, 1, 0)\rangle$ under $\beta$ is $\langle A(0, 1, 0)\rangle = \langle(a_{12}, a_{22}, a_{32})\rangle = \langle(0, 1, 0)\rangle$, and so $a_{12} = a_{32} = 0$.

Finally, $\langle(1, 1, 1)\rangle$ is on $\mathcal{C}$, so $2a_{13} + a_{22} = 0$. Hence we can choose $A$ to be the matrix:

$$A = \begin{bmatrix} 0 & 0 & -1 \\ 0 & 2 & 0 \\ -1 & 0 & 0 \end{bmatrix}.$$

Thus the points of $\mathcal{C}$ are the points $\langle(x, y, z)\rangle$ satisfying $-2xz + 2y^2 = 0$, i.e. $y^2 = xz$. The parametric form follows. $\square$
