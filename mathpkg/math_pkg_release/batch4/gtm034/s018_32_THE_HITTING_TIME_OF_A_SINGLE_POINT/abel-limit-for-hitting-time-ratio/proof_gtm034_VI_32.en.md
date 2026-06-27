---
role: proof
locale: en
of_concept: abel-limit-for-hitting-time-ratio
source_book: gtm034
source_chapter: "VI"
source_section: "32"
---

Observe that $(1-t)\sum_{n=0}^{\infty} t^n P_0[T > n] = 1 - E_0[t^{T_0}]$ and $(1-t)\sum_{n=0}^{\infty} t^n P_x[T > n] = 1 - E_0[t^{T_{-x}}]$. Thus P2 reduces to proving $\lim_{t \to 1} \frac{1 - E_0[t^{T_x}]}{1 - E_0[t^{T_0}]} = a(-x)$.

Define $R_t(x,y) = \sum_{n=0}^{\infty} t^n P_n(x,y)$. Using the stopping time $T_x$,
$$E_0[\sum_{n=0}^{\infty} t^n \phi_0(x_n)] = R_t(0,0) - E_0[t^{T_x}]R_t(x,0), \quad x \neq 0,$$
$$E_x[\sum_{n=0}^{\infty} t^n \phi_0(x_n)] = R_t(x,0) - E_0[t^{T_{-x}}]R_t(0,0), \quad x \neq 0.$$

By Abel's theorem, $\lim_{t \to 1} [R_t(x,0) - R_t(0,0)] = -a(x)$ from T28.1(a). The left side of the first identity tends to $g_{(x)}(0,0) = a(x) + a(-x)$ by P29.4. The left side of the second identity tends to 1 by P10.3. Substituting yields $\lim_{t\to1} E_0[t^{T_x}] = 1 - [a(x)+a(-x) + a(x)]/R = \ldots$, and solving gives the claimed limit $a(-x)$.
