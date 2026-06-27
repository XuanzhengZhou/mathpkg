---
role: proof
locale: en
of_concept: gardner-theorem-on-stationary-kdv-solutions
source_book: gtm060
source_chapter: "Appendix 13"
source_section: "The Korteweg–de Vries equation"
---

Gardner's theorem establishes a deep connection between the stationary (equilibrium) solutions of higher KdV flows and finite-dimensional integrable Hamiltonian systems.

**Step 1: Higher KdV equations.** Each conserved integral $I_s = \int P_s(u, u', \ldots, u^{(s)}) dx$ generates a Hamiltonian flow:
$$\dot{u} = Q_s[u], \quad Q_s = \frac{d}{dx} \frac{\delta I_s}{\delta u},$$
where $Q_s$ is a polynomial in $u$ and its derivatives up to order $2s+1$. These are the "higher KdV equations."

**Step 2: Stationary points.** Stationary solutions of the $s$-th higher KdV flow satisfy $Q_s[u] = 0$, i.e.:
$$\frac{d}{dx} \frac{\delta I_s}{\delta u} = 0.$$
Integrating once gives $\frac{\delta I_s}{\delta u} = d$, a constant. This is the Euler-Lagrange equation for the functional $I_s - d I_{-1}$ (where $I_{-1} = \int u \, dx$).

**Step 3: Order and Hamiltonian structure.** The variational derivative $\frac{\delta I_s}{\delta u}$ involves derivatives of $u$ up to order $2s$. The equation $\frac{\delta I_s}{\delta u} = d$ is therefore an ODE of order $2s$. This ODE can be written as a Hamiltonian system in a $2s$-dimensional phase space with coordinates $(u, u', \ldots, u^{(2s-1)})$ and their conjugate momenta.

**Step 4: Complete integrability.** All the higher integrals $I_1, I_2, \ldots, I_s$ are in involution (their Poisson brackets vanish). When restricted to the level set of the stationary equation, they provide $s$ integrals in involution on a $2s$-dimensional symplectic manifold — exactly the condition for complete Liouville integrability.

**Step 5: Action-angle variables.** By the Liouville-Arnold theorem, one can introduce action-angle variables. The resulting solutions $u(x)$ are quasi-periodic functions (finite-gap potentials) depending on $3s+1$ parameters: $2s$ phase coordinates (actions and initial angles), $s$ constants $c_k$ from the higher integrals, and the constant $d$.

**Step 6: Lax representation of stationary flows.** The stationary equation can also be expressed via the Lax pair. The condition that $[A, L] = 0$ (stationary Lax equation) leads to the existence of a commuting ordinary differential operator $A$ of order $2s+1$, which implies that the Schrödinger operator $L$ has a finite number of gaps in its spectrum — hence the name "finite-gap" solutions.

Novikov's key contribution was to show that these finite-dimensional integrable systems actually produce all finite-gap periodic and quasi-periodic solutions of the KdV equation, providing an explicit integration procedure using Riemann theta functions on hyperelliptic Riemann surfaces.
