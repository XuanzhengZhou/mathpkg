---
role: proof
locale: en
of_concept: riesz-fischer-theorem-hilbert
source_book: gtm012
source_chapter: "5"
source_section: "§5. Orthogonal expansions"
---

# Proof of the Riesz-Fischer Theorem for Hilbert Spaces

**Riesz-Fischer Theorem.** Let $H$ be a Hilbert space with orthonormal basis $(e_n)$. If $(a_n)$ is any sequence of scalars such that $\sum_{n} |a_n|^2 < \infty$, then there exists a unique $u \in H$ such that its Fourier coefficients are $(a_n)$, i.e.,

$$u = \sum_{n} a_n e_n,$$

with convergence in the norm of $H$. Equivalently, the map $u \mapsto ((u, e_n))_n$ is a unitary isomorphism from $H$ onto $\ell^2$.

*Proof.* We present the proof for a singly-indexed orthonormal basis $(e_n)_{1}^{\infty}$; the doubly-indexed case $(e_n)_{-\infty}^{\infty}$ is entirely analogous.

Suppose $(a_n)_{1}^{\infty}$ is a sequence of scalars with

$$\sum_{n=1}^{\infty} |a_n|^2 < \infty.$$

Define the sequence of partial sums

$$u_N = \sum_{n=1}^{N} a_n e_n, \qquad N = 1, 2, 3, \ldots$$

We first show that $(u_N)_{1}^{\infty}$ is a Cauchy sequence in $H$. For $N > M$, using the orthonormality of the $e_n$,

$$
\begin{aligned}
\|u_N - u_M\|^2 &= (u_N - u_M, u_N - u_M) \\
&= \left( \sum_{n=M+1}^{N} a_n e_n, \sum_{k=M+1}^{N} a_k e_k \right) \\
&= \sum_{n=M+1}^{N} |a_n|^2.
\end{aligned}
$$

Since the series $\sum_{n=1}^{\infty} |a_n|^2$ converges, its tail tends to zero:

$$\sum_{n=M+1}^{N} |a_n|^2 \to 0 \quad \text{as} \quad M, N \to \infty.$$

Therefore $(u_N)$ is a Cauchy sequence. By the completeness of the Hilbert space $H$, there exists a unique element $u \in H$ such that

$$u = \lim_{N \to \infty} u_N = \sum_{n=1}^{\infty} a_n e_n,$$

where the series converges in the norm topology of $H$.

It remains to verify that the Fourier coefficients of $u$ are precisely the given $(a_n)$. For any fixed $n$ and for all $N \geq n$, the orthonormality gives $(u_N, e_n) = a_n$. By the continuity of the inner product (Lemma 2.1),

$$(u, e_n) = \lim_{N \to \infty} (u_N, e_n) = a_n.$$

Thus $u$ has the prescribed sequence as its Fourier coefficients, and the existence is proved.

Uniqueness follows from the same argument as in Theorem 5.1: if $v$ is another element with $(v, e_n) = a_n$ for all $n$, then $u - v$ is orthogonal to every $e_n$ and hence to the closed linear span of $\{e_n\}$, which is all of $H$. Therefore $u - v = 0$, i.e., $u = v$.

The map $u \mapsto ((u, e_n))_n$ is therefore a bijective linear isometry from $H$ onto $\ell^2$, i.e., a unitary isomorphism, since $\|u\|^2 = \sum |(u, e_n)|^2 = \sum |a_n|^2$ by Bessel's equality. $\square$
