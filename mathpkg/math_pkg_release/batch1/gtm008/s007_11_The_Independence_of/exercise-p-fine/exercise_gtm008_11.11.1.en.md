---
role: exercise
locale: en
chapter: "11"
section: "11"
exercise_number: 1
---

Prove that the partial order structure $\mathbf{P}$ of Definition 11.1 is fine in the sense of Definition 5.21.

Recall that a partial order $\mathbf{P}$ is *fine* if for every $p \in P$ and every finite set $\{n_1, \ldots, n_k\} \subseteq \omega$, there exists $q \leq p$ such that for each $i = 1, \ldots, k$, either $q \Vdash n_i \in \tilde{a}(\dot{G})$ or $q \Vdash n_i \notin \tilde{a}(\dot{G})$, where $\dot{G}$ denotes the canonical name for the generic filter.

**Hint:** Given $p = \langle p_1, p_2 \rangle$ and $\{n_1, \ldots, n_k\}$, extend $p$ by adding each $n_i$ to either $p_1$ (forcing $n_i$ into the generic set) or $p_2$ (forcing $n_i$ out), maintaining disjointness. The finiteness of both coordinates ensures this is always possible.
