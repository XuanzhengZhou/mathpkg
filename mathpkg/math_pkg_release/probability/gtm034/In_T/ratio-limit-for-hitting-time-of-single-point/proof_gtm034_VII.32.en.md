---
role: proof
locale: en
of_concept: ratio-limit-for-hitting-time-of-single-point
source_book: gtm034
source_chapter: "VII"
source_section: "32"
---

The theorem is proved in several stages. Let $T = \min\{n \mid 1 \leq n \leq \infty; x_n = 0\}$.

**Transient case (P1).** For every aperiodic transient random walk,
$$\lim_{n \to \infty} \frac{P_x[T > n]}{P_0[T > n]} = a(x),$$
where $a(x) = G(0,0) - G(x,0)$ is the potential kernel. Since $P_z[T > n] = P_z[n < T \leq \infty]$, we have
$$\lim_{n \to \infty} \frac{P_z[T > n]}{P_0[T > n]} = \frac{P_z[T = \infty]}{P_0[T = \infty]} = \frac{1 - \sum_{n=1}^{\infty} F_n(x,0)}{1 - F(0,0)}, \quad x \neq 0.$$
From the generating function identity (P1.2),
$$\sum_{n=1}^{\infty} t^n F_n(x,0) = \frac{\sum_{n=0}^{\infty} t^n P_n(x,0)}{\sum_{n=0}^{\infty} t^n P_n(0,0)}, \quad x \neq 0, \quad 0 \leq t < 1.$$
Letting $t \to 1$ and using P1.5, $F(x,0) = G(x,0)/G(0,0)$ for $x \neq 0$. Hence
$$\frac{1 - \sum_{n=1}^{\infty} F_n(x,0)}{1 - F(0,0)} = G(0,0) - G(x,0) = a(x), \quad x \neq 0.$$

**Recurrent case with finite variance (P2-P4).** For one-dimensional aperiodic recurrent random walk with $\sigma^2 < \infty$, the proof uses generating functions and stopping time decompositions to establish the Abel-sum identity $\lim_{t \to 1} (1 - E_0[t^{T_x}])/(1 - E_0[t^{T_0}]) = a(-x)$, then applies Karamata's theorem to obtain the sharp asymptotic $\sqrt{n}P_x[T > n] \sim a(x)\sigma\sqrt{2/\pi}$.

**Recurrent case with infinite variance (P5-P8).** For one-dimensional aperiodic recurrent random walk with $\sigma^2 = \infty$, the proof relies on Kesten's theorem (T2: $\lim F_{n+1}/F_n = 1$), which is established through Propositions P5-P8 using exponential lower bounds (P5), conditional displacement estimates (P6), ratio approximations (P7), and difference inequalities (P8). The fact that $P_x[T > n]/P_0[T > n] \to a(x)$ was already proved in Chapter III for the two-dimensional recurrent case, completing the proof for all dimensions.
