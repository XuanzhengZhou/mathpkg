---
role: proof
locale: en
of_concept: order-statistics-joint-density
source_book: gtm095
source_chapter: "2"
source_section: "8. Random Variables: II"
---

# Proof of Joint Distribution of Order Statistics

Let $X_1, \ldots, X_n$ be independent identically distributed (i.i.d.) random variables with common distribution function $F(x)$ and density $f(x)$. Denote the order statistics by

$$
X^{(1)} = \min(X_1, \ldots, X_n) \leq X^{(2)} \leq \cdots \leq X^{(n)} = \max(X_1, \ldots, X_n).
$$

## (a) Marginal density of the $k$-th order statistic $X^{(k)}$

The event $\{X^{(k)} \leq x\}$ means that **at least $k$** of the $n$ random variables do not exceed $x$. Since the $X_i$ are i.i.d., the number of variables $\leq x$ follows a binomial distribution $\operatorname{Bin}(n, F(x))$. Hence

$$
P(X^{(k)} \leq x) = \sum_{j=k}^{n} \binom{n}{j} [F(x)]^{j} [1 - F(x)]^{n-j}.
$$

To find the density $f_{X^{(k)}}(x)$, differentiate this distribution function with respect to $x$. Using the product rule and noting that $F'(x) = f(x)$,

$$
\begin{aligned}
f_{X^{(k)}}(x)
&= \frac{d}{dx} \sum_{j=k}^{n} \binom{n}{j} F(x)^{j} (1-F(x))^{n-j} \\
&= \sum_{j=k}^{n} \binom{n}{j} \Bigl[ j F(x)^{j-1} f(x) (1-F(x))^{n-j} \\
&\qquad\qquad\qquad - (n-j) F(x)^{j} (1-F(x))^{n-j-1} f(x) \Bigr].
\end{aligned}
$$

This is a telescoping sum. Writing the $j$-th term as $T_j - T_{j+1}$ where

$$
T_j = \binom{n}{j-1} n F(x)^{j-1} (1-F(x))^{n-j} f(x) \quad (\text{using } j\binom{n}{j} = n\binom{n-1}{j-1}),
$$

we obtain that all intermediate terms cancel, leaving only the $j=k$ contribution:

$$
\boxed{f_{X^{(k)}}(x) = n \binom{n-1}{k-1} f(x) [F(x)]^{k-1} [1-F(x)]^{n-k}}.
$$

**Interpretation.** For $X^{(k)}$ to be in a small interval $[x, x+dx]$, one of the $n$ variables ($n$ choices) must fall in that interval (density $f(x)$), exactly $k-1$ must be $\leq x$ (probability $F(x)^{k-1}$), and the remaining $n-k$ must be $> x$ (probability $(1-F(x))^{n-k}$). The combinatorial factor $\binom{n-1}{k-1}$ accounts for choosing which of the $n-1$ remaining variables are $\leq x$.

## (b) Joint density of all order statistics $(X^{(1)}, \ldots, X^{(n)})$

Consider the ordered vector $(x^1, x^2, \ldots, x^n)$ with $x^1 < x^2 < \cdots < x^n$. The probability that each $X^{(i)}$ falls in a small interval $(x^i, x^i + dx^i]$ is, to first order,

$$
P\bigl(X^{(i)} \in (x^i, x^i + dx^i],\; i=1,\ldots,n\bigr) \approx f(x^1, \ldots, x^n)\,dx^1 \cdots dx^n.
$$

Now, the event $\{X^{(i)} \in (x^i, x^i + dx^i] \text{ for all } i\}$ occurs if and only if, for some permutation $\pi$ of $\{1,\ldots,n\}$,

$$
X_{\pi(1)} \in (x^1, x^1+dx^1],\; X_{\pi(2)} \in (x^2, x^2+dx^2],\; \ldots,\; X_{\pi(n)} \in (x^n, x^n+dx^n].
$$

Since the $X_i$ are i.i.d., each of the $n!$ possible permutations has probability

$$
f(x^1)\,dx^1 \cdot f(x^2)\,dx^2 \cdots f(x^n)\,dx^n.
$$

Moreover, these $n!$ events are disjoint (different permutations assign variables to different intervals). Therefore,

$$
f(x^1, \ldots, x^n)\,dx^1 \cdots dx^n = n!\,f(x^1)\cdots f(x^n)\,dx^1 \cdots dx^n,
$$

and consequently

$$
\boxed{f(x^1, \ldots, x^n) = \begin{cases}
n!\,f(x^1) \cdots f(x^n), & \text{if } x^1 < x^2 < \cdots < x^n, \\[4pt]
0, & \text{otherwise}.
\end{cases}}
$$

The factor $n!$ reflects the fact that any permutation of the original unordered sample yields the same ordered vector of order statistics.
