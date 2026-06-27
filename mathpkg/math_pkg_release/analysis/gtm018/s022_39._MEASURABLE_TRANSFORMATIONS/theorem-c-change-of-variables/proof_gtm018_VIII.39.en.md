---
role: proof
locale: en
of_concept: theorem-c-change-of-variables
source_book: gtm018
source_chapter: "VIII"
source_section: "39. Measurable Transformations"
---
It suffices to treat nonnegative $g$. If $g = \chi_F$ for measurable $F \subseteq Y$, then $gT = \chi_{T^{-1}(F)}$ by Theorem A, so
$$\int g \, d(\mu T^{-1}) = (\mu T^{-1})(F) = \mu(T^{-1}(F)) = \int (gT) \, d\mu.$$
The equality extends to simple functions by linearity. For general nonnegative $g$, take an increasing sequence $\{g_n\}$ of simple functions converging to $g$; then $\{g_nT\}$ increases to $gT$, and the result follows by taking limits of integrals.
