---
role: exercise
locale: en
chapter: "3"
section: "Problems"
exercise_number: L
---
Let $U$ and $V$ be open subsets of $\mathbb{C}$, and let $\alpha$ and $\beta$ be rectifiable arcs lying in $U$ and $V$, respectively. Let $W_{\alpha}$ and $W_{\beta}$ denote the ranges of $\alpha$ and $\beta$, and let $g(\zeta, \lambda)$ be a continuous complex-valued function (of two variables) on $W_{\alpha} \times W_{\beta}$. Show that the function
$$f_1(\zeta) = \int_{\beta} g(\zeta, \lambda) \, d\lambda$$
is continuous on $W_{\alpha}$, and likewise that the function
$$f_2(\lambda) = \int_{\alpha} g(\zeta, \lambda) \, d\zeta$$
is continuous on $W_{\beta}$.

Show further that
$$\int_{\alpha} \left[ \int_{\beta} g(\zeta, \lambda) \, d\lambda \right] d\zeta = \int_{\beta} \left[ \int_{\alpha} g(\zeta, \lambda) \, d\zeta \right] d\lambda.$$

(Hint: If $[a, b]$ and $[c, d]$ denote, respectively, the parameter intervals of $\alpha$ and $\beta$, then the function $g(\alpha(s), \beta(t))$ is (uniformly) continuous on the closed rectangle $Q = [a, b] \times [c, d]$. Hence for a given positive $\varepsilon$ there exists a positive $\delta$ such that
$$|g(\alpha(s), \beta(t)) - g(\alpha(s'), \beta(t'))| < \varepsilon$$
for all $(s, t), (s', t')$ in $Q$ such that $|s - s'|, |t - t'| < \delta$. Verify that if $a \leq s, s' \leq b$ and $|s - s'| < \delta$, then
$$\left| \int_{\beta} g(\alpha(s), \lambda) \, d\lambda - \int_{\beta} g(\alpha(s'), \lambda) \, d\lambda \right| \leq L_{\beta} \varepsilon,$$
where $L_{\beta}$ denotes the length of $\beta$; see Problem D(ii).)
