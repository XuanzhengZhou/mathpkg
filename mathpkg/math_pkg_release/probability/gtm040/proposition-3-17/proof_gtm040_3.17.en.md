---
role: proof
locale: en
of_concept: proposition-3-17
source_book: gtm040
source_chapter: "3"
source_section: "17"
---

**Proof:** We first note that $M[\|\hat{\mathbf{f}}_n\|] < \infty$ since $\|\hat{\mathbf{f}}_n\| \leq \sum_{j=0}^{n} |\mathbf{f}_j|$ and each $\mathbf{f}_j$ is integrable. Next, let $R$ be a cell in $\mathcal{R}_n$ with $\mu(R) \neq 0$. In $R$ we have

$$M[\hat{\mathbf{f}}_{n+1} \mid \mathcal{R}_n] = \frac{1}{\mu(R)} \int_R \hat{\mathbf{f}}_{n+1} d\mu$$

$$= \frac{1}{\mu(R)} \left[ \int_R \hat{\mathbf{f}}_{n+1} d\mu + \int_R \hat{\mathbf{f}}_{n+1} d\mu \right]$$

$$= \frac{1}{\mu(R)} \left[ \int_R \hat{\mathbf{f}}_{n} d\mu + \int_R \hat{\mathbf{

on only for values in $S$ (and possibly for no values). We stop $f_n$ the first time it takes on a value in $S$. That is, we let $t$ be the first time that $f_n$ is in $S$, and we introduce the stopped process $f_n$. If the values of $f_n$ are bounded from below or from above, then the "stopped process," is almost sure to stop. The proof proceeds as follows.

First, assume that $f_n \geq 0$. Then $(f_n, \mathcal{R}_n)$ is a non-negative martingale, by Proposition 3-17, which must converge a.e. to a finite value depending on $\omega$. Since by hypothesis these values must be in $S$ for a.e. $\omega$, the process $\{f_n\}$ almost surely stops. Next, if $\{f_n\}$ is bounded below, apply the result for non-negative martingales to $f_n$ plus a suitable constant. Finally, if $f_n \leq c$, apply the result for $\{f_n\}$ bounded below to $\{-f_n\}$.

These results are used in the next section in Examples 1 and 4. In Example 1 a fair game is stopped when it leaves a certain finite set, whereas in Example 4 it is stopped when a positive value is reached for the first time. By the above argument these random times are stopping times.
