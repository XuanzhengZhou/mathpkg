---
role: proof
locale: en
of_concept: integral-domain-cancellation
source_book: gtm030
source_chapter: "2"
source_section: "2"
---

We prove both directions of the equivalence.

**($\Rightarrow$)** Assume $\mathfrak{A}$ is an integral domain and let $a, b, c \in \mathfrak{A}$ with $ab = ac$ and $a \neq 0$. Then:
$$ab - ac = a(b - c) = 0.$$

Since $\mathfrak{A}$ is an integral domain and $a \neq 0$, the product $a(b-c)$ can be zero only if $b - c = 0$. Hence $b = c$, establishing the left cancellation law.

The right cancellation law follows by a symmetric argument: if $ba = ca$ and $a \neq 0$, then $(b - c)a = 0$, so $b - c = 0$ and $b = c$.

**($\Leftarrow$)** Conversely, assume the left cancellation law holds in $\mathfrak{A}$. Let $ab = 0$ with $a \neq 0$. Then:
$$ab = a0.$$

By the left cancellation law (canceling the non-zero $a$), we obtain $b = 0$. Thus there can be no non-zero element $b$ with $ab = 0$ when $a \neq 0$, which means $\mathfrak{A}$ has no non-zero zero-divisors. Hence $\mathfrak{A}$ is an integral domain.
