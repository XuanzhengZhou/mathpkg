---
role: proof
locale: en
of_concept: ordinal-division-algorithm
source_book: gtm001
source_chapter: "8"
source_section: ""
---
**Proof.** (Existence) Since $\beta > 0$, we have $\beta \ge 1$. Then $\alpha < \beta \cdot (\alpha + 1)$ (this can be proved by induction: $\beta \cdot (\alpha + 1) = \beta \cdot \alpha + \beta \ge \beta \cdot \alpha + 1 > \beta \cdot \alpha \ge \alpha$ for all $\alpha$). Let $\gamma$ be the least ordinal such that $\alpha < \beta \cdot (\gamma + 1)$. Then $\beta \cdot \gamma \le \alpha$. By Proposition 8.8 (ordinal subtraction), there exists a unique $\delta$ such that $\beta \cdot \gamma + \delta = \alpha$. If $\delta \ge \beta$, then $\alpha = \beta \cdot \gamma + \delta \ge \beta \cdot \gamma + \beta = \beta \cdot (\gamma + 1)$, contradicting $\alpha < \beta \cdot (\gamma + 1)$. Therefore $\delta < \beta$.

(Uniqueness) If $\alpha = \beta \cdot \gamma_1 + \delta_1 = \beta \cdot \gamma_2 + \delta_2$ with $\delta_1, \delta_2 < \beta$, suppose $\gamma_1 < \gamma_2$. Then $\gamma_1 + 1 \le \gamma_2$, so

$$\beta \cdot \gamma_1 + \delta_1 < \beta \cdot \gamma_1 + \beta = \beta \cdot (\gamma_1 + 1) \le \beta \cdot \gamma_2 \le \beta \cdot \gamma_2 + \delta_2,$$

contradiction. Similarly $\gamma_2 < \gamma_1$ is impossible. Hence $\gamma_1 = \gamma_2$, and by left cancellation for addition, $\delta_1 = \delta_2$.
