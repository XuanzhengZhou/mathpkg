---
role: proof
locale: en
of_concept: norm-equality-theorem
source_book: gtm059
source_chapter: "1"
source_section: "12"
---

The inequality $\|f\| \leq \|\mu\|$ follows from the definition: since
$$
c_i = \int \binom{x}{i} \, d\mu(x)
$$
are the coefficients of the power series $f(X) = \sum c_i X^i$, we have $|c_i| \leq \|\mu\|$, which yields $\|f\| \leq \|\mu\|$.

Conversely, fix a level $p^N$, let $x_i \in \mathbb{Z}_p$ be a representative modulo $p^N$, and let $\varphi$ be the locally constant function such that
$$
\varphi(x_i) = 1, \qquad \varphi(x) = 0 \text{ if } x \not\equiv x_i \pmod{p^N}.
$$
Then
$$
\int \varphi \, d\mu = \mu(x_i + p^N \mathbb{Z}_p).
$$
On the other hand, by the corollary of Theorem 1.3 (which bounds integrals of locally constant functions by $\|f\|$), we have
$$
\left| \int \varphi \, d\mu \right| \leq \|f\|.
$$
Since $x_i$ and $N$ were arbitrary, taking the supremum yields $\|\mu\| \leq \|f\|$. Together with the first inequality, we obtain $\|f\| = \|\mu\|$.
