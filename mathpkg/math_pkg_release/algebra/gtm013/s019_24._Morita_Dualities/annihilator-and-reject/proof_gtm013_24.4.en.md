---
role: proof
locale: en
of_concept: annihilator-and-reject
source_book: gtm013
source_chapter: "7"
source_section: "24. Morita Dualities"
---

First recall from (24.3.2) that $K \leq l_M(r_{M^*}(K))$. If $x \in l_M(r_{M^*}(K))$ and $f: M/K 	o U$, then the natural epimorphism $n_K: M 	o M/K$ composed with $f$ gives $f \circ n_K \in r_{M^*}(K)$. So $f \circ n_K$ is annihilated by $x$. That is, $f(x + K) = f \circ n_K(x) = 0$, and $x + K \in \operatorname{Ker} f$. Thus,

$$\operatorname{Rej}_{M/K}(U) \supseteq l_M(r_{M^*}(K))/K.$$

But every $g \in r_{M^*}(K)$ (so $K \leq \operatorname{Ker} g$) factors through $n_K$ by (3.6.1). That is, $g = f \circ n_K$ where $f: M/K 	o U$. Thus if $x + K \in \operatorname{Rej}_{M/K}(U)$, then for each such $g$ we have $g(x) = f \circ n_K(x) = f(x + K) = 0$; so $x \in l_M(r_{M^*}(K))$.

Now for part (1) of the statement take $K = 0$ and recall (20.12). For part (2) apply (8.13).
