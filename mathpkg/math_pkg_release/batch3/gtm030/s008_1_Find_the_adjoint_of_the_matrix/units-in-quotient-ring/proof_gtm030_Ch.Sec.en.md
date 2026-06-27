---
role: proof
locale: en
of_concept: units-in-quotient-ring
source_book: gtm030
source_chapter: ""
source_section: ""
---

Let $M$ denote the set of units in $I/(m)$. If $\bar{a} \in M$, there exists $b$ such that $\bar{a}\bar{b} = \bar{1}$. Hence $ab = 1 + mq$ for some $q$, so $ab - mq = 1$. This is a linear combination of $a$ and $m$ equal to $1$, which implies $\gcd(a,m) = 1$.

Conversely, if $\gcd(a,m) = 1$, then there exist integers $b, q$ such that $ab - mq = 1$. Reducing modulo $m$ gives $\bar{a}\bar{b} = \bar{1}$, so $\bar{a}$ is a unit with inverse $\bar{b}$.
