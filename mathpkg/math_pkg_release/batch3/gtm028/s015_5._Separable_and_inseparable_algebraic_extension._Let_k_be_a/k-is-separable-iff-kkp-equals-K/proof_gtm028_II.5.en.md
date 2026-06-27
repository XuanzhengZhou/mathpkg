---
role: proof
locale: en
of_concept: k-is-separable-iff-kkp-equals-K
source_book: gtm028
source_chapter: "II"
source_section: "5. Separable and inseparable algebraic extension"
---

**Proof that separability implies $kK^p = K$:** Every element of $K$ is purely inseparable over $kK^p$, since $K^p \subset kK^p$. If $K$ is a separable extension of $k$, then by Lemma 2, $K$ is also separable over $kK^p$ (since $k \subset kK^p \subset K$). But any element of $K$ that is both separable and purely inseparable over $kK^p$ must lie in $kK^p$ by Lemma 1. Hence $kK^p = K$.

**Proof that $kK^p = K$ implies separability:** Assume $kK^p = K$ and let $[K:k] = n$. Let $\omega_1, \omega_2, \ldots, \omega_h$ be elements of $K$ which are linearly independent over $k$. We assert that $\omega_1^p, \omega_2^p, \ldots, \omega_h^p$ are also linearly independent over $k$. Extend $\omega_1, \ldots, \omega_h$ to a basis $\omega_1, \ldots, \omega_n$ of $K/k$. We have:

$$K = \sum_{i=1}^{n} k\omega_i, \quad K^p = \sum_{i=1}^{n} k^p\omega_i^p, \quad K = kK^p = \sum_{i=1}^{n} k\omega_i^p.$$

This shows that $\omega_1^p, \ldots, \omega_n^p$ also form a basis of $K$ over $k$, which proves the assertion. Now let $x \in K$ with minimal polynomial $f(X)$ of degree $m$ over $k$. If $x$ were inseparable, its reduced degree $m_0$ would satisfy $m_0 < m$. Then $1, x, \ldots, x^{m_0}$ are linearly independent over $k$, so by the assertion, $1, x^p, \ldots, x^{m_0p}$ are also linearly independent. But from the definition of reduced degree, $1, x^p, \ldots, x^{m_0p}$ are linearly dependent (since the degree of the separable polynomial $f_0(X)$ associated to $f(X)$ is $m_0$). This contradiction shows $x$ must be separable. Thus $K/k$ is separable.
