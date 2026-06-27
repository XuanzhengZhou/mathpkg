---
role: proof
locale: en
of_concept: ordinal-exponentiation-strict-monotonicity
source_book: gtm001
source_chapter: "8"
source_section: ""
---
**Proof.** (By transfinite induction on $\beta$). For $\beta = \alpha + 1$, $\gamma^{\alpha+1} = \gamma^\alpha \cdot \gamma$. Since $1 < \gamma$, we have $1 \le \gamma^\alpha$ by Proposition 8.32, so $\gamma^\alpha \cdot 1 < \gamma^\alpha \cdot \gamma = \gamma^{\alpha+1}$ (using Proposition 8.19 with the fact that $1 < \gamma$). Hence $\gamma^\alpha < \gamma^{\alpha+1}$.

If $\alpha < \beta$ implies $\gamma^\alpha < \gamma^\beta$, and $\alpha < \beta + 1$, then either $\alpha < \beta$ (so $\gamma^\alpha < \gamma^\beta < \gamma^\beta \cdot \gamma = \gamma^{\beta+1}$) or $\alpha = \beta$ (so $\gamma^\alpha = \gamma^\beta < \gamma^\beta \cdot \gamma = \gamma^{\beta+1}$).

If $\beta \in K_{\mathrm{II}}$ and $\alpha < \beta$, then $\alpha + 1 < \beta$. By the induction hypothesis, $\gamma^\alpha < \gamma^{\alpha+1}$. Hence $\gamma^\alpha \in \gamma^{\alpha+1} \subseteq \bigcup_{\delta < \beta} \gamma^\delta = \gamma^\beta$.
