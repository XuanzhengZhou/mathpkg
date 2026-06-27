---
role: proof
locale: en
of_concept: proposition-18-1
source_book: gtm055
source_chapter: "18"
source_section: "Section 19_Section_19"
---

Proof. It is clear that $\|\xi\| = 0$ if and only if $\xi$ is the zero measure, and that, if $\xi$ is any complex Borel measure on $X$ and $\alpha$ is any complex number, then

$$\|\alpha\xi\| = |\alpha|\|\xi\|.$$ Moreover, if $\xi$ and $\zeta$ are two elements of $\mathcal{M}(X)$, and if $\{E_1, \ldots, E_p\}$ is any partition of $X$ into Borel sets, then

$$\sum_{i=1}^{p} |\xi(E_i) + \zeta(E_i)| \leq \sum_{i=1}^{p} |\xi(E_i)| + \sum_{i=1}^{p} |\zeta(E_i)| \leq \|\xi\| + \|\zeta\|.$$

and therefore $\|\xi + \zeta\| \leq \|\xi\| + \|\zeta\|$. Thus we have proved that $\|\xi\|$ is a norm on $\mathcal{M}(X)$. All that remains is to show that $\mathcal{M}(X)$ is complete in this norm.

Let $\{\xi_n\}$ be a sequence of complex Borel measures that is Cauchy in the total variation norm. Then for any one Borel set $E$ we have $|\xi_m(E) - \xi_n(E)| \leq \|\xi_m - \xi_n\|$, so $\{\xi_n\}$ converges setwise to a set function $\xi$ on the $\sigma$-ring $B$ of Borel subsets of $X$, and it is obvious that $\xi$ is finitely additive. Hence, to prove that $\xi$ is a complex Borel measure, it suffices to show that $\xi$ is semicontinuous (see Problem 7E). Let $\{E_n\}$ be an increasing sequence of Borel sets in $X$ with union $E$, and let $\varepsilon$ be a positive number. Choose $N$ such that $\|\xi_m - \xi_n\| < \varepsilon/3$ for $m, n \geq N$, and then choose $K$ such that $|\xi_N(E_k) - \xi_N(E)| < \varepsilon/3$ for all $k \geq K$. Then $\lim_{n \to \infty} |\xi_N(F) - \xi_n(F)| = |\xi_N(F) - \xi(F)| \leq

closed with respect to the formation of sums, let $\xi_1$ and $\xi_2$ be regular complex Borel measures on $X$, let $E$ be a Borel set, and let $\varepsilon$ be a positive number. Then there exist compact sets $K_1$ and $K_2$ and open sets $U_1$ and $U_2$ such that $K_i \subset E \subset U_i$ and $|\xi_i|(U_i \setminus K_i) < \varepsilon/2$, $i = 1, 2$. But then $K = K_1 \cup K_2 \subset E$, $E \subset U = U_1 \cap U_2$, and we have

$$|\xi_1 + \xi_2|(U \setminus K) \leq |\xi_1|(U \setminus K) + |\xi_2|(U \setminus K) < \varepsilon.$$

Thus $\mathcal{M}_0(X)$ is a linear manifold in $\mathcal{M}(X)$. We show next that $\mathcal{M}_0(X)$ is closed.

Let $\{\xi_n\}_{n=1}^{\infty}$ be a sequence in $\mathcal{M}_0(X)$ that converges to some limit $\xi$ in $\mathcal{M}(X)$. We must show that $\xi$ is regular. To this end let $E$ be a Borel set in $X$, let $\varepsilon$ be a positive number, and let $N$ be a positive integer such that $\|\xi_n - \xi\| < \varepsilon/3$ for all $n \geq N$, so that $\|\xi_n - \xi_m\| < 2\varepsilon/3$ for all $m, n \geq N$. Choose a compact set $K$ and an open set $U$ such that $K \subset E \subset U$ and such that $|\xi_N|(U \setminus K) < \varepsilon/3$. Then $|(|\xi_n| - |\xi_N|)(U \setminus K)| < 2\varepsilon/3$ for $n \geq N$ (see Problem A) and, letting $n

on $X$. Moreover, if we assume that $\mu_1$ and $\mu_2$ are regular signed Borel measures on $X$ such that

$$\text{Re } \varphi(f) = \int_X f \, d\mu_1 \quad \text{and} \quad \text{Im } \varphi(f) = \int_X f \, d\mu_2$$

(2)

for every $f$ in $\mathcal{C}_{\mathbb{R}}(X)$, then $\xi = \mu_1 + i\mu_2$ is a regular complex Borel measure, and $\varphi$ and $\varphi_\xi$ agree on the real functions in $\mathcal{C}(X)$ by (2). But then, of course, $\varphi = \varphi_\xi$ on all of $\mathcal{C}(X)$. (It should be noted, here and below, that since the space $X$ is compact by hypothesis, all (signed) Borel measures on $X$ are finite-valued, and are therefore complex Borel measures.) Thus it suffices to prove the following real version of the theorem.
