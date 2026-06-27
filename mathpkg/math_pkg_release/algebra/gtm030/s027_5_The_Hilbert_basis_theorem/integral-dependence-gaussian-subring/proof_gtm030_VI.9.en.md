---
role: proof
locale: en
of_concept: integral-dependence-gaussian-subring
source_book: gtm030
source_chapter: "VI"
source_section: "9. Integral elements"
---

If $a \in \mathfrak{J}$ is integrally dependent on $\mathfrak{g}$, there exists a monic polynomial $f(x) \in \mathfrak{g}[x]$ with $f(a) = 0$. Hence $a$ is algebraic over $\mathfrak{J}_0$. Let $\mu(x) \in \mathfrak{J}_0[x]$ be the minimum polynomial of $a$ over $\mathfrak{J}_0$. Then $\mu(x) \mid f(x)$ in $\mathfrak{J}_0[x]$.

One of the irreducible factors of $f(x)$ in $\mathfrak{g}[x]$ is an associate of $\mu(x)$ in $\mathfrak{J}_0[x]$. Let this factor be $\mu^*(x)$, so $\mu^*(x) = \beta \mu(x)$ with $\beta \in \mathfrak{J}_0$. Since the leading coefficient of $f(x)$ is $1$ and $\mu^*(x) \mid f(x)$ in $\mathfrak{g}[x]$, we can suppose the leading coefficient of $\mu^*(x)$ is $1$. Then $\mu^*(x) = \beta \mu(x)$ implies $\beta = 1$, so $\mu(x) = \mu^*(x) \in \mathfrak{g}[x]$.

Conversely, if the minimum polynomial $\mu(x)$ of $a$ has coefficients in $\mathfrak{g}$ and is monic, then $\mu(a) = 0$ directly gives an integral dependence relation for $a$ over $\mathfrak{g}$.
