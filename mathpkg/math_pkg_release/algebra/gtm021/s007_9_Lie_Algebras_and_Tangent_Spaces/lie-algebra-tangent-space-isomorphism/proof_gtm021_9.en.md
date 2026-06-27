---
role: proof
locale: en
of_concept: lie-algebra-tangent-space-isomorphism
source_book: gtm021
source_chapter: "9"
source_section: "Lie Algebras and Tangent Spaces"
---
The inverse $\eta: \mathfrak{g} \to \mathcal{L}(G)$ is defined by right convolution: for $x \in \mathfrak{g}$, $f \in A$,
$$(\eta(x)f)(y) = (f * x)(y) = x(\lambda_{y^{-1}} f).$$

To verify $\eta \circ \theta = \operatorname{id}$: for $\delta \in \mathcal{L}(G)$,
\begin{align*}
(f * \theta(\delta))(x) &= \theta(\delta)(\lambda_{x^{-1}} f) \\
&= \delta(\lambda_{x^{-1}} f)(e) \\
&= \lambda_{x^{-1}} (\delta f)(e) \\
&= (\delta f)(x),
\end{align*}
using left invariance of $\delta$. Thus $\eta(\theta(\delta)) = \delta$.

To verify $\theta \circ \eta = \operatorname{id}$: for $x \in \mathfrak{g}$,
\begin{align*}
\theta(\eta(x))(f) &= (f * x)(e) \\
&= x(\lambda_{e^{-1}} f) \\
&= x(f).
\end{align*}

For the bracket preservation under $d\varphi$: let $x, y \in \mathfrak{g}$, $x' = d\varphi(x)$, $y' = d\varphi(y)$. For $f' \in K[G']$, set $f = \varphi^* f'$. Then
\begin{align*}
[x', y'](f') &= (f' * y' * x')(e) - (f' * x' * y')(e) \\
&= x'(f' * y') - y'(f' * x') \\
&= x(\varphi^*(f' * y')) - y(\varphi^*(f' * x')).
\end{align*}
On the other hand,
$$d\varphi([x,y])(f') = (f * y * x)(e) - (f * x * y)(e) = x(f * y) - y(f * x).$$
Using the identity $\varphi^*(f' * y') = \varphi^* f' * y$ (derived from the compatibility of $\varphi^*$ with convolution), the two expressions coincide. Hence $d\varphi([x,y]) = [d\varphi(x), d\varphi(y)]$.
