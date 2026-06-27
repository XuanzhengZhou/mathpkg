---
role: proof
locale: en
of_concept: bessels-equality
source_book: gtm012
source_chapter: "5"
source_section: "§5. Orthogonal expansions"
---

# Proof of Bessel's Equality

**Bessel's Equality.** Let $H$ be a Hilbert space with orthonormal basis $(e_n)$. For any $u \in H$,

$$\|u\|^2 = \sum_{n} |(u, e_n)|^2.$$

*Proof.* We prove the equality for a singly-indexed orthonormal basis $(e_n)_{1}^{\infty}$; the doubly-indexed case is analogous.

By Theorem 5.1, any $u \in H$ has the orthogonal expansion

$$u = \sum_{n=1}^{\infty} a_n e_n, \qquad a_n = (u, e_n),$$

with convergence in norm. Define the partial sums

$$u_N = \sum_{n=1}^{N} a_n e_n.$$

Since the $e_n$ are orthonormal, $(e_n, e_m) = \delta_{nm}$, and we compute

$$
\begin{aligned}
\|u_N\|^2 &= (u_N, u_N) \\
&= \left( \sum_{n=1}^{N} a_n e_n, \sum_{m=1}^{N} a_m e_m \right) \\
&= \sum_{n=1}^{N} \sum_{m=1}^{N} a_n a_m^* (e_n, e_m) \\
&= \sum_{n=1}^{N} |a_n|^2.
\end{aligned}
$$

By Theorem 5.1, $u_N \to u$ in the norm of $H$. The continuity of the norm implies

$$\|u\|^2 = \lim_{N \to \infty} \|u_N\|^2 = \lim_{N \to \infty} \sum_{n=1}^{N} |a_n|^2 = \sum_{n=1}^{\infty} |a_n|^2.$$

Substituting $a_n = (u, e_n)$ yields the stated equality:

$$\|u\|^2 = \sum_{n=1}^{\infty} |(u, e_n)|^2.$$

For a doubly-indexed basis $(e_n)_{-\infty}^{\infty}$, the same argument with symmetric partial sums $u_N = \sum_{n=-N}^{N} a_n e_n$ gives

$$\|u\|^2 = \sum_{n=-\infty}^{\infty} |(u, e_n)|^2. \quad \square$$

**Remark.** Bessel's equality is a special case of Parseval's identity obtained by setting $v = u$, since $(u, u) = \|u\|^2$.
