---
role: proof
locale: en
of_concept: monotone-increasing-sequence-lebesgue-integral
source_book: gtm055
source_chapter: "7"
source_section: "8"
---

If $f$ is integrable, then $0 \le f_n \le f$ implies $L(f_n) \le L(f)$, so $\{L(f_n)\}$ is bounded. Conversely, if bounded, then $\{L(f_n)\}$ is increasing and bounded, hence convergent. For $m > n$, $L(|f_m - f_n|) = L(f_m - f_n) = L(f_m) - L(f_n) \to 0$. Thus $\{f_n\}$ is Cauchy in the mean and converges pointwise to $f$. By $(L_2)$, $f \in \mathcal{L}$ and $L(f) = \lim_n L(f_n)$.
