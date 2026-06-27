---
role: proof
locale: en
of_concept: nilpotent-element-ideal-is-nilpotent-in-dcc-ring
source_book: gtm028
source_chapter: "IV"
source_section: "§3bis. Alternative method for studying rings with d.c.c."
---

Apply the d.c.c. to the descending sequence $\{\mathfrak{a}^n\}$. There exists an exponent $h$ such that $\mathfrak{b} = \mathfrak{a}^h = \mathfrak{a}^{h+1} = \cdots$. Suppose $\mathfrak{b} \neq (0)$, and consider the family $\mathcal{F}$ of all ideals $\mathfrak{w}$ in $R$ such that $\mathfrak{b}\mathfrak{w} \neq (0)$. Since $\mathfrak{b}^2 = \mathfrak{b} \neq (0)$, we have $\mathfrak{b} \in \mathcal{F}$, so $\mathcal{F}$ is non-empty. By the d.c.c., $\mathcal{F}$ admits a minimal element $\mathfrak{v}$.

Since $\mathfrak{b}\mathfrak{v} \neq (0)$, there exists $c \in \mathfrak{v}$ such that $\mathfrak{b}c \neq (0)$. The ideal $\mathfrak{b}c$ is contained in $\mathfrak{v}$ and satisfies $\mathfrak{b}(\mathfrak{b}c) \neq (0)$, so by minimality $\mathfrak{v} = \mathfrak{b}c$. Hence $c = bc'$ for some $c' \in \mathfrak{v}$, giving $c = b^n c^{(n)}$ for all $n$. But $b \in \mathfrak{b} = \mathfrak{a}^h$ so $b$ is a sum of products of elements of $\mathfrak{a}$, hence nilpotent. This implies $c = 0$, contradicting $\mathfrak{b}c \neq (0)$. Thus $\mathfrak{b} = (0)$, so $\mathfrak{a}^h = (0)$.
