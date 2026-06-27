---
role: proof
locale: en
of_concept: uniformly-integrable-convergence
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of Convergence Theorem for Uniformly Integrable Families

**Theorem.** Let $\{\xi_n\}_{n \geq 1}$ be a uniformly integrable family of random variables. Then

(a) $E \liminf \xi_n \leq \liminf E\xi_n \leq \limsup E\xi_n \leq E \limsup \xi_n$.

(b) If in addition $\xi_n \to \xi$ (a.s.), then $\xi$ is integrable and $E\xi_n \to E\xi$, $E|\xi_n - \xi| \to 0$.

*Proof.* (a) For every $c > 0$,

$$E\xi_n = E[\xi_n I_{\{|\xi_n| < -c\}}] + E[\xi_n I_{\{|\xi_n| \geq -c\}}].$$

By uniform integrability, for every $\varepsilon > 0$ we can take $c$ so large that

$$\sup_n |E[\xi_n I_{\{|\xi_n| < -c\}}]| < \varepsilon.$$

By Fatou's lemma, $\liminf E[\xi_n I_{\{|\xi_n| \geq -c\}}] \geq E[\liminf \xi_n I_{\{|\xi_n| \geq -c\}}]$. Combining these estimates yields the desired inequality.

(b) If $\xi_n \to \xi$ (a.s.), then $\liminf \xi_n = \limsup \xi_n = \xi$ (a.s.), so (a) forces $E\xi_n \to E\xi$. The $L^1$ convergence follows by applying (a) to $|\xi_n - \xi|$. $\square$
