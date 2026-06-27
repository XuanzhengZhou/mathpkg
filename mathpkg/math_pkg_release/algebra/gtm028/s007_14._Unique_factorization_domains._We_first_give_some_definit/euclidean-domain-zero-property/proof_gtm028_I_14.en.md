---
role: proof
locale: en
of_concept: euclidean-domain-zero-property
source_book: gtm028
source_chapter: "I"
source_section: "14"
---

Let $b \neq 0$ in $E$. Apply condition E2 with $a = 0$: there exist $q, r \in E$ such that $0 = bq + r$ and $\varphi(r) < \varphi(b)$. Thus $r = -bq$. If $r \neq 0$, then $b \mid r$, so by E1, $\varphi(b) \leq \varphi(r)$, contradicting $\varphi(r) < \varphi(b)$. Hence $r = 0$, and we obtain $\varphi(0) < \varphi(b)$ as asserted.

Note that the function $\varphi_1(a) = \varphi(a) - \varphi(0)$ also satisfies E1 and E2, and has the additional property $\varphi_1(0) = 0$, $\varphi_1(a) > 0$ for $a \neq 0$.
