---
role: proof
locale: en
of_concept: canonical-injections-product
source_book: gtm013
source_chapter: "1"
source_section: "1.6"
---

The condition $\pi_\beta \iota_\alpha = \delta_{\alpha\beta} 1_{R_\alpha}$ means that $(\iota_\alpha(r))(\beta) = r$ if $\beta = \alpha$ and $0$ otherwise. For addition:

$$(\iota_\alpha(r + s))(\beta) = \begin{cases} r + s & \beta = \alpha \\ 0 & \beta \neq \alpha \end{cases} = (\iota_\alpha(r) + \iota_\alpha(s))(\beta).$$

For multiplication:

$$(\iota_\alpha(rs))(\beta) = \begin{cases} rs & \beta = \alpha \\ 0 & \beta \neq \alpha \end{cases} = (\iota_\alpha(r)\iota_\alpha(s))(\beta).$$

Thus $\iota_\alpha$ preserves both operations. Injectivity is clear. However, if $|A| \geq 2$, then $\iota_\alpha(1_{R_\alpha})$ has $1_{R_\alpha}$ at coordinate $\alpha$ and $0$ elsewhere, which differs from $1_R = (1_{R_\beta})_{\beta \in A}$. Hence $\iota_\alpha$ does not preserve the multiplicative identity and is not a ring homomorphism.
