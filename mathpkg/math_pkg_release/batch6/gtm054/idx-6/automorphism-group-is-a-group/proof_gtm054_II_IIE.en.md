---
role: proof
locale: en
of_concept: automorphism-group-is-a-group
source_book: gtm054
source_chapter: "II Algebraic Structures on Finite Sets"
source_section: "IIE The Automorphism Groups of Systems"
---

The set $G(\Lambda)$ is equipped with the operation of componentwise composition $(p_2, q_2)(p_1, q_1) = (p_2p_1, q_2q_1)$. We verify the group axioms:

1. **Closure**: If $(p_1, q_1), (p_2, q_2) \in G(\Lambda)$, then for all $e \in E$,
   $$q_2q_1[f(e)] = q_2[f(p_1(e))] = f(p_2(p_1(e))) = f((p_2p_1)(e)),$$
   so $(p_2p_1, q_2q_1) \in G(\Lambda)$.

2. **Associativity**: Follows from associativity of permutation composition in $\Pi(E)$ and $\Pi(V)$.

3. **Identity**: $(1_E, 1_V) \in G(\Lambda)$ since $1_V[f(e)] = f(e) = f(1_E(e))$ for all $e$.

4. **Inverses**: If $(p, q) \in G(\Lambda)$, then $q[f(e)] = f(p(e))$ for all $e$. Applying $q^{-1}$ to both sides and replacing $e$ by $p^{-1}(e)$ yields $q^{-1}[f(e)] = f(p^{-1}(e))$, so $(p^{-1}, q^{-1}) \in G(\Lambda)$ and $(p^{-1}, q^{-1})(p, q) = (1_E, 1_V)$.

Thus $G(\Lambda)$ is a group.
