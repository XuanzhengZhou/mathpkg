---
role: proof
locale: en
of_concept: characterization-of-mean-first-passage-matrix
source_book: gtm040
source_chapter: "6"
source_section: "4"
---

Proposition 6-42 already shows that the true mean first passage time matrix $M$ satisfies properties (1), (2), and (3). It remains to prove uniqueness.

Let $Y$ be any matrix satisfying (1), (2), and (3). Fix an arbitrary state 0 of the chain. It suffices to show that $y$, the zeroth column of $Y$, equals $m$, the zeroth column of $M$.

Form the chain ${}^0P$ in which state 0 has been made absorbing. The transition matrix of ${}^0P$ has the block form:
$${}^0P = egin{pmatrix} 1 & 0 \ \mathbf{v} & Q \end{pmatrix},$$
where the first row and column correspond to state 0, and $Q$ is the restriction of $P$ to the non-zero states.

Write the zeroth columns of $Y$ and $M$ in corresponding block form:
$$y = egin{pmatrix} y_0 \ ar{y} \end{pmatrix}, \qquad m = egin{pmatrix} m_0 \ ar{m} \end{pmatrix}.$$

We know $m_0 = y_0 = 0$ by property (1). By Corollary 5-17, $ar{m}$ is the minimal finite-valued non-negative solution of the equation $(I - Q)ar{x} = \mathbf{1}$.

We first show that $ar{y}$ is another finite-valued non-negative solution of the same equation. Property (2) gives finiteness, property (1) gives non-negativity. The identity $(I - P)Y = E - D$ (property 3) yields in the zeroth column:
$$egin{pmatrix} 1 - P_{00} & -\mathbf{p}^T \ -\mathbf{v} & I - Q \end{pmatrix} egin{pmatrix} y_0 \ ar{y} \end{pmatrix} = egin{pmatrix} 1 - D_{00} \ \mathbf{1} \end{pmatrix}.$$

Since $y_0 = 0$, the lower block gives $(I - Q)ar{y} = \mathbf{1}$. Thus $ar{y}$ is a finite-valued non-negative solution of $(I - Q)ar{x} = \mathbf{1}$.

Since $ar{m}$ is the minimal such solution, we have $ar{m} \leq ar{y}$ componentwise. But by symmetry (applying the same argument with the roles of $M$ and $Y$ reversed), we also obtain $ar{y} \leq ar{m}$. Therefore $ar{y} = ar{m}$ and consequently $Y = M$.
