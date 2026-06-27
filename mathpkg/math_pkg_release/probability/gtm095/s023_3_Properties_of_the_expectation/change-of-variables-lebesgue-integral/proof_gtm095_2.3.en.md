---
role: proof
locale: en
of_concept: change-of-variables-lebesgue-integral
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of the Change of Variables in a Lebesgue Integral

**Theorem 7 (Change of Variables in a Lebesgue Integral).** Let $(\Omega, \mathcal{F})$ and $(E, \mathcal{E})$ be measurable spaces and $X = X(\omega)$ an $\mathcal{F}/\mathcal{E}$-measurable function with values in $E$. Let $P$ be a probability measure on $(\Omega, \mathcal{F})$ and $P_X$ the probability measure on $(E, \mathcal{E})$ induced by $X = X(\omega)$:

$$P_X(A) = P\{\omega : X(\omega) \in A\}, \quad A \in \mathcal{E}. \tag{40}$$

Then

$$\int_A g(x) P_X(dx) = \int_{X^{-1}(A)} g(X(\omega)) P(d\omega), \quad A \in \mathcal{E}, \tag{41}$$

for every $\mathcal{E}$-measurable function $g = g(x)$, $x \in E$ (in the sense that if one integral exists, the other is well defined, and the two are equal).

*Proof.* Let $A \in \mathcal{E}$ and $g(x) = I_B(x)$, where $B \in \mathcal{E}$. Then (41) becomes

$$P_X(A \cap B) = P(X^{-1}(A) \cap X^{-1}(B)),$$

which holds by definition of $P_X$, since $X^{-1}(A \cap B) = X^{-1}(A) \cap X^{-1}(B)$. Thus (41) holds for indicator functions of measurable sets.

By linearity of the integral, (41) extends to nonnegative simple functions (finite linear combinations of indicator functions). For a general nonnegative $\mathcal{E}$-measurable function $g$, approximate $g$ from below by an increasing sequence of nonnegative simple functions $g_n \uparrow g$. Then $g_n(X(\omega)) \uparrow g(X(\omega))$, and by the Monotone Convergence Theorem applied to both sides of (41) for $g_n$, we obtain (41) for $g$.

For a general $\mathcal{E}$-measurable function $g$, decompose $g = g^+ - g^-$ and apply the result for nonnegative functions to each part. The equality holds whenever either side is well-defined (i.e., not $\infty - \infty$).

In particular, for $A = E$ (or $A = \mathbb{R}$ when $(E, \mathcal{E}) = (\mathbb{R}, \mathcal{B}(\mathbb{R}))$ and $X = \xi$), we obtain

$$E g(\xi(\omega)) = \int_\Omega g(\xi(\omega)) P(d\omega) = \int_{\mathbb{R}} g(x) P_\xi(dx). \tag{43}$$

$\square$
