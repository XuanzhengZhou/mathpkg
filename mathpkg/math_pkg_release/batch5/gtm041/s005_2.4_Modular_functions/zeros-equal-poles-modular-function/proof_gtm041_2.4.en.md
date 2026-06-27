---
role: proof
locale: en
of_concept: zeros-equal-poles-modular-function
source_book: gtm041
source_chapter: "2"
source_section: "2.4"
---

Assume first that $f$ has no zeros or poles on the finite part of the boundary of $R_\Gamma$. Cut $R_\Gamma$ by a horizontal line, $\text{Im}(\tau) = M$, where $M > 0$ is taken so large that all the zeros or poles of $f$ are inside the truncated region which we call $R$. (If $f$ had an infinite number of poles in $R_\Gamma$ they would have an accumulation point at $i\infty$, contradicting condition (c). Similarly, since $f$ is not identically zero, $f$ cannot have an infinite number of zeros in $R_\Gamma$.)

Let $\partial R$ denote the boundary of the truncated region $R$. Let $N$ and $P$ denote the number of zeros and poles of $f$ inside $R$. Then by the argument principle,

$$N - P = \frac{1}{2\pi i} \int_{\partial R} \frac{f'(\tau)}{f(\tau)} d\tau = \frac{1}{2\pi i} \left\{ \int_{(1)} + \int_{(2)} + \int_{(3)} + \int_{(4)} + \int_{(5)} \right\}$$

where the path is split into five parts. The integrals along (1) and (4) cancel because of periodicity under $\tau \mapsto \tau + 1$. They also cancel along (2) and (3) because (2) gets mapped onto (3) with a reversal of direction under the mapping $u = S(\tau) = -1/\tau$, or $\tau = S^{-1}u = S(u)$. The integrand remains unchanged because $f[S(u)] = f(u)$ implies $f'[S(u)]S'(u) = f'(u)$, so

$$\frac{f'(\tau)}{f(\tau)} d\tau = \frac{f'[S(u)]}{f[S(u)]} S'(u) du = \frac{f'(u)}{f(u)} du.$$

Thus we are left with

