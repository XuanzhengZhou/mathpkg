---
role: proof
locale: en
of_concept: generic-set-existence
source_book: gtm001
source_chapter: "18"
source_section: "18.2"
---

Since $M$ is countable, we can enumerate all dense subsets of $P$ in $M$, say $D_1, D_2, \ldots$. We then define $p_{n+1}$ by induction on $n$ such that

$$p_{n+1} \in D_{n+1} \land p_{n+1} \leq p_n.$$

This is possible because each $D_{n+1}$ is dense in $P$. Let $G = \{q \in P \mid (\exists n)[p_n \leq q]\}$. Then $G$ is $\mathcal{P}$-generic: (1) any two conditions in $G$ have a common strengthening (take the $p_n$ with larger index), (2) $G$ is upward closed by definition, and (3) $G$ meets each $D_n$ because $p_n \in D_n$.
