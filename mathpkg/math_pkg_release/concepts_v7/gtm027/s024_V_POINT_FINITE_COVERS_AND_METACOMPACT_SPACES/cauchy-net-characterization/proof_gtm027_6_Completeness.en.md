---
role: proof
locale: en
of_concept: cauchy-net-characterization
source_book: gtm027
source_chapter: "6"
source_section: "Completeness"
---

# Proof of Characterization of Cauchy Nets (Lemma 6.20)

**Lemma 6.20.** A net $\{S_n : n \in D\}$ in a uniform space $(X, \mathcal{U})$ is a Cauchy net if and only if either of the following statements is true.

(a) The net $\{(S_m, S_n) : (m,n) \in D \times D\}$ is eventually in each member of some subbase for the uniformity $\mathcal{U}$.

(b) The net $\{p(S_m, S_n) : (m,n) \in D \times D\}$ converges to zero for each $p$ in some family of pseudo-metrics which generates the gage $P$.

**Proof.** If a family $Q$ of pseudo-metrics generates $P$, then the family of all $V_{p,r}$ for $p \in Q$ and $r > 0$ is a subbase for the uniformity, so the proof of (b) reduces to that of (a).

To prove (a), recall that a net is eventually in each member of a uniformity $\mathcal{U}$ if and only if it is eventually in each member of some base for $\mathcal{U}$. Since every member of a subbase is a member of the uniformity, if a net is eventually in each subbase member, it is eventually in each finite intersection of subbase members (because: if a net is eventually in each of a finite number of sets, it is then eventually in their intersection). The family of finite intersections of subbase members is a base for the uniformity, so the net is eventually in each member of this base and hence in each member of $\mathcal{U}$. Thus the net is Cauchy.

Conversely, if the net is Cauchy (eventually in each member of $\mathcal{U}$), then in particular it is eventually in each member of any subbase. This establishes both directions.
