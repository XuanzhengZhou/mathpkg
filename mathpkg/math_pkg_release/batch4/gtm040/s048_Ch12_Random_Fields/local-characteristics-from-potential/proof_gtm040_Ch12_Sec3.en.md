---
role: proof
locale: en
of_concept: local-characteristics-from-potential
source_book: gtm040
source_chapter: "12"
source_section: "3. Equivalence of finite Markov and neighbor Gibbs fields"
---
A computation similar to the one in the proof of Theorem 12-16 shows that

$$\mu_A^{\bar{A}}(\iota) = z^{-1} \exp\left\{ \sum_{B \in \bar{A}: B \cap A \neq \emptyset} V_B(\iota) \right\} = \mu_A^{\bar{A}}(\iota')$$

whenever $i_t = i'_t$ for all $t \in \bar{A}$. The claim follows from the straightforward generalization of Proposition 12-6 obtained by replacing the singleton $\{a\}$ with the finite set $A$. Since $V$ is a neighbor potential by Theorem 12-16, only cliques $B$ that intersect $A$ contribute, and the exponential form follows directly from the Gibbs field representation.
