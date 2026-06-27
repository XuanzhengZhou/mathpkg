---
role: proof
locale: en
of_concept: projective-inductive-limit-duality
source_book: gtm003
source_chapter: "IV"
source_section: "4"
---

**Proof.** Let $E = \varprojlim g_{\alpha\beta} E_\beta$ be a projective limit of l.c.s. with linking maps $g_{\alpha\beta}: E_\beta \to E_\alpha$ ($\alpha \leq \beta$). By definition, $E$ is a subspace of $\prod_\beta E_\beta$, namely $E = \bigcap_{\alpha \leq \beta} \{x : g_{\alpha\beta} x_\beta = x_\alpha\}$. Let $h_{\beta\alpha} = {}^t g_{\alpha\beta}: E'_\alpha \to E'_\beta$ be the adjoint maps.

By Theorem 4.3, the dual of $\prod_\beta E_\beta$ is $\bigoplus_\beta E'_\beta$. An element $y = (y_\alpha) \in \bigoplus_\beta E'_\beta$ vanishes on $E$ (i.e., belongs to $E^\circ$) if and only if it lies in the weakly closed convex hull of $\bigcup_{\alpha \leq \beta} v_{\beta\alpha}(F)$, where $v_{\beta\alpha}$ are the maps dual to the defining relations. Let $H_0$ be this weakly closed convex hull. Then $H_0 \subset E^\circ$.

Conversely, let $y = (y_\alpha)$ be an element of $E^\circ$, let $H$ be the finite set of indices such that $\alpha \in H$ if and only if $y_\alpha \neq 0$, and choose an index $\beta$ such that $\alpha \leq \beta$ for all $\alpha \in H$. For any $x \in E$, we have

$$\langle x, y \rangle = \sum_{\alpha \in H} \langle x_\alpha, y_\alpha \rangle = \sum_{\alpha \in H} \langle g_{\alpha\beta} x_\beta, y_\alpha \rangle = \sum_{\alpha \in H} \langle x_\beta, h_{\beta\alpha} y_\alpha \rangle = \langle x_\beta, \sum_{\alpha \in H} h_{\beta\alpha} y_\alpha \rangle = 0.$$

Since by assumption $x_\beta$ runs through a dense subspace of $E_\beta$ as $x$ runs through $E$, the preceding relation implies that $\sum_{\alpha \in H} h_{\beta\alpha} y_\alpha = 0$, hence $y \in H_0$.

Thus $H_0$ is weakly closed in $F = \bigoplus_\alpha E'_\alpha$, hence closed for $\tau(F, \prod_\alpha E_\alpha)$, which by Theorem 4.3 is the topology $\bigoplus_\alpha \tau(E'_\alpha, E_\alpha)$. Therefore the inductive limit $\varinjlim h_{\beta\alpha} E'_\alpha$ of the Mackey duals $(E'_\alpha, \tau(E'_\alpha, E_\alpha))$ is algebraically isomorphic to $E'$, and the Mackey topology $\tau(E', E)$ coincides with the inductive limit topology. $\square$
