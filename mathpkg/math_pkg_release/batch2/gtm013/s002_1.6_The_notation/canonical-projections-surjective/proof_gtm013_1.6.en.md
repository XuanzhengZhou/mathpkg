---
role: proof
locale: en
of_concept: canonical-projections-surjective
source_book: gtm013
source_chapter: "1"
source_section: "1.6"
---

The canonical projection $\pi_\alpha: \prod_A R_\alpha \to R_\alpha$ is defined by $\pi_\alpha((r_\beta)_{\beta \in A}) = r_\alpha$. Since addition and multiplication in the product ring are defined coordinatewise, we have

$$\pi_\alpha(r + s) = (r + s)(\alpha) = r(\alpha) + s(\alpha) = \pi_\alpha(r) + \pi_\alpha(s),$$
$$\pi_\alpha(rs) = (rs)(\alpha) = r(\alpha)s(\alpha) = \pi_\alpha(r)\pi_\alpha(s).$$

Moreover, $\pi_\alpha(1) = 1(\alpha) = 1_\alpha$, so $\pi_\alpha$ preserves the multiplicative identity. Surjectivity is immediate: for any $r_\alpha \in R_\alpha$, choose a tuple whose $\alpha$-component is $r_\alpha$ and whose other components are arbitrary (e.g., zeros).
