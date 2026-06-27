---
role: proof
locale: en
of_concept: riesz-representation-lp
source_book: gtm055
source_chapter: "17"
source_section: "18"
---

It follows immediately from the Holder inequality that for any function $g$ in $\mathcal{L}_q(X)$ the functional $\varphi_g$ defined by $\varphi_g(f) = \int_X f g d\mu$ is bounded and satisfies the inequality $\|\varphi_g\| \leq \|g\|_q$. The hard part is to show that if $\varphi$ is an arbitrary element of $\mathcal{L}_p(X)^*$, then there exists a function $g$ in $\mathcal{L}_q(X)$ such that $\varphi = \varphi_g$ and $\|\varphi\| = \|g\|_q$.

We treat first the case in which $\mu(X) < +\infty$. The set function $\nu(E) = \varphi(\chi_E)$, $E \in \mathbf{S}$, is a complex measure on the measurable space $(X, \mathbf{S})$. Indeed, the finite additivity of $\nu$ follows at once from the additivity of $\varphi$, and the countable additivity of $\nu$ is then a consequence of the continuity of $\varphi$. Moreover, it is obvious that $\nu$ is absolutely continuous $[\mu]$. Hence, by the Radon-Nikodym theorem, there exists a function $g$ such that $\nu(E) = \int_E g \, d\mu$ for every measurable set $E$. Thus we have

$$\varphi(\chi_E) = \int_X \chi_E g \, d\mu$$

for characteristic functions of measurable sets, and therefore, by linearity,

$$\varphi(s) = \int_X sg \, d\mu$$

for every measurable simple function $s$ on $X$.

By what has just been shown, we have $\varphi = \varphi_g$ on the dense linear manifold of simple functions in $\mathcal{L}_p(X)$, and therefore $\varphi = \varphi_g$ by continuity. Thus to complete the proof (in the case $\mu(X) < +\infty$) it suffices to verify that $g \in \mathcal{L}_q(X)$ and that $\|g\|_q \leq \|\varphi\|$.

Let $E_0$ be the set where $|g| > 0$, and define $h_0 = |g|^{q-1} \operatorname{sgn} \bar{g}$ on $E_0$ and $h_0 = 0$ elsewhere. Then $\varphi(h_0 \chi_{E_0}) = \int_{E_0} h_0 g d\mu = \int_{E_0} |g|^q d\mu$. But $|h_0| = |g|^{q-1}$, so $|h_0|^p = |g|^{pq-p} = |g|^q$. Consequently $\|h_0 \chi_{E_0}\|_p = [\int_{E_0} |g|^q d\mu]^{1/p}$, and therefore

$$\int_{E_0} |g|^q d\mu \leq \|\varphi\| \left[ \int_{E_0} |g|^q d\mu \right]^{1/p}.$$

From this it follows at once that $\|g \chi_{E_0}\|_q \leq \|\varphi\|$, and since this inequality holds independently of the choice of the bound $M$, we conclude that $\|g\|_q \leq \|\varphi\|$. Thus the theorem is proved in the case $\mu(X) < +\infty$.

For an arbitrary measure space, one uses a sequence of sets $E_n$ of finite measure exhausting $X$, patches together the corresponding functions $g_{E_n}$, and shows that $\varphi$ annihilates the complement, completing the proof.
