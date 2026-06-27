---
role: proof
locale: en
of_concept: random-variable-16
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of Theorem 4 (Uniformly Integrable Convergence)

**Theorem 4.** Let $\{\xi_n\}_{n \geq 1}$ be a uniformly integrable family of random variables. Then

(a) $E \liminf \xi_n \leq \liminf E\xi_n \leq \limsup E\xi_n \leq E \limsup \xi_n$.

(b) If in addition $\xi_n \to \xi$ (a.s.), then $\xi$ is integrable and

$$E\xi_n \to E\xi, \quad E|\xi_n - \xi| \to 0, \quad n \to \infty.$$

*Proof.* (a) For every $c > 0$,

$$E\xi_n = E[\xi_n I_{\{|\xi_n| < -c\}}] + E[\xi_n I_{\{|\xi_n| \geq -c\}}].$$

By uniform integrability, for every $\varepsilon > 0$ we can take $c$ so large that

$$\sup_n |E[\xi_n I_{\{|\xi_n| < -c\}}]| < \varepsilon.$$

By Fatou's lemma,

$$\liminf E[\xi_n I_{\{|\xi_n| \geq -c\}}] \geq E[\liminf \xi_n I_{\{|\xi_n| \geq -c\}}].$$

Combining these estimates yields $E \liminf \xi_n \leq \liminf E\xi_n$. The remaining inequalities follow similarly or by applying the first to $-\xi_n$.

(b) When $\xi_n \to \xi$ (a.s.), part (a) gives $E\xi_n \to E\xi$. The $L^1$ convergence $E|\xi_n - \xi| \to 0$ follows by applying (a) to $|\xi_n - \xi|$, noting that uniform integrability of $\{\xi_n\}$ implies uniform integrability of $\{|\xi_n - \xi|\}$. $\square$
