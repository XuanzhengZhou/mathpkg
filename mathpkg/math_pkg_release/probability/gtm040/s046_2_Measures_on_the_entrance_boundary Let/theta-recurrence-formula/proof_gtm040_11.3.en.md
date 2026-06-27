---
role: proof
locale: en
of_concept: theta-recurrence-formula
source_book: gtm040
source_chapter: "11"
source_section: "2"
---

**Proof of Proposition 11-3.** Using as a set of alternatives the time when the $Q^\nu$-process is last in $E$, we have for $j \in E$:

$$\theta^E_j = \sum_{n=0}^{\infty} (Q^\nu)_{0j}^{(n)} \, \Pr{}_j^\nu[\text{process leaves } E \text{ immediately and never returns}].$$

This can be rewritten as

$$\theta^E_j = N_{0j}^\nu \left[ 1 - \sum_{k \in E} \left( Q_{jk}^\nu + \sum_{c,d \in E} Q_{jc}^\nu \, {}_E N_{cd}^\nu \, Q_{dk}^\nu \right) \right],$$

where ${}_E N_{cd}^\nu$ denotes the fundamental matrix of $Q^\nu$ restricted to $E$.

Now $N_{0j}^\nu = \nu_j + \delta_{0j}$, and direct computation yields the identities

$$N_{0j}^\nu Q_{jk}^\nu = \nu_k P_{kj},$$
$$N_{0j}^\nu Q_{jc}^\nu \, {}_E N_{cd}^\nu \, Q_{dk}^\nu = \nu_k P_{kd} \, {}_E N_{dc}^\nu \, P_{cj},$$

valid for all states, not just those in $S^\nu \cup \{0\}$. Substituting these relations and applying Lemma 6-6 gives

$$\theta^E_j = \nu_j + \delta_{0j} - \sum_{k \in E} \nu_k P^E_{kj}.$$

In matrix notation restricted to $E$, this is precisely $\nu_E (I - P^E) = \theta^E_E - \delta_0$.

In general, $\theta^E$ has total measure less than one, since the $Q^\nu$ process either may fail to reach $E$ or may return to it infinitely often. If $E$ is finite and $0 \in E$, neither of these alternatives has positive probability, and thus $\theta^E$ is a probability measure.
