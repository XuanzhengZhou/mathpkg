---
role: proof
locale: en
of_concept: bilinear-form-continuity-scalar
source_book: gtm049
source_chapter: "6"
source_section: "1"
---

Take $a = (1, 0, \ldots, 0)$ and $b = (0, 1, 0, \ldots, 0)$. For any $x \in \mathbf{R}$, choose a sequence $(r_i)$ of rational numbers converging to $x$. Since $\sigma$ is continuous in the first argument,
$$\sigma(xa, b) = \lim_{i \to \infty} \sigma(r_i a, b).$$
By Exercise 4 (which states that rational scalar multiplication commutes with $\sigma$), we have $\sigma(r_i a, b) = r_i \sigma(a, b)$ for each $i$. Hence
$$\sigma(xa, b) = \lim_{i \to \infty} r_i \sigma(a, b) = (\lim_{i \to \infty} r_i) \sigma(a, b) = x \sigma(a, b).$$
This shows that the scalar multiplication property holds for all real scalars, establishing that continuity plus $\mathbb{Q}$-bilinearity implies $\mathbb{R}$-bilinearity.
