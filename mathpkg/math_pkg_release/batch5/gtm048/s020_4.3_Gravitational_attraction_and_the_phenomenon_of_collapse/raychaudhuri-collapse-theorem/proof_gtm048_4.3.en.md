---
role: proof
locale: en
of_concept: raychaudhuri-collapse-theorem
source_book: gtm048
source_chapter: "4"
source_section: "4.3"
---

Assume the hypotheses: dust ($p = 0$), irrotational comoving frame $Z$, zero electromagnetic field, and $\gamma$ is an observer in $Z$ with $(\operatorname{div} Z)(\gamma(u_0)) < 0$ for some $u_0$. Suppose, for contradiction, that $\gamma$ has all of $\mathbb{R}$ as its domain.

From Lemma 4.3.3a we have

$$
Z(\operatorname{div} Z) = -\operatorname{Ric}(Z, Z) - \operatorname{trace}(A_Z^2).
$$

Since $Z$ is irrotational, $A_Z$ is symmetric with respect to the metric on $\operatorname{span}\{X_1, X_2, X_3\}$. For any symmetric $3 \times 3$ matrix, the Cauchy–Schwarz inequality yields $\operatorname{trace}(A_Z^2) \geq \frac{1}{3}(\operatorname{trace} A_Z)^2$. Using $\operatorname{div} Z = -\operatorname{trace} A_Z$, this becomes $\operatorname{trace}(A_Z^2) \geq \frac{1}{3}(\operatorname{div} Z)^2$. By the Einstein field equation with $\rho > 0$ and $p = 0$, we have $\operatorname{Ric}(Z, Z) > 0$. Hence

$$
Z(\operatorname{div} Z) < -\frac{1}{3}(\operatorname{div} Z)^2.
$$

In fact, a finer decomposition of $A_Z$ into its trace part and trace-free symmetric part (shear) gives the stronger inequality

$$
Z(\operatorname{div} Z) < -\frac{1}{2}(\operatorname{div} Z)^2.
$$

Set $f(u) = (\operatorname{div} Z)(\gamma(u))$ for $u \in \mathbb{R}$. Then $f$ is a smooth function on $\mathbb{R}$ satisfying

$$
\frac{df}{du} = Z(\operatorname{div} Z) \circ \gamma < -\frac{1}{2} f(u)^2.
$$

Since $f(u_0) < 0$, we have $c := 1/f(u_0) < 0$. For $u > u_0$, whenever $f(u) \neq 0$,

$$
\frac{d}{du}\left(\frac{1}{f(u)}\right) = -\frac{f'(u)}{f(u)^2} > \frac{1}{2}.
$$

Integrating from $u_0$ to $u$:

$$
\frac{1}{f(u)} - \frac{1}{f(u_0)} > \frac{1}{2}(u - u_0),
$$

so

$$
\frac{1}{f(u)} > \frac{1}{f(u_0)} + \frac{1}{2}(u - u_0) = c + \frac{1}{2}(u - u_0).
$$

The right-hand side is a linear function with slope $1/2$ and negative intercept $c < 0$. At $u^* = u_0 - 2c = u_0 - \frac{2}{f(u_0)}$, the right-hand side equals $0$. Since $1/f(u)$ is strictly increasing and $1/f(u_0) < 0$, there exists a unique $u_{\infty} \in (u_0, u^*]$ such that $\lim_{u \to u_{\infty}^-} 1/f(u) = 0^-$, i.e., $\lim_{u \to u_{\infty}^-} f(u) = -\infty$.

But $f$ is a smooth function on $\mathbb{R}$ by the assumption that $\gamma$ has $\mathbb{R}$ as domain, and a smooth function cannot tend to $-\infty$ at a finite value of its argument. This contradiction shows that $\gamma$ cannot have all of $\mathbb{R}$ as domain. Moreover, the blow-up time is bounded by

$$
u_{\infty} \leq u_0 - \frac{2}{f(u_0)} = u_0 + \frac{2}{|(\operatorname{div} Z)(\gamma(u_0))|}.
$$

In geometric terms: since $Z$ is irrotational, it is locally synchronizable (Proposition 2.3.5), so there exists a spacelike hypersurface $N$ through $x = \gamma(0)$ everywhere orthogonal to $Z$. The integral curves of $Z$ are geodesics orthogonal to $N$. The exponential map of the normal bundle of $N$ is nonsingular on the fibre over $x$ because $Z$ is nowhere zero. If $Y$ is the $(4,0)$-tensor field dual to the canonical volume element and $Y_0 = \exp_* Y$, then $\mathcal{L}_Z Y_0 = (\operatorname{div} Z) Y_0$, giving an equivalent description of $f = (\operatorname{div} Z) \circ \gamma$ as measuring the volume deformation along the flow.
