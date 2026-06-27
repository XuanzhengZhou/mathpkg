---
role: proof
locale: en
of_concept: finite-sets-are-small-normal-chain
source_book: gtm040
source_chapter: "9"
source_section: "2"
---

Let $E$ be a finite set. The finiteness of $E$ implies that each sum $\sum_{k \in E} {}^0N_{kk} P^E_{kj}$ has only finitely many terms, hence is finite. By Lemma 9-37, $\lambda^E$ exists. Moreover,
$$\lambda^E 1 = \sum_{j \in E} \lambda^E_j = \sum_{j \in E} \lim_n (P^n B^E)_{ij} = \lim_n \sum_{j \in E} (P^n B^E)_{ij} = \lim_n (P^n B^E 1)_i = 1,$$
where the interchange of limit and finite sum is justified since $E$ is finite. Thus $\lambda^E$ is a probability matrix, and $E$ is a small set by Definition 9-35.
