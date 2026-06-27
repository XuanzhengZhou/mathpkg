---
role: proof
locale: en
of_concept: composition-series-chain-conditions
source_book: gtm030
source_chapter: "II"
source_section: "8"
---

**Sufficiency.** Assume that conditions I (DCC) and II (ACC) hold. Set $\mathfrak{G}_1 = \mathfrak{G}$. Since $\mathfrak{G}$ satisfies the ascending chain condition on invariant $M$-subgroups, $\mathfrak{G}_1$ contains a maximal proper invariant $M$-subgroup $\mathfrak{G}_2$. Likewise, $\mathfrak{G}_2$ contains a maximal invariant $M$-subgroup $\mathfrak{G}_3$, and so on. This yields a properly descending sequence
\[
\mathfrak{G} = \mathfrak{G}_1 \supset \mathfrak{G}_2 \supset \mathfrak{G}_3 \supset \cdots
\]
in which each $\mathfrak{G}_{i+1}$ is maximal invariant in the preceding $\mathfrak{G}_i$. By the descending chain condition (I), there exists a finite number $s+1$ such that $\mathfrak{G}_{s+1} = 1$. The chain
\[
\mathfrak{G} = \mathfrak{G}_1 \supset \mathfrak{G}_2 \supset \cdots \supset \mathfrak{G}_{s+1} = 1
\]
is then a composition series for $\mathfrak{G}$.

**Necessity.** Let $\mathfrak{G}$ possess a composition series
\[
\mathfrak{G} = \mathfrak{G}_1 \supset \mathfrak{G}_2 \supset \cdots \supset \mathfrak{G}_{s+1} = 1
\]
and let
\[
\mathfrak{H}_1 \supset \mathfrak{H}_2 \supset \cdots
\]
be a properly descending sequence of $M$-subgroups such that $\mathfrak{H}_1$ is invariant in $\mathfrak{G}$ and $\mathfrak{H}_{i+1}$ is invariant in $\mathfrak{H}_i$ for $i \geq 1$. We assert that the number of terms $\mathfrak{H}_i$ does not exceed $s+1$. For if it did, then
\[
\mathfrak{G} \supseteq \mathfrak{H}_1 \supset \mathfrak{H}_2 \supset \cdots \supset \mathfrak{H}_{s+2} \supseteq 1
\]
would be a normal series. By Schreier's theorem, there exists a refinement of this series that is equivalent to a refinement of the given composition series. Dropping duplicates yields a refinement of the $\mathfrak{H}$-series that is itself a composition series. But this refined series would contain more than $s+1$ terms, contradicting the Jordan-Hölder theorem. Hence condition I (DCC) holds.

A similar argument, using the ascending chain of $M$-subgroups in place of the descending one, establishes condition II (ACC).
