---
role: proof
locale: en
of_concept: adjoint-action-via-conjugation
source_book: gtm021
source_chapter: "9"
source_section: "Lie Algebras and Tangent Spaces"
---
Under the isomorphism $\theta$, we need to show that for $\delta \in \mathcal{L}(G)$,
$$\theta(\rho_x \delta \rho_x^{-1}) = \operatorname{Ad} x (\theta(\delta)).$$

First note that $\rho_x \delta \rho_x^{-1}$ is indeed left invariant: since $\lambda_y$ and $\rho_x$ commute for all $y, x \in G$,
$$\lambda_y (\rho_x \delta \rho_x^{-1}) = \rho_x \lambda_y \delta \rho_x^{-1} = \rho_x \delta \lambda_y \rho_x^{-1} = (\rho_x \delta \rho_x^{-1}) \lambda_y.$$

Now evaluate at the identity:
\begin{align*}
\theta(\rho_x \delta \rho_x^{-1})(f) &= (\rho_x \delta \rho_x^{-1} f)(e) \\
&= \delta(\rho_x^{-1} f)(x).
\end{align*}
On the other hand,
$$\operatorname{Ad} x(\theta(\delta))(f) = \theta(\delta)(f \circ \operatorname{Int} x) = \delta(f \circ \operatorname{Int} x)(e).$$
The equality of these expressions follows from the identity
$$(f \circ \operatorname{Int} x)(y) = f(xyx^{-1}) = (\lambda_x \rho_{x^{-1}} f)(y),$$
together with left invariance of $\delta$ and the commutativity of right and left translations.
