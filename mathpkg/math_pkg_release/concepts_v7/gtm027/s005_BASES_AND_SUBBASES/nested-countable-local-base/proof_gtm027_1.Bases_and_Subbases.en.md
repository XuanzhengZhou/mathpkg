---
role: proof
locale: en
of_concept: nested-countable-local-base
source_book: gtm027
source_chapter: "1"
source_section: "Bases and Subbases"
---

# Proof of Nested Countable Local Base

**Proposition.** If $U_1, U_2, \ldots, U_n, \ldots$ is a countable local base at a point $x$, then there exists a new countable local base $V_1, V_2, \ldots, V_n, \ldots$ at $x$ such that $V_n \supset V_{n+1}$ for each $n$.

**Proof.** Let $U_1, U_2, \ldots$ be a countable local base at $x$. Define $V_n = \bigcap \{U_k : k \leq n\}$ for each $n \in \mathbb{N}$.

Each $V_n$ is a neighborhood of $x$ because it is a finite intersection of neighborhoods of $x$. Moreover, $V_{n+1} = \bigcap \{U_k : k \leq n+1\} \subset \bigcap \{U_k : k \leq n\} = V_n$, so $V_n \supset V_{n+1}$.

To verify that $\{V_n\}_{n=1}^{\infty}$ is a local base at $x$: let $W$ be any neighborhood of $x$. Since $\{U_k\}$ is a local base, there exists $k$ such that $U_k \subset W$. Then $V_k = \bigcap_{i=1}^{k} U_i \subset U_k \subset W$. Hence every neighborhood of $x$ contains some $V_n$, and $\{V_n\}$ is therefore a nested countable local base at $x$. $\square$