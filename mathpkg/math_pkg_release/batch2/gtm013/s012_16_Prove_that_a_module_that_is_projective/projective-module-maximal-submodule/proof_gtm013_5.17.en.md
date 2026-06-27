---
role: proof
locale: en
of_concept: projective-module-maximal-submodule
source_book: gtm013
source_chapter: "5"
source_section: "17"
---

**Proof.** Let ${}_R P$ be projective. By (17.3) we may assume there is a free left $R$-module $F$ with $F = P \\oplus P'$. If $P$ contains no maximal submodule, then by (17.10) we have

$$P = JP \\subseteq JF.$$

To prove the proposition we show that this forces $P = 0$. Let $x \\in P$. Let $e$ be an idempotent endomorphism of $F$ such that $Fe = P$ and let $(x_\\alpha)_{\\alpha \\in A}$ be a free basis for $F$. Then for some finite subset of the basis, $x$ is expressed as a finite linear combination. Since $P = JP$, each term lies in $JF$, which leads to a contradiction unless $P = 0$.
