---
role: proof
locale: en
of_concept: dust-in-simple-cosmological-spacetime
source_book: gtm048
source_chapter: "6"
source_section: "6.2.7"
---

Since $F = 0$, the Einstein field equation $G = T + E$ becomes
$$\rho_0 \, du^4 \otimes du^4 + p_0(g + du^4 \otimes du^4) = \rho \, \omega \otimes \omega,$$
where $\omega$ is the 1-form physically equivalent to $Z$ and we have used Lemma 6.2.6b.

At $x \in M$, choose a nonzero $X \in M_x$ such that $du^4(X) = 0 = \omega(X)$; then $X$ is spacelike. Applying the preceding equation to $(X, X)$:
$$\rho_0 [du^4(X)]^2 + p_0\bigl(g(X,X) + [du^4(X)]^2\bigr) = \rho [\omega(X)]^2.$$

Since $du^4(X) = 0$ and $\omega(X) = 0$, this reduces to $p_0 \, g(X, X) = 0$. Because $X$ is spacelike, $g(X, X) < 0$, hence $p_0 = 0$.

Thus the Einstein field equation simplifies to
$$\rho_0 \, du^4 \otimes du^4 = \rho \, \omega \otimes \omega.$$

A routine verification using this equation and the definition of the comoving frame in Section 6.2.5 then shows that $Z = \partial_4$ and $\rho = \rho_0$. Substituting $p_0 = 0$ into the expression for the Einstein tensor of a simple cosmological spacetime yields $\rho_0 = \frac{4}{3}(u^4)^{-2}$, and hence $\rho = \frac{4}{3}(u^4)^{-2}$.
