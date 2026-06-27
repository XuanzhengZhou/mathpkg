---
role: proof
locale: en
of_concept: van-kampen-image-generate
source_book: gtm057
source_chapter: "V"
source_section: "3"
---

**(III.1) The image groups $\omega_i G_i$ generate $G$.** Let $\alpha \in G = \pi(X,p)$ be represented by a $p$-based loop $a$. Subdivide $[0, \|a\|]$ by $0 = t_0 < t_1 < \dots < t_n = \|a\|$ sufficiently fine that each subinterval maps into some $X_i$. Choose an index function $\mu: \{1,\dots,n\} \to \{0,1,2\}$ with $a[t_{i-1}, t_i] \subset X_{\mu(i)}$. For each $t_i$, select a path $b_i$ from $p$ to $a(t_i)$ lying in $X_{\mu(i)} \cap X_{\mu(i+1)}$. Then $a_i = b_{i-1}^{-1} \cdot (a|_{[t_{i-1},t_i]}) \cdot b_i$ is a $p$-based loop in $X_{\mu(i)}$, and $\alpha = \prod_{i=1}^n \omega_{\mu(i)}[a_i]$.
