---
role: proof
locale: en
of_concept: isomorphism-regular-open-algebras-dense
source_book: gtm008
source_chapter: "22"
source_section: "The Completion of a Boolean Algebra"
---

For $b_0 \in B_0$, define $i(b_0) = b_0^{-0}$ (the interior of the closure of $b_0$ in $X$). Then $i: B_0 \rightarrow B$, and by Theorem 22.2, $b_0 = i(b_0) \cap S$.

Let $b \in B$. Since $b \cap S$ is regular open in $S$ (by Theorem 22.4), we have $i(b \cap S) = (b \cap S)^{-0} = b$. Therefore $i$ is onto.

The map $i$ is one-to-one by Theorem 22.2: if $i(b_0) = i(b_0')$, then $b_0 = i(b_0) \cap S = i(b_0') \cap S = b_0'$.

By Theorem 22.3, $i$ preserves the ordering $\leq$, hence $i$ is a Boolean algebra isomorphism.
