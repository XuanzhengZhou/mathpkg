---
role: proof
locale: en
of_concept: additivity-expectation-nonnegative
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of Additivity of Expectation for Nonnegative Random Variables

**Property E.** Let $\xi \geq 0$ and $\eta \geq 0$. Then $E(\xi + \eta) = E\xi + E\eta$.

*Proof.* Let $\{\xi_n\}$ and $\{\eta_n\}$ be sequences of simple functions such that $\xi_n \uparrow \xi$ and $\eta_n \uparrow \eta$ (such sequences exist by the definition of the Lebesgue integral for nonnegative functions). For simple functions, additivity of the integral holds by the definition of the integral as a sum. Then

$$E(\xi_n + \eta_n) = E\xi_n + E\eta_n.$$

By the monotone convergence theorem (or by the definition of the Lebesgue integral of a nonnegative function),

$$E(\xi_n + \eta_n) \uparrow E(\xi + \eta), \quad E\xi_n \uparrow E\xi, \quad E\eta_n \uparrow E\eta.$$

Taking limits as $n \to \infty$ yields $E(\xi + \eta) = E\xi + E\eta$. $\square$
