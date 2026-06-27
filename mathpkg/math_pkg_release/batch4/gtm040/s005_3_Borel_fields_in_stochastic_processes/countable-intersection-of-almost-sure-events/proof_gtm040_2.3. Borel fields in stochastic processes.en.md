---
role: proof
locale: en
of_concept: countable-intersection-of-almost-sure-events
source_book: gtm040
source_chapter: "2"
source_section: "3. Borel fields in stochastic processes"
---

Let $\{P_n\}$ be the truth sets of the statements $\{p_n\}$. Applying Proposition 1-18 (countable subadditivity), we have
$$1 - \Pr[q] = \mu\left(\Omega \setminus \bigcap_n P_n\right) = \mu\left(\bigcup_n \tilde{P}_n\right) \leq \sum_n \mu(\tilde{P}_n) = \sum_n (1 - \Pr[p_n]) = 0.$$
Hence $\Pr[q] = 1$.
