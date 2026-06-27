---
role: proof
locale: en
of_concept: fatous-lemma
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of Fatou's Lemma

**Theorem 2 (Fatou's Lemma).** Let $\eta, \xi, \xi_1, \xi_2, \ldots$ be random variables.

(a) If $\xi_n \geq \eta$ for all $n \geq 1$ and $E\eta > -\infty$, then

$$E \liminf \xi_n \leq \liminf E\xi_n.$$

(b) If $\xi_n \leq \eta$ for all $n \geq 1$ and $E\eta < \infty$, then

$$\limsup E\xi_n \leq E \limsup \xi_n.$$

(c) If $|\xi_n| \leq \eta$ for all $n \geq 1$ and $E\eta < \infty$, then

$$E \liminf \xi_n \leq \liminf E\xi_n \leq \limsup E\xi_n \leq E \limsup \xi_n.$$

*Proof.* (a) Let $\zeta_n = \inf_{m \geq n} \xi_m$; then

$$\liminf \xi_n = \lim_{n} \inf_{m \geq n} \xi_m = \lim_{n} \zeta_n.$$

It is clear that $\zeta_n \uparrow \liminf \xi_n$ and $\zeta_n \geq \eta$ for all $n \geq 1$, so $E\zeta_n$ is defined (since $E\eta > -\infty$). Then by the Monotone Convergence Theorem (Theorem 1),

$$E \liminf \xi_n = E \lim_{n} \zeta_n = \lim_{n} E\zeta_n = \liminf E\zeta_n \leq \liminf E\xi_n,$$

which establishes (a).

(b) Follows from (a) by replacing $\xi_n$ with $-\xi_n$ and $\eta$ with $-\eta$.

(c) The first inequality follows from (a) with $\eta$ replaced by $-\eta$ (since $|\xi_n| \leq \eta$ implies $\xi_n \geq -\eta$ and $E(-\eta) > -\infty$). The last inequality follows from (b). The middle inequality is always true for any sequence of real numbers. $\square$
