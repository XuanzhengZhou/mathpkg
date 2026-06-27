---
role: proof
locale: en
of_concept: source-map-exact-sequence
source_book: gtm014
source_chapter: "V"
source_section: "5"
---

Since $\lambda$ is injective and $\alpha$ is a submersion we need only show that $\mathrm{Im}\,\lambda = \mathrm{Ker}(d\alpha)_\sigma$.

First we note that $(d\alpha)_\sigma \cdot \lambda = 0$, since $t \mapsto \alpha \cdot j^k F_t(p) = p$ is a curve representing $(d\alpha)_\sigma \lambda(\omega)$ when $F_t$ is a deformation defining $\lambda(\omega)$. Since this curve is constant, $(d\alpha)_\sigma \lambda(\omega) = 0$.

To finish the proof we show that $\dim \mathrm{Im}\,\lambda = \dim \mathrm{Ker}(d\alpha)_\sigma$. Now
$$\dim \mathrm{Im}\,\lambda = \dim J^k(f^*TY) = \dim (\text{polynomial mappings of } \mathbb{R}^n \text{ into } \mathbb{R}^m \text{ of degree } \leq k)$$
where $n = \dim X$ and $m = \dim Y$. On the other hand,
$$\dim \mathrm{Ker}(d\alpha)_\sigma = \dim J^k(X, Y) - \dim X = \dim (\text{polynomial mappings of } \mathbb{R}^n \text{ into } \mathbb{R}^m \text{ of degree } \leq k).$$
Thus the dimensions are equal and the sequence is exact.
