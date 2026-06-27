---
role: exercise
locale: en
chapter: "8-9"
section: "Section 10_Section_10"
exercise_number: 21
---

U. (i) Let $\mu$ be a signed measure on a measurable space $(X, \mathbf{S})$, and let $E$ be a measurable set. Verify that

$$\mu_+(E) + \mu_-(E) = \sup \sum_{i=1}^{n} |\mu(E_i)|,$$

where the supremum is taken in $\mathbb{R}^n$ over all finite partitions $\{E_1, \ldots, E_n\}$ of $E$ into disjoint measurable subsets. Thus the total variation $|\mu|(E)$ of $\mu$ over $E$, defined to be the indicated supremum, is given by $\mu_+(E) + \mu_-(E)$. Verify that a measurable function $f$ on $(X, \mathbf{S})$ is integrable $[\mu]$ if and only if $f$ is integrable $[|\mu|]$, and that if $f$ is integrable $[\mu]$, then $|\int_X f d\mu| \leq \int_X |f| d|\mu|$. Show also that if $\{f_n\}$ is a sequence of measurable functions on $(X, \mathbf{S})$ that converges to a limit $f$ a.e. $[|\mu|]$, and if there exists a function $\varphi$ that is integrable $[\mu]$ such that $|f_n| \leq \varphi$ a.e. $[|\mu|]$ for every index $n$, then $\lim_n \int |f - f_n| d\mu = 0$ and $\lim_n \int f_n d\mu = \int f d\mu$. (In other words, the dominated convergence theorem is valid for signed measures.)

(ii) Prove Proposition 8.7 for a complex measure $\zeta$ on a measurable space $(X, \mathbf{S})$. (Hint: Show first that $|\zeta|$ is finitely additive.)

| $\zeta_x$| is the measure $\mu_L$ associated with the monotone increasing function $L$. (Hint: It suffices to show that $|\zeta_x|$ agrees with the measure associated with $L$ on sub-intervals of the form $[a, t]$, $a < t \leq b$ (Prob. A). This amounts
...
