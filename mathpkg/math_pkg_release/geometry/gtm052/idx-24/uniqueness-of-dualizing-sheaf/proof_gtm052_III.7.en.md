---
role: proof
locale: en
of_concept: uniqueness-of-dualizing-sheaf
source_book: gtm052
source_chapter: "III"
source_section: "7"
---

Since $\omega'$ is dualizing, we get an isomorphism $\operatorname{Hom}(\omega^\circ, \omega') \cong H^n(\omega^\circ)^\vee$. So there is a unique morphism $\varphi: \omega^\circ \to \omega'$ corresponding to the element $t \in H^n(\omega^\circ)^\vee$, i.e., such that $t' \circ H^n(\varphi) = t$. Similarly, using the fact that $\omega^\circ$ is dualizing, there is a unique morphism $\psi: \omega' \to \omega^\circ$ corresponding to $t' \in H^n(\omega')^\vee$, with $t \circ H^n(\psi) = t'$. The composition $\psi \circ \varphi: \omega^\circ \to \omega^\circ$ satisfies $t \circ H^n(\psi \circ \varphi) = t$. But the identity $\operatorname{id}_{\omega^\circ}$ also satisfies this property, and by the dualizing property of $\omega^\circ$, the map $\operatorname{Hom}(\omega^\circ, \omega^\circ) \to H^n(\omega^\circ)^\vee$ is an isomorphism. Hence $\psi \circ \varphi = \operatorname{id}$. Similarly $\varphi \circ \psi = \operatorname{id}$, so $\varphi$ is an isomorphism.
