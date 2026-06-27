---
role: proof
locale: en
of_concept: markov-gibbs-equivalence
source_book: gtm040
source_chapter: "12"
source_section: "3. Equivalence of finite Markov and neighbor Gibbs fields"
---
First direction (neighbor Gibbs $\implies$ Markov): Suppose $\{x_t\}$ is a Gibbs field with neighbor potential $U$. Write the local characteristic as

$$\mu_a^T(\iota) = \frac{\exp\{\sum_{C \in \mathcal{C}: a \in C} U_C(\iota)\}}{\sum_{s \in S} \exp\{\sum_{C \in \mathcal{C}: a \in C} U_C(s_a \iota)\}},$$

where $s_a \iota$ denotes the configuration obtained by changing the value at site $a$ to $s$. Split the sum in the exponent into two parts: $\sum_1$, involving cliques not contained in $\bar{a}$, and $\sum_2$, involving cliques contained in $\bar{a}$. Since configurations that agree on $\bar{a}$ give identical values for $\sum_2$, and $\sum_1$ depends only on the configuration outside $\bar{a}$, the ratio simplifies and $\mu_a^T$ depends only on the configuration on $\bar{a}$. Thus by Proposition 12-6(3), $\{x_t\}$ is a Markov field.

Conversely, if $\{x_t\}$ is Markov, we claim that the canonical potential $V$ from Theorem 12-12 is a neighbor potential. To see this, choose $a, b \in A \subset T$ such that $b \notin \bar{a}$. Expand $V_A$ as

$$V_A(\iota) = \sum_{B \subset A - \{a, b\}} (-1)^{|A-B|} \ln \left[ \frac{\mu_a^T(\iota^B) / \mu_a^T(\iota^{B+a})}{\mu_a^T(\iota^{B+b}) / \mu_a^T(\iota^{B+a+b})} \right].$$

Since $b \notin \bar{a}$, Proposition 12-6 shows that $\mu_a^T(\iota^{B+b}) = \mu_a^T(\iota^{B})$ and $\mu_a^T(\iota^{B+a+b}) = \mu_a^T(\iota^{B+a})$. Therefore the ratio inside the logarithm equals $1$, and $V_A(\iota) = 0$. Hence $V_A \equiv 0$ whenever $A$ is not a clique, proving $V$ is a neighbor potential.
