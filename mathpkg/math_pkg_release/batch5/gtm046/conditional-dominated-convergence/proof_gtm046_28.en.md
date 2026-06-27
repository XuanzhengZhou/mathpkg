---
role: proof
locale: en
of_concept: conditional-dominated-convergence
source_book: gtm046
source_chapter: "VIII"
source_section: "28"
---
Assume $|X_n| \leq Y$ a.s. with $Y$ integrable and $X_n \xrightarrow{\text{a.s.}} X$. By the conditional Fatou-Lebesgue theorem (28.1), since $-Y \leq X_n \leq Y$ a.s.,
$$E^{\mathfrak{B}} X = E^{\mathfrak{B}} \liminf X_n \leq \liminf E^{\mathfrak{B}} X_n \leq \limsup E^{\mathfrak{B}} X_n \leq E^{\mathfrak{B}} \limsup X_n = E^{\mathfrak{B}} X \text{ a.s.}$$
Thus all inequalities are equalities and $E^{\mathfrak{B}} X_n \xrightarrow{\text{a.s.}} E^{\mathfrak{B}} X$.
