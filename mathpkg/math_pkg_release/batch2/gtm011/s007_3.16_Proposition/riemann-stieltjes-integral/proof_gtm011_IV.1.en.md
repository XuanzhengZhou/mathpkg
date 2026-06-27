---
role: proof
locale: en
of_concept: riemann-stieltjes-integral
source_book: gtm011
source_chapter: "IV"
source_section: "1"
---

Since $f$ is continuous on the compact interval $[a,b]$, it is uniformly continuous. We can inductively choose positive numbers $\delta_1 > \delta_2 > \delta_3 > \cdots$ such that if $|s - t| < \delta_m$, then $|f(s) - f(t)| < 1/m$. For each $m \geq 1$, let $\mathcal{P}_m$ be the collection of all partitions $P$ of $[a,b]$ with $\|P\| < \delta_m$; thus $\mathcal{P}_1 \supset \mathcal{P}_2 \supset \cdots$. Define $F_m$ to be the closure of the set of all Riemann-Stieltjes sums

$$\left\{ \sum_{k=1}^{n} f(\tau_k) [\gamma(t_k) - \gamma(t_{k-1})] \right\}$$

taken over partitions $P \in \mathcal{P}_m$ and arbitrary intermediate points $\tau_k$.

Fix $m \geq 1$ and let $P \in \mathcal{P}_m$. The key step is to show that if $P \subset Q$ (hence $Q \in \mathcal{P}_m$), then $|S(P) - S(Q)| < \frac{1}{m} V(\gamma)$. Consider the case where $Q$ is obtained by adding one extra partition point $t^*$ with $t_{p-1} < t^* < t_p$. Let $t_{p-1} \leq \sigma \leq t^*$, $t^* \leq \sigma' \leq t_p$. Then

$$|S(P) - S(Q)| \leq \frac{1}{m} \sum_{k \neq p} |\gamma(t_k) - \gamma(t_{k-1})| + |[f(\tau_p) - f(\sigma)][\gamma(t^*) - \gamma(t_{p-1})] + [f(\tau_p) - f(\sigma')][\gamma(t_p) - \gamma(t^*)]|.$$

Since $|\tau_p - \sigma| < \delta_m$ and $|\tau_p - \sigma'| < \delta_m$, we have $|f(\tau_p) - f(\sigma)| < 1/m$ and $|f(\tau_p) - f(\sigma')| < 1/m$. Therefore

$$|S(P) - S(Q)| \leq \frac{1}{m} V(\gamma).$$

By induction, this holds whenever $P \subset Q$ with any number of additional points.

Now, for any two partitions $P, Q \in \mathcal{P}_m$, let $R = P \cup Q$. Then $R \in \mathcal{P}_m$, $P \subset R$, and $Q \subset R$, so

$$|S(P) - S(Q)| \leq |S(P) - S(R)| + |S(R) - S(Q)| \leq \frac{2}{m} V(\gamma).$$

This shows that the diameter of the set of all Riemann-Stieltjes sums for partitions in $\mathcal{P}_m$ is at most $\frac{2}{m} V(\gamma)$. Consequently, the sets $F_m$ form a nested sequence of nonempty closed sets whose diameters tend to zero. By the completeness of $\mathbb{C}$, $\bigcap_{m=1}^{\infty} F_m$ consists of exactly one complex number $I$. This $I$ satisfies the required property as the limit of Riemann-Stieltjes sums.
