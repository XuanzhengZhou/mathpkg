---
role: proof
locale: en
of_concept: euler-totient-product-formula
source_book: gtm054
source_chapter: "I"
source_section: "2"
---

Clearly $\varphi(1) = 1$. If $n \geq 2$, let $B = \{1, 2, \ldots, n\}$ and define $f: B \to \mathcal{P}(V)$ by
$$f(b) = \{p \in V : p \mid b\}, \quad \text{for each } b \in B.$$
Then $(V, f, B)$ is a system, and $\varphi(n)$ is the number of blocks of size 0 (integers coprime to $n$).

Let $s$ be the selection of $(V, f, B)$. By E8(b), for each $S \in \mathcal{P}(V)$:
$$\bar{s}(S) = \left|\left\{b \in B : f(b) \supseteq S\right\}\right| = \frac{n}{\prod_{p \in S} p},$$
since a number is divisible by all primes in $S$ if and only if it is divisible by their product.

Substituting into E13(b) with $k = 0$:
\begin{align*}
\varphi(n) &= \sum_{t=0}^{|V|} (-1)^t \sum_{|S|=t} \frac{n}{\prod_{p \in S} p} \\
&= n \sum_{S \in \mathcal{P}(V)} \prod_{p \in S} \frac{-1}{p} \\
&= n \prod_{p \in V} \left(1 - \frac{1}{p}\right).
\end{align*}
The last step is a standard algebraic manipulation of the sum over all subsets as a product.
