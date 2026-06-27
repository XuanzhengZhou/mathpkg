---
role: proof
locale: en
of_concept: proposition-10-51
source_book: gtm040
source_chapter: "10"
source_section: "51"
---

**Proof:** The process watched starting in $E$ is a Markov chain with transition matrix $P$ and starting distribution $\mu^E$ if $E$ is a finite set in $S$. By Proposition 10-21, $z_v$ exists and has the required values for almost every path in this chain, and in this chain

$$\Pr_{\mu^E}[z_v \in C] = \sum_{i \in E} \mu^E_i \Pr_i[z_v \in C]$$

$$= \sum_{i \in E} \mu^E_i \int_C K(i, x) d\mu(x)$$

$$= \int_C \mu^E K(\cdot, x) d\mu(x).$$

As $E$ increases to $S$, we obtain almost all paths of $\{z_n\}$ in this way. Hence $z_v$ exists and is in $S \cup B_e$ a.e., and, by Definition 10-4,

$$\Pr[z_v \in C] = \lim_{E \uparrow S} \int_C \mu^E K(\cdot, y) d\mu(y).$$

By Lemma 10-50, this limit equals $\int_C q^\nu(y) d\mu(y)$, completing the proof.
