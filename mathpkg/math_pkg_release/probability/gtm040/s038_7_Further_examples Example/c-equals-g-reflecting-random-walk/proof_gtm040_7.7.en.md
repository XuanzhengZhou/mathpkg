---
role: proof
locale: en
of_concept: c-equals-g-reflecting-random-walk
source_book: gtm040
source_chapter: "7"
source_section: "7. Further examples"
---

In general, the $C$ matrix is related to the $G$ matrix by

$$C_{ij} = \frac{\alpha_j}{\alpha_i} G_{ji},$$

where $\alpha$ is the invariant measure. For the reflecting random walk with $p = \frac{1}{2}$, the transition matrix satisfies $P = \hat{P}$ (the chain is reversible/self-dual with respect to the counting measure), and the invariant measure is $\alpha = 1^T$ (all entries equal to $1$, up to scaling). Therefore

$$C_{ij} = \frac{\alpha_j}{\alpha_i} G_{ji} = G_{ji}.$$

Since $G_{ij} = 2(j-i)$ for $j > i$ and $0$ otherwise, $G$ is not symmetric. However, the equality $C = G$ holds in terms of the existence criterion: the text notes that $\left[ N_{ii}^{(n)} \frac{\alpha_j}{\alpha_i} - N_{ij}^{(n)} \right] = \left[ N_{ii}^{(n)} - N_{ij}^{(n)} \right] = \left[ N_{jj}^{(n)} - N_{ij}^{(n)} \right]$, from which it follows that $G$ exists if and only if $C$ exists, and when they both exist, $C = G$ for this class of recurrent processes.
