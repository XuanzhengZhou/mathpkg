---
role: proof
locale: en
of_concept: first-initial-value-theorem-for-maxwell-equations
source_book: gtm048
source_chapter: "3"
source_section: "3.11"
---

Let us first dispose of the second (necessity) statement. Suppose $(U, F, J)$ obeys Maxwell's equations. Since $F_0 = F \circ \phi$, we have $\phi^* F_0 = \phi^* F$, where the right side is the usual pull-back of forms. Thus
$$
0 = \phi^*(dF) = d(\phi^* F) = d(\phi^* F_0),
$$
which is $(e_1)$. Since $\operatorname{div} \hat{F} = 4\pi J$, Section 3.6.2 implies $d(i(\hat{F})\Omega) = 4\pi i(J)\Omega$. Applying $\phi^*$ to both sides and using the fact that $\phi^*(i(\hat{F})\Omega) = i(\hat{F}_0)(\Omega \circ \phi)$, we obtain $(e_2)$.

To prove the first (existence) part of the theorem, we have to introduce special coordinates around $\phi W$. Because $\phi W$ is spacelike, the exponential map of the normal bundle of $\phi W$ in $U$ provides a diffeomorphism from a neighborhood of the zero section in the normal bundle onto a tubular neighborhood of $\phi W$ in $U$. We choose coordinates $\{x^1, x^2, x^3, x^4\}$ on $U$ such that $x^4 = 0$ on $\phi W$, the coordinate vector field $\partial_4$ is orthogonal to $\phi W$, and $\{x^\alpha\}_{\alpha=1}^3$ are coordinates on $\phi W$. In these coordinates, the metric takes the block-diagonal form with $g_{44} < 0$ (since $\phi W$ is spacelike).

Now $F_0$ on $\mathcal{W}$ is given. If $F$ is to satisfy $F \circ \phi = F_0$, then
$$
\phi^* F_0 = \phi^* F = (F_{\alpha\beta} \omega^\alpha \otimes \omega^\beta) \circ \phi,
$$
$$
\hat{F}_0 = (F^{ij} X_i \otimes X_j) \circ \phi.
$$

Making use of the relations $F_{\alpha\beta} = F^{\alpha\beta}$, $F_{\alpha 4} = -F^{\alpha 4}$, and so on, we see that $(e_1)$ and $(e_2)$ are, respectively, equivalent to:
\begin{align}
  F_{\alpha\beta|\gamma} + F_{\beta\gamma|\alpha} + F_{\gamma\alpha|\beta} &= 0 \quad \text{in } \mathcal{W}, \tag{ic_1}\\
  F_{4\alpha|\alpha} - 4\pi J_4 &= 0 \quad \text{in } \mathcal{W}. \tag{ic_2}
\end{align}

Next, we note that the homogeneous Maxwell equations $(a_0)$ are equivalent to the following two groups of equations:
\begin{align}
  F_{\alpha\beta|\gamma} + F_{\beta\gamma|\alpha} + F_{\gamma\alpha|\beta} &= 0, \tag{a_1}\\
  F_{\alpha\beta|4} + F_{\beta 4|\alpha} + F_{4\alpha|\beta} &= 0. \tag{a_2}
\end{align}

Similarly, the inhomogeneous Maxwell equations $(b_0)$ are equivalent to:
\begin{align}
  F_{4\alpha|\alpha} - 4\pi J_4 &= 0, \tag{b_1}\\
  F_{\alpha 4|4} - F_{\alpha\beta|\beta} + 4\pi J_\alpha &= 0. \tag{b_2}
\end{align}

Thus $(\mathrm{ic}_1)$ [respectively $(\mathrm{ic}_2)$] is just the restriction of $(a_1)$ [respectively $(b_1)$] to $\mathcal{W}$.

Noting that $\operatorname{div} J = 0$ is equivalent to
$$
g^{\alpha\beta}J_{\alpha|\beta} + g^{44}J_{4|4} + \text{(lower order terms)} = 0,
$$
we introduce $f = (F_{\alpha\beta})_{\alpha<\beta}$ and $j = (J_\alpha)$ as column vectors. Define three $(6 \times 6)$-matrices $a^1, a^2, a^3$ of $C^\infty$ functions by:
$$
a^\alpha = \begin{bmatrix}
0 & 0 & 0 & a_2^\alpha & -a_1^\alpha & 0 \\
0 & 0 & 0 & a_3^\alpha & 0 & -a_1^\alpha \\
0 & 0 & 0 & 0 & a_3^\alpha & -a_2^\alpha \\
a_2^\alpha & a_3^\alpha & 0 & 0 & 0 & 0 \\
-a_1^\alpha & 0 & a_3^\alpha & 0 & 0 & 0 \\
0 & -a_1^\alpha & -a_2^\alpha & 0 & 0 & 0
\end{bmatrix}
$$
for $\alpha = 1, 2, 3$, where the $a_\mu^\alpha$ are the coordinate components of the metric connection. Note that each $a^\alpha$ is symmetric. Then a short calculation shows that $(a_2)$ and $(b_2)$ are equivalent to the following matrix equation:
$$
\frac{\partial}{\partial x^4} f = a^\alpha \left( \frac{\partial}{\partial x^\alpha} f \right) + b f - 4\pi j,
$$
where $b$ is a $(6 \times 6)$-matrix of $C^\infty$ functions coming from zero-order terms, and the middle two terms are understood in the sense of matrix multiplication.

Since each $a^\alpha$ is symmetric, this is a symmetric hyperbolic system of partial differential equations in the sense of Friedrichs. Since $\{a^\alpha\}$, $b$, and $j$ are all $C^\infty$, the fundamental theorem of such systems guarantees that, given $j$ and the values of $f$ on the hypersurface $W$, a unique $C^\infty$ solution $f$ satisfying the initial values on $W$ exists in $U$ provided $U$ is sufficiently small. This proves the assertion.

Thus we have a unique $2$-form $F = F_{ij} \omega^i \otimes \omega^j$ satisfying Maxwell's equations on a sufficiently small neighborhood of $\phi W$ and matching the prescribed initial data $F_0$.
