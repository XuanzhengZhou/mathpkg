---
role: proof
locale: en
of_concept: differential-of-action-function
source_book: gtm060
source_chapter: "9"
source_section: "46"
---

We lift every extremal from $(\mathbf{q}, t)$-space to the extended phase space $\{(\mathbf{p}, \mathbf{q}, t)\}$, setting $\mathbf{p} = \partial L / \partial \dot{\mathbf{q}}$, i.e., replacing the extremal by a phase trajectory. We then get an $(n+1)$-dimensional manifold in the extended phase space consisting of phase trajectories, i.e., characteristic curves of the form $\mathbf{p} \, d\mathbf{q} - H \, dt$.

We now give the endpoint $(\mathbf{q}, t)$ an increment $(\Delta \mathbf{q}, \Delta t)$, and consider the set of extremals connecting $(\mathbf{q}_0, t_0)$ with points of the segment $\mathbf{q} + \theta \Delta \mathbf{q}, t + \theta \Delta t$, $0 \leq \theta \leq 1$. In phase space we get a quadrangle $\sigma$ composed of characteristic curves of the form $\mathbf{p} \, d\mathbf{q} - H \, dt$, the boundary of which consists of two phase trajectories $\gamma_1$ and $\gamma_2$, a segment of a curve $\alpha$ lying in the space $(\mathbf{q} = \mathbf{q}_0, t = t_0)$, and a segment of a curve $\beta$ projecting to the segment $(\Delta \mathbf{q}, \Delta t)$. Since $\sigma$ consists of characteristic curves of the form $\mathbf{p} \, d\mathbf{q} - H \, dt$, we have

$$0 = \iint_{\sigma} d(\mathbf{p} \, d\mathbf{q} - H \, dt) = \int_{\partial \sigma} \mathbf{p} \, d\mathbf{q} - H \, dt$$

$$= \int_{\gamma_1} - \int_{\gamma_2} + \int_{\beta} - \int_{\alpha} \mathbf{p} \, d\mathbf{q} - H \, dt.$$

On the segment $\alpha$, we have $d\mathbf{q} = 0$, $dt = 0$. The phase trajectories $\gamma_1$ and $\gamma_2$ are phase trajectories, so

$$\int_{\gamma_{1,2}} \mathbf{p} \, d\mathbf{q} - H \, dt = \int_{\gamma_{1,2}} L \, dt.$$

Therefore,

$$\int_{\beta} \mathbf{p} \, d\mathbf{q} - H \, dt = \left[ S_0(\mathbf{q}_0 + \Delta \mathbf{q}) + \int_{\gamma_2} L \, dt \right] - \left[ S_0(\mathbf{q}_0) + \int_{\gamma_1} L \, dt \right]$$

$$= S(\mathbf{q} + \Delta \mathbf{q}, t + \Delta t) - S(\mathbf{q}, t).$$

If now $\Delta \mathbf{q} \rightarrow 0$, $\Delta t \rightarrow 0$, then

$$\int_{\beta} \mathbf{p} \, d\mathbf{q} - H \, dt = \mathbf{p} \, \Delta \mathbf{q} - H \, \Delta t + o(\Delta t, \Delta \mathbf{q})$$

which proves the theorem. $\square$
