---
role: proof
locale: en
of_concept: mean-relative-acceleration-inequality
source_book: gtm048
source_chapter: "4"
source_section: "4.3"
---

Since $\operatorname{trace} \hat{E} = 0$ (Proposition 3.7.4),

$$
\operatorname{trace} \hat{G} = (\rho + p)\operatorname{trace}(Z \otimes Z) + p\operatorname{trace} \hat{g} + \operatorname{trace} \hat{E} = (\rho + p)g(Z, Z) + 4p = -(\rho + p) + 4p = 3p - \rho.
$$

From the Einstein field equation in $(2,0)$ form, the Ricci tensor satisfies $\operatorname{Ric} - \frac{1}{2}R \hat{g} = \hat{G}$, where $R = -\operatorname{trace} \hat{G} = \rho - 3p$ is the scalar curvature. Contracting with the unit timelike vector field $Q$ twice (i.e., evaluating on $(Q, Q)$) and using $g(Q, Q) = -1$:

$$
\operatorname{Ric}(Q, Q) + \frac{1}{2}R = \hat{G}(Q, Q).
$$

Thus

$$
\begin{aligned}
\operatorname{Ric}(Q, Q) &= \hat{G}(Q, Q) - \frac{1}{2}(\rho - 3p) \\
&= (\rho + p)g(Z, Q)^2 + p\,g(Q, Q) + \hat{E}(Q, Q) - \frac{1}{2}\rho + \frac{3}{2}p \\
&= (\rho + p)g(Z, Q)^2 - p + \hat{E}(Q, Q) - \frac{1}{2}\rho + \frac{3}{2}p \\
&= (\rho + p)g(Z, Q)^2 + \frac{1}{2}(p - \rho) + \hat{E}(Q, Q).
\end{aligned}
$$

Since $Q$ and $Z$ are both unit timelike and future-directed, the reverse Cauchy–Schwarz inequality gives $g(Z, Q)^2 \geq 1$, with equality if and only if $Q = Z$ (at the given point). Hence

$$
\operatorname{Ric}(Q, Q) \geq (\rho + p) + \frac{1}{2}(p - \rho) + \hat{E}(Q, Q) = \frac{1}{2}\rho + \frac{3}{2}p + \hat{E}(Q, Q).
$$

The mean relative-acceleration $\alpha$ of $Q$ is defined by $\alpha = -\frac{1}{3}\operatorname{Ric}(Q, Q)$. Therefore

$$
\alpha \leq -\frac{1}{3}\left(\frac{1}{2}\rho + \frac{3}{2}p + \hat{E}(Q, Q)\right) = -\frac{1}{6}(\rho + 3p) - \frac{1}{3}\hat{E}(Q, Q) < 0,
$$

since $\rho > 0$, $p \geq 0$, and $\hat{E}(Q, Q) \geq 0$. The inequality becomes an equality precisely when $g(Z, Q)^2 = 1$, i.e., when $Q_z = Z_z$ at the point $z \in U$.
