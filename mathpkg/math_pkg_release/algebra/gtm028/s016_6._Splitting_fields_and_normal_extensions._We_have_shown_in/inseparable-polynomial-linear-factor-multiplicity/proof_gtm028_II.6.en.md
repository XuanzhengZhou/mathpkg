---
role: proof
locale: en
of_concept: inseparable-polynomial-linear-factor-multiplicity
source_book: gtm028
source_chapter: "II"
source_section: "6. Splitting fields and normal extensions"
---

We have $f(X) = \varphi(X^{p^e})$, where $\varphi(X)$ is an irreducible separable polynomial in $k[X]$. Each element $x_i^{p^e}$ is a root of $\varphi(X)$, necessarily a simple root, and hence $\varphi(X) = (X - x_i^{p^e})\varphi_i(X)$, where $\varphi_i(X) \in K[X]$ and $\varphi_i(x_i^{p^e}) \neq 0$. We have, then,

$$f(X) = (X^{p^e} - x_i^{p^e})\varphi_i(X^{p^e}) = (X - x_i)^{p^e} \varphi_i(X^{p^e}).$$

Since $\varphi_i(x_i^{p^e}) \neq 0$, the factor $(X - x_i)$ does not divide $\varphi_i(X^{p^e})$. Hence $x_i$ is a root of multiplicity exactly $p^e$ of $f(X)$. The same argument applies to every root $x_i$, so each linear factor in the complete factorization appears exactly $p^e$ times.
