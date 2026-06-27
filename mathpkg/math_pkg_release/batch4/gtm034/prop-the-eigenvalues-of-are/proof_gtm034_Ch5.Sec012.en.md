---
role: proof
locale: en
of_concept: prop-the-eigenvalues-of-are
source_book: gtm034
source_chapter: "5"
source_section: "012"
---

Proof: Let $\Delta_N = \Delta_N(\lambda)$ denote the determinant of $Q_N - \lambda I_N$. Then it is a simple exercise in expanding a determinant in terms of its minors to obtain the difference equation

$$\Delta_n = -\lambda \Delta_{n-1} - \frac{1}{4} \Delta_{n-2}, \quad n = 2, 3, \ldots.$$

Direct computation of the two lowest-order determinants gives the initial conditions

$$\Delta_0 = -\lambda, \quad \Delta_1 = \lambda^2 - \frac{1}{4}.$$

Under these conditions the difference equation has a unique solution. By standard methods (see E1.2) one gets

$$\Delta_n(\lambda) = A r_1^n + Br_2^n$$

where $r_1$ and $r_2$ are the roots of the quadratic equation

$$x^2 + \lambda x + \frac{1}{4} = 0.$$

Making the substitution $\lambda = -\cos t$, one finds that

$$x^2 - x \cos t + \frac{1}{4} = \left(x - \frac{e^{it}}{2}\right)\left(x - \frac{e^{-it}}{2}\right) = 0,$$

so that $2x = e^{\pm it}$, and the general solution of the

Hence $\Delta_n(\lambda) = 0$ when $(n + 2)t$ is a multiple of $\pi$, but not zero, so that one tries $(n + 2)t = (k + 1)\pi$, $k = 0, 1, \ldots, n$. That gives the eigenvalues in (a) of P1 with the sign reversed. But the sign does not matter since

$$\cos \frac{k + 1}{N + 2}\pi = -\cos \frac{(N - k) + 1}{N + 2}\pi$$

for $k = 0, 1, \ldots, N$. As we have found $N + 1$ eigenvalues, (a) is proved since a matrix of size $N + 1$ can have no more.

The task of verifying that the functions in (b) are eigenfunctions is quite straightforward. Indeed it suffices to show that

$$Q_N v_k = \lambda_k v_k \text{ and } (v_k, v_k) = 1 \text{ for } 0 \leq k \leq N.$$

The fact that $(v_k, v_m) = 0$ when $k \neq m$ is a basic result in matrix theory; two eigenvectors belonging to distinct eigenvalues of a symmetric matrix are always orthogonal. To get $Q_N v_k = \lambda_k v_k$ one can use trigonometric identities, and finally the proof of P1 is completed by checking that

$$(v_k, v_k) = \frac{2}{N + 2} \sum_{z=0}^{N} \sin^2 \left[ \frac{k + 1}{N + 2} (x + 1)\pi \right]$$

$$= 1 - \frac{1}{N + 2} \sum_{z=-1}^{N+1} \cos \left[ 2 \frac{k + 1}{N + 2} (x + 1)\pi \right] = 1.$$

The spectral theorem for symmetric matrices (see [38], Ch. III) now yields, in one stroke, the solution of all our problems. In other words, every one of the functions in D1 above can be expressed in terms of the

nothing but the second difference operator, acting on functions defined on the interval $[0, N]$. Thus one is tempted to regard

(1) $$\frac{d^2}{dx^2} f(x) + \mu f(x) = 0, \quad 0 \leq x \leq 1$$

as the proper analogue of

$$(Q_N - I_N)v = -\mu v \text{ or } Q_Nv = \lambda v, \quad \lambda = 1 - \mu.$$

The correct boundary condition to impose in (1) is

(2) $$f(0) = f(1) = 0.$$

This follows from the observation that the matrix equation $Q_Nv = \lambda v$ is the same as the difference equation

$$\frac{1}{2}v(x + 1) + \frac{1}{2}v(x - 1) = \lambda v(x), \quad 0 \leq x \leq N,$$

with $v(-1) = v(N + 1) = 0$. The well-known theory of the boundary value problem consisting of (1) and (2) may be summarized by
