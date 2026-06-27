---
role: proof
locale: en
of_concept: ratio-limit-theorem-for-hitting-time
source_book: gtm034
source_chapter: "VI"
source_section: "32"
---

The proof of T1 proceeds by cases.

**Case 1: Transient random walk.** Handled by P1. For every aperiodic transient random walk, $\lim_{n \to \infty} P_x[T > n]/P_0[T > n] = a(x)$ for $x \neq 0$. The proof uses $P_z[T > n] = P_z[n < T \leq \infty]$ and the renewal equation from P1.2:
$$\sum t^n F_n(x,0) = \frac{\sum t^n P_n(x,0)}{\sum t^n P_n(0,0)}.$$
Letting $t \to 1$ and using P1.5 gives $F(x,0) = G(x,0)/G(0,0)$, whence $\frac{1-F(x,0)}{1-F(0,0)} = G(0,0)-G(x,0) = a(x)$.

**Case 2: One-dimensional aperiodic recurrent with finite variance $\sigma^2 < \infty$.**
- P2 establishes the Abel-summation form of T1: $\lim_{t \to 1} \frac{1-E_0[t^{T_x}]}{1-E_0[t^{T_0}]} = a(-x)$ for $x \neq 0$, using generating functions, the strong Markov property, Abel's theorem, and $g_{(x)}(0,0) = a(x) + a(-x)$ from P29.4.
- P3 gives $\lim_{n \to \infty} \sqrt{n} P_0[T > n] = \sqrt{2/\pi}\,\sigma$ via Fourier analysis and Karamata's theorem.
- P4 combines them to yield $\lim_{n \to \infty} \sqrt{n} P_x[T > n] = \sigma\sqrt{2/\pi}\,a(x)$, which implies T1.

**Case 3: One-dimensional recurrent with $\sigma^2 = \infty$.** Requires T2 (Kesten's theorem): $\lim F_{n+1}/F_n = 1$. Its proof (P5-P8) uses: P5 gives an exponential lower bound $F_n \geq (1-\epsilon)^n/(n-2)$ via cyclic permutation combinatorics; P6 controls conditional expectations using the exponential bound for Bernoulli sums; P7 constructs approximating $q_n$ with $|q_n/F_n-1| \leq \epsilon_1$; P8 shows $|q_n - \tilde{q}_{n+1}| \leq \epsilon_1 q_n$. Together they give $F_{n+1} \geq (1-\epsilon_1)^2 F_n$, so $\liminf F_{n+1}/F_n \geq 1$. A symmetric argument gives $\limsup \leq 1$. T2 implies $R_n/R_{n+1} \to 1$, completing the proof of T1 by the method of T16.1.

**Case 4: Two-dimensional recurrent.** Proved in Chapter III (T16.1).

All cases together establish T1 for arbitrary aperiodic random walk of any dimension $d \geq 1$.
