---
role: proof
locale: en
of_concept: dgamma2-commutative-diagram
source_book: gtm014
source_chapter: "V"
source_section: "5"
---

Let $\xi$ be a vector field on $X$ and $\psi_t$ the one-parameter group whose infinitesimal generator is $\xi$. Let $\omega = \pi_k^\infty(\xi)$. We compute $\lambda \cdot (df)(\omega)$.

Note that $F_t = f \circ \psi_t$ is a deformation of $f$ satisfying $(dF_t/dt)|_{t=0} = (df)(\xi)$. Thus we may use $F_t$ to compute $\lambda((df)(\omega))$. Now
\begin{align*}
\lambda \cdot (df)(\omega) &= \frac{d}{dt}(j^k F_t)(p)\big|_{t=0} \\
&= \frac{d}{dt}[j^k f(\psi_t(p)) \cdot j^k \psi_t(p)]\big|_{t=0} \\
&= \frac{d}{dt} j^k f(\psi_t(p))\big|_{t=0} + \frac{d}{dt} \sigma \cdot j^k \psi_t(p)\big|_{t=0}.
\end{align*}

Thus
$$\lambda \cdot (df)(\omega) = (dj^k f)_p \pi_0^\infty(\xi) - \frac{d}{dt} \sigma \cdot j^k \psi_{-t}(p)\big|_{t=0}$$
where $\pi_0^\infty: C^\infty(TX)_p \to T_p X = J^0(TX)_p$ is the obvious projection. Since $\pi_0^\infty = \pi_0^k \cdot \pi_k$ and $\psi_{-t} = \psi_t^{-1}$ we have that
$$\lambda \cdot (df)(\omega) = (dj^k f)_p \pi_0^k(\omega) - (d\gamma_2)(\xi)$$
or
$$(d\gamma_2)(\xi) = -\lambda \cdot (df)(\omega) + (dj^k f)_p \pi_0^k(\omega).$$

This is precisely the commutativity statement of the diagram.
