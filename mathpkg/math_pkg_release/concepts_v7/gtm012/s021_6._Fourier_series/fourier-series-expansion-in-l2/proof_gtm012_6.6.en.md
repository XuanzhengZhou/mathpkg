---
role: proof
locale: en
of_concept: fourier-series-expansion-in-l2
source_book: gtm012
source_chapter: "6"
source_section: "§6. Fourier series"
---

# Proof of Fourier series expansion in L^2

**Proof.** In view of Lemma 6.1, the sequence $(e_n)_{-\infty}^{\infty}$ is an orthonormal basis for $L^2$. By Theorem 5.2 (expansion with respect to an orthonormal basis in a Hilbert space), every $F \in L^2$ has a unique expansion

$$F = \sum_{n=-\infty}^{\infty} (F, e_n) e_n,$$

converging in the sense of $L^2$, and the coefficients satisfy

$$\sum_{n=-\infty}^{\infty} |(F, e_n)|^2 = \|F\|^2, \qquad (F, G) = \sum_{n=-\infty}^{\infty} (F, e_n) \overline{(G, e_n)}.$$

It remains only to verify that $(F, F_{e_n}) = F(e_n)$ and $\overline{G(e_n)} = G^*(e_n)$, where $F_{e_n}$ is the distribution corresponding to the continuous function $e_n$.

The second identity follows from the first together with the definition of $G^*$. To prove the first, take a sequence $(u_m)_1^{\infty} \subset \mathcal{C}$ such that $u_m \to F$ in $L^2$. Then

$$(F, F_{e_n}) = \lim_{m \to \infty} (u_m, e_n) = \lim_{m \to \infty} F_{u_m}(e_n) = F(e_n).$$

Here we used the continuity of the inner product and the fact that for a continuous function $u$, the inner product $(u, e_n)$ coincides with the distribution action $F_u(e_n) = \frac{1}{2\pi} \int_0^{2\pi} u(x) \overline{e_n(x)} \, dx$.

Therefore the expansion coefficients $a_n = (F, e_n)$ are exactly $F(e_n)$, and the identities (2)-(5) of the theorem hold.

Conversely, suppose $(a_n)_{-\infty}^{\infty} \subset \mathbb{C}$ satisfies $\sum |a_n|^2 < \infty$. Then by the completeness of $L^2$, the series $\sum a_n e_n$ converges in $L^2$ to some $F \in L^2$, and by the first part, $a_n = F(e_n)$. Uniqueness follows from the fact that an orthonormal basis determines coefficients uniquely. $\square$
