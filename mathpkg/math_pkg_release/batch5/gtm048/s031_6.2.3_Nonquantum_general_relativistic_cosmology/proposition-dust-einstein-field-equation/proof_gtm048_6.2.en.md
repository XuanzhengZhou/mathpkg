---
role: proof
locale: en
of_concept: proposition-dust-einstein-field-equation
source_book: gtm048
source_chapter: "6"
source_section: "6.2.7"
---

**Proof.** Since $F = 0$, the Einstein field equation $G = T + E$ becomes $\rho_0 du^4 \otimes du^4 + p_0(g + du^4 \otimes du^4) = \rho \omega \otimes \omega$, where $\omega$ is the 1-form physically equivalent to $Z$ and we have used Lemma 6.2.6b. At $x \in M$, choose a nonzero $X \in M_x$ such that $du^4(X) = 0 = \omega(X)$; $X$ is spacelike. Then the preceding equation implies $p_0 g(X, X) = 0$. Since $g(X, X) > 0$, we have $p_0 = 0$. Lemma 6.2.6b then gives $2(\ddot{R}/R) + (\dot{R}/R)^2 = 0$, which integrates to $R(u) = u^{2/3}$ (up to a constant factor that can be absorbed by rescaling the spatial coordinates). Then $\rho_0 = 3(\dot{R}/R)^2 = (4/3)(u^4)^{-2}$. The equality $\rho_0 du^4 \otimes du^4 = \rho \omega \otimes \omega$ forces $Z$ to be proportional to $\partial_4$, and since both are unit timelike future-pointing, $Z = \partial_4$ and $\rho = \rho_0 = (4/3)(u^4)^{-2}$.
