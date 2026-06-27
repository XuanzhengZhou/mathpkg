---
role: proof
locale: en
of_concept: r1-is-elementary
source_book: gtm037
source_chapter: "4. Recursive Function Theory"
source_section: "4.1"
---

**Proof.** $(m, n, p, q) \in R_1$ iff $m, n, p, q$ are Gödel numbers of words and
$$\operatorname{Cat}(\operatorname{Cat}(m, n), p) = q,$$
and moreover there is no decomposition with a shorter prefix: for any $m', n', p'$ that are Gödel numbers of words with $\operatorname{Cat}(\operatorname{Cat}(m', n'), p') = q$ and $n' = n$, it must be that $m'$ is not a proper prefix of $m$ (i.e., $\neg \exists r \leq q\ [\operatorname{Cat}(m', r) = m \land r > 0]$). Since $\operatorname{Cat}$ is elementary and all quantifiers range over values bounded by $q$, the relation $R_1$ is elementary.
