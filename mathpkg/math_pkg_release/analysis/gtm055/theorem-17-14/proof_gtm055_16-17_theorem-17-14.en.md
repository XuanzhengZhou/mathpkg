---
role: proof
locale: en
of_concept: theorem-17-14
source_book: gtm055
source_chapter: "16-17"
source_section: "Section 18_Section_18"
---

PROOF. The composition $(T \circ \Phi)(x) = T\Phi(x)$ is measurable along with $\Phi$, and since $\| T\Phi(x) \| \leq \| T \| \| \Phi(x) \|$, $x \in X$, it follows that $T \circ \Phi$ belongs to $\mathcal{L}_1(X; \mathcal{F})$ whenever $\Phi$ belongs to $\mathcal{L}_1(X; \mathcal{E})$. A direct calculation shows that if $\Sigma$ is a simple $\mathcal{E}$-valued mapping on $X$, say $\Sigma = \sum_{i=1}^{N} \chi_{E_i} v_i$, then $T \circ \Sigma$ is the simple $\mathcal{F}$-valued mapping $\sum_{i=1}^{N} \chi_{E_i} T v_i$. Hence if $\Sigma$ is integrable and $\mu(E_i) < +\infty$, $i = 1, \ldots, N$, then

$$\int_X (T \circ \Sigma) d\mu = \sum_{i=1}^{N} \mu(E_i) T v_i = T \left( \sum_{i=1}^{N} \mu(E_i) v_i \right) = T \left( \int_X \Sigma d\mu \right),$$

so the proposition is valid for integrable simple $\mathcal{E}$-valued mappings.

Finally, suppose $\Phi$ is an arbitrary element of $\mathcal{L}_1(X; \mathcal{E})$, and let $\{\Sigma_n\}$ be a sequence of integrable simple mappings converging to $\Phi$ as in Lemma 17.12. Then, in the first place, $\{\Sigma_n\}$ tends to $\Phi$ in $\mathcal{L}_1(X; \mathcal{E})$ by the dominated convergence theorem (see the proof of Proposition 17.13), and since $\|\int_X \Phi d\mu - \int_X \Sigma_n d\mu\| = \|\int_X (\Phi - \Sigma_n) d\mu\| \leq \|\Phi - \Sigma_n

I. Thus $\Omega$ is invariant under all rotations $R_{\gamma}$, $\gamma \in Z$, whence it follows that $\Omega$ is constant a.e. $[\theta]$. That is, there exists a complex number $\omega$ such that $\Omega = \omega$ a.e. $[\theta]$. (This may be seen in various ways. Suppose, for example, that the real function $g = \text{Re}(\Omega)$ is not essentially constant on $Z$. Then there exist real numbers $m$ and $m'$ where $m < m'$ such that $E = \{\zeta \in Z : g(\zeta) \leq m\}$ and $E' = \{\zeta \in Z : g(\zeta) \geq m'\}$ both have positive arc-length measure. Thus there exist real numbers $t$ and $t'$ and a positive number $h$ such that the intersection of $E$ with the arc $\{e^{iu} : t \leq u \leq t + h\}$ has arc-length measure greater than $h/2$, while the intersection of $E'$ with the congruent arc $\{e^{iu} : t' \leq u \leq t' + h\}$ likewise has arc-length measure greater than $h/2$ (see Problem 8F). But then it is impossible for $\Omega$ and $R_{\gamma}\Omega$ to be equal a.e. if we take for $\gamma$ the number $e^{i(t' - t)}$. Finally, to determine the value of $\omega$, we employ Example J to write

$$\int_Z \Omega d\theta = 2\pi \omega = \int_Z \left[ \int_Z f_{(\gamma)} d\theta \right] d\theta(\gamma) = 2\pi \int_Z f d\theta.$$

Thus $\omega = \int_Z f d\theta$, and, putting everything together, we see that

$$\int_Z f_{(\gamma)} d\theta(\gamma) = \int_Z f d\theta$$

for almost every $\gamma$ in $Z$ and for every $f$ in $\mathcal{L}_p(Z)$.

If $\gamma \rightarrow R_{\gamma}$ denotes the representation of $Z$ on $\mathcal

of $[a, b]$ and any numbers $\tau_i$ such that $t_{i-1} \leq \tau_i \leq t_i$, $i = 1, \ldots, N$, the sum

$$s = \sum_{i=1}^{N} [\alpha(t_i) - \alpha(t_{i-1})] \Phi(\tau_i)$$

is a Riemann–Stieltjes sum for $\Phi$ with respect to $\alpha$ based on $\mathcal{P}$. Further, a vector $r$ in $\mathcal{E}$ is the Riemann–Stieltjes integral of $\Phi$ over $[a, b]$ with respect to $\alpha$ (notation: $r = \int_a^b \Phi(t) d\alpha(t)$) if for each $\varepsilon > 0$ there exists $\delta > 0$ such that $\|r - s\| < \varepsilon$ for every Riemann–Stieltjes sum $s$ for $\Phi$ with respect to $\alpha$ based on an arbitrary partition $\mathcal{P}$ of $[a, b]$ such that mesh $\mathcal{P} < \delta$. (See Problem 1G for basic definitions.)

It is obvious that the Riemann–Stieltjes integral of $\Phi$ over $[a, b]$ with respect to $\alpha$ is unique if it exists, in which case we say that $\Phi$ is (Riemann–Stieltjes) integrable over $[a, b]$ with respect to $\alpha$. Just as in the case of scalar-valued functions, the mapping $\Phi$ in the integral $\int_a^b \Phi(t) d\alpha(t)$ is called the integrand, the function $\alpha$ the integrator.

**Example L.** Let $\alpha(t) \equiv t$, $a \leq t \leq b$. Then the integral $\int_a^b \Phi(t) d\alpha(t)$ is called the Riemann integral of $\Phi$ over $[a, b]$, and is denoted by

$$\int_a^b \Phi(t) dt,$$

whenever it exists.

**Example M.** If either the integrand $\Phi$ or the integrator $\alpha$ is constant on the closed interval

value of $\Phi$ at any finite number of points of the interval $[a, b]$, provided the changes are made at points of continuity of the integrator $\alpha$. In particular, if

$$\mathcal{P} = \{a = t_0 < \cdots < t_N = b\}$$

is a partition of $[a, b]$ such that the function $\alpha$ is continuous at each point $t_i, i = 1, \ldots, N$, and $\Sigma$ is a mapping of $[a, b]$ into $\mathcal{E}$ such that $\Sigma$ is constantly equal to some vector $v_i$ in each interval $(t_{i-1}, t_i), i = 1, \ldots, N$, then (irrespective of the values of $\Sigma$ at the points of $\mathcal{P}$) $\Sigma$ is Riemann–Stieltjes integrable with respect to $\alpha$ and

$$\int_a^b \Sigma(t) d\alpha(t) = \sum_{i=1}^{N} [\alpha(t_i) - \alpha(t_{i-1})] v_i.$$

The following fact is easily verified (see Problem P).
