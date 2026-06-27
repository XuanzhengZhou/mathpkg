---
role: proof
locale: en
of_concept: coordinate-change-proportional-to-vector-fields
source_book: gtm051
source_chapter: "3"
source_section: "3.6"
---

Consider the vector fields $\bar{X}_i(u) = df_u^{-1} X_i(u)$ defined for $u \in U$. Suppose we could find a change of variables $\eta: U \to V$, $\eta(u) = (v^1(u), v^2(u))$, for which

$$(*) \quad dv^1(\bar{X}_2) = 0, \quad dv^2(\bar{X}_1) = 0.$$

Then in terms of canonical basis vector fields $(\tilde{e}_1, \tilde{e}_2)$ on $V$, $d\eta_u(\bar{X}_1(u)) = dv_u^1(\bar{X}_1(u))\tilde{e}_1 + 0$ and

$$\phi = \eta^{-1}: V \to U,$$

then $\tilde{f} = f \circ \phi$ satisfies $\tilde{f}_{v_i} = d\tilde{f}_v(\tilde{e}_i) = df_{\phi(v)} \circ d\phi_v(\tilde{e}_i) = a_i(v)X_i$, where $a_i(v) = (dv_v^i(\bar{X}_i(\phi(v))))^{-1}$. Thus $\phi$ is the required change of variables. Note that $a_i(v)$ is well defined, for if $dv_v^i(\bar{X}_i(\phi(v))) = 0$, then $dv_v^i = 0$ since $\{\bar{X}_1, \bar{X}_2\}$ are linearly independent and $dv^i(\bar{X}_j) = 0$, $i \neq j$. This contradicts the assumption that $\eta = (v^1, v^2)$ is a change of variables.

In order to complete the proof, it is necessary to establish the existence of a pair of functions $v^1(u), v^2(u)$, defined on some neighborhood of $u_0$, satisfying $(*)$ with $dv^i \neq 0$, $i = 1, 2$. This last condition will ensure that $\eta = (v^1, v^2)$ is a change of variables.

Let $\{e_1, e_2\}$ be the canonical basis vector fields on $U$ and write $\bar{X}_i(u) = \sum_{k=1}^{2} \xi_i^k(u)e_k$. By the standard existence theorem for ordinary differential equations, we may assert the existence, locally, of integral curves $c_i(s)$ of $\bar{X}_i(u)$. That is, for $|s|$ sufficiently small, we may find curves $c_1(s), c_2(s)$ in $V$ with $c_i(0) = u_0$ and $\dot{c}_i(s) = \bar{X}_i(c_i(s))$. We wish to solve $(*)$ which is equivalent to

$$\frac{\partial v^1}{\partial u^1} \xi_2^1(u) + \frac{\partial v^1}{\partial u^2} \xi_2^2(u) = 0, \quad \frac{\partial v^2}{\partial u^1} \xi_1^1(u) + \frac{\partial v^2}{\partial u^2} \xi_1^2(u) = 0.$$

The integral curves provide a regular map from some domain $V$ into $U$. The only obstruction to getting a diffeomorphism is the possibility that the integral curves of $X_i$ may intersect in two different points. Using simple connectivity, one may show that this is impossible.
