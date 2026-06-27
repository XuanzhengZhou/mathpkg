---
role: proof
locale: en
of_concept: kakutanis-equilibrium-potential-theorem
source_book: gtm040
source_chapter: "7"
source_section: "3. Equivalence of Brownian motion and potential theory"
---

The result follows from the probabilistic interpretation of the Newtonian potential kernel. For Brownian motion $\{B_t\}_{t \geq 0}$ in $\mathbb{R}^3$ started at $x$, the expected occupation measure of a set $E$ up to time $T$ is given by

$$\mathbb{E}^x\left[\int_0^T \mathbf{1}_E(B_t)\,dt\right] = \int_E \int_0^T \frac{1}{(2\pi t)^{3/2}} e^{-|x-y|^2/2t}\,dt\,dy.$$

Letting $T \to \infty$, the inner integral converges to $\frac{1}{2\pi}|x-y|^{-1}$, yielding the Newtonian potential kernel. For an equilibrium set $E$ with equilibrium measure $\mu_E$, the equilibrium potential at $x$ is

$$u_E(x) = \int \frac{1}{2\pi|x-y|}\,d\mu_E(y).$$

The hitting probability $\mathbb{P}^x(\tau_E < \infty)$ for the hitting time $\tau_E = \inf\{t \geq 0 : B_t \in E\}$ can be expressed via the same kernel convolved with the equilibrium measure, establishing the equality.
