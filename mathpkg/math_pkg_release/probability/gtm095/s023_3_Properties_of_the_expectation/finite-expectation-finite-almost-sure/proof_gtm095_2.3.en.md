---
role: proof
locale: en
of_concept: finite-expectation-finite-almost-sure
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof that Finite Expectation Implies Finiteness Almost Surely

**Property J.** Let $\xi$ be an extended random variable and $E|\xi| < \infty$. Then $|\xi| < \infty$ (a.s.).

*Proof.* Let $A = \{\omega : |\xi(\omega)| = \infty\}$ and suppose $P(A) > 0$. Then

$$E|\xi| \geq E(|\xi| I_A) = \infty \cdot P(A) = \infty,$$

which contradicts the hypothesis $E|\xi| < \infty$. Therefore $P(A) = 0$, meaning $|\xi| < \infty$ almost surely. $\square$
