---
role: proof
locale: en
of_concept: change-of-variables-in-a-lebesgue-integral
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of the Change of Variables Formula in a Lebesgue Integral

**Theorem 7 (Change of Variables in a Lebesgue Integral).** Let $(\Omega, \mathcal{F})$ and $(E, \mathcal{E})$ be measurable spaces and $X = X(\omega)$ an $\mathcal{F}/\mathcal{E}$-measurable function with values in $E$. Let $P$ be a probability measure on $(\Omega, \mathcal{F})$ and $P_X$ the probability measure on $(E, \mathcal{E})$ induced by $X$:

$$P_X(A) = P\{\omega : X(\omega) \in A\}, \quad A \in \mathcal{E}.$$

Then for every $\mathcal{E}$-measurable function $g = g(x)$, $x \in E$,

$$\int_A g(x) P_X(dx) = \int_{X^{-1}(A)} g(X(\omega)) P(d\omega), \quad A \in \mathcal{E},$$

in the sense that if one integral exists, the other is well defined, and the two are equal.

*Proof.* The proof proceeds by the standard approximation method:

1. **Indicator functions:** For $g(x) = I_B(x)$ with $B \in \mathcal{E}$, the formula reduces to $P_X(A \cap B) = P(X^{-1}(A) \cap X^{-1}(B))$, which holds by the definition of the induced measure $P_X$.

2. **Simple functions:** By linearity, the formula extends to finite linear combinations of indicator functions.

3. **Nonnegative functions:** For a general nonnegative measurable $g$, approximate from below by simple functions $g_n \uparrow g$. Then $g_n \circ X \uparrow g \circ X$, and the Monotone Convergence Theorem applied to both sides yields the result.

4. **General functions:** Decompose $g = g^+ - g^-$ and apply step 3 to each part. The equality holds whenever either side is well-defined (not of the form $\infty - \infty$). $\square$
