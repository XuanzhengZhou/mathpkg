---
role: proof
locale: en
of_concept: closure-of-subspace-is-subspace
source_book: gtm003
source_chapter: "I"
source_section: "2"
---

**Proof.** By axiom $(LT)_1$, the addition map $(x, y) \mapsto x + y$ from $L \times L$ to $L$ is continuous. Since $M$ is a subspace, $M + M \subseteq M$. Taking closures and using continuity of addition, we obtain $\overline{M} + \overline{M} \subseteq \overline{M + M} \subseteq \overline{M}$, so $\overline{M}$ is closed under addition. By axiom $(LT)_2$, for each fixed scalar $\lambda \in K$, the map $x \mapsto \lambda x$ is continuous. Since $\lambda M \subseteq M$, taking closures gives $\lambda \overline{M} \subseteq \overline{\lambda M} \subseteq \overline{M}$. Thus $\overline{M}$ is closed under scalar multiplication. Therefore $\overline{M}$ is a subspace of $L$. $\square$
