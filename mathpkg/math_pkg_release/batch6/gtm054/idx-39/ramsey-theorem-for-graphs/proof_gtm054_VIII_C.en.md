---
role: proof
locale: en
of_concept: ramsey-theorem-for-graphs
source_book: gtm054
source_chapter: "VIII"
source_section: "C"
---

We proceed by induction on the variable $k = q_1 + q_2$. By boundary values and basic properties, the theorem holds for $k = 2, 3, 4$.

As induction hypothesis, we choose $k \geq 5$ and suppose that the theorem holds whenever $q_1 + q_2 < k$.

Now suppose $q_1 + q_2 = k$ and let $\Gamma = (V, \mathcal{E})$ be any graph such that $\omega(\Gamma) < q_1$ and $\alpha_0(\Gamma) < q_2$. Let $p = n(q_1-1, q_2) + n(q_1, q_2-1)$; we must show $\nu_0(\Gamma) < p$. Assume to the contrary that $\nu_0(\Gamma) = p$.

Choose $x \in V$ and let $S = N(x)$ (the set of vertices adjacent to $x$) and let $T = V \setminus (S \cup \{x\})$. Since $\Gamma_S$ contains no $(q_1-1)$-clique (any such clique together with $x$ would give a $q_1$-clique in $\Gamma$), we have $\omega(\Gamma_S) < q_1-1$. Moreover, $\alpha_0(\Gamma_S) \leq \alpha_0(\Gamma) < q_2$. By the induction hypothesis, $\nu_0(\Gamma_S) \leq n(q_1-1, q_2) - 1$.

Similarly, $\Gamma_T$ contains no $q_2$-independent set, so $\alpha_0(\Gamma_T) < q_2-1$, while $\omega(\Gamma_T) \leq \omega(\Gamma) < q_1$. By the induction hypothesis, $\nu_0(\Gamma_T) \leq n(q_1, q_2-1) - 1$.

Now $\nu_0(\Gamma) = 1 + \nu_0(\Gamma_S) + \nu_0(\Gamma_T) \leq 1 + n(q_1-1, q_2) - 1 + n(q_1, q_2-1) - 1 = p - 1$, contradicting the assumption $\nu_0(\Gamma) = p$.

Therefore $n(q_1, q_2) \leq p = n(q_1-1, q_2) + n(q_1, q_2-1)$, completing the induction step.
