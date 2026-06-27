---
role: proof
locale: en
of_concept: hamiltonian-track-integral-lemma
source_book: gtm060
source_chapter: "8"
source_section: "38"
---

It suffices to consider a chain $\gamma$ consisting of a single cell $f: [0, 1] \to M$. Introduce the notation
$$
f'(s, t) = g^t f(s), \quad \xi = \frac{\partial f'}{\partial s}, \quad \eta = \frac{\partial f'}{\partial t} \in TM_{f'(s, t)}.
$$
By the definition of the integral of a $2$-form over a $2$-chain parametrized by $(s, t)$,
$$
\int_{J\gamma} \omega^2 = \int_0^1 \int_0^\tau \omega^2(\xi, \eta) \, dt \, ds.
$$

Now, by the definition of the phase flow $g^t$, the vector $\eta = \frac{\partial f'}{\partial t}$ is precisely the velocity vector of the flow at the point $f'(s, t)$, i.e., the value of the Hamiltonian vector field:
$$
\eta = I\,dH(f'(s, t)).
$$
By the definition of the Hamiltonian vector field via the symplectic isomorphism,
$$
\omega^2(\xi, \eta) = \omega^2(\xi, I\,dH) = dH(\xi).
$$
Therefore,
$$
\int_{J\gamma} \omega^2 = \int_0^1 \int_0^\tau dH(\xi) \, dt \, ds.
$$

Differentiating with respect to the upper limit $\tau$ yields
$$
\frac{d}{d\tau} \int_{J\gamma} \omega^2 = \int_0^1 dH(\xi)\big|_{t=\tau} \, ds.
$$
The right-hand side is precisely the integral of the $1$-form $dH$ over the chain $g^\tau\gamma$ (which is parametrized by $s \mapsto f'(s, \tau) = g^\tau f(s)$). Hence
$$
\frac{d}{d\tau} \int_{J\gamma} \omega^2 = \int_{g^\tau\gamma} dH.
$$
