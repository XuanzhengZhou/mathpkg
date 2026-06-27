---
role: proof
locale: en
of_concept: projective-over-local-ring-free
source_book: gtm013
source_chapter: "5"
source_section: "26"
---

Since $R \cong \operatorname{End}({}_R R)$ by (4.11), and since $R$ is a local ring, the regular module ${}_R R$ has a local endomorphism ring. Moreover, ${}_R R$ is countably generated (in fact, finitely generated).

Now let ${}_R P$ be a projective module over the local ring $R$. Then $P$ is a direct summand of a free module $R^{(A)}$. Write $R^{(A)} = \bigoplus_A R_\alpha$ where each $R_\alpha \cong {}_R R$.

By Theorem (26.5), since each $R_\alpha$ is countably generated and has a local endomorphism ring (being isomorphic to ${}_R R$), every direct summand of $\bigoplus_A R_\alpha$ is itself a direct sum of countably generated submodules, each of which is a direct summand of some $R_\alpha$. But the only direct summands of ${}_R R$ over a local ring are $0$ and ${}_R R$ itself (since $R$ is local, its only idempotents are $0$ and $1$). Therefore each summand is isomorphic to ${}_R R$, and $P$ is a direct sum of copies of ${}_R R$, i.e., $P$ is free.
