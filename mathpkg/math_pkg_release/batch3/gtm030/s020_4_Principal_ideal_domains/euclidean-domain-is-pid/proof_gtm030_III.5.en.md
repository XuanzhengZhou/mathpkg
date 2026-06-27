---
role: proof
locale: en
of_concept: euclidean-domain-is-pid
source_book: gtm030
source_chapter: "III"
source_section: "5"
---

Let $\mathfrak{B}$ be any ideal in the Euclidean domain $\mathfrak{A}$. If $\mathfrak{B} = 0$, then $\mathfrak{B} = (0)$ is principal. Assume $\mathfrak{B} \neq 0$ and choose $b \in \mathfrak{B}$, $b \neq 0$, such that $\delta(b)$ is minimal among all non-zero elements of $\mathfrak{B}$.

Now let $a \in \mathfrak{B}$ be arbitrary. Since $\mathfrak{A}$ is Euclidean, there exist $q, r \in \mathfrak{A}$ such that
$$a = bq + r,$$
where either $r = 0$ or $\delta(r) < \delta(b)$. Since $r = a - bq$ and both $a, b \in \mathfrak{B}$, we have $r \in \mathfrak{B}$. By the minimality of $\delta(b)$, the case $\delta(r) < \delta(b)$ with $r \neq 0$ is impossible. Hence $r = 0$, which gives $a = bq$.

Thus every element of $\mathfrak{B}$ is a multiple of $b$, so $\mathfrak{B} = (b)$. Therefore every ideal in $\mathfrak{A}$ is principal, and $\mathfrak{A}$ is a principal ideal domain.
