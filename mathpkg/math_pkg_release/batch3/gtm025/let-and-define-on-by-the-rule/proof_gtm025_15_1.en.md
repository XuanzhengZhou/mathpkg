---
role: proof
locale: en
of_concept: "let-and-define-on-by-the-rule"
source_book: gtm025
source_chapter: "Lp Spaces"
source_section: "15.1"
---

By Hölder's inequality (13.4) we have

$$|L_g(f)| \leq \|f\|_p \|g\|_{p'}.$$

Thus $L_g$ is a bounded linear functional on $\mathfrak{L}_p$ [the linearity of $L_g$ is obvious], and

$$\|L_g\| \leq \|g\|_{p'}.$$

In fact, equality holds here, i.e., $\|L_g\| = \|g\|_{p'}$. To see this, let $f$ be $|g|^{p'-1}$ sgn $(g)$; then we have $|f|^p = |g|^{p'}$. Thus $f$ is in $\mathfrak{L}_p$, and

$$\|f\|_p = \|g\|_{p'}^{\frac{p'}{p}} = \|g\|_{p'}^{p'-1}.$$

Hence the equalities

$$L_g(f) = \int f \bar{g} \, d\mu = \int |g|^{p'-1} \text{sgn}(g) \bar{g} \, d\mu = \int |g|^{p'} \, d\mu$$

$$= \|g\|_{p'}^{p'} = \|g\|_{p'}^{p'-1} \|g\|_{p'} = \|f\|_p \|g\|_{p'}$$

hold, and so also $\|L_g\| \geq \|g\|_{p'}$. Hence we have $\|L_g\| = \

ative is

$$\Phi'(x) = -\frac{p}{x^{p+1}} \left[ (1+x)^{p-1} + (1-x)^{p-1} - 2^{p-1} \right].$$

Write $\alpha = p - 1$ [note that $\alpha \geq 1$], and consider the function $\Psi$ defined by

$$\Psi(x) = (1+x)^{\alpha} + (1-x)^{\alpha} - 2^{\alpha}.$$

We have

$$\Psi'(x) = \alpha(1+x)^{\alpha-1} - \alpha(1-x)^{\alpha-1} \geq 0 \quad \text{for} \quad 0 < x < 1.$$

Thus $\Psi$ is a nondecreasing function on $[0, 1]$, and since $\Psi(1) = 0$, the mean value theorem implies that $\Psi(x) \leq 0$ for $0 \leq x \leq 1$. Going back to (2), we infer that $\Phi'(x) \geq 0$ for $0 < x < 1$, and since $\Phi(1) = 0$, $\Phi(x)$ is nonpositive for $0 < x < 1$. The definition (1) shows that $F(x)$ is also nonpositive for $0 < x < 1$. $\square$
