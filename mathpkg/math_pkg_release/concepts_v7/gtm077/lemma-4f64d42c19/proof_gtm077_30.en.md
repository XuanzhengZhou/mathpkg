---
role: proof
locale: en
of_concept: lemma-4f64d42c19
source_book: gtm077
source_chapter: "30"
source_section: "30"
---

# Proof of For each number $\rho$ which belongs to the ring $R(\theta)$, we have

$$S\left(\frac{\rho}{F'(\thet

Obviously this assertion needs only to be proved for $\rho = 1, \theta, \ldots, \theta^{n-1}$, where it follows directly from the so-called Euler formulas

$$\sum_{i=1}^{n} \frac{\theta^{(i)k}}{F'(\theta^{(i)})} = \begin{cases} 0 & \text{for } k = 0, 1, 2, \ldots, n-2, \\ 1 & \text{for } k = n-1. \end{cases}$$

These formulas follow from the Lagrange interpolation formula

$$\sum_{i=1}^{n} \frac{\theta^{(i)k+1}}{F'(\theta^{(i)})} \frac{F(x)}{x - \theta^{(i)}} = \begin{cases} x^{k+1} & \text{for } k = 0, 1, \ldots, n-2, \\ x^n - F(x) & \text{for } k = n-1, \end{cases}$$

by setting $x = 0$ (or by expanding in powers of $1/x$ after division by $F(x)$).
