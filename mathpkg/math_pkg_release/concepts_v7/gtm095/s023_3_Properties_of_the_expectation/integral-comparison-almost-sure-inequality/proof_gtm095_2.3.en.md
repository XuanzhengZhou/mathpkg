---
role: proof
locale: en
of_concept: integral-comparison-almost-sure-inequality
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of Integral Comparison Implies Almost Sure Inequality

**Property I.** Let $\xi$ and $\eta$ be such that $E|\xi| < \infty$, $E|\eta| < \infty$ and $E(\xi I_A) \leq E(\eta I_A)$ for all $A \in \mathcal{F}$. Then $\xi \leq \eta$ (a.s.).

*Proof.* Let $B = \{\omega : \xi(\omega) > \eta(\omega)\}$. Then, by hypothesis,

$$E(\eta I_B) \leq E(\xi I_B) \leq E(\eta I_B),$$

and therefore $E(\xi I_B) = E(\eta I_B)$. By Property E (additivity, extended via subtracting finite expectations),

$$E((\xi - \eta)I_B) = 0.$$

Since $(\xi - \eta)I_B \geq 0$ by the definition of $B$, Property H implies $(\xi - \eta)I_B = 0$ (a.s.), whence $P(B) = 0$. Thus $\xi \leq \eta$ almost surely. $\square$
