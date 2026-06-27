---
role: proof
locale: en
of_concept: lorentz-eigenvalue-positive
source_book: gtm023
source_chapter: "9"
source_section: "4"
---

Let $\varphi l = \lambda l$ with $(l, l) = 0$. Select a space-like unit vector $y$ such that $(l, y) = 1$ and consider the vector $z(\tau) = l + \tau y$ for a real parameter $\tau$. Then
$$(z, z) = (l, l) + 2\tau(l, y) + \tau^2(y, y) = 2\tau + \tau^2.$$
Thus $z$ is time-like for $-2 < \tau < 0$, and in this range $(z, z) < 0$.

Since $\varphi$ preserves the fore-cone and past-cone (it is orthochroneous), for any time-like $z$ in $-2 < \tau < 0$ we have
$$(z, \varphi z) < 0.$$

Now compute
\begin{align*}
(z, \varphi z) &= (l + \tau y, \lambda l + \tau \varphi y) \\
&= \lambda(l, l) + \tau(l, \varphi y) + \tau\lambda(y, l) + \tau^2(y, \varphi y) \\
&= \tau(\lambda(y, l) + (l, \varphi y)) + \tau^2(y, \varphi y).
\end{align*}
Since $\varphi$ preserves the inner product, $(l, \varphi y) = (\varphi^{-1}l, y) = (\lambda^{-1}l, y) = \lambda^{-1}(l, y) = \lambda^{-1}$. Also $\lambda(y, l) = \lambda$. Thus
$$(z, \varphi z) = \tau\left(\lambda + \frac{1}{\lambda}\right) + \tau^2(y, \varphi y).$$

For $-2 < \tau < 0$ this expression is negative. As $\tau \to 0^-$, the $\tau^2$ term is negligible and the sign is determined by $\tau(\lambda + 1/\lambda)$. Since $\tau < 0$, we must have $\lambda + 1/\lambda > 0$, which holds precisely when $\lambda > 0$. Therefore $\lambda$ is positive.
