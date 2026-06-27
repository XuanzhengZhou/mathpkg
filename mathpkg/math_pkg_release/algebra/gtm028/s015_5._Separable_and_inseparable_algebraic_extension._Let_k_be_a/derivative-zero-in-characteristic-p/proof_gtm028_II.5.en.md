---
role: proof
locale: en
of_concept: derivative-zero-in-characteristic-p
source_book: gtm028
source_chapter: "II"
source_section: "5. Separable and inseparable algebraic extension"
---

Let $f(X) = a_0 X^n + a_1 X^{n-1} + \cdots + a_n \in k[X]$, $a_0 \neq 0$. The formal derivative is
$$f'(X) = n a_0 X^{n-1} + (n-1) a_1 X^{n-2} + \cdots + a_{n-1}.$$

If $\operatorname{char}(k) = 0$, then each coefficient $(n-i) a_i$ is zero if and only if $a_i = 0$ (since $n-i \neq 0$ in $k$ for $i < n$). In particular, the coefficient $n a_0$ of $X^{n-1}$ is non-zero whenever $n > 0$, so $f'(X) \neq 0$.

If $\operatorname{char}(k) = p \neq 0$, then the coefficient $(n-i) a_i$ is zero whenever $a_i = 0$ or $p \mid (n-i)$. In particular, $n a_0 = 0$ precisely when $p \mid n$. Thus $f'(X) = 0$ if and only if every index $i$ for which $a_i \neq 0$ satisfies $p \mid (n-i)$. This means that only those monomials $a_i X^{n-i}$ with exponent divisible by $p$ can survive, i.e., $f(X)$ is a polynomial in $X^p$ with coefficients in $k$, written $f(X) \in k[X^p]$. Equivalently, $f'(X) = 0$ if and only if $p \mid n$ and all non-zero coefficients correspond to exponents that are multiples of $p$.
