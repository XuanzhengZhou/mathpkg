---
role: proof
locale: en
of_concept: prop-s008-proposition
source_book: gtm034
source_chapter: "3"
source_section: "008"
---

Proof: To obtain parts (a) and (c) (the proofs of (b) and (d) are quite similar and will be omitted) we let

$$g_e(z) = \sum_{k=0}^{\infty} t^k \mathbf{E}[z^{\mathrm{S}}_k; \mathbf{T} > k],$$
$$h_i(z) = 1 - \mathbf{E}[t^{\mathrm{T}} z^{\mathrm{S}} \mathbf{r}].$$

One easily verifies that $g_e(z)$ is an outer function, according to D2, and $h_i(z)$ an inner function. An easy way to do this, say in the case of $g_e(z)$, is to look at

$$g_e(e^{i\theta}) = \sum_{k=0}^{\infty} t^k \mathbf{E}[e^{i\theta} z_k; \mathbf{T} > k] = \sum_{y=-\infty}^{0} e^{i\theta y} \sum_{k=0}^{\infty} t^k \mathbf{P}[S_k = y; \mathbf{T} > k]$$

which clearly is an exterior Fourier series. In view of P2, $g_e(z)$ is an exterior

To determine this constant let $z \to 0$ in the last identity (this is one of several easy ways of doing it). Clearly

$$\lim_{z \to 0} h_i(z) = \lim_{z \to 0} f_i(t;z) = 1,$$

so that $k = [c(t)]^{-1}$. Hence

$$h_i(z) = f_i(t;z),$$

which is part (a) of P5 and

$$g_e(z) = [c(t)f_e(t;z)]^{-1}$$

which is part (c).

E1 For one-dimensional symmetric random walk, certain simplifications of the formulas in D3, P4, and P5 are worth examining in detail. From $P(x,y) = P(y,x)$ it follows that $P[S_n = k] = P[S_n = -k]$, or

$$E[e^{i\theta S_n}; S_n > 0] = E[e^{-i\theta S_n}; S_n < 0].$$

In other words,

(1) $f_i(t;z) = \overline{f_e(t;z)}$ for $0 \leq t < 1$ and $|z| = 1$.
