---
role: proof
locale: en
of_concept: maxwell-initial-value-theorem
source_book: gtm048
source_chapter: "3"
source_section: "3.11"
---

**Proof of Theorem 3.11.1.** Let us first dispose of the second statement. Suppose $(U, F, J)$ obeys Maxwell's equations. Since $F_0 = F \circ \phi$, $\phi^* F_0 = \phi^* F$, where the right side is just the usual pull-back of forms. Thus $0 = \phi^*(dF) = d(\phi^* F) = d(\phi^* F_0)$, which is $(e_1)$. Since $\operatorname{div} \hat{F} = 4\pi J$, Section 3.6.2 implies $d(i(\hat{F})\Omega) = 4\pi i(J)\Omega$. Applying $\phi^*$ to both sides and using the fact that $\phi^*(i(F)\Omega) = i(\hat{F}_0)(\Omega \circ \phi)$, we obtain $(e_2)$.

To prove the first part of the theorem, we introduce special coordinates around $\phi W$. Because $\phi W$ is spacelike, the exponential map of the normal bundle of $\phi W$ in $U$ gives coordinates $\{x^1, x^2, x^3, x^4\}$ on a neighborhood of $W$ such that: $\partial_4$ is orthogonal to $\partial_\alpha$ and $g(\partial_4, \partial_4) = 1$ (up to a sign convention); $\phi(W)$ is given by $x^4 = 0$; and on $\phi(W)$, the $x^\alpha$ for $\alpha = 1, 2, 3$ are coordinates.

Let $\omega^i$ be an orthonormal basis of 1-forms. The 2-form $F$ can be written as $F = F_{ij} \omega^i \otimes \omega^j$ (with $F_{ij} = -F_{ji}$). Now $F_0$ in $\mathcal{W}$ is given. If $F$ is to satisfy $F \circ \phi = F_0$, then
$$\phi^* F_0 = \phi^* F = (F_{\alpha \beta} \omega^\alpha \otimes \omega^\beta) \circ \phi,$$
$$\hat{F}_0 = (F^{ij} X_i \otimes X_j) \circ \phi.$$

Using $F_{\alpha \beta} = F^{\alpha \beta}$, $F_{\alpha 4} = -F_{\alpha 4}$, we see that $(e_1)$ and $(e_2)$ are, respectively, equivalent to:

($\text{ic}_1$) $F_{\alpha \beta | \gamma} + F_{\beta \gamma | \alpha} + F_{\gamma \alpha | \beta} = 0$ in $\mathcal{W}$,

($\text{ic}_2$) $F_{4 \alpha | \alpha} - 4\pi J_4 = 0$ in $\mathcal{W}$.

Next, we note that $(a_0)$ (Maxwell's first equation $dF = 0$) is equivalent to:

($a_1$) $F_{\alpha \beta | \gamma} + F_{\beta \gamma | \alpha} + F_{\gamma \alpha | \beta} = 0$,

($a_2$) $F_{\alpha \beta | 4} + F_{\beta 4 | \alpha} + F_{4 \alpha | \beta} = 0$.

Similarly, $(b_0)$ (Maxwell's second equation $\operatorname{div} \hat{F} = 4\pi J$) is equivalent to:

($b_1$) $F_{4 \alpha | \alpha} - 4\pi J_4 = 0$,

($b_2$) $F_{\alpha 4 | 4} - F_{\alpha \beta | \beta} + 4\pi J_\alpha = 0$.

Thus $(\text{ic}_1)$ [respectively $(\text{ic}_2)$] is just the restriction of $(a_1)$ [respectively $(b_1)$] to $\mathcal{W}$.

Noting that $\operatorname{div} J = 0 \Leftrightarrow g^{\alpha \beta} J_{\alpha | \beta} = 0$, and differentiating $(b_2)$ with respect to $x^4$ and substituting from $(a_2)$ and the divergence condition, one obtains a symmetric hyperbolic system. Specifically, define a six-component column vector $f = (F_{23}, F_{31}, F_{12}, F_{14}, F_{24}, F_{34})^t$ where $t$ denotes transpose. Define three $(6 \times 6)$-matrices $a^1, a^2, a^3$ of $C^\infty$ functions by:

$$a^\alpha = \begin{bmatrix}
0 & 0 & 0 & a_2^\alpha & -a_1^\alpha & 0 \\
0 & 0 & 0 & a_3^\alpha & 0 & -a_1^\alpha \\
0 & 0 & 0 & 0 & a_3^\alpha & -a_2^\alpha \\
a_2^\alpha & a_3^\alpha & 0 & 0 & 0 & 0 \\
-a_1^\alpha & 0 & a_3^\alpha & 0 & 0 & 0 \\
0 & -a_1^\alpha & -a_2^\alpha & 0 & 0 & 0
\end{bmatrix}$$

for $\alpha = 1, 2, 3$. Each $a^\alpha$ is symmetric. A short calculation shows that $(a_2)$ and $(b_2)$ are equivalent to the matrix equation:

$$\frac{\partial}{\partial x^4} f = a^\alpha \left( \frac{\partial}{\partial x^\alpha} f \right) + b f - 4\pi j,$$

where $b$ is a $(6 \times 6)$-matrix of $C^\infty$ functions coming from zero-order terms, and the middle two terms are understood in the sense of matrix multiplication. Since each $a^\alpha$ is symmetric, this is a symmetric hyperbolic system of partial differential equations in the sense of Friedrichs. Since $\{a^\alpha\}$, $b$, and $j$ are all $C^\infty$, the fundamental theorem of such systems guarantees that, given $j$ and the values of $f$ on the hypersurface $W$, a unique $C^\infty$ solution $f$ satisfying the initial values on $W$ exists in $U$ provided $U$ is sufficiently small (Lax and Friedrichs). This proves the assertion.

Thus we obtain a unique 2-form $F = F_{ij} \omega^i \otimes \omega^j$ satisfying the required properties.
