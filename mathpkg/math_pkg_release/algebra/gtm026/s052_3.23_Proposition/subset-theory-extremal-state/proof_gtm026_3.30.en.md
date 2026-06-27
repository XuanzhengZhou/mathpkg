---
role: proof
locale: en
of_concept: subset-theory-extremal-state
source_book: gtm026
source_chapter: "3"
source_section: "3.30"
---

The proof is essentially the same in all cases. A finitely-generated $\mathbf{T}$-algebra $(\bar{Q}, \xi)$ is necessarily finite and we may define subsets $S_n, Q_n$ according to the following inductive scheme:

$$S_0 = \langle \emptyset \rangle$$

$Q_n$ is the set of minimal elements of $\bar{Q} - S_n$ if $S_n \neq \bar{Q}$, and need not be defined if $S_n = \bar{Q}$.

$$S_{n+1} = \langle S_n \cup Q_n \rangle$$

Then each $q \in Q_n$ is isolated, and $\bigcup Q_n$ generates $\bar{Q}$, so $\mathbf{T}$ is extremal state.
