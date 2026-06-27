---
role: proof
locale: en
of_concept: conditional-expectation-measurable-factor
source_book: gtm046
source_chapter: "VIII"
source_section: "28.2"
---
The assertion holds for $X = I_{B'}$ where $B' \in \mathfrak{B}$, since for every $B \in \mathfrak{B}$,
$$\int_B (E^{\mathfrak{B}} I_{B'} Y) \, dP_{\mathfrak{B}} = \int_B I_{B'} Y \, dP = \int_{B B'} (E^{\mathfrak{B}} Y) \, dP_{\mathfrak{B}} = \int_B (I_{B'} E^{\mathfrak{B}} Y) \, dP_{\mathfrak{B}}.$$
Therefore, it holds for simple functions $X_n$:
$$E^{\mathfrak{B}} X_n Y = X_n E^{\mathfrak{B}} Y \text{ a.s.}$$
and, by the monotone convergence theorem for conditional expectations, it holds for nonnegative functions — take $0 \leq X_n \uparrow X$ and let $n \to \infty$ in the foregoing relation. The assertion follows for general $X$ by decomposition into positive and negative parts.
