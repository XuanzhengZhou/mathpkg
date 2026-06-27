---
role: proof
locale: en
of_concept: elementary-embedding-lkappa
source_book: gtm001
source_chapter: "17"
source_section: "17.4"
---

**Case** $\text{cf}(\kappa) = \omega$: We construct $Z$, an elementary submodel of $L_\kappa$, such that $X \subseteq Z$, $\overline{Z} = \overline{X}$, and if $\Pi \subseteq Z$ is a $Z$-well-founded $\kappa$-direct limit system, then $\Pi$ is well-founded. Let $Z = \bigcup_{\alpha < \aleph_1} Z_\alpha$ where the $Z_\alpha$ form a continuous increasing chain of elementary submodels. Then $Z \prec L_\kappa$, $X \subseteq Z$, and $\overline{Z} = \overline{X}$. If $\Pi \subseteq Z$ is a countable $Z$-well-founded system, then $\Pi \subseteq Z_\alpha$ for some $\alpha$, and if $\Pi$ were not well-founded it would not be $Z_{\alpha+1}$-well-founded, contradicting $Z$-well-foundedness.

**Case** $\text{cf}(\kappa) > \omega$: We assume $X$ is closed and unbounded in $\kappa$. Let $S = \{\lambda \in X \mid \text{cf}(\lambda) = \omega\}$. The construction proceeds by building $Z$ through a careful closing-off that handles all $\lambda$-direct limit systems for $\lambda \in S$. Lemma 17.27 provides the necessary extension step.
