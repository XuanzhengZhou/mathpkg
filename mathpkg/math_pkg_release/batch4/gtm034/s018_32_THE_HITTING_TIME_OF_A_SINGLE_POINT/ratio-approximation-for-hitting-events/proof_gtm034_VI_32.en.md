---
role: proof
locale: en
of_concept: ratio-approximation-for-hitting-events
source_book: gtm034
source_chapter: "VI"
source_section: "32"
---

Take $\epsilon = \epsilon_1^2$ in P6 and choose $M$ so that P6 holds. P6 implies that for every $\delta > 0$ and large $n$,
$$\sum_{k=1}^{n-M} P[\{|S_k| \leq A \text{ or } S_{k+j} \neq S_k \text{ for } m \leq j \leq M\} \cap \{T = n\}] \leq (\epsilon_1^2 + \delta) n F_n.$$

Hence there are at least $\epsilon_1 n$ values of $k$ with
$$P[\{|S_k| \leq A \text{ or } S_{k+j} \neq S_k \text{ for } m \leq j \leq M\} \cap \{T = n\}] \leq \epsilon_1 F_n.$$

Pick such a $k$ in defining $q_n$. Then $|q_n - F_n| = P[\{|S_k| \leq A \text{ or } S_{k+j} \neq S_k\} \cap \{T=n\}] \leq \epsilon_1 F_n$, giving $|q_n/F_n - 1| \leq \epsilon_1$.
