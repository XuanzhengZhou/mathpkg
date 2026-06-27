---
role: proof
locale: en
of_concept: rasiowa-sikorski-theorem
source_book: gtm008
source_chapter: "2"
source_section: "Generic Sets"
---

**Proof.** Without loss of generality, assume $(\forall n \in \omega)[0 \notin A_n \land b_n \neq 0]$. Let $\leq$ be the natural order on $B$ and $P = |B| - \{0\}$, so $P = \langle P, \leq \rangle$ is a partial order structure.

For each $n \in \omega$, define $S_n = \{p \in P \mid p \leq -b_n \lor (\exists a \in A_n)[p \leq a]\}$. Then $S_n$ is dense in $P$: for any $p \in P$, either $p \leq -b_n$ (in which case $p \in S_n$), or $p \not\leq -b_n$, meaning $p b_n \neq 0$, i.e., $p \sum_{a \in A_n} a = \sum_{a \in A_n} pa \neq 0$, so there exists $a \in A_n$ with $pa \neq 0$, implying $[p] \cap [a] \neq 0$ and hence $[p] \cap S_n \neq 0$.

Since the family $\{S_n \mid n \in \omega\}$ is countable, by the countable existence theorem for generic sets, there exists $G \subseteq P$ that is $P$-generic over $\{S_n \mid n \in \omega\}$ and contains $a_0$. Then $G$ is a filter for $B$ and a proper filter (since $0 \notin G$).

By Theorem 2.12, $G$ extends to an ultrafilter $F$. Define $h(b) = 1$ if $b \in F$, and $h(b) = 0$ otherwise. Then $h$ is a homomorphism from $B$ onto $2$. Since $a_0 \in F$, $h(a_0) = 1$.

For each $n$, $S_n \cap F \neq 0$, so there exists $p \in F$ with $p \leq -b_n$ or $p \leq a$ for some $a \in A_n$. If $p \leq -b_n$, then $1 = h(p) = h(-b_n) = -h(b_n)$, so $h(b_n) = 0$, and since $(\forall a \in A_n)[h(a) \leq h(b_n) = 0]$, we have $\sum_{a \in A_n} h(a) = 0 = h(b_n)$. If $p \leq a$ for some $a \in A_n$, then $1 = h(p) \leq h(a) \leq \sum_{a \in A_n} h(a) \leq h(b_n)$, so $h(b_n) = 1 = \sum_{a \in A_n} h(a)$.
