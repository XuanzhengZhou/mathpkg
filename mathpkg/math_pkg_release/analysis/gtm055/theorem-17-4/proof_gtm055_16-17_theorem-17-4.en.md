---
role: proof
locale: en
of_concept: theorem-17-4
source_book: gtm055
source_chapter: "16-17"
source_section: "Section 18_Section_18"
---

PROOF. It follows immediately from the Hölder inequality (see Problem A) that for any function $g$ in $\mathcal{L}_q(X)$ the functional $\varphi_g$ defined by (5) is bounded and satisfies the inequality $\|\varphi_g\| \leq \|g\|_q$. The hard part is to show that if $\varphi$ is an arbitrary element of $\mathcal{L}_p(X)^*$, then there exists a function $g$ in $\mathcal{L}_q(X)$ such that $\varphi = \varphi_g$ and $\|\varphi\| = \|g\|_q$.

We treat first the case in which $\mu(X) < +\infty$. The set function $\nu(E) = \varphi(\chi_E), E \in \mathbf{S}$, is a complex measure on the measurable space $(X, \mathbf{S})$. Indeed, the finite additivity of $\nu$ follows at once from the additivity of $\varphi$, and the countable additivity of $\nu$ is then a consequence of the continuity of $\varphi$ (see Problem D). Moreover, it is obvious that $\nu$ is absolutely continuous $[\mu]$. Hence, by the Radon–Nikodym theorem (Prob. 9L), there exists a function $g$ such that $\nu(E) = \int_E g \, d\mu$ for every measurable set $E$. Thus we have

$$\varphi(\chi_E) = \int_X \chi_E g \, d\mu$$

for characteristic functions of measurable sets, and therefore, by linearity,

$$\varphi(s) = \int_X sg \, d\mu$$

for every measurable simple function $s$ on $X$.

Suppose now that $g$ belongs to $\mathcal{L}_q(X)$ and that $\varphi_g$ is the functional defined in (5). By what has just been shown, we have $\varphi = \varphi_g$ on the dense linear manifold of simple functions in $\mathcal{L}_p(X)$ (Prob. D), and therefore $\varphi = \varphi_g$ by continuity. Thus to complete the proof (in the case $\mu(X) < +\infty$) it suffices to verify that $g \in L_q(X)$ and that $\|g\|_q \leq \|\varphi\|

we obtain

$$\varphi(h_0 \chi_{E_0}) = \int_{E_0} h_0 g d\mu = \int_{E_0} |g|^q d\mu.$$

But $|h_0| = |g|^{q-1}$, so $|h_0|^p = |g|^{pq-p} = |g|^q$. Consequently

$$\|h_0 \chi_{E_0}\|_p = \left[ \int_{E_0} |g|^q d\mu \right]^{1/p},$$

and therefore

$$\int_{E_0} |g|^q d\mu \leq \|\varphi\| \left[ \int_{E_0} |g|^q d\mu \right]^{1/p}.$$

From this it follows at once that $\|g \chi_{E_0}\|_q \leq \|\varphi\|$ (recall that $1 - (1/p) = 1/q$), and since this inequality holds independently of the choice of $M$, we conclude that $\|g\|_q \leq \|\varphi\|$. Thus the theorem is proved in the case $\mu(X) < +\infty$.

Suppose now that $(X, S, \mu)$ is an arbitrary measure space. If $E$ is a measurable subset of $X$, then the subspace $\mathcal{L}_E$ of $\mathcal{L}_p(X, S, \mu)$ consisting of the functions $f$ in $\mathcal{L}_p(X)$ that vanish outside $E$ may be identified with the Lebesgue space $\mathcal{L}_p(E, S_E, \mu|E)$ (Prob. E). Consequently, if $\varphi$ is a bounded linear functional on $\mathcal{L}_p(X, S, \mu)$ and if $E$ is any measurable subset of $X$ having finite measure, then by the case already treated there exists a function $g_E$ in $\mathcal{L}_q(E, S_E, \mu|E)$ such that

$$\varphi(f) = \int_E fg_E d\mu$$

for all $f$ in $\mathcal{L}_E$. Moreover, as has been shown, the

from which it follows that $\{g_n\}$ is Cauchy, and therefore convergent, in $\mathcal{L}_q(X)$. Let $g$ denote the function in $\mathcal{L}_q(X)$ to which $\{g_n\}$ converges, and suppose $f$ is a function in $\mathcal{L}_p(X)$ that vanishes outside the set $E_m$. Then $fg_n = fg_m$ a.e. $[\mu]$ for $n \geq m$, while

$$\int_X fg_n d\mu \rightarrow \int_X fg d\mu.$$

It follows that $\varphi_g(f) = \varphi(f)$ provided only that $f$ vanishes outside some one of the sets $E_m$. Hence, by continuity, $\varphi_g$ and $\varphi$ agree on $\mathcal{L}_{E_0}$ (Prob. D). On the other hand, it is clear that $g$ vanishes a.e. on the complement $X \setminus E_0$ (Prob. C). Thus the proof will be complete if we show that $\varphi$ annihilates the subspace $\mathcal{L}_{X \setminus E_0}$.

Suppose, on the contrary, that there is some function $f$ in $\mathcal{L}_p(X)$ such that $f$ vanishes on $E_0$ and $\varphi(f) \neq 0$. Since the support of $f$ is $\sigma$-finite (Prob. 7J), it is easily seen that there is a set $F$ of finite measure such that $F$ is disjoint from $E_0$ and such that $\varphi(f\chi_F) \neq 0$, from which it follows that $\|g_F\|_q > 0$. Set $G_n = E_n \cup F$. Then for sufficiently large $n$ we must have

$$\|g_{G_n}\|_q^2 = \int_{E_n} |g_{E_n}|^q d\mu + \int_F |g_F|^q d\mu > a^q,$$

a manifest contradiction, and the proof is complete.

**Example H.** Let $(X, S, \mu)$ be a measure space, and let $p$ and $q$ be Hölder

formula defines a distinguished bilinear functional on $\mathcal{L}_2(X)$, and the existence of this bilinear functional is of profound importance in the study of such spaces.

A variation of the above formula obtained by writing

$$\langle f, g \rangle = \int_X f g d\mu, \quad f, g \in \mathcal{L}_2(X),$$

defines a sesquilinear functional on $\mathcal{L}_2(X)$ (Ch. 2, p. 22), called an inner product, that turns $\mathcal{L}_2(X)$ into a Hilbert space. The study of Hilbert spaces and operators on them is undertaken in Volume II of this treatise.

A brief examination of the argument employed in Theorem 17.5 shows that the proof goes through without substantial change for $p = 1$ when $\mu(X) < +\infty$, so that we may identify $\mathcal{L}_1(X, S, \mu)^*$ with $\mathcal{L}_\infty(X, S, \mu)$ in the usual way in this case. A standard argument permits us to improve on this result somewhat.
