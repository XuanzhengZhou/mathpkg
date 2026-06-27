---
role: proof
locale: en
of_concept: recurrence-criterion-for-random-walk
source_book: gtm040
source_chapter: "5"
source_section: "7"
---

**Proof of Proposition 5-22.** We may assume that both positive and negative $k$-values exist; otherwise the chain is clearly transient. Consider the generating function
$$f(s) = \sum_k p_k s^k.$$

Note that $f'(1) = (\sum k p_k s^{k-1})|_{s=1} = \sum k p_k = m$, and $f(s) = 1$ has a double root at $s = 1$ if and only if $m = 0$.

**Case $m \neq 0$ (transience).** In this case $f(s) = 1$ has another positive root $r \neq 1$. The process $\{r^{x_n}\}$ is a martingale (since $E[r^{x_{n+1}} \mid x_n] = r^{x_n} \sum p_k r^k = r^{x_n} f(r) = r^{x_n}$). As a nonnegative martingale, $\{r^{x_n}\}$ converges almost everywhere. Since $r \neq 1$ and the process takes integer values, the only possible limit is the zero function. Thus, according as $r < 1$ or $r > 1$, we have
$$\lim_{n \to \infty} x_n = +\infty \quad\text{or}\quad \lim_{n \to \infty} x_n = -\infty.$$
Hence, the process returns to each state only finitely often with probability one. But if the chain were recurrent, each state would be reached infinitely often with probability one. Therefore, if $m \neq 0$, the chain is transient.

**Case $m = 0$ (recurrence).** Let $-u$ be the smallest $k$-value and let $v$ be the largest $k$-value (both are finite by assumption). Let
$$E = \{-u, \ldots, -2, -1\}, \qquad E' = \{j, j+1, \ldots, j+v-1\}$$
for some fixed $j > 0$. Start the process in state $i$ with $0 \leq i < j$, and let $t$ be the time to reach the set $E \cup E'$. The chain stopped at time $t$ is absorbing by Proposition 5-14, and $t$ is therefore a stopping time. Since $\{x_n\}$ is a bounded martingale before time $t$ (the process cannot leave the interval $[-u, j+v-1]$ before reaching $E \cup E'$), Corollary 3-16 (the Optional Stopping Theorem) applies. Therefore $M[x_0] = M[x_t]$, and for $0 \leq i < j$ we have
$$i = M[x_0] = M[x_t] = \sum_{k \in E} B_{ik}^E \, k + \sum_{k \in E'} B_{ik}'^E \, k$$
$$\geq -u \sum_{k \in E} B_{ik}^E + j \sum_{k \in E'} B_{ik}'^E$$
$$= -u \, h_i^E + j \, h_i'^E,$$
where $h_i^E = \Pr_i[\text{reach } E \text{ before } E']$ and $h_i'^E = \Pr_i[\text{reach } E' \text{ before } E] = 1 - h_i^E$.

This inequality rearranges to
$$h_i^E \leq \frac{j - i}{j + u}.$$
Since $j$ is arbitrary, we may let $j \to \infty$, obtaining $h_i^E = 0$ for all $i \geq 0$. Thus, starting from any nonnegative state, the process must eventually reach the negative set $E$ with probability one. By symmetry, starting from any negative state the process must reach the positive states with probability one. Consequently, every state is visited infinitely often with probability one, and the chain is recurrent.

The necessity of $m = 0$ for recurrence also follows immediately from the Strong Law of Large Numbers (Theorem 3-19): if $m \neq 0$, then $x_n/n \to m$ almost surely, so $|x_n| \to \infty$ and the chain cannot be recurrent. The additional assumption of finitely many $k$-values translates exactly into the condition used in that proof.

**Remark.** The proposition generalizes to the case of infinitely many $k$-values provided the mean $m$ exists (i.e., the positive and negative parts of the sum are not both infinite) and the $k$-values still have greatest common divisor one. The same condition $m = 0$ is necessary and sufficient for recurrence.
