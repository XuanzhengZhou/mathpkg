---
role: proof
locale: en
of_concept: canonical-divisor-ruled-surface
source_book: gtm052
source_chapter: "V"
source_section: "2"
---

Let $K \sim aC_0 + bf$. Using the adjunction formula (1.5) for a fibre $f$, we have

$$-2 = f.(f + K) = a.$$

Now we use the adjunction formula for $C_0$ in its invertible sheaf form (II, 8.20), which says that

$$\omega_{C_0} \cong \omega_X \otimes \mathcal{L}(C_0) \otimes \mathcal{O}_{C_0} \cong \mathcal{L}(-C_0 + bf) \otimes \mathcal{O}_{C_0}.$$

Identifying $C_0$ with $C$ via $\pi$, and using the fact that $\omega_C$ corresponds to the canonical divisor
$K_C$ on $C$ of degree $2g - 2$, the restriction gives $\deg \omega_{C_0} = 2g - 2$. On the other hand,
$\mathcal{L}(-C_0 + bf)|_{C_0}$ has degree $(-C_0 + bf).C_0 = -C_0^2 + b = e + b$ (since $C_0^2 = -e$).
Equating: $2g - 2 = e + b$, so $b = 2g - 2 - e$.

Therefore $K \sim -2C_0 + (2g - 2 - e)f$.

This result also follows from (III, Ex. 8.4).
