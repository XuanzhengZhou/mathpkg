---
role: proof
locale: en
of_concept: properties-of-j0-ordinal-pairing
source_book: gtm001
source_chapter: "15"
source_section: ""
---

**Proof.** (1) If $(\forall \alpha)[F' \alpha \triangleq J'_0 \langle 0, \alpha \rangle]$ then $F$ is a strictly monotonic ordinal function and hence $\alpha \leq F' \alpha$. In particular if $\gamma = \max(\alpha, \beta)$ then $\max(\alpha, \beta) = \gamma \leq F' \gamma = J'_0 \langle 0, \gamma \rangle$. But $\langle 0, \gamma \rangle R_0 \langle \alpha, \beta \rangle \lor \langle 0, \gamma \rangle = \langle \alpha, \beta \rangle$. Therefore $J'_0 \langle 0, \gamma \rangle \leq J'_0 \langle \alpha, \beta \rangle$.

(2) If $J'_0 \langle \alpha, \beta \rangle < \aleph_0$ then done. If $J'_0 \langle \alpha, \beta \rangle \geq \aleph_0$, then since order isomorphisms map initial segments onto initial segments, $J'_0 \langle \alpha, \beta \rangle \simeq (R_0^{-1})' \{ \langle \alpha, \beta \rangle \}$. Consequently $\overline{(R_0^{-1})' \{ \langle \alpha, \beta \rangle \}} < \aleph_\gamma$, so $\overline{J'_0 \langle \alpha, \beta \rangle} < \aleph_\gamma$, hence $J'_0 \langle \alpha, \beta \rangle < \aleph_\gamma$.
