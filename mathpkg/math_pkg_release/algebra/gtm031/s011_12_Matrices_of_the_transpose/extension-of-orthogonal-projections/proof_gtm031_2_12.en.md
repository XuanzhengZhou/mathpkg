---
role: proof
locale: en
of_concept: extension-of-orthogonal-projections
source_book: gtm031
source_chapter: "2"
source_section: "12"
---

Since $E_i E_j = 0$ for $i \neq j$ with $i, j \leq r$, we have $E^2 = (\sum E_i)^2 = \sum E_i^2 = \sum E_i = E$, so $E$ is idempotent. Hence $E_{r+1}^2 = (1-E)^2 = 1 - 2E + E^2 = 1 - 2E + E = 1 - E = E_{r+1}$, so $E_{r+1}$ is also idempotent.

For $j \leq r$, $E_j E = E_j \sum E_i = E_j^2 = E_j$ and similarly $E E_j = E_j$. Thus $E_j E_{r+1} = E_j(1-E) = E_j - E_j E = E_j - E_j = 0$, and symmetrically $E_{r+1} E_j = 0$. Finally, $\sum_{i=1}^{r+1} E_i = E + (1-E) = 1$. Therefore $\{E_1, \ldots, E_{r+1}\}$ is a supplementary orthogonal set.
