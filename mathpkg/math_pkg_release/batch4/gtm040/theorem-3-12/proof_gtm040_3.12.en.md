---
role: proof
locale: en
of_concept: theorem-3-12
source_book: gtm040
source_chapter: "3"
source_section: "12"
---

**Proof:** Failure of almost-everywhere convergence means that there exists a set of points $\omega$ of positive measure for which the sequence diverges. At least one of two things must happen. Either $\mathbf{f}_n(\omega)$ for each fixed $\omega$ in a set of positive measure oscillates infinitely often above and below rationals $r(\omega)$ and

But lim inf $|\mathbf{f}_n(\omega)| = +\infty$ on $E$, and $E$ has positive measure $m$. Thus the left side of the inequality is infinite, and we have arrived at a contradiction.

(2) Suppose $\mathbf{f}_n(\omega)$ oscillates infinitely often above and below rationals $r(\omega)$ and $s(\omega)$ on a set of positive measure $m$. Order the set of all pairs of rationals (which is a denumerable set) and call the $k$th pair $q_k$. Consider the denumerable family of sets $A_k$ defined by $A_k = \{\omega | \mathbf{f}_n(\omega)\}$ oscillates infinitely often above and below the rationals of the pair $q_k$.

It is possible for more than one set to have the same point in it, but, on the other hand, every point $\omega$ for which $\mathbf{f}_n(\omega)$ oscillates infinitely often is in some $A_k$. Therefore,

$$\sum \mu(A_k) \geq \mu(\bigcup A_k) = m > 0$$

and there must exist a $t$ for which $\mu(A_t) > 0$. That is, for every $\omega$ in a set $A_t$ of positive measure, $\mathbf{f}_n(\omega)$ oscillates infinitely often above and below fixed rationals $r$ and $s$ with $r < s$. Let $\beta_n(\omega)$ be the number of upcrossings of $[r, s]$ by $\mathbf{f}_0(\omega), \ldots, \mathbf{f}_n(\omega)$. By Proposition 3-11,

$$\mathbf{M}[\beta_n] \leq \frac{\mathbf{M}[|\mathbf{f}_n|] + |r|}{s - r}$$

$$\leq \frac{K + |r|}{s - r}$$

$$= c \quad \text{for every } n.$$

Furthermore, the $\beta_n$ are non-negative and increasing with $n$ to a function $\beta$, so that $\mathbf{M}[\beta] = \lim \mathbf{M}[\beta_n] \leq c$ by the Monotone Convergence Theorem. But

A random time which is finite almost everywhere is called a random stopping time or simply a stopping time. If $t$ is a stopping time, then the set $\bigcap_{n=1}^{\infty} \{\omega \mid t(\omega) \geq n\}$ has measure zero. If $\{f_n\}$ is a sequence of random variables, we define a function $f_t$ almost everywhere by

$$f_t(\omega) = f_n(\omega) \quad \text{if} \quad t(\omega) = n.$$

Since

$$\{\omega \mid f_t(\omega) < c\} = \bigcup_{n=1}^{\infty} \left(\{\omega \mid t(\omega) = n\} \cap \{\omega \mid f_n(\omega) < c\}\right),$$

$f_t$ is a random variable.

Lemma 3-14: If $(f_n, \mathcal{R}_n)$ is a martingale and if $t$ is a stopping time for which $\int_{\Omega} f_t d\mu$ exists, then for any $n$

$$\int_{\Omega} f_t d\mu = \int_{\{t \leq n\}} f_n d\mu + \int_{\{t > n\}} f_t d\mu.$$

Proof: We have

$$\int_{\Omega} f_t d\mu = \sum_{k=0}^{n} \int_{\{t = k\}} f_t d\mu + \int_{\{t > n\}} f_t d\mu$$

$$= \sum_{k=0}^{n} \int_{\{t = k\}} f_k d\mu + \int_{\{t > n\}} f_t d\mu,$$

which by Lemma 3-6

$$= \sum_{k=0}^{n} \int_{\{t = k\}} f_n d\mu + \int_{\{t > n\}} f_t d\mu$$

$$= \int_{\{t \leq n\}} f_n d\mu + \int_{\{t > n\}} f_t d\mu.$$

Theorem 3-15: If $(f_n, \mathcal{R}_n)$ is a martingale and if $t$ is a stopping

PROOF OF THEOREM: By (1), $\int_{\Omega} f_t d\mu$ exists, so that Lemma 3-14 applies. Thus, for any $n$,

$$\int_{\Omega} f_t d\mu = \int_{\{t \leq n\}} f_n d\mu + \int_{\{t > n\}} f_t d\mu$$

$$= \int_{\Omega} f_n d\mu - \int_{\{t > n\}} f_n d\mu + \int_{\{t > n\}} f_t d\mu,$$

which by Lemma 3-10

$$= \int_{\Omega} f_0 d\mu - \int_{\{t > n\}} f_n d\mu + \int_{\{t > n\}} f_t d\mu.$$

Using condition (1) together with Corollary 1-17 and the complete additivity of the integral as a set function, we see that

$$\lim_{n \to \infty} \int_{\{t > n\}} f_t d\mu = 0.$$

Since $\int_{\{t > n\}} f_n d\mu \to 0$ by hypothesis, we have $\int_{\Omega} f_t d\mu = \int_{\Omega} f_0 d\mu$.

Corollary 3-16: Suppose $(f_n, \mathcal{R}_n)$ is a martingale defined on a space $\Omega$ of finite total measure and $t$ is a stopping time. If $|f_n| \leq K$ for all $n$, then $M[f_t] = M[f_0]$.

PROOF: We must show the two conditions of Theorem 3-15 are satisfied. For (1) we have $|f_t| \leq K$ by definition, and hence $f_t$ is integrable. For (2) we have

$$\left| \int_{\{t > n\}} f_n d\mu \right| \leq \int_{\{t > n\}} |f_n| d\mu$$

$$\leq \int_{\{t > n\}} K d\mu$$

$$= K\mu(\{\omega | t(\omega) > n

Corollary 3-16 give sufficient criteria for the game still to be fair. Corollary 3-16 by itself is a general result; it covers the situation, for example, where the game stops if either the player or the house goes bankrupt. If the game does stop under such circumstances, the corollary states that the fairness of the game is not altered by any gambling system whatsoever. Similar remarks apply to supermartingales. If the amount of money that a player has is limited, no system that he adopts for stopping according to how the game is going will make an unfair game favorable.

The following proposition is useful in proving that certain random times are stopping times.
