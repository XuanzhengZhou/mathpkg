---
role: proof
locale: en
of_concept: existence-of-unbounded-potential
source_book: gtm040
source_chapter: "VIII"
source_section: "7. An unbounded potential"
---

**Construction of the chain.** The chain $P$ is a modification of sums of independent random variables on the line with $p_1 = \frac{1}{3}$ and $p_{-1} = \frac{2}{3}$. Define
\[
\begin{cases}
P_{i,i-1} = \frac{2}{3}, \\[2pt]
P_{i,i+1} = \frac{1}{3}
\end{cases}
\quad \text{for } i \leq 0,
\]
and
\[
\begin{cases}
P_{ii} = 1 - \frac{1}{i}, \\[2pt]
P_{i,i-1} = \frac{2}{3i}, \\[2pt]
P_{i,i+1} = \frac{1}{3i}
\end{cases}
\quad \text{for } i > 0.
\]

**Computation of the potential matrix.** If the process is watched only when it changes states, it becomes the $p_1 = \frac{1}{3}, p_{-1} = \frac{2}{3}$ random walk, so the hitting probabilities $H$ can be computed from the latter chain. One obtains
\[
N_{ij} = \begin{cases}
3 & \text{if } j \leq 0,\; i \geq j,\\[4pt]
3\left(\frac{1}{2}\right)^{j-i} & \text{if } j \leq 0,\; i < j,\\[4pt]
3j & \text{if } j > 0,\; i \geq j,\\[4pt]
3j\left(\frac{1}{2}\right)^{j-i} & \text{if } j > 0,\; i < j.
\end{cases}
\]

**Equilibrium set.** Let $E = \{1, 2, 3, \ldots\}$. Since the process moves toward $-\infty$ with probability one, it can be in $E$ only finitely often a.e. Moreover, $e_i^E = 0$ unless $i = 1$, so that $\alpha e^E < \infty$ for any choice of $\alpha$. Thus $E$ is an equilibrium set.

**Choice of $\alpha$.** Take $\alpha$ to be the zeroth row of $N$. Then
\[
\alpha_j = N_{0j} = \begin{cases}
3 & \text{if } j \leq 0,\\[4pt]
3j\left(\frac{1}{2}\right)^j & \text{if } j > 0.
\end{cases}
\]

**The dual chain.** Computing $\hat{P}$ (the dual chain with respect to $\alpha$), one finds
\[
\hat{P}_{ij} = P_{ij} \quad \text{for } i > 0,
\]
\[
\hat{P}_{i,i+1} = \frac{2}{3},\quad \hat{P}_{i,i-1} = \frac{1}{3} \quad \text{for } i < 0,
\]
and
\[
\hat{P}_{01} = \hat{P}_{0,-1} = \frac{1}{3}.
\]
With probability one the $\hat{P}$ process reaches $0$ from all states, and from there it can disappear. Hence the extended chain for $\hat{P}$ is absorbing, and the $\hat{P}$ process is in any set only finitely often a.e. As before, $\alpha \hat{e}^E < \infty$, so $E$ is also an equilibrium set for $\hat{P}$ (i.e., a dual equilibrium set).

**Explicit formula for the potential.** Summing the relevant expressions yields the potential
\[
g_i = \begin{cases}
6\left(\frac{1}{2}\right)^{|i|} & \text{for } i \leq 0,\\[6pt]
\frac{3}{2}\left(i^2 + 3i + 4\right) & \text{for } i > 0.
\end{cases}
\]
Thus $\displaystyle\lim_{i \to +\infty} g_i = +\infty$, and $g$ is unbounded.

**Consistency.** Note that $P^n g$ for large $n$ is a weighted sum of $g$ values along paths that the process is likely to take. The fact that $\lim_{i \to +\infty} g_i = +\infty$ does not contradict $P^n g \to 0$ since the process moves toward $+\infty$ with probability zero. In the direction that the process does move, namely $-\infty$, we have $\lim_{i \to -\infty} g_i = 0$.
