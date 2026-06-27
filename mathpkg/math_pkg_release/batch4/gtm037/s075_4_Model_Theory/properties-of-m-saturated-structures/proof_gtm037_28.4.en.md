---
role: proof
locale: en
of_concept: properties-of-m-saturated-structures
source_book: gtm037
source_chapter: "28"
source_section: "4. Model Theory"
---

These properties are elementary consequences of the definition of $m$-saturatedness and are stated without proof in the text, being described as "trivial properties" that are "useful in applications."

(i) If $\mathfrak{A}$ is $m$-saturated, then for any $n \leq m$ and any $X \subseteq A$ with $|X| < n \leq m$, the $m$-saturatedness condition applied to $X$ (since $|X| < m$) gives the $n$-saturatedness condition. Conversely, if $\mathfrak{A}$ is $n$-saturated for every $n \leq m$, then for any $X \subseteq A$ with $|X| < m$, choose $n = |X|^+ \leq m$; the $n$-saturatedness applies.

(ii) If $m$ is a limit cardinal, $m$-saturatedness implies $n$-saturatedness for all $n < m$ by part (i). Conversely, if $\mathfrak{A}$ is $n$-saturated for all $n < m$, then for any $X \subseteq A$ with $|X| < m$, there exists $n < m$ with $|X| < n$ (since $m$ is a limit cardinal), and $n$-saturatedness applies.

(iii) $\mathfrak{A}$ is $m$-saturated means every type over a set of $< m$ parameters is realized. This is equivalent to: for every $X \subseteq A$ with $|X| < m$, every type over $\emptyset$ in the expanded language (with constants for $X$) is realized in the expanded structure, which is precisely $0$-saturatedness of $(\mathfrak{A}, x)_{x \in X}$.

(iv) If $\mathfrak{A}$ is $m$-saturated and $|X| < m$, then for any $Y \subseteq A$ with $|Y| < m$, the set $X \cup Y$ has cardinality $< m$ (since $m$ is infinite), so any type over $Y$ with parameters from $X$ corresponds to a type over $X \cup Y$ in the original structure, which is realized by $m$-saturatedness of $\mathfrak{A}$.
