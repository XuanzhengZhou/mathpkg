---
role: proof
locale: en
of_concept: parsevals-identity
source_book: gtm012
source_chapter: "5"
source_section: "§5. Orthogonal expansions"
---

# Proof of Parseval's Identity

**Parseval's Identity.** If $u = \sum a_n e_n$ and $v = \sum b_n e_n$ are orthogonal expansions in a Hilbert space $H$ with orthonormal basis $(e_n)$, then

$$(u, v) = \sum_{n} a_n b_n^* = \sum_{n} (u, e_n)(e_n, v).$$

*Proof.* We prove the identity for a singly-indexed orthonormal basis $(e_n)_{1}^{\infty}$; the proof for a doubly-indexed basis $(e_n)_{-\infty}^{\infty}$ is identical after replacing the index range.

Suppose $u, v \in H$ have the orthogonal expansions

$$u = \sum_{n=1}^{\infty} a_n e_n, \qquad v = \sum_{n=1}^{\infty} b_n e_n,$$

where $a_n = (u, e_n)$ and $b_n = (v, e_n)$. Define the partial sums

$$u_N = \sum_{n=1}^{N} a_n e_n, \qquad v_N = \sum_{n=1}^{N} b_n e_n.$$

By Theorem 5.1, we have $u_N \to u$ and $v_N \to v$ in the norm of $H$ as $N \to \infty$.

By the continuity of the inner product (Lemma 2.1), the inner product of limits equals the limit of inner products:

$$(u, v) = \lim_{N \to \infty} (u_N, v_N).$$

Using the orthonormality of the basis $(e_n)$,

$$
\begin{aligned}
(u_N, v_N) &= \left( \sum_{n=1}^{N} a_n e_n, \sum_{m=1}^{N} b_m e_m \right) \\
&= \sum_{n=1}^{N} \sum_{m=1}^{N} a_n b_m^* (e_n, e_m) \\
&= \sum_{n=1}^{N} a_n b_n^*,
\end{aligned}
$$

since $(e_n, e_m) = \delta_{nm}$ (the Kronecker delta).

Taking the limit as $N \to \infty$,

$$(u, v) = \lim_{N \to \infty} \sum_{n=1}^{N} a_n b_n^* = \sum_{n=1}^{\infty} a_n b_n^*.$$

Substituting $a_n = (u, e_n)$ and $b_n^* = (e_n, v)$, we obtain the alternative form

$$(u, v) = \sum_{n=1}^{\infty} (u, e_n)(e_n, v). \quad \square$$
