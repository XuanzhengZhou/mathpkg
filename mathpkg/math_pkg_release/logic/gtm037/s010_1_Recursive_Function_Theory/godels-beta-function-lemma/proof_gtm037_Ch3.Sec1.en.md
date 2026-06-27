---
role: proof
locale: en
of_concept: godels-beta-function-lemma
source_book: gtm037
source_chapter: "3"
source_section: "1"
---

Let $s$ be the maximum of $y_0, \ldots, y_{n-1}, n$. For each $i < n$ let

$$m_i = 1 + (i + 1) \cdot s!.$$

Then for $i < j < n$ the integers $m_i$ and $m_j$ are relatively prime. For, if a prime $p$ divides both $m_i$ and $m_j$, it also divides

$$m_j - m_i = (j + 1) \cdot s! - (i + 1) \cdot s! = (j - i) \cdot s!.$$

Now $p \nmid s!$, since $p \mid 1 + (i + 1)s!$. Hence $p \mid j - i$. But $j - i < n \leq s$, and hence $p \leq s$. Since $p \mid s!$ (as $p \leq s$), this contradicts $p \nmid s!$. Thus the $m_i$ are pairwise coprime.

By the Chinese remainder theorem, there exists $x \in \omega$ such that

$$x \equiv y_i \pmod{m_i} \quad \text{for all } i < n.$$

Hence $\beta(x, i) = \operatorname{rm}(\operatorname{Exc} x, 1 + (i + 1)Lx) = y_i$ for each $i < n$, as desired.
