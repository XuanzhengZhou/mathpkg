---
role: proof
locale: en
of_concept: on-taking-limits-under-the-conditional-expectation-sign
source_book: gtm095
source_chapter: "II"
source_section: "4"
---

# Proof of Theorem 2 (On Taking Limits Under the Conditional Expectation Sign)

**Theorem.** Let $\{\xi_n\}_{n \geq 1}$ be a sequence of random variables, let $\mathcal{G}$ be a $\sigma$-subalgebra of $\mathcal{F}$, and suppose that all expectations are defined.

(a) If $|\xi_n| \leq \eta$, $E\eta < \infty$, and $\xi_n \to \xi$ (a.s.), then

$$E(\xi_n \mid \mathcal{G}) \to E(\xi \mid \mathcal{G}) \quad \text{(a.s. and in } L^1\text{)}.$$

(b) If $\xi_n \uparrow \xi$ (a.s.) and $E\xi_1^- < \infty$, then $E(\xi_n \mid \mathcal{G}) \uparrow E(\xi \mid \mathcal{G})$ (a.s.).

(c) If $\xi_n \geq \eta$, $E\eta > -\infty$, and $\xi_n \downarrow \xi$ (a.s.), then $E(\xi_n \mid \mathcal{G}) \downarrow E(\xi \mid \mathcal{G})$ (a.s.).

(d) If $\xi_n \geq \eta$, $E\eta > -\infty$, then

$$E(\liminf \xi_n \mid \mathcal{G}) \leq \liminf E(\xi_n \mid \mathcal{G}) \quad \text{(a.s.)}.$$

(e) If $\xi_n \leq \eta$, $E\eta < \infty$, then

$$\limsup E(\xi_n \mid \mathcal{G}) \leq E(\limsup \xi_n \mid \mathcal{G}) \quad \text{(a.s.)}.$$

(f) If $\xi_n \geq 0$, then

$$E\left(\sum \xi_n \mid \mathcal{G}\right) = \sum E(\xi_n \mid \mathcal{G}) \quad \text{(a.s.)}.$$

*Proof.* (a) Let $\zeta_n = \sup_{m \geq n} |\xi_m - \xi|$. Since $\xi_n \to \xi$ (a.s.), we have $\zeta_n \downarrow 0$ (a.s.). The expectations $E\xi_n$ and $E\xi$ are finite; therefore by Properties D* and C* (a.s.)

$$|E(\xi_n \mid \mathcal{G}) - E(\xi \mid \mathcal{G})| = |E(\xi_n - \xi \mid \mathcal{G})| \leq E(|\xi_n - \xi| \mid \mathcal{G}) \leq E(\zeta_n \mid \mathcal{G}).$$

Since $E(\zeta_{n+1} \mid \mathcal{G}) \leq E(\zeta_n \mid \mathcal{G})$ (a.s.), the limit $h = \lim_n E(\zeta_n \mid \mathcal{G})$ exists (a.s.). Then

$$0 \leq \int_{\Omega} h \, dP \leq \int_{\Omega} E(\zeta_n \mid \mathcal{G}) \, dP = \int_{\Omega} \zeta_n \, dP \to 0, \quad n \to \infty,$$

where the last statement follows from the dominated convergence theorem, since $0 \leq \zeta_n \leq 2\eta$, $E\eta < \infty$. Consequently $\int_{\Omega} h \, dP = 0$ and then $h = 0$ (a.s.) by Property H.

(b) First let $\eta \equiv 0$. Since $E(\xi_n \mid \mathcal{G}) \leq E(\xi_{n+1} \mid \mathcal{G})$ (a.s.), the sequence $E(\xi_n \mid \mathcal{G})$ increases to a limit $Z$ (a.s.). By the monotone convergence theorem and the definition of conditional expectation,

$$\int_A Z \, dP = \lim_n \int_A E(\xi_n \mid \mathcal{G}) \, dP = \lim_n \int_A \xi_n \, dP = \int_A \xi \, dP, \quad A \in \mathcal{G},$$

so $Z = E(\xi \mid \mathcal{G})$ (a.s.). The general case follows by applying the above to $\xi_n - \xi_1$.

(c) This follows from (b) by considering $-\xi_n$.

(d) Let $\zeta_n = \inf_{m \geq n} \xi_m$. Then $\zeta_n \uparrow \liminf \xi_n$, and by (b),

$$E(\liminf \xi_n \mid \mathcal{G}) = \lim_n E(\zeta_n \mid \mathcal{G}) \leq \liminf E(\xi_n \mid \mathcal{G}) \quad \text{(a.s.)}.$$

Conclusion (e) follows from (d).

(f) If $\xi_n \geq 0$, by Property D* we have

$$E\left( \sum_{k=1}^{n} \xi_k \mid \mathcal{G} \right) = \sum_{k=1}^{n} E(\xi_k \mid \mathcal{G}) \quad \text{(a.s.)},$$

which, with (b), establishes the required result.

This completes the proof of the theorem.
