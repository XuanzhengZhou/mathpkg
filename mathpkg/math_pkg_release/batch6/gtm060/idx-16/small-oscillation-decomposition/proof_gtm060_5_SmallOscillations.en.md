---
role: proof
locale: en
of_concept: small-oscillation-decomposition
source_book: gtm060
source_chapter: "5"
source_section: "Small Oscillations"
---

This follows directly from the theorem that the system has $n$ characteristic oscillations whose directions form an $A$-orthogonal basis. Any solution of the linear system can be expressed in the basis of eigenvectors $\xi_k$. To decompose a given motion, project the initial conditions $q(0)$ and $\dot{q}(0)$ onto each characteristic direction $\xi_i$ and solve the corresponding one-dimensional problem $\ddot{Q}_i = -\lambda_i Q_i$. The general solution is the linear combination:

$$q(t) = \operatorname{Re} \sum_{k=1}^{n} C_k e^{i\omega_k t} \xi_k,$$

where $C_k$ are determined by the projections of initial conditions. Importantly, in Lagrangian systems, unlike general linear differential equations, resonance terms of the form $t \sin \omega t$ do not arise even when eigenvalues are multiple, because the matrices $A$ and $B$ are symmetric and can be simultaneously diagonalized. $\square$
