---
role: proof
locale: en
of_concept: euclidean-domain-is-pid
source_book: gtm030
source_chapter: "II"
source_section: "5"
---

Let $\mathfrak{B}$ be any ideal in the Euclidean domain $\mathfrak{A}$. If $\mathfrak{B} = 0$, then $\mathfrak{B} = (0)$ is principal. Otherwise, choose $b \in \mathfrak{B}, b \neq 0$ with minimal $\delta(b)$. For any $a \in \mathfrak{B}$, the division algorithm gives $a = bq + r$ with $r = 0$ or $\delta(r) < \delta(b)$. Since $r = a - bq \in \mathfrak{B}$, the minimality of $\delta(b)$ forces $r = 0$. Hence $a = bq$ and $\mathfrak{B} = (b)$.
