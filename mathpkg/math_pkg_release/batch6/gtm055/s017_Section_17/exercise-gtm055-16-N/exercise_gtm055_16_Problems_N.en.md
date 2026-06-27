---
role: exercise
locale: en
chapter: "16"
section: "Problems"
exercise_number: "N"
---

Show that the sequence $\{\sigma_n\}_{n=1}^{\infty}$ of pseudonorms on $\mathcal{E}^*$ induces the weak$^*$ topology on every ball $(\mathcal{E}^*)_r$, $r > 0$, and use this fact to prove that the (relative) weak$^*$ topology on $(\mathcal{E}^*)_r$ is metrizable. Conclude that the (relative) weak$^*$ topology is metrizable and satisfies the second axiom of countability on bounded subsets of $\mathcal{E}^*$.

An explicit metric inducing the relative weak$^*$ topology on $(\mathcal{E}^*)_r$ is given by
$$\rho(f, g) = \sum_{n=1}^{\infty} \frac{1}{2^n} \frac{|f(x_n) - g(x_n)|}{1 + |f(x_n) - g(x_n)|}, \quad f, g \in (\mathcal{E}^*)_r.$$

Similarly the formula
$$\rho(x, y) = \sum_{n=1}^{\infty} \frac{1}{2^n} \frac{|f_n(x - y)|}{1 + |f_n(x - y)|}, \quad x, y \in \mathcal{E}_r,$$
defines explicitly a metric on the ball $\mathcal{E}_r$ that induces the relative weak topology there.

\textit{Hint:} The closed ball $(\mathcal{E}^*)_r$, $r > 0$, is compact in the weak$^*$ topology by Alaoglu's theorem (Th. 15.11).
