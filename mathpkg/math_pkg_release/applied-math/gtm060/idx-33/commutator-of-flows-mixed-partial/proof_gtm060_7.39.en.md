---
role: proof
locale: en
of_concept: commutator-of-flows-mixed-partial
source_book: gtm060
source_chapter: "7"
source_section: "39"
---

By the definition of $L_A$,
$$\left. \frac{\partial}{\partial t} \right|_{t=0} \varphi(A^t B^s x) = \left( L_A \varphi \right)(B^s x).$$
If we denote the function $L_A \varphi$ by $\psi$, then by the definition of $L_B$,
$$\left. \frac{\partial}{\partial s} \right|_{s=0} \psi(B^s x) = \left( L_B \psi \right)(x) = \left( L_B L_A \varphi \right)(x).$$
Thus,
$$\left. \frac{\partial^2}{\partial s \partial t} \right|_{s=t=0} \varphi(A^t B^s x) = \left( L_B L_A \varphi \right)(x).$$
A symmetric argument for the term $\varphi(B^s A^t x)$ gives
$$\left. \frac{\partial^2}{\partial s \partial t} \right|_{s=t=0} \varphi(B^s A^t x) = \left( L_A L_B \varphi \right)(x).$$
Subtracting the two yields the desired result:
$$\left. \frac{\partial^2}{\partial s \partial t} \right|_{s=t=0} \left\{ \varphi(A^t B^s x) - \varphi(B^s A^t x) \right\} = \left( L_B L_A \varphi - L_A L_B \varphi \right)(x).$$
