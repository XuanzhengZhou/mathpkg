---
role: proof
locale: en
of_concept: distributivity-of-gcd
source_book: gtm030
source_chapter: "2"
source_section: "3"
---

Let $d = (a, b)$. Then $d \mid a$ and $d \mid b$, so $c d \mid c a$ and $c d \mid c b$. Hence $c d$ is a common divisor of $c a$ and $c b$, and therefore $c d \mid (c a, c b)$.

Now let $g = (c a, c b)$. Since $c d \mid g$, we have $g = c d \cdot u$ for some $u \in \mathfrak{S}$. Since $g \mid c a$, write $c a = g \cdot x = c d \cdot u x$. By the cancellation law, $a = d \cdot u x$. Similarly, $g \mid c b$ gives $b = d \cdot u y$ for some $y$. Thus $d u \mid a$ and $d u \mid b$, so $d u \mid d$ (since $d = (a, b)$). Write $d = d u \cdot v$ for some $v$. Canceling $d$, we obtain $1 = u v$, so $u$ is a unit. Therefore $g \sim c d$, i.e., $(c a, c b) \sim c \cdot (a, b)$.
