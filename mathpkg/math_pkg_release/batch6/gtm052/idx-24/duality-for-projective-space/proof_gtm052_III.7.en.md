---
role: proof
locale: en
of_concept: duality-for-projective-space
source_book: gtm052
source_chapter: "III"
source_section: "7"
---

(a) It follows from (II, 8.13) that $\omega_X \cong \mathcal{O}_X(-n-1)$ (see II, 8.20.1). Thus (a) follows from (5.1c), which gives the cohomology of $\mathcal{O}_{\mathbf{P}^n}(-n-1)$.

(b) A homomorphism of $\mathcal{F}$ to $\omega$ induces a map of cohomology groups $H^n(X, \mathcal{F}) \to H^n(X, \omega)$. This gives the natural pairing. If $\mathcal{F} \cong \mathcal{O}(q)$ for some $q \in \mathbf{Z}$, then $\operatorname{Hom}(\mathcal{F}, \omega) \cong H^0(X, \omega(-q))$, so the result follows from (5.1d), which establishes the perfect pairing for sheaves $\mathcal{O}(q_i)$. Hence (b) holds also for a finite direct sum of sheaves of the form $\mathcal{O}(q_i)$. For general $\mathcal{F}$, one writes $\mathcal{F}$ as a quotient of such a direct sum and uses the resulting exact sequence together with the five lemma to deduce the perfect pairing.

(c) This follows from (b) by standard homological algebra. Since $\omega_X \cong \mathcal{O}_X(-n-1)$, the natural pairing $\operatorname{Hom}(\mathcal{F}, \omega) \times H^n(X, \mathcal{F}) \to k$ gives an isomorphism $\operatorname{Hom}(\mathcal{F}, \omega) \cong H^n(X, \mathcal{F})^\vee$ for $i=0$. For $i > 0$, one uses the $\delta$-functor properties of $\operatorname{Ext}^i(\cdot, \omega)$ and the fact that both sides form universal $\delta$-functors in $\mathcal{F}$, together with the observation that they agree for $i=0$.
