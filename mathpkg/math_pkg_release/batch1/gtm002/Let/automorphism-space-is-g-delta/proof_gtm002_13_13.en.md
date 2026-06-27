---
role: proof
locale: en
of_concept: automorphism-space-is-g-delta
source_book: gtm002
source_chapter: "13"
source_section: "13"
---

Let $H_n$ be the set of all $f \in C[0,1]$ such that $f(x) \neq f(y)$ for all $x$ and $y$ in $I$ with $|x - y| \geq 1/n$. If $f \in H_n$, then the number
$$\delta = \min \{|f(x) - f(y)| : |x - y| \geq 1/n\}$$
is positive. If $\varrho(g, f) < \delta/2$, then $g$ also belongs to $H_n$. Hence each $H_n$ is open in $C[0,1]$.

Every automorphism $h \in H$ is uniformly continuous on $I$, hence $h \in H_n$ for all sufficiently large $n$. Thus $H \subset \bigcap_n H_n$. Conversely, if $f \in \bigcap_n H_n$, then $f(x) \neq f(y)$ whenever $x \neq y$, so $f$ is injective. A continuous injective map of $[0,1]$ into $\mathbb{R}$ that fixes endpoints must be a homeomorphism onto $[0,1]$. Hence $\bigcap_n H_n \subset H$, so $H = \bigcap_n H_n$ is a $G_\delta$ set.
