---
role: proof
locale: en
of_concept: characterization-normalized-simultaneous-eigenform-eisenstein-series
source_book: gtm041
source_chapter: "6"
source_section: "6.13"
---

Since $f$ is not a cusp form, its constant term $c(0) \neq 0$. Recall from (35) that

$$\gamma_n(0) = \sigma_{k-1}(n)c(0)$$

for all $n \geq 1$, where $\sigma_{k-1}(n) = \sum_{d \mid n} d^{k-1}$.

If $f$ is a simultaneous eigenform with eigenvalues $\lambda(n)$, then equating constant terms gives

$$\gamma_n(0) = \lambda(n)c(0).$$

Hence $\lambda(n) = \sigma_{k-1}(n)$. Now from the eigenfunction relation $T_n f = \lambda(n)f$, equating coefficients of $x^m$ for $m \geq 1$ yields

$$\gamma_n(m) = \sigma_{k-1}(n)c(m).$$

In particular, when $m = 1$, formula (36) gives $c(n) = \sigma_{k-1}(n)c(1)$.

If $f$ is normalized ($c(1) = 1$), then $c(n) = \sigma_{k-1}(n)$ for all $n \geq 1$. The constant term of a normalized simultaneous eigenform is determined by the condition $c(1) = 1$ together with the eigenfunction property, yielding the expression in terms of $\zeta(2k)$.

Since the Eisenstein series $G_{2k}$ has the Fourier expansion

$$G_{2k}(\tau) = 2\zeta(2k) + \frac{2(2\pi i)^{2k}}{(2k-1)!} \sum_{m=1}^{\infty} \sigma_{2k-1}(m)x^m,$$

the normalized form is obtained by multiplying by the appropriate constant factor, giving

$$f(\tau) = \frac{(2k-1)!}{(2\pi i)^{2k}} \zeta(2k) + \sum_{m=1}^{\infty} \sigma_{2k-1}(m)x^m.$$

The constant term can also be expressed using Bernoulli numbers: since

$$\zeta(2k) = (-1)^{k+1} \frac{(2\pi)^{2k}}{2(2k)!} B_{2k},$$

the constant term equals $-B_{2k}/(4k)$. Conversely, it is straightforward to verify that any function with this Fourier expansion is a normalized simultaneous eigenform.
