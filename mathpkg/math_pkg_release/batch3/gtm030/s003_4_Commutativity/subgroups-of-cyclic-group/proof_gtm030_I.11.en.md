---
role: proof
locale: en
of_concept: subgroups-of-cyclic-group
source_book: gtm030
source_chapter: "I"
source_section: "11"
---

Let $\mathfrak{Z} = [a]$ and let $\mathfrak{W} \neq \{1\}$ be a subgroup. There exist integers $m \neq 0$ such that $a^m \in \mathfrak{W}$, and if $a^m \in \mathfrak{W}$ then $a^{-m} = (a^m)^{-1} \in \mathfrak{W}$. Let $s$ be the smallest positive integer with $a^s \in \mathfrak{W}$. For any $c = a^m \in \mathfrak{W}$, write $m = sq + u$ with $0 \leq u < s$. Then $a^u = a^m (a^s)^{-q} \in \mathfrak{W}$, so by minimality of $s$, $u = 0$. Hence $c = a^m = (a^s)^q$, and $\mathfrak{W} = [a^s]$.

If $\mathfrak{Z}$ is finite of order $r$, then $a^r = 1$. Write $r = st$. The order of $a^s$ is $t$ since $(a^s)^t = a^{st} = a^r = 1$ and no smaller positive power gives $1$. Thus the order $t$ of $\mathfrak{W}$ divides $r$. For uniqueness, if $\mathfrak{W}'$ is another subgroup of order $t$, then by the above argument $\mathfrak{W}' = [a^{s'}]$ with order $r/s' = t$, so $s' = s$ and $\mathfrak{W}' = \mathfrak{W}$.

Conversely, if $t$ divides $r$, let $s = r/t$. Then $[a^s]$ is a subgroup of order $t$.

If $\mathfrak{Z}$ is infinite, the mapping $\mathfrak{W} \mapsto s$ (where $s$ is the smallest positive integer with $a^s \in \mathfrak{W}$, with $1 \mapsto 0$) is a bijection onto the non-negative integers.
