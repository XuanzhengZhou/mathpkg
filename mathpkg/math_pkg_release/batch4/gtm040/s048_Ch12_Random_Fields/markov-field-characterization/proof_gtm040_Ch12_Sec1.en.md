---
role: proof
locale: en
of_concept: markov-field-characterization
source_book: gtm040
source_chapter: "12"
source_section: "1. Markov fields"
---
When $T$ is finite, (2) is simply the Markov field property with $\Lambda = T$, while the fact that $\mu_a^T$ depends only on $t \in \bar{a}$ together with (2) implies $\mu_a^T(\iota) = \mu_a^{\bar{a}}(\iota) = \mu_a^{\bar{a}}(\iota') = \mu_a^T(\iota')$ whenever $\iota$ and $\iota'$ agree on $\bar{a}$.

To see that (3) implies (2), fix $a \in T$ and let $\kappa = \{k_t; t \in T - \bar{a}\}$ be any prescription of values from $S$ on $T - \bar{a}$. Denote by $p, q$, and $r_\kappa$ the statements

$$x_a = i_a, \quad x_t = i_t \text{ for all } t \in \partial a, \quad x_t = k_t \text{ for all } t \in T - \bar{a},$$

respectively. Then (3) asserts that

$$\Pr[p \mid q \wedge r_\kappa] = c \quad \text{for all } \kappa,$$

or equivalently,

$$\Pr[p \wedge q \wedge r_\kappa] = c \Pr[q \wedge r_\kappa].$$

Summing over all possible $\kappa$, we obtain $\Pr[p \mid q] = c$. Thus $\Pr[p \mid q \wedge r_\kappa] = \Pr[p \mid q]$, which is precisely (2) when $k_t = i_t$ for all $t \in T - \bar{a}$.

Finally, to show that (2) implies (1) we choose $\bar{a} \subset \Lambda \subset T$ and $\iota = \{i_t\} \in \Omega$. Since $\mu_a^{\bar{a}}$ depends only on sites in $\bar{a}$, (2) yields

$$\Pr[x_t = i_t \text{ for all } t \in \Lambda \wedge x_t = k_t \text{ for all } t \in T - \Lambda]$$

expressed in terms of $\mu_a^{\bar{a}}$, showing the Markov field property holds.
