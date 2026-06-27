---
role: proof
locale: en
of_concept: kam-equilibrium-autonomous
source_book: gtm060
source_chapter: "Appendix 8"
source_section: "D.4"
---

The proof proceeds by first reducing the Hamiltonian to Birkhoff normal form (Appendix 7), which requires the absence of low-order resonances ($\sum |k_i| \leq 4$). After this reduction, the truncated Hamiltonian $H_0(\tau) = \sum \omega_k \tau_k + \frac{1}{2} \sum \omega_{kl} \tau_k \tau_l$ plays the role of the integrable part, with $\tau_k = (p_k^2 + q_k^2)/2$ as action variables.

The Hessian $\omega_{kl} = \partial^2 H_0 / \partial \tau_k \partial \tau_l$ takes the place of $\partial^2 H_0 / \partial I^2$ in the standard KAM setup. The nondegeneracy condition $\det |\omega_{kl}| \neq 0$ allows the Kolmogorov iteration to proceed: fix Diophantine frequencies, solve the linearized homological equation at each step using Fourier series on the torus, and apply a Newton iteration to achieve quadratic convergence.

The isoenergetic variant follows by restricting to a fixed energy surface $H = h$ and using the bordered Hessian condition. For $n = 2$, isoenergetic nondegeneracy is equivalent to the quadratic part of $H_0$ not being divisible by the linear part. The 2-dimensional invariant tori divide the 3-dimensional energy level manifolds, giving Liapunov stability.
