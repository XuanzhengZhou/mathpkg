---
role: proof
locale: en
of_concept: trace-of-direct-sum
source_book: gtm013
source_chapter: "1"
source_section: "8"
---

Applying Proposition 8.16 to the natural injections $\iota_\alpha: M_\alpha \to \oplus_A M_\alpha$ and projections $\pi_\alpha: \oplus_A M_\alpha \to M_\alpha$, we have:

$$\mathrm{Tr}_{\oplus_A M_\alpha}(\mathcal{U}) = \Sigma \iota_\alpha \pi_\alpha(\mathrm{Tr}_{\oplus_A M_\alpha}(\mathcal{U}))$$

$$\leq \Sigma \iota_\alpha(\mathrm{Tr}_{M_\alpha}(\mathcal{U})) \leq \mathrm{Tr}_{\oplus_A M_\alpha}(\mathcal{U}).$$

Thus the inequalities are equalities. But

$$\Sigma \iota_\alpha(\mathrm{Tr}_{M_\alpha}(\mathcal{U})) = \bigoplus_A \mathrm{Tr}_{M_\alpha}(\mathcal{U}),$$

which completes the proof.
