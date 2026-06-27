---
role: proof
locale: en
of_concept: equivalence-preserves-exact-sequences
source_book: gtm013
source_chapter: "6"
source_section: "21"
---

It suffices to prove one direction by symmetry. The split case follows immediately because $F$ is additive. Let

$$0 \to M' \xrightarrow{f} M \xrightarrow{g} M'' \to 0$$

be exact in ${}_R \mathbf{M}$. By (21.2), $F(f)$ is monic, $F(g)$ is epic, and $F(g)F(f) = F(gf) = F(0) = 0$. Thus $\operatorname{Im} F(f) \subseteq \operatorname{Ker} F(g)$. It remains to prove $\operatorname{Ker} F(g) \subseteq \operatorname{Im} F(f)$.

Let $K = \operatorname{Ker} F(g)$ and let $i_K: K \to F(M)$ be the inclusion map. Consider $\phi(i_K): G(K) \to M$, where $\phi$ is the isomorphism from (21.3). By (21.3.1),

$$g \circ \phi(i_K) = \phi(F(g) \circ i_K) = \phi(0) = 0.$$

Thus $\operatorname{Im} \phi(i_K) \subseteq \operatorname{Ker} g = \operatorname{Im} f$. By the Factor Theorem, there exists $\bar{\gamma} \in \operatorname{Hom}_R(G(K), M')$ such that $f \circ \bar{\gamma} = \phi(i_K)$.

Now applying $\phi^{-1}$ via (21.3.3):

$$i_K = \phi^{-1}(f \circ \bar{\gamma}) = F(f) \circ \phi^{-1}(\bar{\gamma}).$$

Therefore $\operatorname{Ker} F(g) = \operatorname{Im} i_K \subseteq \operatorname{Im} F(f)$, completing the proof.
