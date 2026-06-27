---
role: proof
locale: en
of_concept: asymptotic-of-hitting-time-distribution-finite-variance
source_book: gtm034
source_chapter: "VII"
source_section: "32"
---

From P2, $\lim_{t \to 1} (1 - E_0[t^{T_x}])/(1 - E_0[t^{T_0}]) = a(-x) = a(x)$. Combined with $\lim_{t \to 1}\sqrt{1-t}\sum R_n t^n = \sigma\sqrt{2}$ from P3, we obtain $\lim_{t \to 1}\sqrt{1-t}\sum t^n P_x[T > n] = \sigma\sqrt{2}\,a(x)$. Since $P_x[T > n]$ is monotone nonincreasing, Karamata's theorem applies: $\lim \sqrt{n}P_x[T > n] = \sigma\sqrt{2/\pi}\,a(x)$.
