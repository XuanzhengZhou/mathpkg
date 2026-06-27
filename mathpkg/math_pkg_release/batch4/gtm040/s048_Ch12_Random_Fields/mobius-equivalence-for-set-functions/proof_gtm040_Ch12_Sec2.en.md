---
role: proof
locale: en
of_concept: mobius-equivalence-for-set-functions
source_book: gtm040
source_chapter: "12"
source_section: "2. Gibbs fields"
---
Given $\iota = \{i_t\}$ and $A \subset T$, define the modification $\iota^A = \{i_t^A\}$ of $\iota$ by

$$i_t^A = \begin{cases} i_t & \text{for } t \in A \\ 0 & \text{otherwise.} \end{cases}$$

For any $a \in T$ and $B \subset T - \{a\}$, using the definition of the Gibbs field with potential $U$,

$$\ln \frac{\mu(\{\iota^B\})}{\mu(\{\iota^{B+a}\})} = H_U(\iota^B) - H_U(\iota^{B+a}) = \sum_{D \subset T} U_D(\iota^B) - \sum_{D \subset T} U_D(\iota^{B+a}).$$

Since $U_D(\iota^B) = 0$ unless $D \subset B$, and $U_D(\iota^{B+a}) = 0$ unless $D \subset B \cup \{a\}$, the difference simplifies. This identity provides the connection between probability ratios and potentials used in the canonical potential construction.
