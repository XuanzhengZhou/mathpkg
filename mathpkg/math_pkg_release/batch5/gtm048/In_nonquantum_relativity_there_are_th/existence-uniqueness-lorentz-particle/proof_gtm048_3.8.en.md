---
role: proof
locale: en
of_concept: existence-uniqueness-lorentz-particle
source_book: gtm048
source_chapter: "3"
source_section: "3.8"
---

\textbf{Proof of (a).} Let $\{x^i\}$ be coordinate functions around $x$ such that $x^i(x) = 0$ for all $i$, and write $W = W^i(\partial_i)_x$, $F = F_{ij}\,dx^i \otimes dx^j$ with $F_{ij} = -F_{ji}$. For a sought-for curve $\gamma$, define $\gamma^i \equiv x^i \circ \gamma$, $\dot{\gamma}^i \equiv d\gamma^i/du$, $\ddot{\gamma}^i \equiv d^2\gamma^i/du^2$. Then conditions (1)–(3) are respectively equivalent to:

\[
\text{(1a)}\quad \gamma^i(0) = 0,
\qquad
\text{(2a)}\quad \dot{\gamma}^i(0) = W^i,
\]

\[
\text{(3a)}\quad \ddot{\gamma}^i + (\Gamma^i_{jk} \circ \gamma)\,\dot{\gamma}^j \dot{\gamma}^k = e\,(F^i_j \circ \gamma)\,\dot{\gamma}^j,
\]

where $\Gamma^i_{jk}$ are the connection coefficients defined by $D_{\partial_j}\partial_k = \Gamma^i_{jk}\partial_i$ (cf. 3.6.1e). Here $F^i_j = g^{ik}F_{kj}$ is the $(1,1)$-tensor corresponding to the electromagnetic field.

Equation (3a) is a system of ordinary differential equations satisfied by $\{\gamma^i\}$ with prescribed initial conditions (1a) and (2a). Both local existence and uniqueness are guaranteed by the basic theorem of such equations. Equivalently, local existence and uniqueness of a $\gamma$ satisfying (1)–(3) of part (a) are now established. The existence of an inextendible such $\gamma$ follows by standard arguments using Zorn's lemma.

\textbf{Proof of (b).} From (a) we already know $|\gamma_*0| = |W|$. It suffices to show that

\[
\frac{d}{du}\,g(\gamma_*, \gamma_*) = 0.
\]

The left side is

\[
\frac{d}{du}\,g(\gamma_*, \gamma_*) = 2g(D_{\gamma_*}\gamma_*, \gamma_*) = 2g(e\tilde{F}\gamma_*, \gamma_*).
\]

Since $\tilde{F}\gamma_*u \in (\gamma_*u)^\perp$ for all $u \in \mathcal{E}$, we have $g(\tilde{F}\gamma_*, \gamma_*) = 0$ everywhere. Hence the derivative vanishes identically, so $g(\gamma_*, \gamma_*)$ is constant along $\gamma$. Therefore $g(\gamma_*, \gamma_*) = g(W, W) = -m^2$ everywhere, and $(\gamma, m, e)$ is indeed a particle on $M$ with rest mass $m$.
