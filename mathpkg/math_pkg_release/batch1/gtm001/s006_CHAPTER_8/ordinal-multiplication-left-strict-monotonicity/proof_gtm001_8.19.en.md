---
role: proof
locale: en
of_concept: ordinal-multiplication-left-strict-monotonicity
source_book: gtm001
source_chapter: "8"
source_section: ""
---
**Proof.** First we prove, by transfinite induction on $\beta$, that $\alpha < \beta$ and $\gamma > 0$ imply $\gamma \cdot \alpha < \gamma \cdot \beta$.

If $\beta = \alpha + 1$ and $\gamma > 0$, then $\gamma \cdot \beta = \gamma \cdot (\alpha + 1) = \gamma \cdot \alpha + \gamma \ge \gamma \cdot \alpha + 1 > \gamma \cdot \alpha$. If $\alpha < \beta$ implies $\gamma \cdot \alpha < \gamma \cdot \beta$, and $\alpha < \beta + 1$, then either $\alpha < \beta$ (in which case $\gamma \cdot \alpha < \gamma \cdot \beta < \gamma \cdot \beta + \gamma = \gamma \cdot (\beta + 1)$) or $\alpha = \beta$ (in which case $\gamma \cdot \alpha = \gamma \cdot \beta < \gamma \cdot \beta + \gamma = \gamma \cdot (\beta + 1)$). If $\beta \in K_{\mathrm{II}}$, then $\alpha + 1 < \beta$ and from the induction hypothesis $\gamma \cdot \alpha < \gamma \cdot (\alpha + 1)$. Hence $\gamma \cdot \alpha \in \bigcup_{\delta < \beta} \gamma \cdot \delta = \gamma \cdot \beta$.

The converse: if $\gamma \cdot \alpha < \gamma \cdot \beta$, then $\alpha < \beta$ follows by trichotomy (if $\beta \le \alpha$, then by what we just proved or the definition, $\gamma \cdot \beta \le \gamma \cdot \alpha$, contradiction).
