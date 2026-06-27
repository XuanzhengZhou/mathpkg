---
role: proof
locale: en
of_concept: equivalence-of-ordinary-dirichlet-series-characterization
source_book: gtm041
source_chapter: "8"
source_section: "8.8"
---

**Proof.** For ordinary Dirichlet series the sequence of exponents $\Lambda = \{\lambda(n)\}$ is $\{\log n\}$, and for a basis we may use the logarithms of primes: $\beta(k) = \log p_k$, where $p_k$ is the $k$-th prime. The Bohr matrix entries $a_{n,k}$ are then the exponents in the prime factorization of $n$:

$$n = \prod_{k=1}^{\infty} p_k^{a_{n,k}}. \tag{5}$$

Now let $A(s) = \sum a(n)n^{-s}$, $B(s) = \sum b(n)n^{-s}$.

**($\Rightarrow$) Forward direction.** Suppose that $A(s) \sim B(s)$. Then there exists a real sequence $\{y_k\}$ such that

$$b(n) = a(n) \exp \left\{ i \sum_{k=1}^{\infty} a_{n,k} y_k \right\}, \tag{7}$$

where the integers $a_{n,k}$ are determined by equation (5). Define a function $f$ by

$$f(n) = \exp \left\{ i \sum_{k=1}^{\infty} a_{n,k} y_k \right\}.$$

Since $a_{mn,k} = a_{m,k} + a_{n,k}$, we have $f(mn) = f(m)f(n)$ for all $m$ and $n$, so $f$ is completely multiplicative. Equation (7) states that $b(n) = a(n)f(n)$, and the definition of $f$ shows that $|f(n)| = 1$ for all $n$, so conditions (a) and (b) of the theorem are satisfied.

**($\Leftarrow$) Converse direction.** Assume there exists a completely multiplicative function $f$ satisfying conditions (a) and (b). We must show that there is a real sequence $\{y_k\}$ satisfying (7) for all $n$.

First we consider those $n$ for which $a(n) = 0$. Property (a) implies $b(n) = 0$, so equation (7) holds for such $n$ since both sides are zero, regardless of the choice of the real numbers $y_k$. We shall now construct the sequence $\{y_k\}$ so that equation (7) also holds for those $n$ for which $a(n) \neq 0$.

Assume, then, that $n$ is such that $a(n) \neq 0$. We use the prime-power decomposition (5) and the completely multiplicative property of $f$ to write

$$f(n) = \prod_{k=1}^{\infty} g(n,k),$$

where

$$g(n,k) = \begin{cases} f(p_k)^{a_{n,k}} & \text{if } p_k \mid n, \\ 1 & \text{otherwise.} \end{cases}$$

Condition (b) implies that $|f(p_k)| = 1$ whenever $p_k$ divides such an $n$, so we can write $f(p_k) = e^{i\theta_k}$ for some real $\theta_k$. Define $y_k = \theta_k$. Then

$$f(n) = \prod_{k=1}^{\infty} e^{i a_{n,k} \theta_k} = \exp\left(i \sum_{k=1}^{\infty} a_{n,k} y_k\right),$$

which is precisely the form required in (7). This completes the proof.
