---
role: proof
locale: en
of_concept: ratio-limit-via-generating-functions
source_book: gtm034
source_chapter: "VII"
source_section: "32"
---

Observe $(1-t)\sum_{n=0}^{\infty} t^n P_0[T > n] = 1 - E_0[t^{T_0}]$ and $(1-t)\sum_{n=0}^{\infty} t^n P_z[T > n] = 1 - E_z[t^{T_0}] = 1 - E_0[t^{T_{-z}}]$. Define $R_t(x,y) = \sum_{n=0}^{\infty} t^n P_n(x,y)$ and $\phi_0(x) = 1_{x=0}$. Then $E_0[\sum_{n=0}^{\infty} t^n \phi_0(x_n)] = R_t(0,0) - E_0[t^{T_x}]R_t(x,0)$. By Abel's theorem, $\lim_{t \to 1}[R_t(x,0) - R_t(0,0)] = -a(x)$. By D10.1, $\lim_{t \to 1} E_0[\sum_{n=0}^{T_x-1} t^n \phi_0(x_n)] = g_{(x)}(0,0)$. By P29.4, $g_{(x)}(0,0) = a(x) + a(-x)$. By P10.3, $\lim E_x[\sum_{n=0}^{T_x-1} t^n \phi_0(x_n)] = 1$. Combining yields the result.
