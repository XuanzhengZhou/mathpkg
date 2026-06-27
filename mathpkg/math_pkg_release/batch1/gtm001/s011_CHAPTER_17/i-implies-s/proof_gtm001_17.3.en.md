---
role: proof
locale: en
of_concept: i-implies-s
source_book: gtm001
source_chapter: "17"
source_section: "17.3"
---

We prove the contrapositive $\neg S \rightarrow \neg I$. Let $h: L_{\bar{\kappa}} \rightarrow L_\kappa$ be as in Lemma 17.23. By Lemma 17.22, $h \upharpoonright \bar{\kappa}$ is not the identity. Let $\bar{\mu}$ be an arbitrary limit ordinal with $\bar{\mu} \geq \bar{\kappa}$.

Claim: $(\forall \bar{\eta} < \bar{\mu})(\forall \bar{\alpha} < \bar{\kappa})(\forall \bar{Q} \subseteq \bar{\eta}) [\bar{Q} \text{ is finite} \rightarrow o(M^{\bar{\eta}}(\bar{\alpha} \cup \bar{Q})) < \bar{\kappa}]$.

From this claim and Lemma 17.13, there exists a well-founded $\bar{\kappa}$-direct limit system $\bar{\Pi}$ with $\bar{\mu}$ as its limit. By Lemma 17.23, $h(\bar{\Pi})$ is also well-founded, and by Lemma 17.16 its limit map provides a medium $M$-map on a regular cardinal that is not the identity. Hence $\neg I$.
