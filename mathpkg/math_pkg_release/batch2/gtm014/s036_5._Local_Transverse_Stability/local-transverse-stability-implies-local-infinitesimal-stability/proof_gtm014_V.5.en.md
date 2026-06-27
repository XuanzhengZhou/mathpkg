---
role: proof
locale: en
of_concept: local-transverse-stability-implies-local-infinitesimal-stability
source_book: gtm014
source_chapter: "V"
source_section: "5"
---

Assume that $f$ is locally transverse stable at $p$. By Corollary 1.3 it is sufficient to show that $f$ satisfies the conditions of infinitesimal stability to order $m$. In particular, we need to show that if $\tau$ is in $J^m(f^*TY)_p$, then there is a $v_1$ in $J^m(TX)_p$ and a $v_2$ in $J^m(TY)_q$ so that $\tau = (df)(v_1) + f^*(v_2)$.

Consider $\lambda(\tau)$ in $T_\sigma J^m(X, Y)$ where $\sigma = j^m f(p)$. Since $f$ is locally transverse stable at $p$, we have $j^m f \pitchfork \mathcal{D}_\sigma$ at $p$, which means
$$T_\sigma J^m(X, Y) = (dj^m f)_p(T_p X) + T_\sigma \mathcal{D}_\sigma.$$
Thus there exists $w$ in $T_\sigma \mathcal{D}_\sigma$ and $v$ in $T_p X$ so that
$$\lambda(\tau) = w + (dj^m f)_p(v).$$

By Lemma 5.12 there exists $\xi$ in $C^\infty(TX)_p$ and $\eta$ in $C^\infty(TY)_q$ so that $w = (d\gamma_2)(\xi) + (d\gamma_1)(\eta)$.

Let $v_1 = \pi_k^\infty(\xi)$ and $v_2 = \pi_k^\infty(\eta)$. Applying Propositions 5.10 and 5.11 we have that
\begin{align*}
(d\gamma_1)(\eta) &= \lambda \cdot f^*(v_2), \\
(d\gamma_2)(\xi) &= -\lambda \cdot (df)(v_1) + (dj^m f)_p \pi_0^m(v_1).
\end{align*}

Thus
\begin{align*}
\lambda(\tau) &= (d\gamma_2)(\xi) + (d\gamma_1)(\eta) + (dj^m f)_p(v) \\
&= -\lambda \cdot (df)(v_1) + (dj^m f)_p \pi_0^m(v_1) + \lambda \cdot f^*(v_2) + (dj^m f)_p(v).
\end{align*}

Apply $(d\alpha)_\sigma$ to both sides (where $\alpha$ is the source map) and apply Proposition 5.9. Since $(d\alpha)_\sigma \cdot \lambda = 0$ and $(d\alpha)_\sigma \cdot (dj^m f)_p = \mathrm{id}_{T_p X}$, we obtain
$$0 = 0 + \pi_0^m(v_1) + 0 + v$$
so $v = -\pi_0^m(v_1)$.

Therefore
\begin{align*}
\lambda(\tau) &= -\lambda \cdot (df)(v_1) - (dj^m f)_p(v) + \lambda \cdot f^*(v_2) + (dj^m f)_p(v) \\
&= \lambda \cdot (df)(v_1) + \lambda \cdot f^*(v_2).
\end{align*}

But $\lambda$ is injective (Proposition 5.8), so $\tau = (df)(v_1) + f^*(v_2)$. This completes the proof.
