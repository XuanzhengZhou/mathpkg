---
role: proof
locale: en
of_concept: tangent-curves-in-mapping-space
source_book: gtm014
source_chapter: "III"
source_section: "§1. Stable and Infinitesimally Stable Mappings"
---

**Proof.** Let $h = f_0 = g_0$ and $X_h = \operatorname{graph}(h) \subset X \times Y$. Let $Z$ be a tubular neighborhood of $X_h$ in $X \times Y$. As shown in the proof of Theorem 1.11, nearby functions to $h$ can be identified with sections in $C^\infty(Z)$. So for small $t$ we can regard $t \mapsto f_t$ and $t \mapsto g_t$ as smooth curves of sections in $C^\infty(Z)$.

The Fr\'{e}chet derivative of $t \mapsto f_t$ at $t = 0$ is given pointwise by
$$
(df)_p(1) = \left( \lim_{t \to 0} \frac{|f_t - f_0|}{|t|} \right)(p) = \lim_{t \to 0} \frac{|f_t(p) - f_0(p)|}{|t|}.
$$
Since $f_0 = g_0 = h$, the curves $t \mapsto f_t$ and $t \mapsto g_t$ in $C^\infty(X, Y)$ are tangent at $t = 0$ precisely when their Fr\'{e}chet derivatives at $0$ coincide. By the above pointwise expression, this holds exactly when for each $p \in X$, the curves $t \mapsto f_t(p)$ and $t \mapsto g_t(p)$ in $Y$ are tangent at $t = 0$ in the finite-dimensional sense.
