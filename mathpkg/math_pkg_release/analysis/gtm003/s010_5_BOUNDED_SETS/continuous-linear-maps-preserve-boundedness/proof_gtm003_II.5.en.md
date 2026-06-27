---
role: proof
locale: en
of_concept: continuous-linear-maps-preserve-boundedness
source_book: gtm003
source_chapter: "II"
source_section: "5"
---

Let $V$ be any $0$-neighborhood in $M$. Since $u$ is continuous, $u^{-1}(V)$ is a $0$-neighborhood in $L$.

If $B$ is bounded in $L$, there exists $\lambda \in K$ such that $B \subset \lambda u^{-1}(V)$. Applying $u$, we obtain $u(B) \subset u(\lambda u^{-1}(V)) = \lambda u(u^{-1}(V)) \subset \lambda V$. Hence $u(B)$ is bounded in $M$.

If $B$ is totally bounded in $L$, there exists a finite set $B_0 \subset B$ such that $B \subset B_0 + u^{-1}(V)$. Then $u(B) \subset u(B_0) + u(u^{-1}(V)) \subset u(B_0) + V$, and $u(B_0)$ is a finite subset of $u(B)$. Thus $u(B)$ is totally bounded in $M$.
