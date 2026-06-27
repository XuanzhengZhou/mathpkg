---
role: proof
locale: en
of_concept: one-parameter-group-from-differential-equation
source_book: gtm023
source_chapter: "8"
source_section: "8.30"
---

Fix $\tau$ and set $\varphi_1(t) = \varphi(t + \tau)$ and $\varphi_2(t) = \varphi(t) \circ \varphi(\tau)$. Both satisfy the same differential equation: $\dot{\varphi}_1(t) = \dot{\varphi}(t + \tau) = \psi \circ \varphi(t + \tau) = \psi \circ \varphi_1(t)$, and $\dot{\varphi}_2(t) = \dot{\varphi}(t) \circ \varphi(\tau) = \psi \circ \varphi(t) \circ \varphi(\tau) = \psi \circ \varphi_2(t)$. They also satisfy the same initial condition: $\varphi_1(0) = \varphi(\tau) = \varphi_2(0)$. By uniqueness of solutions, $\varphi_1(t) = \varphi_2(t)$ for all $t$, i.e. $\varphi(t + \tau) = \varphi(t) \circ \varphi(\tau)$.
