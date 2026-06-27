---
role: proof
locale: en
of_concept: b-epsilon-is-closed
source_book: gtm038
source_chapter: "II"
source_section: "4. The Thullen Theorem"
---

Let $\zeta_0 \in \mathbb{C}^n - B_\varepsilon$. Define $\delta := \operatorname{dist}'(\zeta_0, \mathbb{C}^n - B)$. We have $\varepsilon > \delta \geq 0$, so $\varepsilon - \delta > 0$. Let $U := U'_{\varepsilon - \delta}(\zeta_0) = \{ z : |z - \zeta_0| < \varepsilon - \delta \}$. For $z \in U$,

$$\operatorname{dist}'(z, \mathbb{C}^n - B) \leq \operatorname{dist}'(z, \zeta_0) + \operatorname{dist}'(\zeta_0, \mathbb{C}^n - B) \leq (\varepsilon - \delta) + \delta = \varepsilon.$$

If $\operatorname{dist}'(z, \mathbb{C}^n - B) < \varepsilon$ then $z \notin B_\varepsilon$. If equal to $\varepsilon$, still $z \notin B_\varepsilon$ since the defining inequality is strict. Therefore $U \subset \mathbb{C}^n - B_\varepsilon$, so $\mathbb{C}^n - B_\varepsilon$ is open. Hence $B_\varepsilon$ is closed.
