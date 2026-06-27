---
role: proof
locale: en
of_concept: prop-for-every-aperiodic-transient-random-walk-1
source_book: gtm034
source_chapter: "6"
source_section: "013"
---

Proof: For convenience, call $G(x,0) = u(x)$. If P3 were false, then there would be some $\epsilon > 0$ and a sequence $x_n$ in $R$ with

$$\lim_{n \to \infty} |x_n| = \infty$$

such that

$$|u(x_n + t) - u(x_n)| > \epsilon$$

for all $n$ at some point $t$ in $R$. Suppose this is the case. Then, using the diagonal process, as in the proof of T1, one can extract a subsequence $y_n$ from the sequence $x_n$ such that

$$\lim_{n \to \infty} u(y_n + y) = v(y)$$

exists for every $y$ in $R$, and such that $|v(t) - v(0)| \ge \epsilon$. The proof of P3 will be completed by showing that this is impossible, because $v(x)$ must be constant on $R$.

Since

$$G(x,0) = \sum_{y \in R} P(x,y)G(y,0) + \delta(x,0), \quad x \in R,$$

$$u(y_n + x) = \sum_{y \in R} P(y_n + x,y)u(y) + \delta(y_n + x,0)$$

$$= \sum_{s \in R} P(0,s)u(y_n + s + x) + \delta(y_n, -x),$$

for all $x \in R$ and all $n$. Letting $n \to \infty$ one obtains

$$v(x) = \sum_{s \in R} P(0,s)v(s + x) = \sum_{y \in R} P(x,y)v(y), \quad x \in R.$$

Thus $v(x)$ is a regular function, by T1 it is constant, and this contradicts the earlier statement that $v(t) \neq v(0)$.

At this point we abandon, but only moment
