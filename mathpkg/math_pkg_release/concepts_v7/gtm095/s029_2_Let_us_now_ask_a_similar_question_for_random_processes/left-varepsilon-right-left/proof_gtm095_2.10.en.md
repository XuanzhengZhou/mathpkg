---
role: proof
locale: en
of_concept: left-varepsilon-right-left
source_book: gtm095
source_chapter: "2"
source_section: "10"
---

# Proof of Sufficient Condition for Almost Sure Convergence via Summability

**Corollary.** Since

$$P\left\{\sup_{k \geq n} |\xi_k - \xi| \geq \varepsilon\right\} = P\left\{\bigcup_{k \geq n} (|\xi_k - \xi| \geq \varepsilon)\right\} \leq \sum_{k \geq n} P\{|\xi_k - \xi| \geq \varepsilon\},$$

a sufficient condition for $\xi_n \to \xi$ (P-a.s.) is that

$$\sum_{k=1}^{\infty} P\{|\xi_k - \xi| \geq \varepsilon\} < \infty$$

is satisfied for every $\varepsilon > 0$.

*Proof.* This follows directly from Theorem 1(a) and the union bound. Set $A_k^\varepsilon = \{|\xi_k - \xi| \geq \varepsilon\}$. Then

$$P\left\{\sup_{k \geq n} |\xi_k - \xi| \geq \varepsilon\right\} = P\left(\bigcup_{k \geq n} A_k^\varepsilon\right) \leq \sum_{k \geq n} P(A_k^\varepsilon).$$

If $\sum_{k=1}^{\infty} P(A_k^\varepsilon) < \infty$, then the tail sum $\sum_{k \geq n} P(A_k^\varepsilon) \to 0$ as $n \to \infty$. Hence $P\{\sup_{k \geq n} |\xi_k - \xi| \geq \varepsilon\} \to 0$, and by Theorem 1(a), $\xi_n \to \xi$ (P-a.s.). $\square$
