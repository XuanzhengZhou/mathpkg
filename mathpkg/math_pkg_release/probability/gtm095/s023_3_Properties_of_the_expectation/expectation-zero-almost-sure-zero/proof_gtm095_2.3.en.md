---
role: proof
locale: en
of_concept: expectation-zero-almost-sure-zero
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof that Zero Expectation Implies Almost Sure Zero for Nonnegative Variables

**Property H.** Let $\xi \geq 0$ and $E\xi = 0$. Then $\xi = 0$ (a.s.).

*Proof.* Let $A = \{\omega : \xi(\omega) > 0\}$ and $A_n = \{\omega : \xi(\omega) \geq 1/n\}$. It is clear that $A_n \uparrow A$ and $0 \leq \xi I_{A_n} \leq \xi I_A$. Hence, by Property B,

$$0 \leq E[\xi I_{A_n}] \leq E\xi = 0.$$

Consequently

$$0 = E[\xi I_{A_n}] \geq \frac{1}{n} P(A_n),$$

and therefore $P(A_n) = 0$ for all $n \geq 1$. But $P(A) = \lim_{n} P(A_n)$ (by continuity of probability measure), and therefore $P(A) = 0$, which means $\xi = 0$ almost surely. $\square$
