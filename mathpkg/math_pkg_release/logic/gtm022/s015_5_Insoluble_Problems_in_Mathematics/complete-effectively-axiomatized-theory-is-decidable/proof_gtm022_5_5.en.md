---
role: proof
locale: en
of_concept: complete-effectively-axiomatized-theory-is-decidable
source_book: gtm022
source_chapter: "5"
source_section: "5"
---

Since $\mathcal{T}$ is effectively axiomatised, there is a Turing machine $M$ that, given the Gödel number of a candidate proof, verifies whether it is a valid proof in $\mathcal{T}$. Construct a Turing machine $D$ as follows: on input the Gödel number of $p \in \mathcal{L}(\mathcal{T})$, enumerate natural numbers $n = 0, 1, 2, \ldots$ in increasing order. For each $n$, use $M$ to check whether $n$ is the Gödel number of a proof of $p$ or a proof of $\sim p$ in $\mathcal{T}$.

Since $\mathcal{T}$ is complete, for every $p \in \mathcal{L}(\mathcal{T})$, either $\mathcal{T} \vdash p$ or $\mathcal{T} \vdash \sim p$. Therefore the enumeration will eventually find a proof of one of them. When it does, $D$ outputs "yes, $p$ is a theorem" together with the proof if it found a proof of $p$, or "no, $p$ is not a theorem" together with the proof of $\sim p$ if it found a proof of $\sim p$. Consistency of $\mathcal{T}$ ensures that $D$ never finds proofs of both $p$ and $\sim p$. Thus $D$ decides theoremhood in $\mathcal{T}$ and provides a proof of its answer.
