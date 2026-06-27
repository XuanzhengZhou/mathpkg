---
role: proof
locale: en
of_concept: conditional-convergence-rth-mean
source_book: gtm046
source_chapter: "VIII"
source_section: "28"
---
If $X_n \xrightarrow{r} X$, then $E|X_n - X|^r \to 0$. By the conditional $c_r$-inequality (which holds a.s. by 28.1),
$$E^{\mathfrak{B}}|X_n - X|^r \leq c_r (E^{\mathfrak{B}}|X_n|^r + E^{\mathfrak{B}}|X|^r) \text{ a.s.}$$
and $E^{\mathfrak{B}} X_n \xrightarrow{r} E^{\mathfrak{B}} X$ follows by the corresponding proof for ordinary expectations, using the fact that $E^{\mathfrak{B}}$ preserves monotonicity and linearity. The conditional expectation preserves $L_r$-convergence because it is an a.s. contraction on $L_r$ spaces.
