---
role: proof
locale: en
of_concept: hahn-banach-theorem
source_book: gtm025
source_chapter: "4"
source_section: "14"
---

The proof uses Zorn's lemma. Consider the set of all linear extensions of $f$ that are still dominated by $p$, partially ordered by inclusion. Every chain has an upper bound (the union), so a maximal extension $g$ exists by Zorn's lemma. If the domain $G$ of $g$ is not all of $E$, choose $y \in E \setminus G$. The key step is to extend $g$ to $G \oplus \mathbb{R}y$ by defining $h(x + \alpha y) = g(x) + \alpha c$ for a suitable constant $c$ satisfying $\sup_{u \in G}(g(u) - p(u - y)) \le c \le \inf_{v \in G}(-g(v) + p(v + y))$. Such a $c$ exists because $g(u) + g(v) = g(u+v) \le p(u+v) \le p(u-y) + p(v+y)$. This contradicts maximality, so $G = E$.
