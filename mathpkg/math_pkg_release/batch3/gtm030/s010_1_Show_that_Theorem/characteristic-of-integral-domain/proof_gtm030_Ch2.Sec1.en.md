---
role: proof
locale: en
of_concept: characteristic-of-integral-domain
source_book: gtm030
source_chapter: "2"
source_section: "1"
---
We first note that in an integral domain $\mathfrak{A}$, either the characteristic is $0$ or the characteristic is $m > 0$, and then every non-zero element has order $m$. We now show that in the latter case $m$ is a prime.

Suppose, for contradiction, that $m = m_1 m_2$ where $m_1 > 1$ and $m_2 > 1$. Let $a \in \mathfrak{A}$ be any non-zero element. Consider

$$m a^2 = m_1 m_2 a^2 = (m_1 a)(m_2 a).$$

Since $m$ is the characteristic of $\mathfrak{A}$, we have $m a^2 = 0$, hence $(m_1 a)(m_2 a) = 0$. Because $\mathfrak{A}$ is an integral domain, this product being zero implies that either $m_1 a = 0$ or $m_2 a = 0$. But $m$ is the smallest positive integer such that $m x = 0$ for all $x \in \mathfrak{A}$, and $m_1, m_2 < m$. Moreover, $m_1 a \neq 0$ and $m_2 a \neq 0$ since the additive order of $a$ is $m$. This yields a contradiction. Therefore $m$ cannot be factored as a product of two integers greater than $1$, so $m$ is prime.
