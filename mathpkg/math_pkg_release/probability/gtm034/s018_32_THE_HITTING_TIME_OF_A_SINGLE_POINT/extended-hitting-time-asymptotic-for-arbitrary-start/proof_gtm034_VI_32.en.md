---
role: proof
locale: en
of_concept: extended-hitting-time-asymptotic-for-arbitrary-start
source_book: gtm034
source_chapter: "VI"
source_section: "32"
---

Combining the Abel limit identity from P2 with the asymptotic of $U(t)$ from the proof of P3 yields
$$\lim_{t \to 1} \sqrt{1-t} \sum_{n=0}^{\infty} t^n P_x[T > n] = \sigma \sqrt{2} \, a(x), \quad x \neq 0.$$

Since $P_x[T > n]$ is monotone nonincreasing in $n$, Karamata's theorem (P20.2) applies directly:
$$\lim_{n \to \infty} \sqrt{n} \, P_x[T > n] = \frac{\sigma\sqrt{2}\,a(x)}{\Gamma(3/2)} = \sigma \sqrt{\frac{2}{\pi}} \, a(x), \quad x \neq 0.$$
