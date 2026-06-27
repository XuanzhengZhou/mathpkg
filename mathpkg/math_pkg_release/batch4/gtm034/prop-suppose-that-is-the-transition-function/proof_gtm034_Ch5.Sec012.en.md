---
role: proof
locale: en
of_concept: prop-suppose-that-is-the-transition-function
source_book: gtm034
source_chapter: "5"
source_section: "012"
---

Proof: The existence of a unique system of polynomials $p_n(z)$ satisfying (b) and (c) follows from the well known Gram Schmidt orthogonalization process. The sequence $f_n(e^{i\theta}) = e^{i\nu\theta}, \quad n = 0, \pm 1, \pm 2, \ldots,$ forms a complete orthonormal set for the Hilbert space $L_2(-\pi,\pi)$ of functions square integrable on the interval $[-\pi,\pi].$ Here orthogonality is defined in the sense that

$$\frac{1}{2\pi} \int_{-n}^{n} f_n(e^{i\theta}) \overline{f_m(e^{i\theta})} d\theta = \delta(m,n), \quad m,n = 0, \pm 1, \ldots.$$

We are interested, however, in constructing a system of polynomials $p_n(z)$ which are orthogonal with respect to the inner product

$$(f,g) = \frac{1}{2\pi} \int_{-n}^{n} f(e^{i\theta}) \overline{g(e^{i\theta})} [1 - \phi(\theta)] d\theta.$$

It is easy to verify that the explicit formulas

$$p_0(z) = [1 - P(0,0)]^{-1/2},$$

(1) $p_n(z) = (D_nD_{n-1})^{-1/2}$

where $D_n = \left| \begin{array}{cccc} (f_0,f_0) & (f_1,f_0) & \cdots & (f_n,f_0) \\ (f_0,f_1) & (f_1,f_1) & \cdots

and such that (b) and (c) are satisfied. Nor is it difficult to prove uniqueness. The above representation of $p_n(z)$ as a ratio of determinants is of course quite general—it holds when $1 - \phi(\theta)$ is replaced by any non-negative weight function $w(\theta)$ whose integral over $[-\pi, \pi]$ is positive. In our case one has

$$\left(f_n, f_m\right) = \frac{1}{2\pi} \int_{-\pi}^{\pi} e^{in\theta} e^{-im\theta} \left[1 - \phi(\theta)\right] d\theta = \delta(m, n) - P(n, m),$$

in other words, the matrix $(f_n, f_m)$, $0 \leq m, n \leq N$, is exactly the $(N + 1) \times (N + 1)$ matrix which we called $I_N - Q_N$ in definition D21.1.

The proof of (d) is based on the observation that $g_N(j,k)$ is the $(j,k)^{\text{th}}$ element of the inverse of the matrix $I_N - Q_N$. This was already pointed out in connection with P21.2. It is equally true here, for although we do not know the eigenvalues of $Q_N$ it is easy to see that they are between 0 and 1. Hence

$$g_N(j,k) = \sum_{n=0}^{\infty} Q_N^n(j,k) = \left(I_N - Q_N\right)^{-1}(j,k).$$

Because of the symmetry of the random walk it is clear that

$$g_N(k,j) = g_N(N - k, N - j).$$

Therefore it suffices to prove the first identity in (d) which, in terms of generating functions, becomes

$$\sum_{k=0}^{N} \sum_{j=0}^{N} g_N(k,j) z^j w^k = \sum_{n=0}^{N} p_n(z) p_n(w)$$

for arbitrary complex $z$ and $w$. To verify (3) one first derives, using (1) and (2), that

$$\sum_{n=0}^{N} p_n(z) \overline{p_n(w

for the reproducing kernel. Inspection of the determinant in (4) shows that the coefficient of $\bar{w}^k z^j$ is simply

$$- (1/D_N) M_{k,j} (-1)^{k+j}, \quad 0 \leq k, j \leq N,$$

where $M_{k,j}$ is the minor of the $(k,j)^{\text{th}}$ element of the matrix $(I_N - Q_N)^{-1}$. Consequently we have

$$\sum_{k=0}^{N} \sum_{j=0}^{N} g_N(k,j) z^j \bar{w}^k = \sum_{n=0}^{N} p_n(z) \overline{p_n(w)}.$$

From (5) we should be able to conclude (3), and hence (d), if we knew that all coefficients $p_{nk}$ of $p_n(z)$ are real. That comes from (5) which gives

$$g_N(N,k) = g_N(k,N) = p_{N,N} \overline{p_{N,k}} = \overline{p_{N,N}} p_{N,k},$$

because $g_N = I_N - Q_N$ is a symmetric matrix. Furthermore $p_{N,N} = \overline{p_{N,N}}$ according to (b), so that $p_{N,k}$ is real for all $0 \leq k \leq N$.

For the proof of part (e) we shall rely on results from Chapter IV. If

$$g_B(x,y) = g(x,y), \quad B = [x | -\infty < x \leq -1]$$

is the Green function of the half-line in D19.3, we have

$$\lim_{N \to \infty} g_N(k,j) = g(k,j) \text{ for } k \geq 0, \quad j \geq 0,$$

since the sequence $g_N(k,j)$ is the expected number of visits from $k$ to $j$ before leaving $[0,N]$ and therefore increases monotonically to $g(k,j)$ which is a similar expectation for the half-line $[0,\infty)$. Since we are here in the symmetric case, P19.3 gives

$$\lim_{N \to \

Setting $k = 0$ in (7), while observing that $p_{N,N} > 0$, yields

(8) $$\lim_{N \to \infty} p_{N,N} = u(0), \quad \lim_{N \to \infty} p_{N,N-k} = u(k).$$

That completes the proof of P3.

In the sequel we shall actually never use P3 explicitly, but only the added conviction it gives us that one should pay attention to the algebraic aspects of the problem—i.e., to the fact that $P(x,y) = P(0,y-x)$, and its various manifestations. From Chapter IV we shall now copy certain results, to obviate the need for tedious references. They concern the Green function

$$g(x,y) = g_B(x,y), \quad B = [x \mid -\infty < x \leq -1].$$

It is given by the amazingly simple formula (6) in the proof of P3, which is valid precisely because $P(x,y)$ is a difference kernel. We shall restrict ourselves to random walk with $\mu = 0, \sigma^2 < \infty$ so that all the asymptotic results concerning $g(x,y)$ from section 19 become available.
