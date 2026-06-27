---
role: proof
locale: en
of_concept: ratio-approximation-for-return-with-excursion
source_book: gtm034
source_chapter: "VII"
source_section: "32"
---

Take $\epsilon = \epsilon_1^2$ in P6 and choose $M$ accordingly. P6 implies that for every $\delta > 0$ and sufficiently large $n$, $\sum_{k=1}^{n-M} P[\{|S_k| \leq A \text{ or } S_{k+j} \neq S_k \text{ for } m \leq j \leq M\} \cap \{T=n\}] \leq (\epsilon_1^2 + \delta)nF_n$. Hence at least $\epsilon_1 n$ values of $k$ satisfy $P[\{|S_k| \leq A \text{ or } S_{k+j} \neq S_k\} \cap \{T=n\}] \leq \epsilon_1 F_n$. Selecting such a $k$, the complementary event gives $q_n$ close to $F_n$, yielding $(1-\epsilon_1)F_n \leq q_n \leq F_n$ for large $n$.
