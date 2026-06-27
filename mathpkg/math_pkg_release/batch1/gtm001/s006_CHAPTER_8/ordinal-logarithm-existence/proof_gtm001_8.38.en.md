---
role: proof
locale: en
of_concept: ordinal-logarithm-existence
source_book: gtm001
source_chapter: "8"
source_section: ""
---
**Proof.** (Existence) Since $\alpha > 1$, we have $\alpha^\beta \ge \beta$ (can be proved by induction on $\beta$). Therefore $\beta < \alpha^{\beta+1}$ (since $\alpha^{\beta+1} = \alpha^\beta \cdot \alpha \ge \beta \cdot \alpha \ge \beta \cdot 2 > \beta$). Let $\delta$ be the least ordinal such that $\beta < \alpha^{\delta+1}$. Then $\alpha^\delta \le \beta < \alpha^{\delta+1}$ by minimality of $\delta$.

(Uniqueness) If $\alpha^{\delta_1} \le \beta < \alpha^{\delta_1+1}$ and $\alpha^{\delta_2} \le \beta < \alpha^{\delta_2+1}$, and $\delta_1 < \delta_2$, then $\delta_1 + 1 \le \delta_2$, so $\beta < \alpha^{\delta_1+1} \le \alpha^{\delta_2} \le \beta$, contradiction. Similarly $\delta_2 < \delta_1$ is impossible. Hence $\delta_1 = \delta_2$.
