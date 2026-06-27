---
role: proof
locale: en
of_concept: factor-algebra-field-irreducible
source_book: gtm023
source_chapter: "XII"
source_section: "3"
---

Suppose $f$ is reducible: $f = gh$ with $\deg g \geq 1$, $\deg h \geq 1$. Then $g \notin I_f$ and $h \notin I_f$ (since their degrees are less than $\deg f$). Thus $\bar{g} \neq 0$ and $\bar{h} \neq 0$ in $\Gamma[t]/I_f$. But $\bar{g}\bar{h} = \overline{gh} = \bar{f} = 0$, so $\Gamma[t]/I_f$ has zero divisors and is not a field.

Conversely, suppose $f$ is irreducible. Let $\bar{g} \neq 0$ in $\Gamma[t]/I_f$, so $f \nmid g$. Since $f$ is irreducible, $f$ and $g$ are relatively prime. By the Bezout identity (Corollary to Proposition II, sec. 12.7), there exist $u, v$ such that $uf + vg = 1$. Modulo $I_f$, this gives $\bar{v}\bar{g} = \bar{1}$, so $\bar{g}$ is invertible. Thus every non-zero element is invertible, making $\Gamma[t]/I_f$ a field.
