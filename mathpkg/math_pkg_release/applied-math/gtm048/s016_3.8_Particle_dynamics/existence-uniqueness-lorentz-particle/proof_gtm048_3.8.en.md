---
role: proof
locale: en
of_concept: existence-uniqueness-lorentz-particle
source_book: gtm048
source_chapter: "3"
source_section: "3.8"
---

We first prove (a). Let $\{x^i\}$ be coordinate functions around $x$ such that $x^i(x) = 0$ for all $i$, and write $W = W^i(\partial_i|_x)$, $F = F_{ij}\, dx^i \otimes dx^j$ with $F_{ij} = -F_{ji}$. If $\gamma$ is the sought-for curve, set $\gamma^i \equiv x^i \circ \gamma$, $\dot{\gamma}^i \equiv d\gamma^i/du$, $\ddot{\gamma}^i \equiv d^2\gamma^i/du^2$.

Conditions (1)--(3) are respectively equivalent to:
\begin{align}
\text{(1a)}&\quad \gamma^i 0 = 0,\\
\text{(2a)}&\quad \dot{\gamma}^i 0 = W^i,\\
\text{(3a)}&\quad \ddot{\gamma}^i + (\Gamma^i_{jk} \circ \gamma)\,\dot{\gamma}^j \dot{\gamma}^k = e\,(F^i_k \circ \gamma)\,\dot{\gamma}^k,
\end{align}
where the $\Gamma^i_{jk}$ are the connection coefficients defined by $D_{\partial_j}\partial_k = \Gamma^i_{jk}\partial_i$ (cf. (3.6.1e)).

(3a) is a system of ordinary differential equations satisfied by $\{\gamma^i\}$ with prescribed initial conditions (1a) and (2a). The basic theorem for such equations guarantees both local existence and uniqueness. Equivalently, local existence and uniqueness of a $\gamma$ satisfying (1)--(3) of part (a) are now established. The existence of an inextendible such $\gamma$ follows by standard arguments using Zorn's lemma.

We next prove (b). From (a) we know $|g(\gamma_*, \gamma_*)|_0 = |g(W, W)| = m^2$. It suffices to show that
$$\frac{d}{du}\, g(\gamma_*, \gamma_*) = 0$$
everywhere on $\mathcal{E}$. Computing the derivative:
\begin{align*}
\frac{d}{du}\, g(\gamma_*, \gamma_*) &= 2g(D_{\gamma_*}\gamma_*, \gamma_*) \\
&= 2g(e\tilde{F}\gamma_*, \gamma_*) \quad\text{(by the Lorentz world-force law)} \\
&= 2e\,g(\tilde{F}\gamma_*, \gamma_*) = 0,
\end{align*}
since $\tilde{F}\gamma_*$ is orthogonal to $\gamma_*$ for any electromagnetic field $F$ (by antisymmetry of $\tilde{F}$: $g(\tilde{F}v, v) = 0$ for any vector $v$). Hence $g(\gamma_*, \gamma_*)$ is constant and equals $-m^2$ on the entire domain.

Thus both (a) and (b) are established.
