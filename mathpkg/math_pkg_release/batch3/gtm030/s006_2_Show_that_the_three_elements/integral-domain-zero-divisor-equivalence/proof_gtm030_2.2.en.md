---
role: proof
locale: en
of_concept: integral-domain-zero-divisor-equivalence
source_book: gtm030
source_chapter: "2"
source_section: "2"
---

The proof is immediate from the definitions.

($\Rightarrow$) Suppose $\mathfrak{A}$ is an integral domain. By definition, the set $\mathfrak{A}^*$ of non-zero elements forms a sub-semi-group of the multiplicative semi-group. This means that if $a \neq 0$ and $b \neq 0$, then $ab \neq 0$. Consequently, there can be no left or right zero-divisor $\neq 0$: if $a \neq 0$ were a left zero-divisor, there would exist $b \neq 0$ with $ab = 0$, contradicting the integral domain property.

($\Leftarrow$) Suppose $\mathfrak{A}$ possesses no zero-divisors $\neq 0$. Then for any $a \neq 0$ and $b \neq 0$, we cannot have $ab = 0$ (for that would make $a$ a left zero-divisor). Hence $ab \neq 0$, which means $\mathfrak{A}^*$ is closed under multiplication and therefore forms a sub-semi-group. Thus $\mathfrak{A}$ is an integral domain.
