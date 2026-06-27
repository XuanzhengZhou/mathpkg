---
role: proof
locale: en
of_concept: max-partial-sum-limit-distribution
source_book: gtm034
source_chapter: "V"
source_section: "23"
---

The crucial observation is that the two events coincide:
$$\left\{ \max_{1 \leq k \leq n} |\mathbf{S}_k| \leq \sigma x \sqrt{n} \right\} = \left\{ \mathbf{T}_{[\sigma x \sqrt{n}]} > n \right\}.$$

Therefore, letting $G_n(x) = \mathbf{P}[(\sigma^2 n)^{-1/2} \max_{1 \leq k \leq n} |\mathbf{S}_k| \leq x]$,
$$G_n(x) = \mathbf{P}\left[ \mathbf{T}_{[\sigma x \sqrt{n}]} > n \right].$$

Fix $x > 0$ and let $m = m(n) = [\sigma x \sqrt{n}]$. Then
$$\frac{m^2}{\sigma^2 x^2} \leq n < \frac{(m+1)^2}{\sigma^2 x^2}.$$

Using the monotonicity of distribution functions,
$$G_n(x) \leq \mathbf{P}\left[ \mathbf{T}_m > \frac{m^2}{\sigma^2 x^2} \right] \to 1 - F\left(\frac{1}{x^2}\right)$$
by Theorem T2. Similarly,
$$G_n(x) \geq \mathbf{P}\left[ \mathbf{T}_m > \frac{m^2}{\sigma^2} \frac{1}{x^2} \left(1 + \frac{1}{m}\right)^2 \right] \geq \mathbf{P}\left[ \mathbf{T}_m > \frac{m^2}{\sigma^2} \frac{c}{x^2} \right] \to 1 - F\left(\frac{c}{x^2}\right)$$
for any $c > 1$. Since $F$ is continuous, taking $c \to 1^+$ yields $G_n(x) \to 1 - F(1/x^2)$.
