---
role: proof
locale: en
of_concept: independence-of-choice-of-r
source_book: gtm026
source_chapter: "2"
source_section: "2.22"
---

Observe that for any $\alpha: V \longrightarrow VT$ we have

$$
\alpha^{\#}.\Gamma = (\alpha\Gamma)^{\#'\prime}
\tag{2.23}
$$

since $\alpha^{\#}.\Gamma = (\text{id}_{VT} \circ \alpha).\Gamma = (\text{id}_{VT}.\Gamma) \circ' (\alpha\Gamma) = (\alpha\Gamma)^{\#'\prime}$.

Define $f: V \longrightarrow V$ by

$$
v_i f = \begin{cases}
v_i & \text{if } n \geqslant 1 \text{ and } 1 \leqslant i \leqslant n \\
v_1 & \text{otherwise}
\end{cases}
$$

and set $\alpha: V \longrightarrow VT$ to be $f.V\eta$. Let $X, \delta, \omega', r$ be as in 2.21. Observing that $\alpha^{\#}.r^{\#} = (f.r)^{\#}$ (use 2.5 and 2.14) and using 2.23, we have:

$$
\begin{aligned}
\langle [v_1 \cdots v_n \omega'], \Gamma^{-1}.r^{\#} \rangle
&= \langle v_1, \alpha.\Gamma^{-1}.r^{\#} \rangle \\
&= \langle v_1, (\alpha\Gamma^{-1}).r^{\#} \rangle \\
&= \langle v_1, (\alpha\Gamma^{-1})^{\#'\prime}.\Gamma.r^{\#} \rangle \quad \text{(by 2.23 applied to } \alpha\Gamma^{-1}\text{)} \\
&= \langle v_1, \alpha^{\#}.\Gamma^{-1}.\Gamma.r^{\#} \rangle \\
&= \langle v_1, \alpha^{\#}.r^{\#} \rangle \\
&= \langle v_1, (f.r)^{\#} \rangle \\
&= (v_1 f) r = (x_1, \ldots, x_n) \delta'_{\omega'}.
\end{aligned}
$$

Since the final expression depends only on $x_1, \ldots, x_n$ and not on the specific choice of $r$, the lemma is proved.
