---
role: proof
locale: en
of_concept: conditional-fatou-lebesgue
source_book: gtm046
source_chapter: "VIII"
source_section: "28"
---
Assume $Y$ and $Z$ are integrable and $Y \leq X_n$ a.s. or $X_n \leq Z$ a.s. For the case $Y \leq X_n$ a.s., set $\underline{X}_n = \inf_{k \geq n} X_k$. Then $\underline{X}_n \uparrow \liminf X_n$ and $Y \leq \underline{X}_n$. By the conditional monotone convergence theorem (28.1),
$$E^{\mathfrak{B}} \underline{X}_n \uparrow E^{\mathfrak{B}} \liminf X_n \text{ a.s.}$$
Since $E^{\mathfrak{B}} X_n \geq E^{\mathfrak{B}} \underline{X}_n$, we obtain
$$\liminf E^{\mathfrak{B}} X_n \geq E^{\mathfrak{B}} \liminf X_n \text{ a.s.}$$
The case $X_n \leq Z$ a.s. yields, by symmetry, $\limsup E^{\mathfrak{B}} X_n \leq E^{\mathfrak{B}} \limsup X_n$ a.s. The full Fatou-Lebesgue assertion follows from these inequalities exactly as in the non-conditional case.
