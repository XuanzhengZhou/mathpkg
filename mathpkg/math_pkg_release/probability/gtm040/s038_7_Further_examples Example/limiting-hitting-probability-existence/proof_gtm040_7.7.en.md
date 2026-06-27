---
role: proof
locale: en
of_concept: limiting-hitting-probability-existence
source_book: gtm040
source_chapter: "7"
source_section: "7. Further examples"
---

We prove that $iH_{-\infty,j}$ exists; the proof for $iH_{+\infty,j}$ is similar. Since $i\lambda_j = 0\lambda_{j-i}$ and $0\lambda_{j-j} = j\lambda_0 = 1 - 0\lambda_j$, it suffices to prove $0H_{-\infty,j}$ exists for $j > 0$.

Let $v$ be the largest $k$-value and $E = \{0, \ldots, v\}$. Then

$$0H_{-k,j} = \sum_{s \in E} B_{-k,s}^E \, 0H_{sj},$$

since neither $0$ nor $j$ can be reached from the negative side except through $E$ (the chain must first enter the finite set $E$ before hitting either $0$ or $j$).

If we can show that $B_{-k,s}^E = \lim_{k \to -\infty} B_{k,s}^E$ exists, then since $E$ is finite,

$$0H_{-\infty,j} = \sum_{s \in E} B_{-k,s}^E \, 0H_{sj}.$$

Now form the ladder process $P^+$. By construction, $p_j^+ = 0$ unless $0 < j \leq v$. By the special choice of $E$, $B_{-k,s}^E = (B^+)_{-k,s}^E$.

Let $f_j = p_j^+$ (the ladder height distribution) and $u_n = H_{-n,0}^+$ (the probability of hitting $0$ from $-n$ in the ladder process). Then $u_0 = 1$ and the renewal equation holds:

$$u_n = \sum_{k=1}^{n} p_k^+ H_{-(n-k),0}^+ = \sum_{k=0}^{n-1} p_{n-k}^+ H_{-k,0}^+ = \sum_{k=0}^{n-1} f_{n-k} u_k.$$

This is exactly the renewal equation. By the Renewal Theorem (Theorem 1-67 from the text), we have

$$\lim_{n \to \infty} H_{-n,0}^+ = \frac{1}{\mu^+},$$

where $\mu^+ = \sum j p_j^+$ is the mean ladder height.

The existence of the limit for $H_{-n,0}^+$ implies, through the finite sum decomposition over $E$, that $B_{-k,s}^E$ converges as $k \to \infty$, which in turn gives the convergence of $0H_{-k,j}$ to $0H_{-\infty,j}$.

Since $i\lambda_j = \lim_n \sum_k P_{0k}^{(n)} \, iH_{kj}$, the existence of the limits $iH_{+\infty,j}$ and $iH_{-\infty,j}$ allows one to split the sum into three parts (near $0$, far left, and far right) and take limits, establishing that $i\lambda_j$ exists for all $i, j$. Hence the process is normal.
