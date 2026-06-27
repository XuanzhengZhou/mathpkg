---
role: proof
locale: en
of_concept: deformation-germ-infinitesimally-stable-point
source_book: gtm014
source_chapter: "IV"
source_section: "4"
---

We proceed by induction on the number of deformation parameters. Let $F \colon X \times \mathbf{R}^k \to Y \times \mathbf{R}^k$ be a $k$-deformation of $f$, with infinitesimal generator $\tau_F = dF(\partial/\partial t)$. By applying Lemma 3.2, the deformation factors as $M \colon X \times \mathbf{R}^{k-1} \to Y \times \mathbf{R}^{k-1}$ trivially extended to a $k$-deformation, with $F = H \circ (M \times \mathrm{id}) \circ G$ where $H$ and $G$ are suitable diffeomorphisms.

We must show that $\tau_M^i$ ($1 \leq i \leq k-1$) can be written as
$$\tau_M^i = (dM)(\bar{\zeta}^i) + M^*(\bar{\eta}^i)$$
where $\bar{\zeta}^i$ and $\bar{\eta}^i$ are vector fields whose $\mathbf{R}^k$-components are zero. This allows induction to conclude that $F$ is trivial.

A direct computation gives the relation
$$\tau_M^i \cdot G = (dH)\tau_F^i - (dM)\pi(dG)(\partial/\partial t).$$

Since $H$ and $F$ are deformations, $(dH)(\tau_F^i) = (dH)\pi(dF)(\partial/\partial t_i) = \pi(dH)(dF)(\partial/\partial t_i)$. Expanding,
$$\begin{align*}
(dH)(\tau_F^i) &= \pi(dM)(dG)\left(\frac{\partial}{\partial t_i}\right) \\
&= \pi(dM)\left(\frac{\partial}{\partial t_i}\right) + (dG)\left(\frac{\partial}{\partial t_i}\right) \\
&= \pi(dM)\left(\frac{\partial}{\partial t_i}\right) + (dM)\pi(dG)\left(\frac{\partial}{\partial t_i}\right).
\end{align*}$$

Noting that $\pi(dM)(\partial/\partial t_i)|_G = \tau_M^i \cdot G$, we obtain
$$(dH)\tau_F^i = \tau_M^i \cdot G + (dM)\pi(dG)\left(\frac{\partial}{\partial t_i}\right),$$
which proves the relation. Thus it suffices to show that $(dH)\tau_F^i$ has the desired form.

Now compute $(dH)(\tau_F^i) = (dH)(dF)(\zeta^i) + (dH)(\eta^i)|_F$, and define $\bar{\zeta}_{G(p)} = (dG)_p(\zeta_p)$.

Define a one-parameter group $\phi_t \colon X \times Y \to X \times Y$ whose infinitesimal generator is $\bar{\tau}$, and set $F \colon X \times \mathbf{R} \to Y \times \mathbf{R}$ by
$$F(x, t) = (\pi_Y \cdot \phi_t(x, f(x)), t),$$
where $\pi_Y \colon X \times Y \to Y$ is the projection. Then $F$ is smooth and is a deformation of $f$ since $F(x, 0) = (\pi_Y(x, f(x)), 0) = (f(x), 0)$.

Since $f$ is stable under deformations, Theorem 3.3 provides vector fields $\bar{\zeta}$ on $X \times I_\delta$ and $\bar{\eta}$ on $Y \times I_\delta$ (for some $\delta > 0$) with vanishing $\mathbf{R}$-components such that
$$\tau_F = (dF)(\bar{\zeta}) + F^*\bar{\eta}$$
on $X \times I_\delta$. Restricting to $X \times \{0\}$ yields
$$\tau_F|_{X \times \{0\}} = (df)(\zeta) + f^*\eta,$$
where $\zeta_p = \bar{\zeta}_{(p,0)}$ and $\eta_q = \bar{\eta}_{(q,0)}$ are vector fields on $X$ and $Y$ respectively (the $\mathbf{R}$-components vanish).

Now $\tau_F|_{(p,0)} = \pi(dF)_{(p,0)}((\partial/\partial t)|_{(p,0)})$. The curve $t \mapsto (p, t)$ represents $(\partial/\partial t)|_{(p,0)}$, so $t \mapsto \pi_Y \cdot \phi_t(p, f(p))$ represents $\tau_F|_{(p,0)}$. Computing the derivative,
$$\frac{d}{dt} \pi_Y \cdot \phi_t(p, f(p))|_{t=0} = (d\pi_Y)_{(p, f(p))}(\bar{\tau}_{(p, f(p))}).$$

The vector fields along $F$, namely $F^*(\partial/\partial y_i)$, generate the module $N$. Thus $A$ is a finitely generated module over $C^\infty_{(p,0)}(X \times \mathbf{R}^k)$. Via $F^*$, $A$ is also a module over $C^\infty_{(q,0)}(Y \times \mathbf{R}^k)$ where $q = f(p)$.

We claim that $A$ is also a finitely generated $C^\infty_{(q,0)}(Y \times \mathbf{R}^k)$-module with generators $e_i = \text{projection of } F^*(\partial/\partial y_i)$ in $A$. It is in proving this claim that infinitesimal stability of $f$ at $p$ is used.

To see the claim suffices: in $A$,
$$[\tau_F]_{(p,0)} = \sum_{i=1}^{m} \left[ \eta_i F^*\left(\frac{\partial}{\partial y_i}\right) \right]_{(p,0)}.$$
Thus in $N$,
$$[\tau_F]_{(p,0)} = (dF)[\zeta]_{(p,0)} + F^*\left[ \sum_{i=1}^{m} \eta_i \frac{\partial}{\partial y_i} \right]_{(p,0)}$$
where $\zeta$ has $\mathbf{R}^k$-component zero since $(dF)[\zeta]_{(p,0)} \in K$.

Setting $\eta = \sum_{i=1}^{m} \eta_i (\partial/\partial y_i)$, whose $\mathbf{R}^k$-component is zero, we obtain $\tau_F = (dF)(\zeta) + F^*\eta$ on the germ level near $(p,0)$. The local form of Theorem 3.3 then completes the proof.

To prove the claim, we use the Malgrange Preparation Theorem (IV, Theorem 3.6). By Taylor's Theorem, write
$$\tau(x, t) = \tau_0(x) + \sum_{j=1}^{k} t_j \tau_j(x, t).$$
The finite generation property follows from the infinitesimal stability hypothesis applied to the module structure described above, together with the Malgrange Preparation Theorem applied to the map germ $(F, \pi) \colon (X \times \mathbf{R}^k, (p,0)) \to (Y \times \mathbf{R}^k, (q,0))$.
