---
role: proof
locale: en
of_concept: r.e.-image-under-partial-recursive
source_book: gtm037
source_chapter: "6"
source_section: "6.3"
---

We may assume that $A \neq \emptyset$. Say $A = \operatorname{Rng} g$, $g$ recursive. Clearly

$$f[A] = \{f(g(x)) : x \in \omega \text{ and } g(x) \in \operatorname{Dmn} f\}.$$

Define the partial function $h(x) \simeq f(g(x))$. Since $g$ is recursive and $f$ is partial recursive, $h$ is partial recursive. Its range $\operatorname{Rng} h = f[A]$ is therefore r.e. by definition of r.e. sets (the range of a partial recursive function is r.e.). $\square$
