---
role: proof
locale: en
of_concept: theorem-1-15-analyticity-of-modular-functions
source_book: gtm041
source_chapter: "1"
source_section: "1.12"
---

Since $\Delta(\tau) \neq 0$ in $H$ it suffices to prove that $g_2$ and $g_3$ are analytic in $H$. Both $g_2$ and $g_3$ are given by double series of the form

$$\sum_{m, n = -\infty}^{+\infty} \frac{1}{(m + n\tau)^\alpha}$$

with $\alpha > 2$. Let $\tau = x + iy$, where $y > 0$. We prove that if $\alpha > 2$ this series converges absolutely for any fixed $\tau$ in $H$ and uniformly in every strip $S$ of the form

$$S = \{x + iy : |x| \leq A, y \geq \delta > 0\}.$$

To do this we prove that there is a constant $M > 0$, depending only on $A$ and $\delta$, such that

$$\frac{(m + n\tau)^2}{1 + n^2} \geq K$$

for some $K > 0$, with

$$K = \frac{\delta^2}{1 + (A + \delta)^2}$$

if $|x| \leq A$ and $y \geq \delta$.

If $|n| \leq A + \delta$ the inequality holds trivially since $(n + x)^2 \geq 0$ and $y^2 \geq \delta^2$. If $|n| > A + \delta$ then $|x/n| < |x|/(A + \delta) \leq A/(A + \delta) < 1$ so

$$\left| 1 + \frac{x}{n} \right| \geq 1 - \left| \frac{x}{n} \right| > 1 - \frac{A}{A + \delta} = \frac{\delta}{A + \delta}$$

hence

$$|n + x| \geq \frac{n\delta}{A + \delta}$$

and

$$\frac{(n + x)^2 + y^2}{1 + n^2} > \frac{\delta^2}{(A + \delta)^2} \frac{n^2}{1 + n^2}.$$

Now $n^2/(1 + n^2)$ is an increasing function of $n^2$ so

$$\frac{n^2}{1 + n^2} \geq \frac{(A + \delta)^2}{1 + (A + \delta)^2}$$

when $n^2 > (A + \delta)^2$. Using this we obtain the bound with the specified $K$. Therefore the double series converges uniformly on $S$, and since each term is analytic in $H$, the sum $g_2$ and $g_3$ are analytic in $H$. It follows that $\Delta = g_2^3 - 27g_3^2$ and $J = g_2^3/\Delta$ are also analytic in $H$. $\square$
