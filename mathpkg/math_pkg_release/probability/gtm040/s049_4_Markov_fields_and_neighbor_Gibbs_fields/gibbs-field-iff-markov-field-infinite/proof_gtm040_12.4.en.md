---
role: proof
locale: en
of_concept: gibbs-field-iff-markov-field-infinite
source_book: gtm040
source_chapter: "12"
source_section: "4"
---

**Proof.** Suppose $\{x_t\}$ is a neighbor Gibbs field. From the definition we see that $\mu_a^{\Lambda}(\iota) = \mu_a^{\Lambda}(\iota')$ whenever $\Lambda \supset \bar{a}$ and $\iota'$ agrees with $\iota$ on $\bar{a}$. Just as in Proposition 12-6, this implies that $\mu_a^{\Lambda}(\iota) = \mu_a^{\Lambda}(\iota')$ for all finite $\Lambda \supset \bar{a}$, so $\{x_t\}$ is Markov.

Conversely, if $\{x_t\}$ is Markov we define a potential $V$ by $V_\emptyset = 0$ and

$$
V_{\Lambda}(\iota) = \sum_{B \subset \Lambda} (-1)^{|\Lambda \setminus B|} \log \mu_{a}^{\bar{B}}(\iota),
$$

where $a$ is any element of $\Lambda$ and $\bar{B}$ denotes the closure of $B$ under the neighbor system. The Markov property ensures that this definition is independent of the choice of $a \in \Lambda$. It can then be verified that the local characteristics of the Gibbs field with potential $V$ coincide with those of the original Markov field, establishing the converse.
