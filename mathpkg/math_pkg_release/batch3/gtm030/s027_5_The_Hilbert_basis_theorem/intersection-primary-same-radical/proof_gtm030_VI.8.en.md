---
role: proof
locale: en
of_concept: intersection-primary-same-radical
source_book: gtm030
source_chapter: "VI"
source_section: "8. Uniqueness theorems"
---

We know that $\mathfrak{R}(\mathfrak{Q}_1 \cap \mathfrak{Q}_2) = \mathfrak{R}(\mathfrak{Q}_1) \cap \mathfrak{R}(\mathfrak{Q}_2)$ (Exercise 3, §7). Since $\mathfrak{R}(\mathfrak{Q}_1) = \mathfrak{R}(\mathfrak{Q}_2) = \mathfrak{P}$, we have $\mathfrak{R}(\mathfrak{Q}_1 \cap \mathfrak{Q}_2) = \mathfrak{P}$.

Now let $a$ be a zero-divisor modulo $\mathfrak{Q}_1 \cap \mathfrak{Q}_2$. Then there exists $b \not\equiv 0 \pmod{\mathfrak{Q}_1 \cap \mathfrak{Q}_2}$ such that $ab \equiv 0 \pmod{\mathfrak{Q}_1 \cap \mathfrak{Q}_2}$. Hence $ab \equiv 0 \pmod{\mathfrak{Q}_1}$ and $ab \equiv 0 \pmod{\mathfrak{Q}_2}$. Since $b \notin \mathfrak{Q}_1 \cap \mathfrak{Q}_2$, either $b \notin \mathfrak{Q}_1$ or $b \notin \mathfrak{Q}_2$. In either case, since $\mathfrak{Q}_1$ and $\mathfrak{Q}_2$ are primary, $a$ is nilpotent modulo $\mathfrak{Q}_1$ or $\mathfrak{Q}_2$, hence $a \in \mathfrak{R}(\mathfrak{Q}_1) = \mathfrak{R}(\mathfrak{Q}_2) = \mathfrak{P}$. Thus $a \in \mathfrak{P} = \mathfrak{R}(\mathfrak{Q}_1 \cap \mathfrak{Q}_2)$. Therefore $\mathfrak{Q}_1 \cap \mathfrak{Q}_2$ is primary.
