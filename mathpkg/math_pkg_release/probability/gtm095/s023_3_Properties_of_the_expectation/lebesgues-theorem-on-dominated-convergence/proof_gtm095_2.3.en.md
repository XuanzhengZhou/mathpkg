---
role: proof
locale: en
of_concept: lebesgues-theorem-on-dominated-convergence
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of Lebesgue's Theorem on Dominated Convergence

**Theorem 3 (Lebesgue's Theorem on Dominated Convergence).** Let $\eta, \xi, \xi_1, \xi_2, \ldots$ be random variables such that $|\xi_n| \leq \eta$, $E\eta < \infty$ and $\xi_n \to \xi$ (a.s.). Then $E|\xi| < \infty$,

$$E\xi_n \to E\xi \quad \text{and} \quad E|\xi_n - \xi| \to 0$$

as $n \to \infty$.

*Proof.* Since $\xi_n \to \xi$ (a.s.), we have $\liminf \xi_n = \limsup \xi_n = \xi$ (a.s.). By Fatou's lemma (item (c)),

$$E\xi = E \liminf \xi_n \leq \liminf E\xi_n \leq \limsup E\xi_n \leq E \limsup \xi_n = E\xi.$$

Hence $\lim E\xi_n = E\xi$. Moreover, $|\xi| \leq \eta$ implies $E|\xi| < \infty$.

For the $L^1$ convergence, observe that $|\xi_n - \xi| \leq 2\eta$, $E[2\eta] < \infty$, and $|\xi_n - \xi| \to 0$ (a.s.). Applying the first part to the sequence $\{|\xi_n - \xi|\}$ yields $E|\xi_n - \xi| \to 0$. $\square$
