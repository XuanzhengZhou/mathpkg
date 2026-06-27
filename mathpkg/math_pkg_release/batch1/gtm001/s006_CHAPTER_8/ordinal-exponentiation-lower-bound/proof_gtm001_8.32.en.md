---
role: proof
locale: en
of_concept: ordinal-exponentiation-lower-bound
source_book: gtm001
source_chapter: "8"
source_section: ""
---
**Proof.** By transfinite induction on $\beta$. For $\beta = 0$, $\alpha^0 = 1 \ge 1$. If $\alpha^\beta \ge 1$, then $\alpha^{\beta+1} = \alpha^\beta \cdot \alpha \ge 1 \cdot \alpha = \alpha \ge 1$. If $\beta \in K_{\mathrm{II}}$ and $\alpha^\gamma \ge 1$ for $\gamma < \beta$, then $\alpha^\beta = \bigcup_{\gamma < \beta} \alpha^\gamma \ge \alpha^0 = 1$ (since $0 < \beta$). If $\alpha = 0$, the hypothesis $1 \le \alpha$ is false so the implication holds vacuously.
