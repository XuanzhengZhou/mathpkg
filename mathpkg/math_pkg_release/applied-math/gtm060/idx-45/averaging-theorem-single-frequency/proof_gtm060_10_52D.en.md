---
role: proof
locale: en
of_concept: averaging-theorem-single-frequency
source_book: gtm060
source_chapter: "10"
source_section: "52D"
---

In place of the variables $I$ we introduce new variables $P$

$$P = I + \varepsilon k(I, \varphi),$$

where the function $k$, $2\pi$-periodic in $\varphi$, will be chosen so that $P$ satisfies a simpler differential equation.

By the original equations, the rate of change of $P(t)$ is

$$\dot{P} = \dot{I} + \varepsilon \frac{\partial k}{\partial I} \dot{I} + \varepsilon \frac{\partial k}{\partial \varphi} \dot{\varphi} = \varepsilon \left[ g(I, \varphi) + \frac{\partial k}{\partial \varphi} \omega(I) \right] + \varepsilon^2 \frac{\partial k}{\partial I} g + \varepsilon^2 \frac{\partial k}{\partial \varphi} f.$$

We assume that the substitution can be inverted, so that

$$I = P + \varepsilon h(P, \varphi, \varepsilon)$$

where the functions $h$ are $2\pi$-periodic in $\varphi$. Then $\dot{P}$ satisfies

$$\dot{P} = \varepsilon \left[ g(P, \varphi) + \frac{\partial k}{\partial \varphi} \omega(P) \right] + R,$$

where the remainder term $R$ is small of second order with respect to $\varepsilon$:

$$|R| < c_2 \varepsilon^2, \quad c_2(c_1, c_3, c_4) > 0,$$

provided that $\|\omega\|_{C^2} < c_1$, $\|f\|_{C^2} < c_1$, $\|g\|_{C^2} < c_1$, $\|k\|_{C^2} < c_3$, $\|h\|_{C^2} < c_4$.

We now choose $k$ so that the term involving $\varepsilon$ becomes zero. For $k$ we obtain the equation

$$\frac{\partial k}{\partial \varphi} = -\frac{1}{\omega} g.$$

In general, such an equation is not solvable in the class of functions $k$ periodic in $\varphi$, because the average value (with respect to $\varphi$) of the left-hand side is always zero while the right-hand side need not have zero average. We therefore split $g$ into its mean $\bar{g}$ and the oscillatory part $\tilde{g} = g - \bar{g}$, and choose $k$ to satisfy

$$\frac{\partial k}{\partial \varphi} = -\frac{1}{\omega} \tilde{g}.$$

Since $\tilde{g}$ has zero mean with respect to $\varphi$, the equation is solvable. We then obtain

$$\dot{P} = \varepsilon \bar{g}(P) + R.$$

**Lemma (Invertibility of the change of variables).** For sufficiently small $\varepsilon$, the map $I \mapsto I + \varepsilon k(I, \varphi)$ in the region $G - \alpha$ (consisting of points whose $\alpha$-neighborhood is contained in $G$) is a diffeomorphism. The inverse diffeomorphism in the region $G - 2\alpha$ satisfies $\|h\|_{C^2} < c_4$ with some constant $c_4(\alpha, c_3) > 0$.

*Proof of Lemma.* The necessary estimate follows from the implicit function theorem. The only difficulty is to verify that the map is one-to-one. The function $k$ satisfies a Lipschitz condition (with some constant $L(\alpha, c_3)$) in $G - \alpha$. Consider two points $I_1, I_2$ in $G - \alpha$. For sufficiently small $\varepsilon$ (namely, for $L\varepsilon < 1$) the distance between $\varepsilon k(I_1)$ and $\varepsilon k(I_2)$ will be smaller than $|I_1 - I_2|$. Therefore, $I_1 + \varepsilon k(I_1) \neq I_2 + \varepsilon k(I_2)$, so the map is one-to-one on $G - \alpha$.

It follows from the lemma that for $\varepsilon$ small enough all the estimates are satisfied.

We now compare the differential equations for $J$ and $P$:

$$\dot{J} = \varepsilon \bar{g}(J), \qquad \dot{P} = \varepsilon \bar{g}(P) + R.$$

Since the difference between the right-hand sides is of order $\lesssim \varepsilon^2$, for time $t \lesssim 1/\varepsilon$ the difference $|P - J|$ between the solutions is of order $\varepsilon$. On the other hand, $|I - P| = \varepsilon |k| \lesssim \varepsilon$.

Set $z = P - J$. Then

$$|\dot{z}| \leq c_5 \varepsilon |z| + c_2 \varepsilon^2.$$

**Lemma (Gronwall-type inequality).** If $|\dot{z}| \leq a |z| + b$ and $|z(0)| < d$ for $a, b, d, t > 0$, then $|z(t)| \leq (d + bt)e^{at}$.

*Proof.* $|z(t)|$ is no greater than the solution $y(t)$ of $\dot{y} = ay + b$, $y(0) = d$. Solving this equation, we find $y = Ce^{at}$, $\dot{C}e^{at} = b$, $\dot{C} = e^{-at}b$, $C(0) = d$, $C \leq d + bt$.

Applying this lemma with $a = c_5 \varepsilon$, $b = c_2 \varepsilon^2$, $d = c_3 \varepsilon$, we obtain, for $0 \leq t \leq 1/\varepsilon$,

$$|z(t)| < (c_3 \varepsilon + c_2 \varepsilon^2 t) e^{c_5 \varepsilon t} \leq (c_3 \varepsilon + c_2 \varepsilon) e^{c_5} = c_7 \varepsilon, \quad c_7 = (c_3 + c_2) e^{c_5}.$$

If $\alpha = d/3$ and $\varepsilon$ is small enough, the entire segment $(P(t), J(t))$ ($t \leq 1/\varepsilon$) lies inside $G - \alpha$ and therefore

$$|P(t) - J(t)| < c_8 \varepsilon \quad \text{for all } 0 \leq t \leq 1/\varepsilon.$$

On the other hand, $|P(t) - I(t)| < |\varepsilon k| < c_3 \varepsilon$. Thus, for all $t$ with $0 \leq t \leq 1/\varepsilon$,

$$|I(t) - J(t)| < c_9 \varepsilon, \quad c_9 = c_8 + c_3 > 0,$$

and the theorem is proved.
