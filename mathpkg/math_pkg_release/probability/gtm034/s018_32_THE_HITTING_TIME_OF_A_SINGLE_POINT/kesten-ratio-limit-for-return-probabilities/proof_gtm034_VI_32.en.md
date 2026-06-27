---
role: proof
locale: en
of_concept: kesten-ratio-limit-for-return-probabilities
source_book: gtm034
source_chapter: "VI"
source_section: "32"
---

The proof of T2 occupies propositions P5 through P8.

**P5 (Exponential lower bound):** For strongly aperiodic recurrent random walk in one dimension, for every $\epsilon > 0$, $F_n \geq (1-\epsilon)^n/(n-2)$ for sufficiently large $n$. The proof uses a combinatorial argument: choose $a_1 > 0$, $a_2 > 0$ with $P(0,a_1) > 0$, $P(0,-a_2) > 0$. Then $P[S_1 = a_1, S_{n-1}-S_1 = a_2-a_1, S_n = 0] \geq (1-\epsilon)^n$. Considering cyclic permutations of $X_2,\ldots,X_{n-1}$, at least one yields a polygonal line lying above its chord, and each permutation is equally likely, giving $F_n \geq (1-\epsilon)^n/(n-2)$.

**P6 (Conditional expectation estimate):** For every integer $m$ and $\epsilon > 0$ there exists $M = M(m,\epsilon)$ such that for each $A > 0$,
$$\lim_{n \to \infty} \frac{1}{n} \sum_{k=1}^{n-M} P[|S_k| \leq A \text{ or } S_{k+j} \neq S_k \text{ for } m \leq j \leq M \mid T = n] \leq \epsilon.$$
The proof uses truncation estimates, the exponential bound for Bernoulli sums (P5.3), and P5 to control exponential decay.

**P7 (Ratio approximation):** There exist $k$ and $M$ such that $|q_n/F_n - 1| \leq \epsilon_1$ for large $n$, where $q_n = P[T = n, |S_k| > A \text{ and } S_{k+j} = S_k \text{ for some } m \leq j \leq M]$. P6 guarantees suitable $k$; the estimate follows from T5.1.

**P8 (Difference estimate):** $|q_n - \tilde{q}_{n+1}| \leq \epsilon_1 q_n$, where $\tilde{q}_{n+1}$ is similar with $k+1$ instead of $k$. The proof decomposes according to the last time the walk revisits $S_k$, and uses asymptotics of $U_n = P_n(0,0)$.

**Completion:** By definition $\tilde{q}_{n+1} \leq F_{n+1}$, so $F_{n+1} \geq \tilde{q}_{n+1} \geq (1-\epsilon_1)q_n \geq (1-\epsilon_1)^2 F_n$, giving $\liminf F_{n+1}/F_n \geq 1$. A symmetric argument yields $\limsup \leq 1$, proving T2.
