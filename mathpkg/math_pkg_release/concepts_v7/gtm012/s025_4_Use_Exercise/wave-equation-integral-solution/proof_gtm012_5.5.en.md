---
role: proof
locale: en
of_concept: wave-equation-integral-solution
source_book: gtm012
source_chapter: "5"
source_section: "5. The wave equation"
---

# Proof of Integral Solution of the Wave Equation with Zero Initial Displacement

Consider the special case of Theorem 5.1 where $G$ and $H$ are the distributions defined by functions $g$ and $h$ in $\mathcal{P}$, and suppose $g = 0$. Then $b_n = 0$ for all $n$, and the Fourier coefficients of $F_t$ are

$$a_n(t) = n^{-1} c_n \sin nt, \quad n \neq 0,$$
$$a_0(t) = c_0 t,$$

where $(c_n)_{n=-\infty}^{\infty}$ are the Fourier coefficients of $h$. Using the identity $\sin nt = \frac{1}{2i}(\exp(int) - \exp(-int))$, we obtain for $n \neq 0$:

$$a_n(t) = \frac{c_n}{2in} (\exp(int) - \exp(-int)).$$

Then $F_t$ is the distribution defined by the function $u_t \in \mathcal{P}$, where

$$u(x,t) = u_t(x) = c_0 t + \sum_{n \neq 0} \frac{c_n}{2in} [\exp(int) - \exp(-int)] \exp(inx).$$

The antiderivative of $\exp(iny)$ with respect to $y$ is $(in)^{-1} \exp(iny)$ (for $n \neq 0$). Therefore, the above series can be recognized as the Fourier series of the function

$$u(x,t) = \frac{1}{2} \int_{x-t}^{x+t} h(y) \, dy.$$

To verify: note that $h(y) = \sum_{n=-\infty}^{\infty} c_n \exp(iny)$, and integrating term by term (which is justified in $\mathcal{P}'$) gives

$$\frac{1}{2} \int_{x-t}^{x+t} h(y) \, dy = \frac{1}{2} \sum_{n=-\infty}^{\infty} c_n \int_{x-t}^{x+t} \exp(iny) \, dy.$$

For $n \neq 0$:

$$\int_{x-t}^{x+t} \exp(iny) \, dy = \frac{1}{in} [\exp(in(x+t)) - \exp(in(x-t))] = \frac{1}{in} \exp(inx) [\exp(int) - \exp(-int)].$$

For $n = 0$:

$$\int_{x-t}^{x+t} 1 \, dy = 2t.$$

Thus

$$\frac{1}{2} \int_{x-t}^{x+t} h(y) \, dy = c_0 t + \sum_{n \neq 0} \frac{c_n}{2in} \exp(inx) [\exp(int) - \exp(-int)],$$

which matches the expression for $u(x,t)$ derived from the Fourier coefficients. The periodicity of $h$ ensures that $u$ is periodic in $x$, and the integration constant is determined to be zero by this periodicity requirement.

This function $u$ satisfies

$$\frac{\partial^2 u}{\partial t^2} = \frac{\partial^2 u}{\partial x^2}, \quad u(x,0) = 0, \quad \frac{\partial u}{\partial t}(x,0) = h(x).$$

The formula shows that the solution with zero initial displacement is obtained by integrating the initial velocity $h$ over the interval of dependence $[x-t, x+t]$, weighted by a factor of $1/2$. $\square$
