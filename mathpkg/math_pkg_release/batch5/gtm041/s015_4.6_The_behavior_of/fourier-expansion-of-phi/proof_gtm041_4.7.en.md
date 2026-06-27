---
role: proof
locale: en
of_concept: fourier-expansion-of-phi
source_book: gtm041
source_chapter: "4"
source_section: "4.7"
---
We start from the Fourier expansion $\Delta(\tau) = (2\pi)^{12} \sum_{n=1}^{\infty} \tau(n)x^n$ where $x = e^{2\pi i\tau}$ and $\tau(1) = 1$. Then
$$\Delta(\tau) = (2\pi)^{12} x \left\{ 1 + \sum_{n=1}^{\infty} \tau(n+1)x^n \right\}.$$
Replacing $\tau$ by $q\tau$,
$$\Delta(q\tau) = (2\pi)^{12} x^q \left\{ 1 + \sum_{n=1}^{\infty} \tau(n+1)x^{nq} \right\}.$$
Therefore
$$\varphi(\tau) = \frac{\Delta(q\tau)}{\Delta(\tau)} = x^{q-1} \frac{1 + \sum_{n=1}^{\infty} \tau(n+1)x^{nq}}{1 + \sum_{n=1}^{\infty} \tau(n+1)x^n}.$$
Expanding the denominator as a power series in $x$ (the constant term is $1$) yields
$$\varphi(\tau) = x^{q-1} \left( 1 + \sum_{n=1}^{\infty} b_n x^n \right)$$
where the $b_n$ are integers, since the $\tau(n)$ are integers.
