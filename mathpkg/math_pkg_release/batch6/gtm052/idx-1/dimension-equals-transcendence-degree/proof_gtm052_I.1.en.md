---
role: proof
locale: en
of_concept: dimension-equals-transcendence-degree
source_book: gtm052
source_chapter: "I"
source_section: "1"
---

The proof uses Noether normalization. See Matsumura [2, Ch. 5, §14] or, in the case $k$ is algebraically closed, Atiyah--Macdonald [1, Ch. 11].

The key idea of the proof is as follows. By Noether normalization, there exists $y_1, \ldots, y_d \in B$, algebraically independent over $k$, such that $B$ is integral over $k[y_1, \ldots, y_d]$. Then $d = \operatorname{tr.deg}_k K(B)$. The going-up theorem shows that the Krull dimension of $B$ equals that of $k[y_1, \ldots, y_d]$, which is $d$. This proves part (a). For part (b), apply part (a) to $B/\mathfrak{p}$ and note that a chain of primes from $0$ to $\mathfrak{p}$ together with a chain from $\mathfrak{p}$ to a maximal ideal gives a chain of total length in $B$.
