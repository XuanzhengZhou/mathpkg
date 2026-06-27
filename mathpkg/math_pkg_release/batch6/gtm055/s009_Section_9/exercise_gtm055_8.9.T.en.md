---
role: exercise
locale: en
chapter: "8"
section: "9"
exercise_number: T
---

Let $(X, \mathbf{S}, \mu)$ be a measure space and let $g$ be a nonnegative function on $X$ that is integrable $[\mu]$.

(i) Show that for an arbitrarily given positive number $\varepsilon$ there exists a measurable set $W$ such that $\int_W g d\mu < \varepsilon$ and such that $g$ is bounded on $X \setminus W$, and use this fact to conclude that for an arbitrarily given positive number $\varepsilon$ there exists a positive number $\delta$ such that $\mu(E) < \delta$ implies $\int_E g d\mu < \varepsilon$. (Hint: For each positive integer $N$ set
$$g_N(x) = \begin{cases} g(x), & g(x) \leq N, \\ 0, & g(x) > N, \end{cases}$$
and invoke the monotone convergence theorem.)

(ii) Use these observations to give another proof of the dominated convergence theorem (Th. 7.12). (Hint: First treat the case $\mu(X) < +\infty$ using Egorov's theorem; then employ the fact that the support of $g$ is $\sigma$-finite (Prob. J).)
