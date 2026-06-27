---
role: proof
locale: en
of_concept: turing-computable-implies-recursive
source_book: gtm037
source_chapter: "3"
source_section: "1"
---

Let $M$ be a Turing machine which computes $f$ as described in Definition 3.9(ii), and let $e = gM$. Then for any $x_0, \ldots, x_{m-1} \in \omega$,

$$f(x_0, \ldots, x_{m-1}) = V\left(\mu u \left[ (e, x_0, \ldots, x_{m-1}, u) \in T_m \right]\right).$$

Since $T_m$ is elementary by Lemma 3.36, the relation $(e, x_0, \ldots, x_{m-1}, u) \in T_m$ is elementary, hence recursive. The unbounded $\mu$-operator applied to a recursive relation yields a partial recursive function. As $V$ is elementary (hence recursive), the composition $V(\mu u[\cdots])$ is recursive. Therefore $f$ is recursive.
