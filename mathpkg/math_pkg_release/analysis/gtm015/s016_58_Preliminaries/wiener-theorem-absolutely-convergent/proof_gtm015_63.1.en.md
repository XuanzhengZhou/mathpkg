---
role: proof
locale: en
of_concept: wiener-theorem-absolutely-convergent
source_book: gtm015
source_chapter: "63"
source_section: "Wiener's theorem"
---

# Proof of Wiener's theorem on absolutely convergent Fourier series

Proof. (i) From the inequality

$$\left| \sum_{n=-\infty}^{\infty} x(n) \mu^n \right| \leq \sum_{n=-\infty}^{\infty} |x(n) \mu^n| = \sum_{n=-\infty}^{\infty} |x(n)| = \|x\|_1,$$

it is clear that (*) defines a continuous linear form on $l^1(\mathbb{Z})$. In particular,

$$f_{\mu}(e_n) = \mu^n \quad (n \in \mathbb{Z}),$$

therefore

$$f_{\mu}(e_m e_n) = f_{\mu}(e_{m+n}) = \mu^{m+n} = \mu^m \mu^n = f_{\mu}(e_m) f_{\mu}(e_n).$$

This shows that $f_{\mu}$ is multiplicative on the linear span of the $e_n$, that is, on $c_{00}(\mathbb{Z})$; since $c_{00}(\mathbb{Z})$ is dense in $l^1(\mathbb{Z})$, it follows from elementary continuity and linearity arguments that $f_{\mu}$ is multiplicative on $l^1(\mathbb{Z})$. Thus $f_{\mu} \in \mathcal{X}$, the character space of $l^1(\mathbb{Z})$ (52.8).

(ii) Suppose $f$ is any character of $l^1(\mathbb{Z})$. Let $\mu = f(e_1)$. Since $\|f\| = 1$ (52.7), we have

$$|\mu| = |f(e_1)| \leq \|e_1\| = 1;$$

also $f(e_{-1}) = f((e_1)^{-1}) = f(e_1)^{-1} = \mu^{-1}$, therefore

$$|\mu^{-1}| = |f(e_{-

continuous periodic function on $\mathbb{R}$ of period $2\pi$. The range of the Gel'fand transformation,

$$(l^1(\mathbb{Z}))^^ = \{\hat{x} : x \in l^1(\mathbb{Z})\},$$

may thus be identified as the algebra (operations pointwise) of all continuous periodic functions $\mathbb{R} \to \mathbb{C}$ of period $2\pi$ whose Fourier series are absolutely convergent.

If such a function, say $\hat{x}$, never vanishes, then $1/\hat{x} = \hat{y}$ for suitable $y \in l^1(\mathbb{Z})$ (by (v) of (52.13)). This is Wiener's theorem.

Exercise
