---
role: proof
locale: en
of_concept: eisenstein-series-are-only-noncusp-simultaneous-eigenforms
source_book: gtm041
source_chapter: "6"
source_section: "6.13"
---

Since $f \in M_{2k}$ and is not a cusp form, its constant term $c(0) \neq 0$. For the Hecke operator $T_n$, formula (34) gives

$$\gamma_n(m) = \sum_{d \mid (n,m)} d^{2k-1} \, c\!\left(\frac{mn}{d^2}\right).$$

When $m = 0$, we have $(n,0) = n$, so by (35),

$$\gamma_n(0) = \sigma_{2k-1}(n) \, c(0), \quad \text{where } \sigma_{2k-1}(n) = \sum_{d \mid n} d^{2k-1}.$$

If $f$ is a simultaneous eigenform, then $T_n f = \lambda(n) f$, so equating constant terms yields

$$\lambda(n) c(0) = \sigma_{2k-1}(n) c(0).$$

Since $c(0) \neq 0$, we deduce

$$\lambda(n) = \sigma_{2k-1}(n)$$

for all $n \geq 1$. Equating the coefficients of $x^m$ for $m \geq 1$ in the eigenform equation gives

$$\gamma_n(m) = \sigma_{2k-1}(n) c(m).$$

When $m = 1$, using $\gamma_n(1) = c(n)$ from (36), we obtain

$$c(n) = \sigma_{2k-1}(n) c(1).$$

If $f$ is normalized (i.e., $c(1) = 1$), then $c(n) = \sigma_{2k-1}(n)$ for all $n \geq 1$. The Eisenstein series $G_{2k}$ has the Fourier expansion

$$G_{2k}(\tau) = 2\zeta(2k) + \frac{2(2\pi i)^{2k}}{(2k-1)!} \sum_{m=1}^{\infty} \sigma_{2k-1}(m) x^m,$$

so the normalized form with these coefficients is

$$f(\tau) = \frac{(2k-1)!}{2(2\pi i)^{2k}} \, G_{2k}(\tau) = \frac{(2k-1)!}{(2\pi i)^{2k}} \,\zeta(2k) + \sum_{m=1}^{\infty} \sigma_{2k-1}(m) x^m.$$

Using $\zeta(2k) = (-1)^{k+1} \frac{(2\pi)^{2k}}{2(2k)!} B_{2k}$, the constant term simplifies to $-B_{2k}/(4k)$.
