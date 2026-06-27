---
role: proof
locale: en
of_concept: intermediate-value-theorem
source_book: gtm012
source_chapter: "2"
source_section: "1. Continuity, uniform continuity, and compactness"
---

# Proof of Theorem 1.5: Intermediate Value Theorem

Suppose $f: [a, b] \to \mathbb{R}$ is continuous. We consider only the case $f(a) \leq c \leq f(b)$ (the other case $f(b) \leq c \leq f(a)$ is symmetric).

Consider the two subintervals $[a, \frac{1}{2}(a + b)]$ and $[\frac{1}{2}(a + b), b]$. For at least one of these, $c$ lies between the values of $f$ at the endpoints (i.e., $f$ of the left endpoint $\leq c \leq f$ of the right endpoint). Denote this subinterval by $[a_1, b_1]$. Thus

$$f(a_1) \leq c \leq f(b_1).$$

Continuing in this way we obtain a nested sequence of intervals $[a_n, b_n]$, $n = 0, 1, 2, \ldots$ (with $[a_0, b_0] = [a, b]$) such that

$$[a_{n+1}, b_{n+1}] \subset [a_n, b_n], \quad b_{n+1} - a_{n+1} = \tfrac{1}{2}(b_n - a_n) = 2^{-(n+1)}(b - a),$$

and $f(a_n) \leq c \leq f(b_n)$ for all $n$. The sequences $(a_n)_{n=0}^{\infty}$ and $(b_n)_{n=0}^{\infty}$ are monotone and satisfy $b_n - a_n \to 0$. Hence there exists a unique point $x_0 \in [a, b]$ such that

$$a_n \to x_0, \quad b_n \to x_0.$$

By continuity of $f$,

$$f(x_0) = \lim_{n \to \infty} f(a_n) \leq c,$$
$$f(x_0) = \lim_{n \to \infty} f(b_n) \geq c.$$

Therefore $f(x_0) = c$. $\square$
