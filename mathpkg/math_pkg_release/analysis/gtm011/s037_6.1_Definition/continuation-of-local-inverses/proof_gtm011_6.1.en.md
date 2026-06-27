---
role: proof
locale: en
of_concept: continuation-of-local-inverses
source_book: gtm011
source_chapter: "6"
source_section: "6.1"
---

Since $G$ is connected there is a path $\gamma$ in $G$ from $a$ to $b$. For $0 \leq t \leq 1$ let $D_t$ be a disk about $\gamma(t)$ such that $D_t \subset G$ and on which $f$ is one-one. Let $\sigma = f \circ \gamma$ and let $\Delta_t$ be a disk about $\sigma(t)$ such that $\Delta_t \subset f(D_t)$. Finally, let $g_t: \Delta_t \to \mathbb{C}$ be an analytic function such that

$$f(g_t(\zeta)) = \zeta \text{ for } \zeta \text{ in } \Delta_t$$
$$g_t(\sigma(t)) = \gamma(t).$$

Claim. $\{(g_t, \Delta_t)\}$ is an analytic continuation along $\sigma$. To show this fix $t$ and let $\delta$ be chosen so that $\gamma(s) \in f^{-1}(\Delta_t) \cap D_t$ whenever $|s-t| < \delta$. Now fix $s$ with $|s-t| < \delta$ and let $B$ be a disk about $\gamma(s)$ such that $B \subset f^{-1}(\Delta_t) \cap D_s \cap D_t$. So $f(B)$ is an open set containing $\sigma(s) = f(\gamma(s))$ and $f(B) \subset f(D_t)$. By definition $g_s(f(z)) = z$ for all $z$ in $D_s$, and hence in $B$. Thus $g_s$ and $g_t$ agree on $f(B)$, establishing the continuation property.
