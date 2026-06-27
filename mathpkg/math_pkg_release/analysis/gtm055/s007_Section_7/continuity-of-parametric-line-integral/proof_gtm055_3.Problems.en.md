---
role: proof
locale: en
of_concept: continuity-of-parametric-line-integral
source_book: gtm055
source_chapter: "3"
source_section: "Problems"
---

Let $[a, b]$ and $[c, d]$ be the parameter intervals of $\alpha$ and $\beta$. Then $g(\alpha(s), \beta(t))$ is uniformly continuous on $Q = [a, b] \times [c, d]$. For $\varepsilon > 0$ there exists $\delta > 0$ such that $|g(\alpha(s), \beta(t)) - g(\alpha(s'), \beta(t'))| < \varepsilon$ whenever $|s - s'|, |t - t'| < \delta$. For $a \leq s, s' \leq b$ with $|s - s'| < \delta$,
$$\left| \int_{\beta} g(\alpha(s), \lambda) d\lambda - \int_{\beta} g(\alpha(s'), \lambda) d\lambda \right| \leq \int_c^d |g(\alpha(s), \beta(t)) - g(\alpha(s'), \beta(t))| \, |\beta'(t)| \, dt \leq L_{\beta} \varepsilon,$$
where $L_{\beta}$ is the length of $\beta$. This gives uniform continuity, hence continuity, of $f_1$ on $W_{\alpha}$. The argument for $f_2$ is symmetric.
