---
role: proof
locale: en
of_concept: conditional-monotone-convergence
source_book: gtm046
source_chapter: "VIII"
source_section: "28"
---
Assume $0 \leq X_n \uparrow X$ a.s. For every $B \in \mathfrak{B}$, by the ordinary monotone convergence theorem,
$$\int_B E^{\mathfrak{B}} X_n \, dP = \int_B X_n \, dP \uparrow \int_B X \, dP = \int_B E^{\mathfrak{B}} X \, dP.$$
Thus the indefinite integrals of $E^{\mathfrak{B}} X_n$ converge monotonically to the indefinite integral of $E^{\mathfrak{B}} X$ on $\mathfrak{B}$. Since $E^{\mathfrak{B}} X_n$ is an increasing sequence of $\mathfrak{B}$-measurable functions, the limit is $\mathfrak{B}$-measurable and equals $E^{\mathfrak{B}} X$ up to $P_{\mathfrak{B}}$-equivalence. The particular case $P^{\mathfrak{B}} \sum A_k = \sum P^{\mathfrak{B}} A_k$ a.s. follows by taking $X_n = \sum_{k=1}^n I_{A_k}$.
