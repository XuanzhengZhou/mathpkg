---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

The Riesz-Fischer theorem states that $\mathcal{L}^p$ is complete with respect to its seminorm: every Cauchy sequence converges to a limit in $\mathcal{L}^p$. The proof is classical: extract a subsequence with $\|f_{n_{k+1}} - f_{n_k}\|_p \leq 2^{-k}$, show that $\sum |f_{n_{k+1}} - f_{n_k}|$ converges pointwise almost everywhere via the monotone convergence theorem, define $f$ as the pointwise limit (or zero on the null set), and use Fatou's lemma to prove $\|f_n - f\|_p \to 0$. This theorem, together with the quotient construction, shows that $L^p$ is a Banach space.
