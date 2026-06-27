---
role: proof
locale: en
of_concept: ideal-filter-correspondence
source_book: gtm037
source_chapter: "9"
source_section: "2"
---

(i) Let $I$ be an ideal. If $x \in I^f$, then $-x \in I$. For $x \leq y$ with $x \in I^f$, we have $-x \in I$. Since $-y \leq -x$ and $I$ is an ideal, $-y \in I$, so $y \in I^f$. If $x, y \in I^f$, then $-x, -y \in I$, so $-x + -y = -(x \cdot y) \in I$, hence $x \cdot y \in I^f$. Thus $I^f$ is a filter.

(ii) Let $F$ be a filter. If $x \in F^i$, then $-x \in F$. For $x \leq y$ with $y \in F^i$, we have $-y \in F$. Since $F$ is a filter and $-y \leq -x$, $-x \in F$, so $x \in F^i$. If $x, y \in F^i$, then $-x, -y \in F$, so $(-x) \cdot (-y) = -(x + y) \in F$, hence $x + y \in F^i$. Thus $F^i$ is an ideal.

(iii) $I^{fi} = \{x : -x \in I^f\} = \{x : --x \in I\} = \{x : x \in I\} = I$.

(iv) $F^{if} = \{x : -x \in F^i\} = \{x : --x \in F\} = \{x : x \in F\} = F$.
