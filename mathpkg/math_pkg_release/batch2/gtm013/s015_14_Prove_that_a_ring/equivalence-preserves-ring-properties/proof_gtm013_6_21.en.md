---
role: proof
locale: en
of_concept: equivalence-preserves-ring-properties
source_book: gtm013
source_chapter: "6"
source_section: "21"
---

**Semisimple**: A ring is semisimple iff every left module is semisimple. By (21.8.1), $F$ preserves the semisimple property for each module, so if every $R$-module is semisimple, then every $S$-module (being isomorphic to $F(M)$ for some $R$-module $M$) is also semisimple. This matches the characterization in (13.9).

**Left artinian/noetherian**: By (10.19) and (10.20), a ring is left artinian (noetherian) iff each of its finitely generated left modules is artinian (noetherian). By (21.8.2) and (21.8.3), $F$ preserves finite generation and the chain conditions. Since $F$ is an equivalence, it hits every $S$-module up to isomorphism, so the property transfers.

**Primitive**: $R$ is primitive iff it has a faithful simple left module. By (21.8.1), $F$ preserves simplicity, and by (21.5.4), $F$ preserves faithfulness. Thus if $R$ has a faithful simple module $M$, then $F(M)$ is a faithful simple $S$-module.

**Zero radical**: $J(R) = 0$ iff $R$ has a faithful semisimple module (see exercises). As above, faithfulness and semisimplicity are both preserved by $F$.
