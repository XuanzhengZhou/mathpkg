---
role: proof
source_book: gtm-0073
chapter: VII
section: "VII.3"
proof_technique: uniqueness-and-existence
locale: en
content_hash: ""
written_against: ""
---
(Uniqueness) If such an alternating $n$-linear form $f$ exists and $(X_1, \ldots, X_n) \in (R^n)^n$, write $X_i = \sum_{j=1}^{n} a_{ij} \varepsilon_j$. By multilinearity,
\[
f(X_1, \ldots, X_n) = \sum_{\sigma \in S_n} (\operatorname{sgn} \sigma) a_{1\sigma 1} a_{2\sigma 2} \cdots a_{n\sigma n} \cdot r.
\]
Thus any such $f$ is given by this formula, proving uniqueness.

(Existence) Define $f$ by the formula above. Verify multilinearity and the alternating property: if $X_i = X_j$, the terms in the sum cancel pairwise by grouping each $\sigma$ with $\sigma\rho$ where $\rho = (i\; j)$, giving $f = 0$. Finally, $f(\varepsilon_1, \ldots, \varepsilon_n) = r$ since only $\sigma = \text{id}$ contributes.
