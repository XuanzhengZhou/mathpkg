---
role: proof
locale: en
of_concept: smallest-proof-turing-machine
source_book: gtm022
source_chapter: "5"
source_section: "5"
---

Since $\mathcal{T}$ is effectively axiomatised, there is a Turing machine $M$ that, given the Gödel number of a candidate proof, verifies whether it is a valid proof of $p$ in $\mathcal{T}$. Construct a Turing machine that, on input the Gödel number of $p$, enumerates $n = 0, 1, 2, \ldots$ in increasing order. For each $n$, it checks whether $n$ is the Gödel number of a proof of $p$ using $M$. The first $n$ that passes the verification is the smallest number which is the Gödel number of a proof of $p$. Since $p$ is a theorem, such an $n$ exists, and the enumeration terminates.
