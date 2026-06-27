---
role: proof
locale: en
of_concept: radical-ideal-properties
source_book: gtm028
source_chapter: "III"
source_section: "§7"
---

That $\mathfrak{A} \subset \sqrt{\mathfrak{A}}$ is obvious. To show that $\sqrt{\mathfrak{A}}$ is an ideal, let $b, c \in \sqrt{\mathfrak{A}}$, so that $b^m \in \mathfrak{A}, c^n \in \mathfrak{A}$ for some integers $m, n$. In the binomial expansion of $(b-c)^{m+n-1}$ every term has a factor $b^i c^j$, with $i + j = m + n - 1$. Since either $i \geq m$ or $j \geq n$, either $b^i$ or $c^j$ is in $\mathfrak{A}$, hence $(b-c)^{m+n-1} \in \mathfrak{A}$, and $b - c \in \sqrt{\mathfrak{A}}$. If $b \in \sqrt{\mathfrak{A}}$, and $d \in R$, then $b^m \in \mathfrak{A}$ for some $m$; hence $(db)^m \in \mathfrak{A}$ and $db \in \sqrt{\mathfrak{A}}$. Thus $\sqrt{\mathfrak{A}}$ is indeed an ideal.

Suppose $\mathfrak{A}^k \subset \mathfrak{B}$. If $c \in \sqrt{\mathfrak{A}}$, then $c^m \in \mathfrak{A}$ for some $m$, $c^{mk} \in \mathfrak{A}^k \subset \mathfrak{B}$, hence $c \in \sqrt{\mathfrak{B}}$.

Since $\mathfrak{AB} \subset \mathfrak{A} \cap \mathfrak{B}$, and $\mathfrak{A} \cap \mathfrak{B}$ is contained in $\mathfrak{A}$ and in $\mathfrak{B}$, we have $\sqrt{\mathfrak{AB}} \subset \sqrt{\mathfrak{A} \cap \mathfrak{B}} \subset \sqrt{\mathfrak{A}} \cap \sqrt{\mathfrak{B}}$. Conversely, if $c \in \sqrt{\mathfrak{A}} \cap \sqrt{\mathfrak{B}}$, then $c^m \in \mathfrak{A}$ and $c^n \in \mathfrak{B}$ for some $m, n$, hence $c^{m+n} \in \mathfrak{AB}$, so $c \in \sqrt{\mathfrak{AB}}$.
