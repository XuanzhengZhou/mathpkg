---
role: proof
locale: en
of_concept: lebesgue-dominated-convergence-theorem
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of Lebesgue's Dominated Convergence Theorem

**Theorem 3 (Lebesgue's Theorem on Dominated Convergence).** Let $\eta, \xi, \xi_1, \xi_2, \ldots$ be random variables such that $|\xi_n| \leq \eta$, $E\eta < \infty$ and $\xi_n \to \xi$ (a.s.). Then $E|\xi| < \infty$,

$$E\xi_n \to E\xi$$

and

$$E|\xi_n - \xi| \to 0$$

as $n \to \infty$.

*Proof.* By hypothesis, $\liminf \xi_n = \limsup \xi_n = \xi$ (a.s.). Therefore by Fatou's lemma (Theorem 2, item (c)),

$$E\xi = E \liminf \xi_n \leq \liminf E\xi_n \leq \limsup E\xi_n \leq E \limsup \xi_n = E\xi,$$

which forces all inequalities to be equalities, establishing $\lim E\xi_n = E\xi$, i.e., (8).

It is also clear that $|\xi| \leq \eta$, hence $E|\xi| \leq E\eta < \infty$.

For conclusion (9), note that $|\xi_n - \xi| \leq 2\eta$ and $|\xi_n - \xi| \to 0$ (a.s.). Applying what was just proved to the sequence $|\xi_n - \xi|$ (dominated by $2\eta$ with finite expectation), we obtain $E|\xi_n - \xi| \to E[0] = 0$. $\square$
