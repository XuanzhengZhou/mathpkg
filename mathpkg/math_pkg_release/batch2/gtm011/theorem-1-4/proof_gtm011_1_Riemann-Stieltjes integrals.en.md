---
role: proof
locale: en
of_concept: theorem-1-4
source_book: gtm011
source_chapter: "Complex Integration"
source_section: "1. Riemann-Stieltjes integrals"
---

Proof. Since $f$ is continuous it is uniformly continuous; thus, we can find (inductively) positive numbers $\delta_1 > \delta_2 > \delta_3 > \ldots$ such that if $|s-t| < \delta_m$, $|f(s) - f(t)| < \frac{1}{m}$. For each $m \geq 1$ let $\mathcal{P}_m =$ the collection of all partitions $P$ of $[a, b]$ with $\|P\| < \delta_m$; so $\mathcal{P}_1 \supset \mathcal{P}_2 \supset \ldots$. Finally define $F_m$ to be the closure of the set:

1.5 $$\left\{ \sum_{k=1}^{n} f(\tau_k) [

Riemann-Stieltjes integrals

Fix $m \geq 1$ and let $P \in \mathcal{P}_m$; the first step will be to show that if $P \subset Q$ (and hence $Q \in \mathcal{P}_m$) then $|S(P) - S(Q)| < \frac{1}{m} V(\gamma)$. We only give the proof for the case where $Q$ is obtained by adding one extra partition point to $P$. Let $1 \leq p \leq m$ and let $t_{p-1} < t^* < t_p$; suppose that $P \cup \{t^*\} = Q$. If $t_{p-1} \leq \sigma \leq t^*$, $t^* \leq \sigma' \leq t_p$, and

$$S(Q) = \sum_{k \neq p} f(\sigma_k) \left[ \gamma(t_k) - \gamma(t_{k-1}) \right] + f(\sigma) \left[ \gamma(t^*) - \gamma(t_{p-1}) \right] + f(\sigma') \left[ \gamma(t_p) - \gamma(t^*) \right],$$

then, using the fact that $|f(\tau) - f(\sigma)| < \frac{1}{m}$ for $|\tau - \sigma| < \delta_m$,

$$|S(P) - S(Q)| = \left| \sum_{k \neq p} \left[ f(\tau_k) - f(\sigma_k) \right] \left[ \gamma(t_k) - \gamma(t_{k-1}) \right] + f(\tau_p) \left[ \gamma(t_p) - \gamma(t_{p-1}) \right] \right|$$

$$- f(\sigma) \left[ \gamma(t^*) - \gamma(t_{p-1}) \right] - f(\sigma') \left[ \gamma(t_p) - \gamma(t^*) \right]$$

$$\leq \frac{1}{m} \sum_{k \neq p} \left| \gamma(t_k) - \gamma(t_{k-1}) \right| + \left| [f(\tau_p) - f(\sigma)] \left[

The proof is left as an exercise.

As was mentioned before, we will mainly be concerned with those $\gamma$ which are piecewise smooth. The following theorem says that in this case we can find $ffd\gamma$ by the methods of integration learned in calculus.
