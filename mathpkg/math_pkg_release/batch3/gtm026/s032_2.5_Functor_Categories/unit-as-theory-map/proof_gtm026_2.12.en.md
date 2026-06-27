---
role: proof
locale: en
of_concept: unit-as-theory-map
source_book: gtm026
source_chapter: "2"
source_section: "2.12"
---

To verify that $\eta: \mathrm{id}_\mathcal{K} \to T$ is a theory map from the identity theory $(\mathrm{id}_\mathcal{K}, \mathrm{id}, \mathrm{id})$ to $T = (T, \eta, \mu)$, we must check the two commuting diagrams of a theory map:

For the unit condition: $\mathrm{id} \cdot \eta = \eta$, and the unit of the identity theory is $\mathrm{id}: \mathrm{id}_\mathcal{K} \to \mathrm{id}_\mathcal{K}$. The diagram
$$
\begin{CD}
\mathrm{id}_\mathcal{K} @= \mathrm{id}_\mathcal{K} \\
@V{\mathrm{id}}VV @VV{\eta}V \\
\mathrm{id}_\mathcal{K} @>>{\eta}> T
\end{CD}
$$
commutes trivially since the left vertical arrow is the identity.

For the multiplication condition: the multiplication of the identity theory is $\mathrm{id}: \mathrm{id}_\mathcal{K} \cdot \mathrm{id}_\mathcal{K} \to \mathrm{id}_\mathcal{K}$ (also the identity), and we need $\mathrm{id} \cdot \eta = \eta\eta \cdot \mu$, which is exactly the unit law for a monoid: $\eta \cdot \mathrm{id}_T = \mu \cdot (T\eta)$. This follows from the monoid axioms for $(T, \eta, \mu)$.

Under Proposition 2.9, the theory map $\eta$ induces a functor $\mathcal{K}^T \to \mathcal{K}^{\mathrm{id}_\mathcal{K}}$. Since the identity theory has $\mathcal{K}^{\mathrm{id}_\mathcal{K}} \cong \mathcal{K}$, this functor is precisely the forgetful functor $U^T: \mathcal{K}^T \to \mathcal{K}$.
