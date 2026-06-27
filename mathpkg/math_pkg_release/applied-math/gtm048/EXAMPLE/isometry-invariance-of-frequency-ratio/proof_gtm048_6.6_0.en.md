---
role: proof
locale: en
of_concept: isometry-invariance-of-frequency-ratio
source_book: gtm048
source_chapter: "6"
source_section: "6.0"
---

The cosmological frequency ratio $\iota(x, z)$ is defined in terms of the spacetime metric $g$, the light signal $[\lambda]$ from $x$ to $z$, and the comoving reference frame $\partial_4$. Specifically, $\iota([\lambda], \partial_4 x, \partial_4 z)$ is computed from the metric inner products of the tangent vectors to the light signal at $x$ and $z$ with $\partial_4 x$ and $\partial_4 z$.

Let $\psi: M \to M$ be an isometry, so $\psi^* g = g$. Then:
\begin{itemize}
    \item $\psi$ maps the light signal $[\lambda]$ from $x$ to $z$ to a light signal $[\psi \circ \lambda]$ from $\psi x$ to $\psi z$.
    \item By Proposition 6.0.5, $\psi$ preserves the comoving reference frame: $\psi_* \partial_4 = \partial_4$ (since $\psi(w, t) = (\tilde{\psi}w, t)$ implies $\psi_* \partial_4 = \partial_4$).
\end{itemize}

Since the frequency ratio is defined purely in terms of $g$, the light signal, and $\partial_4$, and all three are preserved by $\psi$, we obtain:
$$\iota(\psi x, \psi z) = \iota(x, z).$$

More explicitly, if $\lambda: I \to M$ is a lightlike geodesic with $\lambda(u) = x$ and $\lambda(v) = z$, then the frequency ratio is:
$$\iota = \frac{g(\lambda_*(u), \partial_4|_x)}{g(\lambda_*(v), \partial_4|_z)}.$$

Applying the isometry:
\begin{align*}
\iota(\psi x, \psi z) &= \frac{g((\psi \circ \lambda)_*(u), \partial_4|_{\psi x})}{g((\psi \circ \lambda)_*(v), \partial_4|_{\psi z})} \\
&= \frac{g(\psi_* \lambda_*(u), \psi_* \partial_4|_x)}{g(\psi_* \lambda_*(v), \psi_* \partial_4|_z)} \\
&= \frac{(\psi^* g)(\lambda_*(u), \partial_4|_x)}{(\psi^* g)(\lambda_*(v), \partial_4|_z)} \\
&= \frac{g(\lambda_*(u), \partial_4|_x)}{g(\lambda_*(v), \partial_4|_z)} = \iota(x, z).
\end{align*}
