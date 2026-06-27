---
role: proof
locale: en
of_concept: gauss-lemma
source_book: gtm030
source_chapter: "III"
source_section: "6"
---

Let $f(x) = a_0 + a_1 x + \cdots + a_n x^n$ and $g(x) = b_0 + b_1 x + \cdots + b_m x^m$ be primitive polynomials in $\mathfrak{A}[x]$. Suppose, for contradiction, that $f(x) g(x) = c_0 + c_1 x + \cdots + c_{n+m} x^{n+m}$ is not primitive. Then there exists an irreducible element $p \in \mathfrak{A}$ such that $p \mid c_i$ for all $i$.

Since $f(x)$ is primitive, $p$ does not divide all the $a_i$. Let $a_{n'}$ be the last coefficient of $f(x)$ (i.e., with largest index) not divisible by $p$. Similarly, since $g(x)$ is primitive, let $b_{m'}$ be the last coefficient of $g(x)$ not divisible by $p$.

Now consider the coefficient $c_{m'+n'}$ in the product $f(x)g(x)$:
$$c_{m'+n'} = a_0 b_{m'+n'} + a_1 b_{m'+n'-1} + \cdots + a_{n'-1} b_{m'+1} + a_{n'} b_{m'} + a_{n'+1} b_{m'-1} + \cdots + a_{n'+m'} b_0.$$

In the terms preceding $a_{n'} b_{m'}$ in this sum, the $b_j$ have index $j > m'$, so by the choice of $m'$, each such $b_j$ is divisible by $p$. In the terms following $a_{n'} b_{m'}$, the $a_i$ have index $i > n'$, so by the choice of $n'$, each such $a_i$ is divisible by $p$. Therefore, all terms in the sum except possibly $a_{n'} b_{m'}$ are divisible by $p$.

Since $p \mid c_{m'+n'}$ by assumption, it follows that $p \mid a_{n'} b_{m'}$. But $p$ is irreducible, and $p$ does not divide $a_{n'}$ nor $b_{m'}$. This contradicts the fact that in a Gaussian domain, an irreducible element is prime. Hence our assumption is false, and $f(x) g(x)$ must be primitive.
