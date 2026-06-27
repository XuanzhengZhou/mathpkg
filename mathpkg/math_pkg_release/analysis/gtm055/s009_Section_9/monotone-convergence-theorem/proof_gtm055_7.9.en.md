---
role: proof
locale: en
of_concept: monotone-convergence-theorem
source_book: gtm055
source_chapter: "7"
source_section: "9"
---

By hypothesis there exists a measurable set $X_0$ such that $\mu(X \setminus X_0) = 0$ and such that the sequence $\{f_n\}$ is defined, nonnegative, and monotone increasing pointwise on $X_0$. Clearly it suffices to prove the theorem with $X$ replaced by $X_0$, so we may, without loss of generality, assume that $X = X_0$. Let $f(x) = \lim_n f_n(x)$, $x \in X$. Denote by $E$ the set of points $x \in X$ where $f(x) < +\infty$, by $Y$ the complement where $f(x) = +\infty$, and let
$$\tilde{f}(x) = \begin{cases} f(x), & x \in E, \\ 0, & x \in Y. \end{cases}$$
Note that $E$, $Y$, and $\tilde{f}$ are all measurable (Prop. 6.2). Suppose first that $f$ is integrable $[\mu]$. Then $Y$ is a null set and $\int f d\mu = \int \tilde{f} d\mu$. The sequence $\{f_n \chi_E\}$ converges pointwise to $\tilde{f}$; by Proposition 7.2 the sequence $\{\int_E f_n d\mu\}$ is bounded.

Conversely, suppose the sequence of integrals $\{\int_X f_n d\mu\}$ is bounded above by some $M < +\infty$. If $f$ were not integrable, there would exist a measurable set $Z$ of positive measure and a subset $W$ with $\mu(W) < \mu(Z)/2$ and a positive integer $n_0$ such that $f_{n_0}(x) \geq 2M/\mu(Z)$ for all $x \in Z \setminus W$. But then
$$\int_X f_{n_0} d\mu \geq \int_{Z \setminus W} f_{n_0} d\mu \geq \frac{2M}{\mu(Z)}\mu(Z \setminus W) > M,$$
which is impossible. Thus $f$ is integrable and $\int_X f d\mu = \lim_n \int_X f_n d\mu$.
