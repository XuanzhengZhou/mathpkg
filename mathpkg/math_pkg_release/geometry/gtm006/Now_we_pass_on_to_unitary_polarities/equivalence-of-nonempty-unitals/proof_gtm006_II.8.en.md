---
role: proof
locale: en
of_concept: equivalence-of-nonempty-unitals
source_book: gtm006
source_chapter: "II"
source_section: "8. Unitals"
---

Let $\mathcal{U}$ be a non-empty unital defined by a unitary polarity $\beta$. Choose three non-collinear points $X, Z, J \in \mathcal{U}$. Let $Y$ be the intersection of the absolute lines $X^{\beta}$ and $Z^{\beta}$. Since $X^{\beta}$ and $Z^{\beta}$ are absolute lines, neither contains $J$, so $\{X, Y, Z, J\}$ forms a frame for the projective plane.

With respect to this frame, write $X = \langle (1,0,0) \rangle$, $Y = \langle (1,1,0) \rangle$, $Z = \langle (0,0,1) \rangle$, $J = \langle (1,1,1) \rangle$. Imitating the proof of Theorem 2.36, the polarity $\beta$ can be represented by a matrix of the form
$$A = \begin{bmatrix} 0 & 0 & c \\ 0 & b & 0 \\ c^{\phi} & 0 & 0 \end{bmatrix}$$
where $\phi$ is the associated involutory automorphism, $b \in F$ (the fixed field), and $b + c + c^{\phi} = 0$. Since this canonical form depends only on the choice of the field automorphism $\phi$ and the elements $b, c$, any two non-empty unitals can be mapped to this same canonical form by appropriate choice of frame, establishing their equivalence under $PGL(V)$. $\square$
