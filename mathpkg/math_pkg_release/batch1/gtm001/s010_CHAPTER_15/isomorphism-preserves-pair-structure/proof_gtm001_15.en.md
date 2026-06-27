---
role: proof
locale: en
of_concept: isomorphism-preserves-pair-structure
source_book: gtm001
source_chapter: "15"
source_section: ""
---

**Proof.** (1) $\{x, y\} \in F''(b \cap \eta) \rightarrow x, y \in F''(b \cap \eta)$ (Lemma 8). Since $H$ is an order isomorphism, $H'x, H'y \in H'\{x, y\}$, so $\{H'x, H'y\} \subseteq H'\{x, y\}$. By cardinality, equality holds.

(2) $H' \langle x, y \rangle = H' \{ \{x\}, \{x, y\} \} = \{ H' \{x\}, H' \{x, y\} \} = \langle H'x, H'y \rangle$.

(4) For $Q_4$: if $\langle x, y \rangle \in Q_4$, then $(\exists z)[y = \langle x, z \rangle]$. By Lemma 8, $x, z \in F''(b \cap \eta)$, so $H'y = \langle H'x, H'z \rangle$, giving $\langle H'x, H'y \rangle \in Q_4$. Converse by symmetry using $H^{-1}$.
