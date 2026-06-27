---
role: proof
locale: en
of_concept: action-function-solves-cauchy-problem
source_book: gtm060
source_chapter: "9"
source_section: "46"
---

Lift every extremal from $(\mathbf{q}, t)$-space to the extended phase space $\{(\mathbf{p}, \mathbf{q}, t)\}$ by setting $\mathbf{p} = \partial L / \partial \dot{\mathbf{q}}$. We get an $(n+1)$-dimensional manifold consisting of phase trajectories (characteristic curves of $\mathbf{p} \, d\mathbf{q} - H \, dt$).

Give the endpoint $(\mathbf{q}, t)$ an increment $(\Delta \mathbf{q}, \Delta t)$ and consider extremals connecting $(\mathbf{q}_0, t_0)$ with points of the segment $\mathbf{q} + \theta \Delta \mathbf{q}, t + \theta \Delta t$. In phase space we get a quadrangle $\sigma$ composed of characteristic curves, with boundary consisting of two phase trajectories $\gamma_1$ and $\gamma_2$, a curve $\alpha$ in $( \mathbf{q} = \mathbf{q}_0, t = t_0 )$, and a curve $\beta$ projecting to $(\Delta \mathbf{q}, \Delta t)$.

Since $\sigma$ consists of characteristic curves of $\mathbf{p} \, d\mathbf{q} - H \, dt$, we have

$$0 = \iint_{\sigma} d(\mathbf{p} \, d\mathbf{q} - H \, dt) = \int_{\partial \sigma} \mathbf{p} \, d\mathbf{q} - H \, dt = \int_{\gamma_1} - \int_{\gamma_2} + \int_{\beta} - \int_{\alpha} \mathbf{p} \, d\mathbf{q} - H \, dt.$$

On $\alpha$, $d\mathbf{q} = 0$, $dt = 0$. On the phase trajectories $\gamma_1$ and $\gamma_2$,

$$\int_{\gamma_{1,2}} \mathbf{p} \, d\mathbf{q} - H \, dt = \int_{\gamma_{1,2}} L \, dt.$$

Therefore,

$$\int_{\beta} \mathbf{p} \, d\mathbf{q} - H \, dt = \left[ S_0(\mathbf{q}_0 + \Delta \mathbf{q}) + \int_{\gamma_2} L \, dt \right] - \left[ S_0(\mathbf{q}_0) + \int_{\gamma_1} L \, dt \right] = S(A + \Delta A) - S(A).$$

For $\Delta t, \Delta \mathbf{q} \rightarrow 0$, we get $\partial S / \partial t = -H$, $\partial S / \partial \mathbf{q} = \mathbf{p}$, which proves the theorem. $\square$
