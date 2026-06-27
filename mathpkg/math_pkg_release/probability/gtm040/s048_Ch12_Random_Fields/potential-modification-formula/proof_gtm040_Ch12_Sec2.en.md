---
role: proof
locale: en
of_concept: potential-modification-formula
source_book: gtm040
source_chapter: "12"
source_section: "2. Gibbs fields"
---
For any $a \in T$ and $B \subset T - \{a\}$, using the first equation for $V$ in Theorem 12-12,

$$V_A(\iota) = \sum_{B \subset A - \{a\}} (-1)^{|A - B|} \ln \frac{\mu(\{\iota^B\})}{\mu(\{\iota^{B+a}\})}.$$

Now substitute the Gibbs field representation $\mu(\{\iota\}) = z^{-1} e^{H_U(\iota)}$:

$$\ln \frac{\mu(\{\iota^B\})}{\mu(\{\iota^{B+a}\})} = \sum_{D \subset T} U_D(\iota^B) - \sum_{D \subset T} U_D(\iota^{B+a}).$$

Since $U_D(\iota^B) = U_D(\iota^{B \cap D})$ and $U_D(\iota^{B+a}) = U_D(\iota^{(B+a) \cap D})$, we obtain

$$V_A(\iota) = \sum_{D \subset T} \sum_{B \subset A} (-1)^{|A - B|} U_D(\iota^{B \cap D})$$

$$= \sum_{D \subset T} \sum_{B_1 \subset D \cap A} \left[ (-1)^{|A - B_1|} U_D(\iota^{B_1}) \left\{ \sum_{B_2 \subset \tilde{D} \cap A} (-1)^{|\tilde{D} \cap A| - |B_2|} \right\} \right],$$

where $\tilde{D} = T - D$. The inner sum in the last expression is $0$ unless $\tilde{D} \cap A = \varnothing$, i.e., unless $A \subset D$. Thus only terms with $A \subset D$ contribute to the sum.
