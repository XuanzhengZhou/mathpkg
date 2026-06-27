---
role: proof
locale: en
of_concept: hamiltonian-flow-preserves-symplectic-structure
source_book: gtm060
source_chapter: "8"
source_section: "38"
---

Let $M$ be an arbitrary manifold, $c$ a $k$-chain on $M$, and $g^t: M \to M$ a one-parameter family of differentiable mappings. Construct a $(k+1)$-chain $Jc$ on $M$, called the **track** of the chain $c$ under the homotopy $g^t$, $0 \leq t \leq \tau$.

If $c$ is the image of a standard $k$-dimensional cube $D^k$ under a map $f: D^k \to M$, we define a map $F: I \times D^k \to M$ (where $I = [0, \tau]$) by $F(t, x) = g^t(f(x))$. The image of the $(k+1)$-dimensional cube $I \times D^k$ under $F$ is the track $Jc$.

Under the appropriate orientation, the boundary of $Jc$ satisfies:
$$
\partial(Jc_k) = g^\tau c_k - c_k - J\partial c_k. \tag{1}
$$

**Lemma.** Let $\gamma$ be a $1$-chain in the symplectic manifold $(M^{2n}, \omega^2)$. Let $g^t$ be a phase flow on $M$ with Hamiltonian function $H$. Then
$$
\frac{d}{d\tau} \int_{J\gamma} \omega^2 = \int_{g^\tau\gamma} dH.
$$

**Proof of the Lemma.** It suffices to consider a chain $\gamma$ with one cell $f: [0, 1] \to M$. Introduce the notation
$$
f'(s, t) = g^t f(s), \quad \xi = \frac{\partial f'}{\partial s}, \quad \eta = \frac{\partial f'}{\partial t} \in TM_{f'(s, t)}.
$$
By the definition of the integral,
$$
\int_{J\gamma} \omega^2 = \int_0^1 \int_0^\tau \omega^2(\xi, \eta) \, dt \, ds.
$$
By the definition of the phase flow, $\eta$ is a vector (at the point $f'(s, t)$) of the Hamiltonian field with Hamiltonian function $H$. By definition of a Hamiltonian field,
$$
\omega^2(\xi, \eta) = dH(\xi).
$$
Thus
$$
\int_{J\gamma} \omega^2 = \int_0^1 \int_0^\tau dH(\xi) \, dt \, ds.
$$
Differentiating with respect to $\tau$ yields
$$
\frac{d}{d\tau} \int_{J\gamma} \omega^2 = \int_0^1 dH(\xi)\big|_{t=\tau} \, ds = \int_{g^\tau\gamma} dH.
$$

**Proof of the Theorem.** Apply formula (1) to a $2$-chain $c$ (so $k=2$):
$$
\partial(Jc) = g^\tau c - c - J\partial c.
$$
Integrate $\omega^2$ over both sides. Since $\omega^2$ is closed ($d\omega^2 = 0$), Stokes' theorem gives $\int_{\partial(Jc)} \omega^2 = \int_{Jc} d\omega^2 = 0$. Hence
$$
\int_{g^\tau c} \omega^2 - \int_c \omega^2 - \int_{J\partial c} \omega^2 = 0.
$$
Now specialize to a closed $2$-chain $c$ (so $\partial c = 0$). Then $J\partial c = 0$, and we obtain
$$
\int_{g^\tau c} \omega^2 = \int_c \omega^2.
$$
Since this holds for every closed $2$-chain $c$ and every $\tau$, we conclude $(g^\tau)^* \omega^2 = \omega^2$ (the form $\omega^2$ is an integral invariant of $g^\tau$), which is equivalent to the preservation of the symplectic structure.
