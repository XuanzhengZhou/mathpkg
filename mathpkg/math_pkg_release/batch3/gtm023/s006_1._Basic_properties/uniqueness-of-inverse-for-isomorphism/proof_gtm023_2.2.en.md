---
role: proof
locale: en
of_concept: uniqueness-of-inverse-for-isomorphism
source_book: gtm023
source_chapter: "2"
source_section: "§2. Operations with linear mappings, 2.11"
---
The relation $\varphi^{-1} \circ \varphi = \iota_E$ and $\varphi \circ \varphi^{-1} = \iota_F$ shows that $\varphi^{-1}$ is both a left and right inverse to $\varphi$.

Now let $\psi$ be any left inverse of $\varphi$, so $\psi \circ \varphi = \iota_E$. Multiplying (composing) by $\varphi^{-1}$ on the right gives
$$\psi \circ \varphi \circ \varphi^{-1} = \iota_E \circ \varphi^{-1} = \varphi^{-1},$$
hence $\psi = \varphi^{-1}$.

Similarly, if $\psi$ is any right inverse of $\varphi$, so $\varphi \circ \psi = \iota_F$, then composing with $\varphi^{-1}$ on the left yields $\varphi^{-1} \circ \varphi \circ \psi = \varphi^{-1} \circ \iota_F$, hence $\psi = \varphi^{-1}$. Thus the only left inverse and the only right inverse of $\varphi$ are both equal to $\varphi^{-1}$.
