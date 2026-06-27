---
role: proof
locale: en
of_concept: characteristic-oscillation-existence
source_book: gtm060
source_chapter: "5"
source_section: "Small Oscillations"
---

In the principal axis coordinates $Q$, the equations decouple: $\ddot{Q}_i = -\lambda_i Q_i$. If $\lambda_k = \omega^2 > 0$, the $k$-th equation has solution $Q_k = C_1 \cos \omega t + C_2 \sin \omega t$, while setting $Q_j = 0$ for all $j \neq k$ gives a valid solution. Transforming back to the original coordinates via $q = C^{-1} Q$, the $k$-th column of $C^{-1}$ is precisely an eigenvector $\xi$ of the generalized eigenvalue problem $B\xi = \lambda A\xi$, yielding the stated form $q(t) = (C_1 \cos \omega t + C_2 \sin \omega t)\xi$. $\square$
