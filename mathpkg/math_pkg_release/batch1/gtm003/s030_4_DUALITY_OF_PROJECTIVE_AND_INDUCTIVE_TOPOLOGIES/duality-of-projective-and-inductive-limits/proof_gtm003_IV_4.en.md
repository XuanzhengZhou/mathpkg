---
role: proof
locale: en
of_concept: duality-of-projective-and-inductive-limits
source_book: gtm003
source_chapter: "IV"
source_section: "4"
---

The projective limit $E = \varprojlim g_{\alpha\beta} E_\beta$ is by definition a subspace of $\prod_\beta E_\beta$, specifically the subspace $\bigcap_{\alpha \leq \beta} u_{\alpha\beta}^{-1}(0)$ where $u_{\alpha\beta}$ denotes the difference of the relevant projections. The dual of $\prod_\beta E_\beta$ is $\bigoplus_\beta E'_\beta$ by Theorem 4.3. Let $F = \bigoplus_\beta E'_\beta$ be this direct sum, and let $E^\circ$ be the polar of $E$ in $F$ with respect to the canonical duality between $\prod_\beta E_\beta$ and $\bigoplus_\beta E'_\beta$.

Let $H_0$ be the linear hull of $\bigcup_{\alpha \leq \beta} [u_{\alpha\beta}^{-1}(0)]^\circ$, which by the corollary of Theorem 2.3 equals the weakly closed convex hull of $\bigcup_{\alpha \leq \beta} v_{\beta\alpha}(F)$, where $v_{\beta\alpha} = h_{\beta\alpha}$ are the dual linking maps. This establishes $H_0 \subset E^\circ$.

Conversely, let $y = (y_\alpha) \in E^\circ$, let $H$ be the finite set of indices with $y_\alpha \neq 0$, and choose $\beta$ with $\alpha \leq \beta$ for all $\alpha \in H$. For any $x \in E$,
$$\langle x, y \rangle = \sum_{\alpha \in H} \langle x_\alpha, y_\alpha \rangle = \sum_{\alpha \in H} \langle g_{\alpha\beta} x_\beta, y_\alpha \rangle = \sum_{\alpha \in H} \langle x_\beta, h_{\beta\alpha} y_\alpha \rangle = \langle x_\beta, \sum_{\alpha \in H} h_{\beta\alpha} y_\alpha \rangle = 0.$$

Since $x_\beta$ runs through a dense subspace of $E_\beta$ as $x$ runs through $E$, we obtain $\sum_{\alpha \in H} h_{\beta\alpha} y_\alpha = 0$, hence
$$y = \sum_{\alpha \in H} (q_\alpha - q_\beta \circ h_{\beta\alpha}) y_\alpha \in H_0.$$

Thus $H_0 = E^\circ$ is weakly closed in $F$, hence closed for $\tau(F, \prod_\alpha E_\alpha)$, which by Theorem 4.3 is the topology $\bigoplus_\alpha \tau(E'_\alpha, E_\alpha)$. Therefore
$$E' = F / E^\circ = \bigoplus_\alpha E'_\alpha / H_0$$
with the quotient Mackey topology is precisely the inductive limit $\varinjlim h_{\beta\alpha} (E'_\alpha, \tau(E'_\alpha, E_\alpha))$.
