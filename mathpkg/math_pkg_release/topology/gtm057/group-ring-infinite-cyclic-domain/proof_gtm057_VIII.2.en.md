---
role: proof
locale: en
of_concept: group-ring-infinite-cyclic-domain
source_book: gtm057
source_chapter: "VIII"
source_section: "2"
---
Let $t$ generate $H$. Write $a = \sum a_n t^n$, $b = \sum b_n t^n$, and $c = ab = \sum c_n t^n$ where $c_n = \sum_i a_i b_{n-i}$. If $n < \mu(a) + \mu(b)$ and $i \geq \mu(a)$, then $n-i < \mu(b)$, so $a_i b_{n-i} = 0$. Thus $c_n = 0$ for $n < \mu(a) + \mu(b)$. For $n = \mu(a) + \mu(b)$, the only nonzero term is $a_{\mu(a)} b_{\mu(b)} \neq 0$, so $\mu(ab) = \mu(a) + \mu(b)$ and $ab \neq 0$.
