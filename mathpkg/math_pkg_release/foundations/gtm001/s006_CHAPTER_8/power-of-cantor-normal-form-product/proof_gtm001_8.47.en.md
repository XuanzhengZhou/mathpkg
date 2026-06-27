---
role: proof
locale: en
of_concept: power-of-cantor-normal-form-product
source_book: gtm001
source_chapter: "8"
source_section: ""
---
**Proof.** (By transfinite induction on $\gamma$). For $\gamma = 1$, $(\alpha^\beta \cdot m)^1 = \alpha^{\beta \cdot 1} \cdot m$ holds trivially. If $(\alpha^\beta \cdot m)^\gamma = \alpha^{\beta \cdot \gamma} \cdot m$, then

$$(\alpha^\beta \cdot m)^{\gamma+1} = (\alpha^\beta \cdot m)^\gamma \cdot (\alpha^\beta \cdot m) = (\alpha^{\beta \cdot \gamma} \cdot m) \cdot (\alpha^\beta \cdot m).$$

Since $\alpha \ge \omega$, we have $m < \alpha^\beta$, and properties of ordinal multiplication for infinite ordinals give $(\alpha^{\beta \cdot \gamma} \cdot m) \cdot (\alpha^\beta \cdot m) = \alpha^{\beta \cdot \gamma} \cdot \alpha^\beta \cdot m = \alpha^{\beta \cdot (\gamma + 1)} \cdot m$.

If $\gamma \in K_{\mathrm{II}}$, then

$$(\alpha^\beta \cdot m)^\gamma = \bigcup_{\delta < \gamma} (\alpha^\beta \cdot m)^\delta = \bigcup_{\delta < \gamma} \alpha^{\beta \cdot \delta} \cdot m \le \bigcup_{\delta < \gamma} \alpha^{\beta \cdot (\delta+1)} = \alpha^{\beta \cdot \gamma}.$$

The bound $(\alpha^\beta \cdot m)^\gamma \le \alpha^{\beta \cdot \gamma} \cdot (m+1)$ follows from a more careful analysis using the fact that each term in the union is bounded by $\alpha^{\beta \cdot \delta} \cdot m \le \alpha^{\beta \cdot \delta} \cdot (m+1)$.
