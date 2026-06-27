---
role: proof
locale: en
of_concept: skew-symmetry-of-angular-velocity-operator
source_book: gtm060
source_chapter: "6"
source_section: "26"
---

Since $B: K \to k$ is an orthogonal operator from one Euclidean space to another, its transpose is its inverse: $B^t = B^{-1}: k \to K$. By differentiating the relationship $BB^t = E$ with respect to $t$:

$$\dot{B}B^t + B\dot{B}^t = 0.$$

Substituting $B^t = B^{-1}$:

$$\dot{B}B^{-1} + B\dot{B}^t = 0.$$

Now, taking the transpose of $\dot{B}B^{-1}$, we have $(\dot{B}B^{-1})^t = (B^{-1})^t \dot{B}^t = (B^t)^{-1} \dot{B}^t = B \dot{B}^t$ (since $B^t = B^{-1}$, so $(B^t)^{-1} = B$). Thus:

$$\dot{B}B^{-1} + (\dot{B}B^{-1})^t = 0,$$

which means $A + A^t = 0$, i.e., $A$ is skew-symmetric.
