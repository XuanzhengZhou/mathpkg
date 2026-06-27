---
role: proof
locale: en
of_concept: asymptotic-of-survival-probability-finite-variance
source_book: gtm034
source_chapter: "VII"
source_section: "32"
---

Write $U(t) = \sum_{n=0}^{\infty} U_n t^n = \frac{1}{2\pi}\int_{-\pi}^{\pi} \frac{d\theta}{1 - t\phi(\theta)}$. Using $\phi(\theta) \sim 1 - \frac{1}{2}\sigma^2\theta^2$ near $\theta = 0$, $\sqrt{1-t}\,U(t) \sim \frac{1}{2\pi}\int_{-\delta}^{\delta} \frac{\sqrt{1-t}\,d\theta}{1 - t + \frac{1}{2}t\sigma^2\theta^2} \to \frac{1}{\sqrt{2}\sigma}$. By P1.2, $\sum R_n t^n = [(1-t)U(t)]^{-1}$, giving $\lim_{t \to 1} \sqrt{1-t} \sum R_n t^n = \sigma\sqrt{2}$. Since $R_n$ is monotone nonincreasing, Karamata's theorem (P20.2) yields $\lim \sqrt{n}R_n = \sigma\sqrt{2/\pi}$.
