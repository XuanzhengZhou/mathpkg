---
role: proof
locale: en
of_concept: expansion-evolution-lemma
source_book: gtm048
source_chapter: "4"
source_section: "4.3"
---

Assume dust ($p = 0$) with irrotational comoving frame $Z$ and zero electromagnetic field. From Proposition 3.15.3 we have $D_Z Z = 0$ (observers in $Z$ are geodesics) and $\operatorname{div}(\rho Z) = 0$. Since $Z$ is irrotational, Proposition 2.3.5 implies $Z$ is locally synchronizable, and for all $X, W \perp Z$ we have $g(A_Z X, W) = g(X, A_Z W)$, where $A_Z X = -D_X Z$.

Let $\{X_1, X_2, X_3, Z\}$ be an orthonormal frame on an open set $\mathcal{U}$ with $X_\alpha \perp Z$. Write $D_{X_\alpha} Z = f_\alpha^\beta X_\beta$ for some functions $f_\alpha^\beta$ on $\mathcal{U}$. The symmetry condition $g(A_Z X_\alpha, X_\beta) = g(X_\alpha, A_Z X_\beta)$ gives $f_\beta^\alpha = f_\alpha^\beta$.

\textbf{Part (a).} Let $\{\omega^1, \omega^2, \omega^3, \omega\}$ be the dual basis to $\{X_1, X_2, X_3, Z\}$. Then

$$
\operatorname{div} Z = \omega^\alpha(D_{X_\alpha} Z) + \omega(D_Z Z) = g(D_{X_\alpha} Z, X_\alpha) = f_\alpha^\alpha = -\operatorname{trace} A_Z.
$$

Now compute $Z(\operatorname{div} Z)$:

$$
\begin{aligned}
Z(\operatorname{div} Z) &= Z\, g(D_{X_\alpha} Z, X_\alpha) \\
&= g(D_Z D_{X_\alpha} Z, X_\alpha) + g(D_{X_\alpha} Z, D_Z X_\alpha) \\
&= g(R_{Z X_\alpha} Z + D_{[Z, X_\alpha]} Z + D_{X_\alpha} D_Z Z, X_\alpha) + g(D_{X_\alpha} Z, D_Z X_\alpha).
\end{aligned}
$$

Since $D_Z Z = 0$, the term $D_{X_\alpha} D_Z Z$ vanishes. Using the definition of the Ricci tensor,

$$
g(R_{Z X_\alpha} Z, X_\alpha) = -\operatorname{Ric}(Z, Z).
$$

For the remaining terms: $g(D_{[Z, X_\alpha]} Z, X_\alpha) + g(D_{X_\alpha} Z, D_Z X_\alpha)$. Since $Z$ is irrotational, $g([Z, X_\alpha], Z) = 0$, so $[Z, X_\alpha]$ is orthogonal to $Z$ and $D_{[Z, X_\alpha]} Z = -A_Z([Z, X_\alpha])$. Moreover, using the symmetry $f_\beta^\alpha = f_\alpha^\beta$, one finds

$$
g(D_{[Z, X_\alpha]} Z, X_\alpha) + g(D_{X_\alpha} Z, D_Z X_\alpha) = -f_\alpha^\beta f_\beta^\alpha = -\operatorname{trace}(A_Z^2) \leq 0.
$$

Thus

$$
Z(\operatorname{div} Z) = -\operatorname{Ric}(Z, Z) - \operatorname{trace}(A_Z^2).
$$

Since $\operatorname{Ric}(Z, Z) > 0$ (from the Einstein field equation with $\rho > 0$) and $\operatorname{trace}(A_Z^2) \geq 0$, we obtain $Z(\operatorname{div} Z) < 0$.

\textbf{Part (b).} From $\operatorname{div}(\rho Z) = 0$ (Proposition 3.15.3), we have

$$
0 = \operatorname{div}(\rho Z) = Z\rho + \rho \operatorname{div} Z,
$$

hence $Z\rho = -\rho \operatorname{div} Z$.
