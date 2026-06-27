---
role: proof
locale: en
of_concept: dgamma2-dgamma1-onto
source_book: gtm014
source_chapter: "V"
source_section: "5"
---

Let $v$ be in $T_\sigma \mathcal{D}_\sigma$ and $c(t)$ a curve representing $v$ in $\mathcal{D}_\sigma$. Suppose there exists a curve of diffeomorphisms $t \mapsto (g_t, h_t)$ in $\mathrm{Diff}(X) \times \mathrm{Diff}(Y)$ such that $c(t) = j^k h_t(q) \cdot \sigma \cdot j^k g_t^{-1}(g_t(p))$; then $v$ is in the image of $(d\gamma_2) \oplus (d\gamma_1)$.

Let $\xi_p = (dg_t/dt)|_{t=0}(p)$ and $\eta_q = (dh_t/dt)|_{t=0}(q)$. Then $\xi$ and $\eta$ are vector fields on $X$ and $Y$ respectively. (Since we are only interested in the germ of $\eta$ at $q$ we may assume that $\eta$ has compact support.) Let $\phi_t$ and $\psi_t$ be the one-parameter groups associated with $\xi$ and $\eta$ respectively. Then the curve $\tilde{c}(t) = j^k \psi_t(q) \cdot \sigma \cdot j^k \phi_{-t}(\phi_t(p))$ satisfies
$$\frac{d\tilde{c}}{dt}\bigg|_{t=0} = \frac{dc}{dt}\bigg|_{t=0} = v$$
since $(dc/dt)|_{t=0}$ only depends on $(dg_t/dt)|_{t=0}$ and $(dh_t/dt)|_{t=0}$, but $(dg_t/dt)|_{t=0} = (d\phi_t/dt)|_{t=0}$ and $(dh_t/dt)|_{t=0} = (d\psi_t/dt)|_{t=0}$.

Recall that when we proved that $\mathcal{D}_\sigma$ is an immersed submanifold (see the proof of Theorem 5.1) we showed that $\mathcal{D}_\sigma^{U,V} =$ connected component of $\mathcal{D}_\sigma \cap J^k(U,V)$ containing $\sigma$ is equal to $T(U \times V \times \mathring{\mathcal{O}}_\sigma)$ where $\mathring{\mathcal{O}}_\sigma$ is the orbit through $\sigma$ of the action of the Lie group $G = \mathring{G}^k(X)_p \times \mathring{G}^k(Y)_q$ on $J^k(X,Y)_{p,q}$.

Since $T_\sigma \mathcal{D}_\sigma = T_\sigma \mathcal{D}_\sigma^{U,V}$ we may assume that the curve $c(t)$ is in $\mathcal{D}_\sigma^{U,V}$. Since $T$ is a diffeomorphism there is a curve $a(t) = (p(t), q(t), \tau(t))$ in $U \times V \times \mathring{\mathcal{O}}_\sigma$ such that $T(a(t)) = c(t)$. Thus $c(t) = j^k T_{q(t)} \cdot \tau(t) \cdot j^k(T_{p(t)}^{-1})$.

So if we can show that $\tau(t) = j^k(h(t)) \cdot \sigma \cdot j^k(g(t)^{-1})$ then we will be finished by the last paragraph. But $\tau(t)$ is a curve in $\mathring{\mathcal{O}}_\sigma$. Thus there is a curve $(\tilde{g}(t), \tilde{h}(t))$ in $\mathring{G}^k(X)_p \times \mathring{G}^k(Y)_q$ such that $\tilde{h}(t) \cdot \sigma \cdot \tilde{g}(t)^{-1} = \tau(t)$ since $\mathring{G}$ is a Lie group.

In local coordinates $\mathring{G}^k(X)$ is just polynomial mappings of degree $\leq k$ on $\mathbb{R}^n$ which are diffeomorphisms on a nbhd of $0$. Let $g(t)$ be the unique polynomial of degree $\leq k$ such that $j^k g(t) = \tilde{g}(t)$. Similarly for $h(t)$ and $\tilde{h}(t)$. Since $\det(dg_0)_p > 0$ and $\det(dh_0)_q > 0$ we may assume that $g_t$ and $h_t$ are globally defined diffeomorphisms on $X$ and $Y$ respectively. (Apply Proposition 5.5.) Thus we obtain the desired $g_t$ and $h_t$.
