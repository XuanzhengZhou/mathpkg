---
role: proof
locale: en
of_concept: theorem-5-2-doubly-indexed-orthogonal-expansion
source_book: gtm012
source_chapter: "5"
source_section: "§5. Orthogonal expansions"
---

# Proof of Orthogonal Expansion for Doubly-Indexed Orthonormal Basis (Theorem 5.2)

**Theorem 5.2.** Suppose $H$ is a Hilbert space with an orthonormal basis $(e_n)_{-\infty}^{\infty}$ indexed by all integers. If $u \in H$, then

$$u = \sum_{n=-\infty}^{\infty} (u, e_n) e_n$$

in the sense that

$$\left\| u - \sum_{n=-N}^{N} (u, e_n) e_n \right\| \to 0 \quad \text{as} \quad N \to \infty.$$

The coefficients satisfy Bessel's equality:

$$\sum_{n=-\infty}^{\infty} |(u, e_n)|^2 = \|u\|^2.$$

More generally, if $u = \sum a_n e_n$ and $v = \sum b_n e_n$, then Parseval's identity holds:

$$(u, v) = \sum_{n=-\infty}^{\infty} a_n b_n^* = \sum_{n=-\infty}^{\infty} (u, e_n)(e_n, v).$$

Conversely, if $(a_n)_{-\infty}^{\infty}$ satisfies $\sum_{n=-\infty}^{\infty} |a_n|^2 < \infty$, then there is a unique $u \in H$ with this expansion.

*Proof.* The proof is essentially identical to that of Theorem 5.1, with the index set $\{1, 2, \ldots\}$ replaced by the set of all integers $\{\ldots, -2, -1, 0, 1, 2, \ldots\}$. All sums that ran over $n = 1$ to $N$ or $n = 1$ to $\infty$ are replaced by symmetric sums over $n = -N$ to $N$ or $n = -\infty$ to $\infty$ respectively.

Explicitly, the modifications are:

1. **Partial sums:** Define $u_N = \sum_{n=-N}^{N} a_n e_n$ instead of $\sum_{n=1}^{N} a_n e_n$.

2. **Uniqueness:** For any fixed integer $n$, when $N \geq |n|$, we have $(u_N, e_n) = a_n$. By continuity of the inner product, $a_n = \lim_{N \to \infty} (u_N, e_n) = (u, e_n)$.

3. **Convergence:** The subspace $H_N = \operatorname{span}\{e_{-N}, \ldots, e_N\}$ has the property that $u_N$ is the orthogonal projection of $u$ onto $H_N$. By Lemma 2.3, $\|u - u_N\| \leq \|u - v\|$ for any $v \in H_N$, and since the $e_n$ form a basis, $u_N \to u$.

4. **Bessel's equality:** $\|u_N\|^2 = \sum_{n=-N}^{N} |a_n|^2$, and taking the limit yields $\|u\|^2 = \sum_{n=-\infty}^{\infty} |(u, e_n)|^2$.

5. **Parseval's identity:** For $u_N = \sum_{n=-N}^{N} a_n e_n$ and $v_N = \sum_{n=-N}^{N} b_n e_n$, we have $(u, v) = \lim_{N \to \infty} (u_N, v_N) = \sum_{n=-\infty}^{\infty} a_n b_n^*$.

6. **Riesz-Fischer:** If $\sum_{n=-\infty}^{\infty} |a_n|^2 < \infty$, then $\|u_N - u_M\|^2 = \sum_{n=M+1}^{N} |a_n|^2 + \sum_{n=-N}^{-M-1} |a_n|^2 \to 0$ as $M, N \to \infty$, so $(u_N)$ is Cauchy and its limit is the desired element.\quad\square$
