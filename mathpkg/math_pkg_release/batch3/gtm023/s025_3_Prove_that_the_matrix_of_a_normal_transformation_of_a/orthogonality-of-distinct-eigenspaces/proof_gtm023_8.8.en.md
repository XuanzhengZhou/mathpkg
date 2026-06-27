---
role: proof
locale: en
of_concept: orthogonality-of-distinct-eigenspaces
source_book: gtm023
source_chapter: "VIII"
source_section: "8.8"
---

Assume $\varphi e = \lambda e$ and $\varphi e' = \lambda' e'$. Then
$$(e', \varphi e) = \lambda(e, e') \quad \text{and} \quad (e, \varphi e') = \lambda'(e, e').$$
Since $\varphi$ is selfadjoint, $(e', \varphi e) = (\varphi e', e) = (e, \varphi e')$. Subtracting the two equations:
$$(\lambda' - \lambda)(e, e') = 0.$$
If $\lambda' \neq \lambda$, then $(e, e') = 0$. Hence any two eigenvectors belonging to different eigenvalues are orthogonal, and consequently the eigenspaces $E(\lambda)$ and $E(\lambda')$ are orthogonal.
