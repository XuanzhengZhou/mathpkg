---
role: proof
locale: en
of_concept: subgroups-of-cyclic-group
source_book: gtm030
source_chapter: "1"
source_section: "11"
---

Let $\mathfrak{Z} = [a]$ be cyclic of order $r$. Let $\mathfrak{W}$ be a subgroup of $\mathfrak{Z}$. If $\mathfrak{W} = \{1\}$, its order is $1$, which divides $r$.

Assume $\mathfrak{W} \neq \{1\}$. Then there exist positive integers $m$ such that $a^m \in \mathfrak{W}$ (for if $a^m \in \mathfrak{W}$ with $m \neq 0$, then $(a^m)^{-1} = a^{-m} \in \mathfrak{W}$). Let $s$ be the smallest positive integer such that $a^s \in \mathfrak{W}$.

We show that $\mathfrak{W} = [a^s]$. Let $c = a^m$ be any element of $\mathfrak{W}$. Write $m = sq + u$ with $0 \leq u < s$. Then $a^u = a^m (a^s)^{-q} \in \mathfrak{W}$. By minimality of $s$, $u = 0$. Thus $c = a^m = (a^s)^q$ and $\mathfrak{W} = [a^s]$.

Now, since $a^r = 1 \in \mathfrak{W}$ and $s$ is minimal positive with $a^s \in \mathfrak{W}$, $s$ must divide $r$ (write $r = sq + u'$, then $a^{u'} = 1 \cdot (a^s)^{-q} = 1 \in \mathfrak{W}$, so $u' = 0$). The order of $[a^s]$ is $r/s = t$, which divides $r$.

Conversely, if $t$ is any positive divisor of $r$, let $s = r/t$ and consider $\mathfrak{W} = [a^s]$. This subgroup has order $t$. Moreover, the mapping $\mathfrak{W} \to s$ (the smallest positive integer with $a^s \in \mathfrak{W}$) is 1-1: if $\mathfrak{W} \to s$ and $\mathfrak{W}' \to s$, then $\mathfrak{W} = [a^s] = \mathfrak{W}'$. Hence there is exactly one subgroup of order $t$.
