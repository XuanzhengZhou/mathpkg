---
role: proof
locale: en
of_concept: ordinal-exponentiation-limit-ordinal-properties
source_book: gtm001
source_chapter: "8"
source_section: ""
---
**Proof.** (1) If $\alpha > 1$, then $\alpha^\beta \ge 1$ by Proposition 8.32, so $\alpha^\beta \neq 0$. Suppose $\alpha^\beta = \delta + 1$. Since $\beta \in K_{\mathrm{II}}$ and $\alpha \neq 0$, $\alpha^\beta = \bigcup_{\gamma < \beta} \alpha^\gamma$. Then $\delta \in \delta + 1 = \alpha^\beta$, so $(\exists \gamma < \beta)[\delta < \alpha^\gamma]$. Since $1 < \alpha$ and $\delta < \alpha^\gamma$, we have $\delta + 1 \le \alpha^\gamma < \alpha^\gamma \cdot \alpha = \alpha^{\gamma+1}$. But $\gamma + 1 < \beta$ (since $\beta \in K_{\mathrm{II}}$), so $\delta + 1 \in \alpha^{\gamma+1} \subseteq \bigcup_{\eta < \beta} \alpha^\eta = \alpha^\beta = \delta + 1$, a contradiction. Hence $\alpha^\beta \in K_{\mathrm{II}}$.

(2) If $\beta \in K_{\mathrm{II}}$, then $\alpha^\beta \in K_{\mathrm{II}}$ by (1) above (since $\alpha \in K_{\mathrm{II}}$ implies $\alpha > 1$). If $\beta \in K_{\mathrm{I}}$, then since $\beta \neq 0$, $\beta = \delta + 1$ for some $\delta$. Then $\alpha^\beta = \alpha^{\delta+1} = \alpha^\delta \cdot \alpha$. Since $\alpha \in K_{\mathrm{II}}$, by Proposition 8.24, $\alpha^\delta \cdot \alpha \in K_{\mathrm{II}}$ (if $\alpha^\delta \neq 0$; if $\alpha^\delta = 0$, then $\alpha = 0$, contradicting $\alpha \in K_{\mathrm{II}}$).
