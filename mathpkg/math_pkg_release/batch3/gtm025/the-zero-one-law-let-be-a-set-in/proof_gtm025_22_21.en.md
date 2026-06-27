---
role: proof
locale: en
of_concept: "the-zero-one-law-let-be-a-set-in"
source_book: gtm025
source_chapter: "Further Topics"
source_section: "22.21"
---

Consider the function $f = \xi_U$ and form the functions $f_n$ as in (22.16.i). For all $n$ and all $(t_1, \ldots, t_n)$ and $(t'_1, \ldots, t'_n)$ in $T_{\Omega_n}$, the points $(t_1, \ldots, t_n, u_{n+1}, u_{n

Thus $f'_n$ is a Lebesgue-Radon-Nikodym derivative of $\eta$ with respect to $\mu$ for $M^{(n)}$, and (20.59) implies that $\lim_{n \to \infty} f'_n(t) = f_0(t)$ exists and is a Lebesgue-Radon-Nikodym derivative of $\eta$ with respect to $\mu$ on $M_0$.

Since $f_0$ is $M_0$-measurable and $\mu$ assumes only the values 0 and 1 on $M_0$, it is easy to see that there is a number $\alpha$ such that $f_0(t) = \alpha$ for all $t$ in a set of $\mu$-measure 1. Thus we have

$$\eta(T) = \int_T f d\mu = \int_T f_0 d\mu = \alpha,$$

and so (i) is proved. $\square$

(22.23) Exercise. Let $f$ be an $M$-measurable complex-valued function such that

(i) $f(u_1, u_2, \ldots, u_n, t_{n+1}, t_{n+2}, \ldots) = f(v_1, v_2, \ldots, v_n, t_{n+1}, t_{n+2}, \ldots)$ for all positive integers $n$ and all choices of $u_1, u_2, \ldots, u_n$ and $v_1, v_2, \ldots, v_n$.

Prove that $f$ is a constant $\mu$-a.e. [Hint. Use the argument of (22.21).]

(22.24) Remarks. Theorems (22.14), (22.17), and (22.22) assume a particularly simple form for functions that are products of functions depending on a single coordinate. Making no effort to be exhaustive, we list a few examples.

(a) Let $\Gamma$ be an arbitrary infinite index set, let $\Omega$ be a nonvoid finite subset of $\Gamma$, and let $f_\gamma$ be a function in $\mathfrak{L}_1(T_\gamma

(d) Nothing like (iii) holds for uncountable products even if we consider the completed measure space $(T, \bar{M}, \bar{\mu})$. For example, suppose that $\bar{\Gamma} > \aleph_0$ and $T_\gamma = [0, 1]$ for all $\gamma \in \Gamma$. For each $\gamma$, let $E_\gamma$ be $\lambda$-measurable, $E_\gamma \subsetneq [0, 1]$, and $\lambda(E_\gamma) = 1$. Then $\prod_{\gamma \in \Gamma} E_\gamma$ is not measurable in the product space in which each coordinate has Lebesgue measure. For a proof of this rather delicate fact, see Hewitt and Ross, Abstract Harmonic Analysis I [Springer-Verlag Heidelberg 1963], p. 228. Also, for general $(T_\gamma, \mathcal{M}_\gamma, \mu_\gamma)$, if $\bar{\Gamma} > \aleph_0$, if $A_\gamma \in \mathcal{M}_\gamma$, and $\mu_\gamma(A_\gamma) < 1$ for uncountably many $\gamma$'s, then $\bar{\mu}(\prod_{\gamma \in \Gamma} A_\gamma) = 0$. This is very simple to show, and we omit the argument.

We continue with a fact (22.26) related to but not dependent on (22.21), for which an elementary lemma is needed. Lemma (22.26) is of independent interest and is also needed in the proof of (22.31).
