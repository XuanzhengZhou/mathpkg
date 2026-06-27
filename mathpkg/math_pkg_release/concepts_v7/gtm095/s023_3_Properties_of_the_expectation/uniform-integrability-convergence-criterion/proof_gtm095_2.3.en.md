---
role: proof
locale: en
of_concept: uniform-integrability-convergence-criterion
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of Uniform Integrability Criterion for Convergence of Expectations

**Theorem (Uniform Integrability Criterion).** A family $\{\xi_n\}_{n\geq 1}$ is uniformly integrable if and only if

$$\sup_n E|\xi_n| < \infty$$

and for every $\varepsilon > 0$ there exists $\delta > 0$ such that $P(A) < \delta$ implies $\sup_n E[|\xi_n| I_A] \leq \varepsilon$ (uniform absolute continuity).

*Proof.* **Necessity.** Condition $\sup_n E|\xi_n| < \infty$ was verified above. Moreover,

$$E[|\xi_n| I_A] = E[|\xi_n| I_{A \cap \{|\xi_n| \geq c\}}] + E[|\xi_n| I_{A \cap \{|\xi_n| < c\}}]$$
$$\leq E[|\xi_n| I_{\{|\xi_n| \geq c\}}] + cP(A). \tag{17}$$

Take $c$ so large that $\sup_n E[|\xi_n| I_{\{|\xi_n| \geq c\}}] \leq \varepsilon/2$. Then if $P(A) \leq \varepsilon/(2c)$, we have $\sup_n E[|\xi_n| I_A] \leq \varepsilon$ by (17). This establishes the uniform absolute continuity.

**Sufficiency.** Let $\varepsilon > 0$ and let $\delta > 0$ be chosen so that $P(A) < \delta$ implies $E[|\xi_n| I_A] \leq \varepsilon$, uniformly in $n$. Since

$$E[|\xi_n|] \geq E[|\xi_n| I_{\{|\xi_n| \geq c\}}] \geq cP(|\xi_n| \geq c)$$

for every $c > 0$ (cf. Chebyshev's inequality), we have

$$\sup_n P(|\xi_n| \geq c) \leq \frac{1}{c} \sup_n E|\xi_n| \to 0, \quad c \to \infty.$$

Therefore, when $c$ is sufficiently large, any set $\{|\xi_n| \geq c\}$, $n \geq 1$, can be taken as $A$. Hence $\sup_n E[|\xi_n| I_{\{|\xi_n| \geq c\}}] \leq \varepsilon$, which establishes uniform integrability. $\square$
