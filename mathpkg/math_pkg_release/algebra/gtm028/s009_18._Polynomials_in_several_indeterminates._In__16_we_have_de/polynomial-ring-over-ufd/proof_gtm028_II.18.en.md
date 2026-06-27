---
role: proof
locale: en
of_concept: polynomial-ring-over-ufd
source_book: gtm028
source_chapter: "II"
source_section: "18"
---

The proof proceeds by induction on $n$. The case $n = 1$ is Theorem 10 of §17: if $R$ is a UFD, then $R[X]$ is a UFD. Assume the theorem holds for $n-1$ indeterminates. Using the inductive structure of polynomial rings, we have $R[X_1, \cdots, X_n] \cong (R[X_1, \cdots, X_{n-1}])[X_n]$. By the induction hypothesis, $R[X_1, \cdots, X_{n-1}]$ is a UFD. Then applying Theorem 10 of §17 to the ring $R[X_1, \cdots, X_{n-1}]$ with the single indeterminate $X_n$, we conclude that $(R[X_1, \cdots, X_{n-1}])[X_n] \cong R[X_1, \cdots, X_n]$ is a UFD. This completes the induction.
