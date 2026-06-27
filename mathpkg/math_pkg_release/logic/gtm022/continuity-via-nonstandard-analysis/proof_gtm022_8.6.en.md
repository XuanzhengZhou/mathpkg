---
role: proof
locale: en
of_concept: continuity-via-nonstandard-analysis
source_book: gtm022
source_chapter: "VIII"
source_section: "6"
---

The translation of the epsilon-delta definition into non-standard terms: $\lim_{x \to a} f(x) = \ell$ means $\forall \varepsilon > 0 \exists \delta > 0 \forall x (0 < |x-a| < \delta \Rightarrow |f(x)-\ell| < \varepsilon)$. In $*\mathbb{R}$, this transfers to: for $x \in \mu(a)$, $x \neq a$, we have $|x-a| < \delta$ for all standard $\delta > 0$, hence $|*f(x)-\ell| < \varepsilon$ for all standard $\varepsilon > 0$, so $*f(x) \in \mu(\ell)$.
