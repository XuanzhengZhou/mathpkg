---
role: proof
locale: en
of_concept: intersection-union-open-confined-configurations
source_book: gtm006
source_chapter: "XI"
source_section: "2"
---

Both claims follow directly from the definitions.

(i) Suppose all $\mathcal{A}_\alpha$ are open. If $\bigcap_\alpha \mathcal{A}_\alpha$ were not open, it would contain some confined sub-configuration $\mathcal{B}$. But then $\mathcal{B}$ would be a sub-configuration of every $\mathcal{A}_\alpha$ (since $\mathcal{B} < \bigcap_\alpha \mathcal{A}_\alpha$ implies $\mathcal{B} < \mathcal{A}_\alpha$ for each $\alpha$), contradicting the assumption that each $\mathcal{A}_\alpha$ is open.

(ii) Suppose all $\mathcal{A}_\alpha$ are confined. Any element of $\bigcup_\alpha \mathcal{A}_\alpha$ belongs to some particular $\mathcal{A}_\alpha$. Since that $\mathcal{A}_\alpha$ is confined, the element has at least three incidences within $\mathcal{A}_\alpha$, and therefore certainly has at least three incidences within the larger configuration $\bigcup_\alpha \mathcal{A}_\alpha$. Thus every element of the union has at least three incidences, so the union is confined.
