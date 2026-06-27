---
role: proof
locale: en
of_concept: r0-is-elementary
source_book: gtm037
source_chapter: "4. Recursive Function Theory"
source_section: "4.1"
---

**Proof.** $(m, n) \in R_0$ iff $m$ is the Gödel number of a word, $n$ is the Gödel number of a word, and
$$\exists x \leq n\ \exists y \leq n\ [\operatorname{Cat}(\operatorname{Cat}(x, m), y) = n].$$

Here $\operatorname{Cat}$ is the concatenation function for Gödel numbers of words (see 3.30). The condition states that $a$ (with Gödel number $m$) occurs in $b$ (with Gödel number $n$) exactly when $b$ can be obtained by concatenating some prefix word $x$, then $a$, then some suffix word $y$. Since $\operatorname{Cat}$ is elementary and the quantifiers are bounded by $n$, the relation $R_0$ is elementary.
