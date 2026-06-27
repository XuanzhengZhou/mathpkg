---
role: proof
locale: en
of_concept: tangent-space-vector-space-structure
source_book: gtm014
source_chapter: "1"
source_section: "3"
---

**Proof.**

Let $\phi, \psi$ be charts with $p \in \operatorname{dom} \phi \cap \operatorname{dom} \psi$. Then for any $v \in \mathbf{R}^n$, the curve $c_v(t) = \phi^{-1}(\phi(p) + t v)$ satisfies
$$
\lambda_\phi^p(v) = [c_v].
$$
Similarly, $\lambda_\psi^p$ maps $\mathbf{R}^n$ to $T_p X$. The relationship between these two identifications is given by
$$
(\lambda_\psi^p)^{-1} \circ \lambda_\phi^p = d(\psi \circ \phi^{-1})_{\phi(p)} \colon \mathbf{R}^n \to \mathbf{R}^n.
$$
Indeed, for $v \in \mathbf{R}^n$, the curve $c = \phi^{-1}(\phi(p) + t v)$ has $(d\phi \cdot c)_0 = v$, and applying $\psi$ gives
$$
(d\psi \cdot c)_0 = d(\psi \circ \phi^{-1})_{\phi(p)}(v).
$$
Thus $[c]$ is mapped by $(\lambda_\psi^p)^{-1}$ to $d(\psi \circ \phi^{-1})_{\phi(p)}(v)$, establishing the formula.

The map $d(\psi \circ \phi^{-1})_{\phi(p)}$ is a linear automorphism of $\mathbf{R}^n$ (it is the derivative of a diffeomorphism between open subsets of $\mathbf{R}^n$). Therefore, if $\lambda_\phi^p$ were linear under some vector space structure on $T_p X$, then $\lambda_\psi^p = \lambda_\phi^p \circ (d(\psi \circ \phi^{-1})_{\phi(p)})^{-1}$ would also be linear.

Define the vector space structure on $T_p X$ by transporting the structure from $\mathbf{R}^n$ via $\lambda_\phi^p$ for some fixed chart $\phi$: for $\alpha, \beta \in T_p X$ and $a \in \mathbf{R}$,
$$
\alpha + \beta = \lambda_\phi^p\bigl((\lambda_\phi^p)^{-1}(\alpha) + (\lambda_\phi^p)^{-1}(\beta)\bigr), \qquad
a \alpha = \lambda_\phi^p\bigl(a (\lambda_\phi^p)^{-1}(\alpha)\bigr).
$$
By the transition formula above, this definition is independent of the choice of chart $\phi$, and every chart map $\lambda_\psi^p$ becomes a linear isomorphism. Conversely, any vector space structure on $T_p X$ making all $\lambda_\psi^p$ linear isomorphisms must coincide with this one, proving uniqueness.
