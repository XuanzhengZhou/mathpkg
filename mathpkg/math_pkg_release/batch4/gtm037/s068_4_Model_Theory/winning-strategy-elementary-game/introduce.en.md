---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Definition 26.11 formalizes the Ehrenfeucht-Fraisse game of length $m$ between two structures $\mathfrak{A}$ and $\mathfrak{B}$. Player I chooses elements from either structure at each of the $m$ rounds, and Player II must respond with an element from the other structure. The function $F$ encodes Player II's strategy: given the play history (the $k$-tuples chosen so far from each structure) and Player I's latest move, $F$ determines Player II's response. Condition (ii) requires that after $m$ rounds, regardless of how Player I plays (encoded by the sequence $z$), the resulting $m$-tuples $x$ and $y$ form a partial isomorphism -- meaning they satisfy the same atomic formulas. A winning strategy for Player II thus witnesses that the two structures are indistinguishable by sentences of quantifier rank at most $m$.
