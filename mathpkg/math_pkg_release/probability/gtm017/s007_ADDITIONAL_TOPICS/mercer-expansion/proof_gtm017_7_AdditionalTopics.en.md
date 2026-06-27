---
role: proof
locale: en
of_concept: mercer-expansion
source_book: gtm017
source_chapter: "7"
source_section: "Additional Topics"
---

The integral operator $R$ with kernel $r$ is symmetric and completely continuous. Let $q(t,\tau) = \sum_i \varphi_i(t)\varphi_i(\tau)/\lambda_i$ and $s(t,\tau) = r(t,\tau) - q(t,\tau)$. The operator $S$ with kernel $s$ satisfies $S\varphi_i = 0$ for all $\varphi_i$. By the existence theorem, if $\|S\| > 0$, $S$ would have an eigenfunction orthogonal to all $\varphi_i$, which would also be an eigenfunction of $R$ -- a contradiction. Hence $\|S\| = 0$, so $Sf = 0$ for all continuous $f$. Taking $f(\tau) = r(t,\tau) - q(t,\tau)$ gives pointwise equality.

For uniform convergence: $\sum_{i=1}^n \varphi_i^2(t)/\lambda_i$ increases monotonically to $r(t,t)$. By Dini's theorem, this convergence is uniform. The Cauchy-Schwarz bound on the tail implies uniform convergence of the full series.
