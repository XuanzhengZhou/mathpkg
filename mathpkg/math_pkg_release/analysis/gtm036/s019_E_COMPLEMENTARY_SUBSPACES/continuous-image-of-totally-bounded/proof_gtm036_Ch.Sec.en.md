---
role: proof
locale: en
of_concept: continuous-image-of-totally-bounded-is-totally-bounded
source_book: gtm036
source_chapter: ""
source_section: "F"
---

Let $T: E \to F$ be a continuous linear map and let $B \subset E$ be totally bounded. Let $V$ be a neighborhood of $0$ in $F$. By continuity of $T$, $U = T^{-1}(V)$ is a neighborhood of $0$ in $E$. Since $B$ is totally bounded, there exists a finite set $N$ such that $B \subset N + U$. Then $T(B) \subset T(N) + T(U) \subset T(N) + V$. Since $T(N)$ is finite, $T(B)$ is totally bounded.
