---
role: proof
locale: en
of_concept: euclidean-domain-unit-characterization
source_book: gtm028
source_chapter: "I"
source_section: "14"
---

(b) Since $1 \mid a$ for any $a \in E$, by E1 we have $\varphi(1) \leq \varphi(a)$ whenever $a \neq 0$.

(c) If $a$ and $b$ are associates, then $a \mid b$ and $b \mid a$. By E1, $\varphi(a) \leq \varphi(b)$ and $\varphi(b) \leq \varphi(a)$, hence $\varphi(a) = \varphi(b)$.

(d) If $\epsilon$ is a unit, then $\epsilon$ and $1$ are associates (since $\epsilon \mid 1$ and $1 \mid \epsilon$), so by (c), $\varphi(\epsilon) = \varphi(1)$. Conversely, if $\varphi(\epsilon) = \varphi(1)$ and $\epsilon \neq 0$, apply E2 with $a = 1$, $b = \epsilon$: there exist $q, r$ such that $1 = \epsilon q + r$ and $\varphi(r) < \varphi(\epsilon) = \varphi(1)$. By (a) and (b), $\varphi(r) < \varphi(1)$ implies $r = 0$. Thus $1 = \epsilon q$, so $\epsilon$ is a unit.
