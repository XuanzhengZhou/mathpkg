---
role: proof
locale: en
of_concept: "let-and-be-in-then-for-almost-all"
source_book: gtm025
source_chapter: "Hilbert Spaces and Spectral Theory"
source_section: "21.31"
---

Suppose for the moment that the function $(x, y) \rightarrow f(x - y)g(y)$ is $\overline{\mathcal{M}_{\lambda} \times \mathcal{M}_{\lambda}}$-measurable on $R^2$. We apply (21.12) to write

$$\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} |f(x - y)g(y)| dx dy = \int_{-\infty}^{\infty} |g(y)| \cdot \int_{-\infty}^{\infty} |f(x - y)| dx dy$$

$$= \int_{-\infty}^{\infty} |g(y)| \cdot \|f\|_1 dy = \|f\|_1 \cdot \|g\|_1$$

$< \infty$.

Thus the hypothesis of Fubini's theorem (21.13) is satisfied, and so $y \rightarrow f(x - y)g(y)$ is in $\mathfrak{L}_1(R)$ for almost all $x \in R$, $

such that $M \subset \bigcap_{k=1}^{\infty} U_k$ and $\lambda(U_k) \to 0$. Let $B_k = \{(x, y) \in R^2 : (x - y) \in U_k, |y| \leq n\}$. We see at once that $(B_k) \subset \mathcal{B}(R^2)$ and $P_n \subset \bigcap_{k=1}^{\infty} B_k$. Use (10.15), (21.12), and (12.44) to write

$$\lambda \times \lambda \left( \bigcap_{k=1}^{\infty} B_k \right) = \lim_{k \to \infty} \lambda \times \lambda(B_k)$$

$$= \lim_{k \to \infty} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \xi_B_k(x, y) \, dx \, dy$$

$$= \lim_{k \to \infty} \int_{-n}^{n} \int_{-\infty}^{\infty} \xi_U_k(x - y) \, dx \, dy$$

$$= \lim_{k \to \infty} \int_{-n}^{n} \int_{-\infty}^{\infty} \xi_U_k(x) \, dx \, dy$$

$$= \lim_{k \to \infty} 2n \lambda(U_k) = 0.$$

Since $P_n \subset \bigcap_{k=1}^{\infty} B_k$, we have proved that $\lambda \times \lambda(P_n) = 0$.

It is possible to convolve some pairs of functions not both of which are in $\mathfrak{L}_1(R)$. This is brought out in the following two theorems and in Exercise (21.56).
