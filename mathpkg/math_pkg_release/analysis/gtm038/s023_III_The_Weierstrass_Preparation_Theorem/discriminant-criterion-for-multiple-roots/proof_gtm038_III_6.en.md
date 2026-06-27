---
role: proof
locale: en
of_concept: discriminant-criterion-for-multiple-roots
source_book: gtm038
source_chapter: "III"
source_section: "6. Analytic Sets"
---

**Proof.**

1. Let $\omega = \omega_1^2 \cdot \tilde{\omega}$ with $\deg(\omega_1) > 0$. If $\mathfrak{z} \in G$, then we can decompose $\omega_1(u, \mathfrak{z})$ into linear factors,
$$\omega_1(u, \mathfrak{z}) = (u - c_1) \cdots (u - c_t).$$
For $\omega(u, \mathfrak{z})$ we obtain a decomposition of the form
$$\omega(u, \mathfrak{z}) = (u - c_1)^2 \cdots (u - c_t)^2 (u - c_{t+1}) \cdots (u - c_p).$$
Hence
$$\Delta_\omega(\mathfrak{z}) = D(c_1, \ldots, c_t, c_1, \ldots, c_t, c_{t+1}, \ldots, c_p) = 0.$$
Since $\mathfrak{z}$ was arbitrary, $\Delta_\omega = 0$.

2. Let $\omega$ be a polynomial without multiple factors. Then by Theorem 6.8 there are elements $q_1, q_2 \in A[u]$ such that $h := q_1 \cdot \omega + q_2 \cdot D(\omega) \in A$ does not vanish identically. We can find a $\mathfrak{z}_0 \in G$ with $h(\mathfrak{z}_0) \neq 0$. Let $a_i(u) := q_i(u, \mathfrak{z}_0) \in \mathbb{C}[u]$ for $i = 1, 2$. Then
$$a := a_1(u) \cdot \omega(u, \mathfrak{z}_0) + a_2(u) \cdot D(\omega)(u, \mathfrak{z}_0) \neq 0$$
(independent of $u$). If $\omega(u, \mathfrak{z}_0) = (u - c_1)^2 \cdot \tilde{\omega}(u)$, then $D(\omega)(u, \mathfrak{z}_0)$ would vanish, contradicting the fact that $a \neq 0$ is independent of $u$. Therefore $\omega(\cdot, \mathfrak{z}_0)$ has no multiple factors, hence $\Delta_\omega(\mathfrak{z}_0) \neq 0$.
