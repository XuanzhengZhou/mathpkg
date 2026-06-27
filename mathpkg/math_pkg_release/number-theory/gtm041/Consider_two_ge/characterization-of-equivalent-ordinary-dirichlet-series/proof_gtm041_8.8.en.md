---
role: proof
locale: en
of_concept: characterization-of-equivalent-ordinary-dirichlet-series
source_book: gtm041
source_chapter: "8"
source_section: "8.8"
---

For ordinary Dirichlet series the sequence of exponents $\Lambda = \{\lambda(n)\}$ is $\{\log n\}$ and for a basis we may use the prime-power logarithms. Let $A(s) = \sum a(n)n^{-s}$, $B(s) = \sum b(n)n^{-s}$.

Suppose first that $A(s) \sim B(s)$. Then there exists a real sequence $\{y_k\}$ such that
$$b(n) = a(n) \exp \left\{ i \sum_{k=1}^{\infty} a_{n,k} y_k \right\}$$
where the integers $a_{n,k}$ are determined by the prime-power decomposition of $n$. Define a function $f$ by
$$f(n) = \exp \left\{ i \sum_{k=1}^{\infty} a_{n,k} y_k \right\}.$$
Since the exponents $a_{n,k}$ are additive under multiplication ($a_{mn,k} = a_{m,k} + a_{n,k}$), it follows that $f(mn) = f(m)f(n)$ for all $m$ and $n$, so $f$ is completely multiplicative. By definition we have $b(n) = a(n)f(n)$, and $|f(n)| = 1$ for all $n$, so conditions (a) and (b) of the theorem are satisfied.

Conversely, assume there exists a completely multiplicative function $f$ satisfying conditions (a) and (b). We must show that there is a real sequence $\{y_k\}$ satisfying the equivalence condition for all $n$. First consider those $n$ for which $a(n) = 0$. Property (a) implies $b(n) = 0$, so the equivalence equation holds for such $n$ regardless of the choice of $\{y_k\}$.

Now consider $n$ such that $a(n) \neq 0$. Using the prime-power decomposition of $n$ and the complete multiplicativity of $f$, write
$$f(n) = \prod_{k=1}^{\infty} g(n,k),$$
where
$$g(n,k) = \begin{cases} f(p_k)^{a_{n,k}} & \text{if } p_k \mid n \\ 1 & \text{otherwise.} \end{cases}$$
By condition (b), $|f(p_k)| = 1$ whenever $p_k$ divides some $n$ with $a(n) \neq 0$, so for each such $k$ we can write $f(p_k) = e^{iy_k}$ for some real $y_k$. The required sequence $\{y_k\}$ is then constructed to satisfy the equivalence condition, completing the proof.
