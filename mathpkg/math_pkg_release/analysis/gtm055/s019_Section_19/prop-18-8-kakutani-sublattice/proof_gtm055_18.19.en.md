---
role: proof
locale: en
of_concept: prop-18-8-kakutani-sublattice
source_book: gtm055
source_chapter: "18"
source_section: "19"
---

It suffices to verify that if $f \in \mathcal{A}$, then $|f| \in \mathcal{A}$ also. To establish this, consider the binomial series for $\sqrt{1+\lambda}$:
$$\sqrt{1+\lambda} = 1 + \sum_{n=1}^{\infty} \binom{1/2}{n} \lambda^n, \quad |\lambda| < 1.$$
Since all factors $(\frac{1}{2} - k)$ in the numerator of $\binom{1/2}{n}$ are negative except the first, one has $\binom{1/2}{n} = (-1)^{n+1} A_n$ for $n \geq 1$ where $A_n = |\binom{1/2}{n}|$. Defining $p_n(\lambda) = 1 - \sum_{k=1}^{n} A_k \lambda^k$, the sequence $\{p_n(\lambda)\}$ converges to $\sqrt{1-\lambda}$ for $|\lambda| < 1$. In particular, for real $t$ with $0 \leq t < 1$, one has $1 - \sum_{n=1}^{\infty} A_n t^n = \sqrt{1-t}$ and $p_n(t) \geq 0$.

Now set $q_n(t) = p_n(1-t)$, so $\{q_n(t)\}$ converges uniformly to $\sqrt{t}$ on $[0,1]$. If $a_n = q_n(0)$, then $a_n \to 0$, and $r_n(t) = q_n(t) - a_n$ are polynomials with zero constant term converging uniformly to $\sqrt{t}$. Given nonzero $f \in \mathcal{A}$, set $g(x) = (f(x)/\|f\|_\infty)^2$; then $g \in \mathcal{A}$ and $r_n \circ g \in \mathcal{A}$ since $r_n(0) = 0$. The sequence $\{r_n \circ g\}$ converges uniformly on $X$ to $\sqrt{g} = |f|/\|f\|_\infty$. Since $\mathcal{A}$ is closed, $|f| \in \mathcal{A}$. Thus $\mathcal{A}$ is a sublattice.
