---
role: proof
locale: en
of_concept: ideal-quotient-criterion
source_book: gtm028
source_chapter: "IV"
source_section: "§5. Uniqueness theorems"
---

Let $\mathfrak{a} = \bigcap_i \mathfrak{q}_i$ be an irredundant primary representation of $\mathfrak{a}$, $\mathfrak{p}_i = \sqrt{\mathfrak{q}_i}$.

If $\mathfrak{b}$ is contained in no $\mathfrak{p}_i$, then from $(\mathfrak{a} : \mathfrak{b})\mathfrak{b} \subset \mathfrak{a} \subset \mathfrak{q}_i$, we deduce $\mathfrak{a} : \mathfrak{b} \subset \mathfrak{q}_i : \mathfrak{b} = \mathfrak{q}_i$ for all $i$ (since $\mathfrak{b} \not\subset \mathfrak{p}_i$ implies $\mathfrak{q}_i : \mathfrak{b} = \mathfrak{q}_i$). Hence $\mathfrak{a} : \mathfrak{b} \subset \bigcap_i \mathfrak{q}_i = \mathfrak{a}$, and since $\mathfrak{a} \subset \mathfrak{a} : \mathfrak{b}$ always, we get equality.

Conversely, if $\mathfrak{b} \subset \mathfrak{p}_i$ for some $i$, then there exists a power $\mathfrak{b}^n \subset \mathfrak{q}_i$. Then one can show $\mathfrak{a} : \mathfrak{b} \supsetneq \mathfrak{a}$.
