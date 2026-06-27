---
role: proof
locale: en
of_concept: integers-mod-p-is-field
source_book: gtm030
source_chapter: ""
source_section: ""
---

Suppose first that $m$ is composite, say $m = m_1 m_2$ where $m_i > 1$. Then $m_i$ is not divisible by $m$, so $\bar{m}_i \neq 0$. But $\bar{m}_1 \bar{m}_2 = \overline{m_1 m_2} = \bar{m} = 0$. Hence $I/(m)$ has zero divisors and is not an integral domain.

Now assume $m = p$ is prime. We prove $I/(p)$ is a field. It has an identity $\bar{1}$. Let $\bar{a} \neq 0$. Then $a$ is not divisible by $p$, so $\gcd(a,p) = 1$ (since $p$ is prime, the only divisors are $1$ and $p$). Hence there exist integers $b, q$ such that $ab + pq = 1$. Then $\bar{a}\bar{b} = \overline{ab} = \bar{1}$. Thus $\bar{a}$ has inverse $\bar{b}$ in $I/(p)$. Every nonzero element is a unit, so $I/(p)$ is a field with exactly $p$ elements.
