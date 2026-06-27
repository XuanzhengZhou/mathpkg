---
role: proof
locale: en
of_concept: minimal-iff-not-convex-combination
source_book: gtm040
source_chapter: "10"
source_section: "6"
---

If $h = c_1 h_1 + c_2 h_2$ is a nontrivial convex combination with $h_1 \neq h$, then $h \geq c_1 h_1$, so $c_1 h_1 = c h$ for some $c$ if $h$ is minimal. Multiplying by $\pi$ gives $c_1 = c$. Since $c_1 \neq 0$, $h_1 = h$, contradiction.

Conversely, if $h \geq h' \geq 0$ with $h'$ regular and $h'$ not equal to $0$ or $h$, then
$$h = (\pi h') \frac{h'}{\pi h'} + [\pi(h - h')] \frac{h - h'}{\pi(h - h')}$$
is a nontrivial convex combination of two distinct normalized non-negative regular functions.
