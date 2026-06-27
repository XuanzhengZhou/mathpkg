---
role: proof
locale: en
of_concept: tangency-of-curves-in-mapping-space
source_book: gtm014
source_chapter: "III"
source_section: "§1. Stable and Infinitesimally Stable Mappings"
---

Let $h = f_0 = g_0$ and $X_h = \operatorname{graph}(h) \subset X \times Y$. Let $Z$ be a tubular neighborhood of $X_h$ in $X \times Y$. As shown in the proof of Theorem 1.11, functions near $h$ can be identified with sections in $C^\infty(Z)$. So for $t$ small we can think of $t \mapsto f_t$ as a smooth curve of sections in $C^\infty(Z)$.

The Frechet derivative of $t \mapsto f_t$ at $t = 0$ is determined pointwise by

$$(df)_p(1) = \lim_{t \to 0} \frac{|f_t - f_0|}{|t|}(p) = \lim_{t \to 0} \frac{|f_t(p) - f_0(p)|}{|t|}.$$

If for each $p \in X$ the curves $t \mapsto f_t(p)$ and $t \mapsto g_t(p)$ are tangent at $t = 0$ in $Y$, then the limits coincide for all $p$, which means the derivatives in the Frechet sense are equal. Conversely, if $f_t$ and $g_t$ represent the same tangent vector in $T_h C^\infty(X, Y)$, then evaluating at any $p \in X$ shows the pointwise curves are tangent in $Y$.