$$N - P = \frac{1}{2\pi i} \int_{(5)} \frac{f'(\tau)}{f(\tau)} d\tau.$$

We transform this integral to the $x$-plane, $x = e^{2\pi i\tau}$. As $\tau$ varies on the horizontal segment $\tau = u + iM$, $-\frac{1}{2} \leq u \leq \frac{1}{2}$, we have

$$x = e^{2\pi i(u + iM)} = e^{-2\pi M} e^{2\pi iu}$$

so $x$ varies once around a circle $K$ of radius $e^{-2\pi M}$ about $x = 0$ in the negative direction. The points above this segment are mapped inside $K$, so $f$ has no zeros or poles inside $K$, except possibly at $x = 0$. The Fourier expansion gives us

$$f(\tau) = \frac{a_{-m}}{x^m} + \cdots = F(x),$$

say, with

$$f'(\tau) = F'(x) \frac{dx}{d\tau}, \quad \frac{f'(\tau)}{f(\tau)} d\tau = \frac{F'(x)}{F(x)} dx.$$

Hence

$$N - P = \frac{1}{2\pi i} \int_{(5)} \frac{f'(\tau)}{f(\tau)} d\tau = -\frac{1}{2\pi i} \oint_K \frac{F'(x)}{F(x)} dx = -(N_F - P_F) = P_F - N_F,$$

where $N_F$ and $P_F$ are the number of zeros and poles of $F$ inside $K$. If there is a pole of order $m$ at $x = 0$ then $m > 0$, $N_F = 0$, $P_F = m$ so $P_F - N_F = m$, and

$$N = P + m.$$

Therefore $f$ takes on the value $0$ in $R_\Gamma$ as often as it takes the value $\infty$.

If there is a zero of order $n$ at $x = 0$, then $m = -n$ so $P_F = 0$, $N_F = n$, hence

$$N + n = P.$$

Again, $f$ takes the value $0$ in $R_\Gamma$ as often as it takes the value $\infty$. This proves the theorem if $f$ has no zeros or poles on the finite part of the boundary of $R_\Gamma$.

If $f$ has a zero or a pole on an edge but not at a vertex, we introduce detours in the path of integration so as to include the zero or pole in the interior of $R$. The integrals along equivalent edges cancel as before. Only one member of each pair of new zeros or poles lies inside the new region and the proof goes through as before, since by convention only one of the equivalent points (zero or pole) is considered as belonging to the closure of $R_\Gamma$.

If $f$ has a zero or pole at a vertex $\rho$ or $i$ we further modify the path of integration with new detours. Arguing as above we find

$$N - P = \frac{1}{2\pi i} \left\{ \left( \int_{C_1} + \int_{C_3} \right) + \int_{C_2} + \int_{1/2 + iM}^{-1/2 + iM} \right\} \frac{f'(\tau)}{f(\tau)} d\tau$$

$$= \frac{1}{2\pi i} \left\{ \left( \int_{C_1} + \int_{C_3} \right) + \int_{C_2} \right\} \frac{f'(\tau)}{f(\tau)} d\tau.$$

Near the vertex $\rho$ we write

$$f(\tau) = (\tau - \rho)^k g(\tau), \quad \text{where } g(\rho) \neq 0.$$

The exponent $k$ is positive if $f$ has a zero at $\rho$, and negative if $f$ has a pole at $\rho$. On the path $C_1$ we write $\tau - \rho = re^{i\theta}$ where $r$ is fixed and $\alpha \leq \theta \leq \pi/2$ where $\alpha$ depends on $r$. Then

$$\frac{f'(\tau)}{f(\tau)} = \frac{k}{\tau - \rho} + \frac{g'(\tau)}{g(\tau)}$$

and

$$\frac{1}{2\pi i} \int_{C_1} \frac{f'(\tau)}{f(\tau)} d\tau = \frac{1}{2\pi i} \int_{\pi/2}^{\alpha} \left( \frac{k}{re^{i\theta}} + \frac{g'(\rho + re^{i\theta})}{g(\rho + re^{i\theta})} \right) re^{i\theta} i d\theta$$

$$= \frac{-k\alpha'}{2\pi} + \frac{r}{2\pi} \int_{\pi/2}^{\alpha} \frac{g'(\rho + re^{i\theta})}{g(\rho + re^{i\theta})} e^{i\theta} d\theta, \quad \text{where } \alpha' = \frac{\pi}{2} - \alpha.$$

As $r \to 0$, the last term tends to $0$ since the integrand is bounded. Also, $\alpha' \to \pi/3$ as $r \to 0$ so

$$\lim_{r \to 0} \frac{1}{2\pi i} \int_{C_1} \frac{f'(\tau)}{f(\tau)} d\tau = -\frac{k}{6}.$$

Similarly,

$$\lim_{r \to 0} \frac{1}{2\pi i} \int_{C_3} \frac{f'(\tau)}{f(\tau)} d\tau = -\frac{k}{6},$$

so

$$\lim_{r \to 0} \frac{1}{2\pi i} \left( \int_{C_1} + \int_{C_3} \right) \frac{f'(\tau)}{f(\tau)} d\tau = -\frac{k}{3}.$$

Similarly, near the vertex $i$ we write

$$f(\tau) = (\tau - i)^l h(\tau), \quad \text{where } h(i) \neq 0$$

and we find, in the same way,

$$\lim_{r \to 0} \frac{1}{2\pi i} \int_{C_2} \frac{f'(\tau)}{f(\tau)} d\tau = -\frac{l}{2}.$$

Therefore we get the formula

$$N - P = m - \frac{k}{3} - \frac{l}{2}.$$

If $f$ has a pole at $x = 0$, and zeros at $\rho$ and $i$, then $m, k$ and $l$ are positive and we have

$$N + \frac{k}{3} + \frac{l}{2} = P + m.$$

The left member counts the number of zeros of $f$ in the closure of $R_\Gamma$ (with the conventions agreed on at the vertices) and the right member counts the number of poles. If $f$ has a zero of order $n$ at $x = 0$ then $m = -n$ and the equation becomes

$$N + n + \frac{k}{3} + \frac{l}{2} = P.$$

Similarly, if $f$ has a pole at $\rho$ or at $i$ the corresponding term $k/3$ or $l/2$ is negative and gets counted along with $P$. This completes the proof.
