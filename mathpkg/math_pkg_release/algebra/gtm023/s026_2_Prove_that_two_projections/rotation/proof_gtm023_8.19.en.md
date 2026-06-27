---
role: proof
locale: en
of_concept: rotation
source_book: gtm023
source_chapter: "8"
source_section: "8.19"
---

The isometry property of a rotation $\varphi$ implies $(\varphi x, \varphi y) = (x, y)$ for all $x, y \in E$. From formula (8.36), $\tilde{\varphi} = \varphi^{-1}$. Taking determinants of both sides yields $\det \tilde{\varphi} = \det \varphi^{-1}$. Since $\det \tilde{\varphi} = \det \varphi$ and $\det \varphi^{-1} = (\det \varphi)^{-1}$, we obtain $(\det \varphi)^2 = 1$, so $\det \varphi = \pm 1$.

For an eigenvalue: if $\varphi e = \lambda e$ with $e \neq 0$, then $|e|^2 = (\varphi e, \varphi e) = (\lambda e, \lambda e) = |\lambda|^2 |e|^2$, whence $|\lambda| = 1$.

The set of all rotations forms the general orthogonal group; proper rotations ($\det = +1$) form the special orthogonal group, a subgroup since $\det(\varphi_2 \circ \varphi_1) = \det \varphi_2 \cdot \det \varphi_1$.

For a stable subspace $F \subset E$ under a rotation $\varphi$, the orthogonal complement $F^\perp$ is also stable: if $z \in F^\perp$, then for any $y \in F$, $(\varphi z, y) = (z, \varphi^{-1} y) = 0$, since $\varphi^{-1} y \in F$. Thus $\varphi z \in F^\perp$.
