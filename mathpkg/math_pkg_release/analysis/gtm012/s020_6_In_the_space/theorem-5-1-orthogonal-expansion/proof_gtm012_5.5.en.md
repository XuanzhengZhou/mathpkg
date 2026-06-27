---
role: proof
locale: en
of_concept: theorem-5-1-orthogonal-expansion
source_book: gtm012
source_chapter: "5"
source_section: "§5. Orthogonal expansions"
---

# Proof of Orthogonal Expansion in a Hilbert Space (Theorem 5.1)

**Theorem 5.1.** Suppose $H$ is a Hilbert space with an orthonormal basis $(e_n)_{1}^{\infty}$. If $u \in H$, then

$$u = \sum_{n=1}^{\infty} (u, e_n) e_n$$

in the sense that

$$\left\| u - \sum_{n=1}^{N} (u, e_n) e_n \right\| \to 0 \quad \text{as} \quad N \to \infty.$$

The coefficients satisfy Bessel's equality:

$$\sum_{n=1}^{\infty} |(u, e_n)|^2 = \|u\|^2.$$

More generally, if $u = \sum a_n e_n$ and $v = \sum b_n e_n$, then Parseval's identity holds:

$$(u, v) = \sum_{n=1}^{\infty} a_n b_n^* = \sum_{n=1}^{\infty} (u, e_n)(e_n, v).$$

Conversely (Riesz-Fischer), if $(a_n)_{1}^{\infty}$ is a sequence of scalars with $\sum |a_n|^2 < \infty$, then there is a unique $u \in H$ such that $u = \sum_{n=1}^{\infty} a_n e_n$.

*Proof.* The proof proceeds in five parts: uniqueness of coefficients, convergence of partial sums for any $u$, Bessel's equality, Parseval's identity, and the converse (Riesz-Fischer theorem).

**1. Uniqueness of coefficients.** Suppose $(a_n)_{1}^{\infty}$ is a sequence of scalars such that

$$\left\| u - \sum_{n=1}^{N} a_n e_n \right\| \to 0 \quad \text{as} \quad N \to \infty.$$

Define the partial sums

$$u_N = \sum_{n=1}^{N} a_n e_n.$$

Since the sequence $(e_n)_{1}^{\infty}$ is orthonormal, we have

$$(u_N, e_n) = a_n \quad \text{if } N \geq n.$$

By the continuity of the inner product (Lemma 2.1), for each fixed $n$,

$$a_n = \lim_{N \to \infty} (u_N, e_n) = (u, e_n).$$

Thus the coefficients are uniquely determined as the Fourier coefficients $a_n = (u, e_n)$.

**2. Convergence of partial sums.** Let $u \in H$ and set $a_n = (u, e_n)$. Let $H_N$ be the subspace spanned by $\{e_1, \ldots, e_N\}$. The partial sum $u_N = \sum_{n=1}^{N} a_n e_n$ belongs to $H_N$. Moreover,

$$(u - u_N, e_k) = (u, e_k) - a_k = 0 \quad \text{for } k = 1, \ldots, N,$$

so $u - u_N \perp H_N$. This means $u_N$ is the orthogonal projection of $u$ onto $H_N$, and therefore $u_N$ is the best approximation to $u$ in $H_N$ (Lemma 2.3). Explicitly, for any $v \in H_N$,

$$\|u - u_N\| \leq \|u - v\|.$$

Since $\{e_1, e_2, \ldots\}$ is an orthonormal basis, the union of the subspaces $H_N$ is dense in $H$. Hence for any $\varepsilon > 0$, there exist $N_0$ and $v \in H_{N_0}$ such that $\|u - v\| < \varepsilon$. For all $N \geq N_0$, we have $v \in H_N$, and thus

$$\|u - u_N\| \leq \|u - v\| < \varepsilon.$$

This proves $u_N \to u$ as $N \to \infty$.

**3. Bessel's equality.** Since the $e_n$ are orthonormal,

$$\|u_N\|^2 = (u_N, u_N) = \sum_{n=1}^{N} |a_n|^2.$$

Taking the limit as $N \to \infty$ and using the continuity of the norm,

$$\|u\|^2 = \lim_{N \to \infty} \|u_N\|^2 = \sum_{n=1}^{\infty} |a_n|^2 = \sum_{n=1}^{\infty} |(u, e_n)|^2.$$

**4. Parseval's identity.** Suppose $u$ and $v$ are given by

$$u = \sum_{n=1}^{\infty} a_n e_n, \qquad v = \sum_{n=1}^{\infty} b_n e_n.$$

Define $u_N$ and $v_N$ as the corresponding partial sums. By the continuity of the inner product (Lemma 2.1),

$$(u, v) = \lim_{N \to \infty} (u_N, v_N).$$

Since the $e_n$ are orthonormal,

$$(u_N, v_N) = \left( \sum_{n=1}^{N} a_n e_n, \sum_{m=1}^{N} b_m e_m \right) = \sum_{n=1}^{N} a_n b_n^*.$$

Therefore,

$$(u, v) = \lim_{N \to \infty} \sum_{n=1}^{N} a_n b_n^* = \sum_{n=1}^{\infty} a_n b_n^* = \sum_{n=1}^{\infty} (u, e_n)(e_n, v).$$

**5. Converse (Riesz-Fischer Theorem).** Suppose $(a_n)_{1}^{\infty}$ is any sequence of scalars satisfying

$$\sum_{n=1}^{\infty} |a_n|^2 < \infty.$$

Define $u_N = \sum_{n=1}^{N} a_n e_n$ as before. We show that $(u_N)_{1}^{\infty}$ is a Cauchy sequence in $H$. If $N > M$, then

$$\|u_N - u_M\|^2 = (u_N - u_M, u_N - u_M) = \sum_{n=M+1}^{N} |a_n|^2.$$

Since the series $\sum |a_n|^2$ converges, the right-hand side tends to zero as $M, N \to \infty$. Hence $(u_N)$ is Cauchy, and by the completeness of $H$, there exists $u = \lim_{N \to \infty} u_N \in H$.

For this $u$, we have $(u, e_n) = \lim_{N \to \infty} (u_N, e_n) = a_n$ (for $N \geq n$), so $u$ has the prescribed Fourier coefficients. The uniqueness was established in part 1. $\square$
