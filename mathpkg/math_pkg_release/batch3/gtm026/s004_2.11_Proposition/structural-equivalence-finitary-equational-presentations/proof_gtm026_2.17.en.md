---
role: proof
locale: en
of_concept: structural-equivalence-finitary-equational-presentations
source_book: gtm026
source_chapter: "2"
source_section: "2.17"
---

**(2.18) implies (2.19).** By 2.5, there exists a unique $\Omega$-homomorphism $X\lambda: XT \longrightarrow XT'$ (where $XT'$ is an $(\Omega, E)$-algebra by virtue of $\psi_{XT'}^{-1}$) such that preservation of variables holds. To prove that composition is preserved, consider the diagram

$$
\begin{array}{ccc}
A & \xrightarrow{\alpha} & BT & \xrightarrow{\beta^{\#}} & CT \\
& & \downarrow B\lambda & & \downarrow C\lambda \\
& & BT' & \xrightarrow{(B\lambda)^{\#}} & CT'
\end{array}
$$

where the bottom morphism of the square can be regarded as an $\Omega$-homomorphism with the help of $\psi^{-1}$. The remaining details are similar to the proof of 2.10 and need no repeating.

**(2.19) implies (2.20).** Set $\Gamma = V\lambda$. That composing with $\Gamma$ is a monoid isomorphism is clear, and it suffices to prove

$$
x^{\#}.\Gamma = x'^{\#}.
$$

To this end,

$$
x^{\#}.\Gamma = (\text{id}_{\phi T} \circ x).\Gamma = (\text{id}_{\phi T}.\phi\lambda) \circ' (x.\Gamma) = \phi\lambda \circ' x' = \phi\lambda.x'^{\#}.
$$

**(2.20) implies (2.18).** Let us begin by observing that we have symmetry: it is easy to check that $\Gamma^{-1}$ enjoys the same properties as $\Gamma$. Next, let us make some comments about the empty set.

For each nonempty set $X$ define the desired $\psi_X$ of 2.18 by $\delta\psi_X = \delta'$ where for all $\omega'$ in $\Omega'_n$,

$$
\langle [v_1 \cdots v_n \omega'], \Gamma^{-1}.r^{\#} \rangle
\tag{2.21}
$$

where $r: V \longrightarrow X$ is any function such that $v_i r = x_i$; in case $n = 0$ let $r$ be arbitrary (but here we require that $X$ be nonempty). For an example see exercise 9. We need:

**Lemma 2.22.** $(x_1, \ldots, x_n) \delta'_{\omega'}$ as in 2.21 is independent of the choice of $r$.

*Proof of Lemma 2.22.* Observe that for any $\alpha: V \longrightarrow VT$ we have

$$
\alpha^{\#}.\Gamma = (\alpha\Gamma)^{\#'\prime}
\tag{2.23}
$$

since $\alpha^{\#}.\Gamma = (\text{id}_{VT} \circ \alpha).\Gamma = (\text{id}_{VT}.\Gamma) \circ' (\alpha\Gamma) = (\alpha\Gamma)^{\#'\prime}$. Define $f: V \longrightarrow V$ by

$$
v_i f = \begin{cases}
v_i & \text{if } n \geqslant 1 \text{ and } 1 \leqslant i \leqslant n \\
v_1 & \text{otherwise}
\end{cases}
$$

and set $\alpha: V \longrightarrow VT$ to be $f.V\eta$. Let $X, \delta, \omega', r$ be as in 2.21. Observing that $\alpha^{\#}.r^{\#} = (f.r)^{\#}$ (use 2.5 and 2.14) and using 2.23 we have the desired independence.

To complete the proof of (2.20) $\Rightarrow$ (2.18), we must verify the homomorphism condition for the $\psi_X$ defined in 2.21. This requires showing that for arbitrary $r: V \longrightarrow X$ and any equation $(e_1, e_2) \in E'$, we have $e_1 r^{\#\#\#} = e_2 r^{\#\#\#}$ because $\langle e_1, V\rho' \rangle = \langle e_2, V\rho' \rangle$. We prove this by algebraic general recursion:

**Basis step:** Each path sends $v$ to $vr$.

**Recursive step:** Let $p = p_1 \cdots p_n \omega'$ with both paths agreeing on $p_i$.

Let $\alpha, \beta: V \longrightarrow VT$ satisfy $v_1 \alpha = [v_1 \cdots v_n \omega']$, $v_i \beta = [p_i]$. Then $\langle v_1, \alpha \circ' \beta \rangle = [p]$ by 2.10. Then

$$
\begin{aligned}
\langle [p], \Gamma^{-1}.r^{\#} \rangle
&= \langle v_1, (\alpha\Gamma^{-1}) \circ (\beta\Gamma^{-1}) \rangle r^{\#} \\
&= \langle [v_1 \cdots v_n \omega'] \Gamma^{-1}, (\beta\Gamma^{-1}.r^{\#})^{\#} \rangle \quad \text{(use 2.5)} \\
&= (\langle v_1, \beta\Gamma^{-1}.r^{\#} \rangle, \ldots, \langle v_n, \beta\Gamma^{-1}.r^{\#} \rangle) \delta'_{\omega'} \quad \text{(by 2.22)} \\
&= (p_1 r^{\#\#\#}, \ldots, p_n r^{\#\#\#}) \delta'_{\omega'} \\
&= p r^{\#\#\#}.
\end{aligned}
$$

The remaining details of the proof that 2.18 holds are easy: if $f: (X, \delta) \longrightarrow (Y, \gamma)$ is an $\Omega$-homomorphism between $(\Omega, E)$-algebras, then $r^{\#}.f$ satisfies the necessary condition.

This theorem is a "folklore theorem" which has not, to the author's knowledge, appeared in print before (however, see Felscher '72, 2.1.8, 2.3.2). More general clone homomorphisms will appear in 3.2.8.
