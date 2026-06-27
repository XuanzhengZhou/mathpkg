---
role: proof
locale: en
of_concept: suspension-loop-adjunction
source_book: gtm005
source_chapter: "VII"
source_section: "9. Loops and Suspensions"
---

Let $X^{(*)Y}$ denote the subspace of $X^Y$ consisting of all base-point-preserving maps $Y \to X$. Since $X^{(*)Y}$ is a closed subspace of $X^Y$ (the condition $f(*_Y) = *_X$ is a closed condition in a Hausdorff space), and closed subspaces of compactly generated spaces are compactly generated, $X^{(*)Y} \in \mathbf{CGHaus}_*$ with the constant map to $*_X$ as base point.

Now observe that a map $f: Z \mathbin{\square} Y \to X$ in $\mathbf{CGHaus}_*$ satisfies $f(z, *) = *_X = f(*, y)$ for all $z \in Z, y \in Y$ exactly when $f$ collapses the wedge $Z \vee Y = (Z \mathbin{\square} *) \cup (* \mathbin{\square} Y)$ to the base point $*_X$. Such maps factor uniquely through the smash product $Z \wedge Y = (Z \mathbin{\square} Y) /\!/ (Z \vee Y)$. Hence there is a natural bijection
$$\mathbf{CGHaus}_*(Z \wedge Y, X) \cong \{ f \in \mathbf{CGHaus}_*(Z \mathbin{\square} Y, X) \mid f|_{Z \vee Y} = * \}.$$

On the other hand, the cartesian closed structure of $\mathbf{CGHaus}$ gives
$$\mathbf{CGHaus}(Z \mathbin{\square} Y, X) \cong \mathbf{CGHaus}(Z, X^Y).$$
Under this bijection, maps $f$ vanishing on the wedge correspond precisely to maps $\hat{f}: Z \to X^Y$ whose image lies in $X^{(*)Y}$. Thus we obtain the adjunction
$$\mathbf{CGHaus}_*(Z \wedge Y, X) \cong \mathbf{CGHaus}_*(Z, X^{(*)Y}).$$

Specializing to $Y = S^1 = I /\!/ \{0,1\}$ yields $\Sigma X = X \wedge S^1$ and $\Omega X = X^{(*)S^1}$, giving the $\Sigma \dashv \Omega$ adjunction:
$$\mathbf{CGHaus}_*(\Sigma X, Y) \cong \mathbf{CGHaus}_*(X, \Omega Y).$$
