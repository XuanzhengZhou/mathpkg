---
role: proof
locale: en
of_concept: alpha-beta-gamma-alpha-beta-gamma
source_book: gtm001
source_chapter: "8"
source_section: ""
---

** (By transfinite induction on $\gamma$). For $\gamma = 0$ we note that $(\alpha + \beta) + 0 = \alpha + \beta = \alpha + (\beta + 0)$. If $(\alpha + \beta) + \gamma = \alpha + (\beta + \gamma)$ then $(\alpha + \beta) + (\gamma + 1) = ((\alpha + \beta) + \gamma) + 1 = (\alpha + (\beta + \gamma)) + 1 = \alpha + ((\beta + \gamma) + 1) = \alpha + (\beta + (\gamma + 1))$. If $\gamma \in K_{\text{II}}$ and $(\alpha + \beta) + \delta = \alpha + (\beta + \delta)$ for $\delta < \gamma$ then

$$(\alpha + \beta) + \gamma = \bigcup_{\delta < \gamma} ((\alpha + \beta) + \delta) = \bigcup_{\delta < \gamma} (\alpha + (\beta + \delta)).$$

Furthermore since $\gamma \in K_{\text{II}}$ we have by Proposition 8.11 that $\beta + \gamma \in K_{\text{II}}$. Therefore

$$\alpha + (\beta + \gamma) = \bigcup_{\eta < \beta + \gamma} (\alpha + \eta).$$

If $\delta < \gamma$ and $\eta = \beta + \delta$, then $\eta < \beta + \gamma$ and $\alpha + (\beta + \delta) \leq \alpha + \eta$. Conversely if $\eta < \beta + \gamma$, then $\eta < \beta$ or $(\exists

EXERCISES

Prove the following.

(1) $\alpha + \beta \in \omega \rightarrow \alpha \in \omega \land \beta \in \omega$.

(2) $\alpha \leq \beta \rightarrow \alpha + (\beta - \alpha) = \beta$.

(3) $\omega \div n = \omega$.

(4) $[m + n = n + m] \land [m + n = k + n \rightarrow m = k]$.

(5) $\alpha \leq \alpha + \beta \land [\beta > 0 \rightarrow \alpha < \alpha + \beta]$.

(6) $\alpha \leq \beta + \alpha$.

(7) $\alpha + \beta \in K_{\text{II}} \leftrightarrow \beta \in K_{\text{II}} \lor [\beta = 0 \land \alpha \in K_{\text{II}}]$.

(8) $\beta \in K_{\text{II}} \land \alpha < \beta \rightarrow (\forall n)[\alpha + n < \beta]$.

(9) $\alpha + \beta$ is order isomorphic to $(\{0\} \times \alpha) \cup (\{1\} \times \beta)$ where the order on the latter set is Le, i.e., $(\exists f)[f \text{ Isom}_{E, \text{Le}}(\alpha + \beta, (\{0\} \times \alpha) \cup (\{1\} \times \beta))]$.

(10) Prove Proposition 8.8 by transfinite induction on $\beta$.

Remark. From the foregoing we see that ordinal addition on $\omega$ has all of the arithmetic properties that we expect. Addition on On is however not commutative and the right-hand cancellation law fails.

In very much the same way as we define integer multiplication as repeated addition we can also define ordinal multiplication as repeated addition. For the justification of our definition we again appeal to Proposition 7.44.

If in Proposition 7.44, $H_{\alpha} = \{ \langle \beta, \beta + \alpha \rangle | \beta \in \text{On} \}$ and if $a
