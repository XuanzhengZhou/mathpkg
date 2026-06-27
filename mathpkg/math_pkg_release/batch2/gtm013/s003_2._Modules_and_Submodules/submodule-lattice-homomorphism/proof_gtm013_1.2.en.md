---
role: proof
locale: en
of_concept: submodule-lattice-homomorphism
source_book: gtm013
source_chapter: "1"
source_section: "2"
---

If $S'$ is a subring of $S$, the inclusion map $i_{S'}: S' \to S$ induces an $S'$-module structure on each $S$-module $M$ via $(s', x) \mapsto s' x = i_{S'}(s') x$. Thus with each $S$-module $_S M$ and ring homomorphism $\phi: R \to S$, we obtain four modules: $_S M$, $_R M$, $_{\phi(R)} M$, and $_{\mathbb{Z}} M$.

Each submodule of any one of these is a submodule of each subsequent one: an $S$-submodule is automatically an $R$-submodule (since $r x = \phi(r) x$), which is the same as a $\phi(R)$-submodule (since the scalar actions coincide), which is simply an additive subgroup and hence a $\mathbb{Z}$-submodule. Since the meet and join of submodules are just intersection and sum, the submodule lattice of each is a sublattice of that of the subsequent modules. The equality $\mathcal{S}(_R M) = \mathcal{S}(_{\phi(R)} M)$ holds because the scalar actions of $R$ and $\phi(R)$ coincide via the identification $r x = \phi(r) x$.
