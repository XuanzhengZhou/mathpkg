---
role: proof
locale: en
of_concept: ideal-contains-projection-on-any-one-dimensional-subspace
source_book: gtm031
source_chapter: "VIII"
source_section: "2. Operator methods"
---

Let $\mathfrak{B} \neq 0$ be a two-sided ideal in $\mathfrak{L}$. Choose $B \neq 0$ in $\mathfrak{B}$ and let $\mathfrak{R}B = [y_1, y_2, \cdots, y_r]$ where the $y_i$ are linearly independent. Pick $x_1$ such that $x_1B = y_1$.

We can find a linear transformation $A_1$ such that $y_1A_1 = x_1$ and $y_iA_1 = 0$ for $i > 1$ (extend the partial mapping defined on the $y_i$ to all of $\mathfrak{R}$). Then

$$x_1BA_1 = y_1A_1 = x_1.$$

Hence $E_1 \equiv BA_1$ satisfies $x_1E_1 = x_1$ and $\mathfrak{R}E_1 = [x_1]$, so $E_1$ is a projection of $\mathfrak{R}$ on $[x_1]$. Since $B \in \mathfrak{B}$ and $\mathfrak{B}$ is an ideal, $E_1 = BA_1 \in \mathfrak{B}$.

Now let $[x]$ be any one-dimensional subspace. Choose linear transformations $C$ and $D$ such that $xC = x_1$ and $x_1D = x$. Set $E = CE_1D$. Then

$$\mathfrak{R}E = \mathfrak{R}CE_1D = [x_1]D = [x]$$

and

$$xE = xCE_1D = x_1E_1D = x_1D = x.$$

Thus $E$ is a projection of $\mathfrak{R}$ on $[x]$. Since $E_1 \in \mathfrak{B}$ and $\mathfrak{B}$ is a two-sided ideal, $E = CE_1D \in \mathfrak{B}$, completing the proof.
