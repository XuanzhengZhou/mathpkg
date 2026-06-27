---
role: proof
locale: en
of_concept: idempotent-closed-subsemigroup
source_book: gtm026
source_chapter: "4"
source_section: "1"
---

*Proof.* Let $F$ be a nonempty closed subsemigroup of $M$ (so $FF \subset F$). By Zorn's lemma (using compactness of $M$ and continuity of multiplication), $F$ possesses a minimal closed subsemigroup $S$. For any $p$ in $S$, we have $\emptyset \neq pS \subset S$, and $(pS)(pS) \subset pSSS \subset pS$. Since $pS$ is closed (as left multiplication is a homeomorphism), minimality of $S$ forces $pS = S$. Hence there exists $u$ in $S$ with $pu = p$.

Set $R = \{s \in S : us = u\}$. $R$ is a closed subsemigroup of $S$, nonempty (it contains $u$ since $p = pu$ implies $puu = pu$, and one can verify $uu = u$), and by minimality $R = S$. Thus $u \in R$, so $uu = u$, and $u$ is an idempotent. $\square$
