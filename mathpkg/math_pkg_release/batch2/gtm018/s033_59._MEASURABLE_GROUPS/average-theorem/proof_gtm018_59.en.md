---
role: proof
locale: en
of_concept: average-theorem
source_book: gtm018
source_chapter: "XI"
source_section: "59. Measurable Groups"
---

**Measurability and integral of $f$.** Recall $Q = S^{-1}RS$ is a measure preserving transformation of $(X \times X, \mathbf{S} \times \mathbf{S}, \mu \times \mu)$ onto itself (since $S$, $R$, and $S^{-1}$ are each measure preserving). Now
$$f(x) = \mu(x^{-1}A \cap B) = \mu((Q(A \times B^{-1}))_x).$$
Indeed, by Theorem C,
$$(Q(A \times B^{-1}))_x = x^{-1}(x^{-1})^{-1}(Q(A \times B^{-1}))_{x^{-1}}?$$
Wait — let us verify. By Theorem C,
$$(Q(A \times B^{-1}))_{x^{-1}} = x A \cap (B^{-1})^{-1} = xA \cap B.$$
Replacing $x^{-1}$ by $x$, we have $(Q(A \times B^{-1}))_x = x^{-1}A \cap B$. Therefore
$$f(x) = \mu((Q(A \times B^{-1}))_x).$$
Since $Q$ is measure preserving, by Fubini's theorem,
$$\int f(x) \, d\mu(x) = \int \mu((Q(A \times B^{-1}))_x) \, d\mu(x) = (\mu \times \mu)(Q(A \times B^{-1})) = (\mu \times \mu)(A \times B^{-1}) = \mu(A)\mu(B^{-1}).$$
The measurability of $f$ follows from the standard fact that the section measure function of a measurable set is measurable (a consequence of Fubini's theorem).

**Measurability of $\{x : g(x) < \varepsilon\}$.** Define $\hat{f}(x) = f(x^{-1}) = \mu(xA \cap B)$. By Theorem D, $\hat{f}$ is measurable. Observe the symmetric difference identity:
$$\mu(xA \,\Delta\, B) = \mu(xA) + \mu(B) - 2\mu(xA \cap B) = \mu(A) + \mu(B) - 2\hat{f}(x),$$
using the translation invariance $\mu(xA) = \mu(A)$. Therefore
$$g(x) < \varepsilon \iff \mu(A) + \mu(B) - 2\hat{f}(x) < \varepsilon \iff \hat{f}(x) > \frac{1}{2}(\mu(A) + \mu(B) - \varepsilon).$$
The set on the right is the inverse image under the measurable function $\hat{f}$ of an open interval, hence measurable.
