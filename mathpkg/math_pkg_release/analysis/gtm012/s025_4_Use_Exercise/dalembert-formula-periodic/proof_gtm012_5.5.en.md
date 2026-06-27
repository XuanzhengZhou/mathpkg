---
role: proof
locale: en
of_concept: dalembert-formula-periodic
source_book: gtm012
source_chapter: "5"
source_section: "5. The wave equation"
---

# Proof of d'Alembert Formula for the Wave Equation on Periodic Functions

Consider the special case of Theorem 5.1 where $G$ and $H$ are the distributions defined by functions $g$ and $h$ in $\mathcal{P}$, and suppose $h = 0$. Then $c_n = 0$ for all $n$, and the Fourier coefficients of $F_t$ are

$$a_n(t) = b_n \cos nt, \quad n \in \mathbb{Z},$$

where $(b_n)_{n=-\infty}^{\infty}$ are the Fourier coefficients of $g$. The Fourier series of $g$ converges (in the sense of distributions):

$$g(x) = \sum_{n=-\infty}^{\infty} b_n \exp(inx).$$

Since $\cos nt$ is bounded and $(b_n)$ is slowly growing, the Fourier series for $F_t$ also converges; then $F_t$ is the distribution defined by the function $u_t \in \mathcal{P}$, where

$$u(x,t) = u_t(x) = \sum_{n=-\infty}^{\infty} b_n \cos nt \cdot \exp(inx).$$

Using the identity $\cos nt = \frac{1}{2}(\exp(int) + \exp(-int))$, we obtain

$$u(x,t) = \frac{1}{2} \sum_{n=-\infty}^{\infty} b_n [\exp(int) + \exp(-int)] \exp(inx)$$
$$= \frac{1}{2} \sum_{n=-\infty}^{\infty} b_n \exp(in(x+t)) + \frac{1}{2} \sum_{n=-\infty}^{\infty} b_n \exp(in(x-t))$$
$$= \frac{1}{2} g(x+t) + \frac{1}{2} g(x-t).$$

This is the **d'Alembert formula** for the solution of the wave equation on periodic functions with zero initial velocity. It is easily verified that $u$ satisfies

$$\frac{\partial^2 u}{\partial t^2} = \frac{\partial^2 u}{\partial x^2}, \quad u(x,0) = g(x), \quad \frac{\partial u}{\partial t}(x,0) = 0.$$

The d'Alembert formula shows that the initial displacement $g$ splits into two waves traveling in opposite directions with speed $1$, each with half the original amplitude. $\square$
