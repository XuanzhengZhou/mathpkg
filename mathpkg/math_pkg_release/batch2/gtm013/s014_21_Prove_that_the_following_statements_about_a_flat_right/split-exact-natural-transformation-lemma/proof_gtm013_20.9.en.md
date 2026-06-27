---
role: proof
locale: en
of_concept: split-exact-natural-transformation-lemma
source_book: gtm013
source_chapter: "20"
source_section: "20.9"
---

Since the sequence is split exact, $M \cong M' \oplus M''$ via the isomorphism $m \mapsto (\iota'(m), \pi(m))$ where $\iota'$ is a splitting map for $\iota$. By (16.2), additive functors preserve split exact sequences, so we obtain commutative diagrams with split exact rows:

$$\begin{CD}
0 @>>> F(M') @>{F(\iota)}>> F(M) @>{F(\pi)}>> F(M'') @>>> 0\\
@. @V{\eta_{M'}}VV @V{\eta_M}VV @V{\eta_{M''}}VV @.\\
0 @>>> G(M') @>{G(\iota)}>> G(M) @>{G(\pi)}>> G(M'') @>>> 0
\end{CD}$$

For the monic case: If $\eta_{M'}$ and $\eta_{M''}$ are monic, then by the Five Lemma (or by the split direct sum decomposition $F(M) \cong F(M') \oplus F(M'')$ and $G(M) \cong G(M') \oplus G(M'')$), $\eta_M \cong \eta_{M'} \oplus \eta_{M''}$ is monic. Conversely, if $\eta_M$ is monic, then the composite $\eta_M \circ F(\iota) = G(\iota) \circ \eta_{M'}$ being monic forces $\eta_{M'}$ to be monic. Similarly, considering the splitting $M'' \to M$, one gets that $\eta_{M''}$ is monic.

The proof for epics is dual.
