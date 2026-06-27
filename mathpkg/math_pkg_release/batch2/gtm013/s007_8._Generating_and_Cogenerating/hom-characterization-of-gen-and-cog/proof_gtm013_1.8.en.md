---
role: proof
locale: en
of_concept: hom-characterization-of-gen-and-cog
source_book: gtm013
source_chapter: "1"
source_section: "8"
---

If $U$ generates $M$, there is an epimorphism $h: U^{(A)} \to M \to 0$. Let $H = \{h \circ \iota_\alpha \mid \alpha \in A\}$ where $\iota_\alpha: U \to U^{(A)}$ are the natural injections. Then $M = \Sigma_{f \in H} \mathrm{Im}\, f$, and $H \subseteq \mathrm{Hom}_R(U, M)$ is finite if $A$ is finite.

Conversely, given a (finite) subset $H \subseteq \mathrm{Hom}_R(U, M)$ with $M = \Sigma_{h \in H} \mathrm{Im}\, h$, the direct sum $\bigoplus_{h \in H} h: U^{(H)} \to M$ is an epimorphism, so $U$ (finitely) generates $M$.
