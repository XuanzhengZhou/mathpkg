---
role: proof
locale: en
of_concept: alpha-geq-omega-rightarrow-overlinealpha-times-alpha-overlinealpha
source_book: gtm001
source_chapter: "9"
source_section: ""
---

(By transfinite induction on $\alpha$). As our induction hypothesis we have

$$\mu < \alpha \rightarrow [\mu < \omega \vee \overline{\mu \times \mu} = \overline{\mu}].$$

By *Proposition 10.13 if $\mu < \alpha$, then $\overline{\mu} \leq \overline{\alpha}$. If $(\exists \mu < \alpha)[\overline{\mu} = \overline{\alpha}]$ then $\mu \simeq \alpha$ and

$$\overline{\alpha \times \alpha} = \overline{\mu \times \mu} = \overline{\mu} = \overline{\alpha}.$$

However if $(\forall \mu < \alpha)[\overline{\mu} < \overline{\alpha}],$ then since $\mu < \omega \vee \overline{\mu + 1} = \overline{\mu}$ it follows from Proposition 10.37 that $\mu + 1 < \overline{\alpha} \leq \alpha$. Therefore by our induction hypothesis

$$\alpha > \mu \geq \omega \rightarrow (\mu + 1) \times (\mu + 1) = \overline{\mu + 1}.$$

Recall the relation $R_0$ of Definition 7.57. By Theorem 7.58, $R_0$ well orders $On^2$. Consequently there is an order isomorphism $J_0$ such that

$$J_0 \text{ Isom}_{R_0, E}(\text{On}^2, \text{On}).$$

We wish to show that $J_0''(\alpha \times \

Since $J_0$ is one-to-one

$$\overline{\alpha \times \alpha} = J_0^\alpha(\alpha \times \alpha) \leq \overline{\alpha}.$$

But from Proposition 10.38

$$\overline{\alpha} = \overline{\alpha} + 1 \leq \overline{\alpha \times \alpha}.$$

Therefore $\overline{\alpha \times \alpha} = \overline{\alpha}.$
