---
role: proof
locale: en
of_concept: theta-bracket-identity
source_book: gtm004
source_chapter: "VII"
source_section: "4"
---

# Proof of Bracket Identity for the Theta Map

For $y \in \mathfrak{g}$, define the $\mathfrak{g}$-module homomorphism $\theta(y) : C_n \to C_n$ by

$$\theta(y) \langle x_1, \ldots, x_n \rangle = -y \langle x_1, \ldots, x_n \rangle + \sum_{i=1}^{n} (-1)^{i+1} \langle [y, x_i], x_1, \ldots, \hat{x}_i, \ldots, x_n \rangle,$$

where $\langle x_1, \ldots, x_n \rangle$ denotes the image of $x_1 \otimes \cdots \otimes x_n$ in $E_n \mathfrak{g}$.

We claim that

$$\theta([x, y]) = \theta(x) \theta(y) - \theta(y) \theta(x). \tag{4.2}$$

**Proof.** We compute $\theta(x) \theta(y) \langle x_1, \ldots, x_n \rangle$ term by term:

$$\begin{aligned}
\theta(x) \theta(y) \langle x_1, \ldots, x_n \rangle &= y x \langle x_1, \ldots, x_n \rangle \\
&\quad - \sum_{i=1}^{n} x \langle x_1, \ldots, [y, x_i], \ldots, x_n \rangle \\
&\quad - \sum_{i=1}^{n} y \langle x_1, \ldots, [x, x_i], \ldots, x_n \rangle \\
&\quad + \sum_{i,j=1}^{n} \langle x_1, \ldots, [x, x_i], \ldots, [y, x_j], \ldots, x_n \rangle \\
&\quad + \sum_{i=1}^{n} \langle x_1, \ldots, [x, [y, x_i]], \ldots, x_n \rangle.
\end{aligned}$$

Interchanging $x$ and $y$ and subtracting (using $y x - x y = [y, x] = -[x, y]$ on the first term and the Jacobi identity $[x, [y, x_i]] - [y, [x, x_i]] = [[x, y], x_i]$ on the last sums), we obtain

$$\theta(x) \theta(y) - \theta(y) \theta(x) = \theta([x, y]).$$

The cancellation uses the Jacobi identity in $\mathfrak{g}$ together with the fact that $(-1)^{i+1} \langle [y, x_i], x_1, \ldots, \hat{x}_i, \ldots, x_n \rangle = \langle x_1, \ldots, [y, x_i], \ldots, x_n \rangle$, so that the signs align correctly. $\square$
