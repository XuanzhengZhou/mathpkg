---
role: proof
locale: en
of_concept: existence-of-power-series-hk
source_book: gtm059
source_chapter: "Iwasawa Theory of Local Units"
source_section: "1"
---

Let
$$f(X) = D \log f(X) = (1 + X) \frac{f'(X)}{f(X)}.$$
By Lemma 6 of Chapter 4,
$$\varphi_0(x) = D^{-1} f(f(x)) = \int_{-1}^{1} x^{k-1} \, d\varphi_0(x).$$
A computation then shows that
$$1 - p^{k+1} y_k = D^{-1}\left(X \frac{f'(f(X))}{f(f(X))}\right) = \int_{-1}^{1} x^{k-1} \, d\varphi_0(x)$$
for some measure $\mu$. By decomposing the integral over cosets of $\mu_{p-1}$ in $\mathbb{Z}_p^\times$, we write
$$\int_{-1}^{1} \mu(x) \, D^2 \varphi_0^*(x) \, d\varphi_0(x) = \sum_{i=0}^{k-1} \int_{-1}^{1} \mu^i \, d\varphi_0(x),$$
where $\mu_i$ is a measure with support in $1 + p\mathbb{Z}_p$. By Example 2 of Chapter 4, Section 1, we conclude that for each $i$ there exists a power series $f_i$ such that
$$\int_{-1}^{1} \mu^i \, d\varphi_0^*(x) = f_i(\gamma) - (1-p)\varphi_0^{(i)}.$$
Setting $h_k = \sum_{i=0}^{k-1} f_i$, we obtain the desired power series. For $k \equiv a \pmod{p-1}$, the computation of $h_k(\gamma)^k$ reduces to an integral over the corresponding congruence component, which yields the stated formula. The verification that $h_k$ is a unit when $a$ is even follows from the fact that $\varphi_0^{(2^k)}$ is a unit under these conditions, which in turn follows from the properties established in Example 2 of Chapter 4, Section 1.
