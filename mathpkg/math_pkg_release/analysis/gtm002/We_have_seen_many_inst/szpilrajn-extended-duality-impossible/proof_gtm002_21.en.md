---
role: proof
locale: en
of_concept: szpilrajn-extended-duality-impossible
source_book: gtm002
source_chapter: "21"
source_section: "The Extended Principle of Duality"
---

Suppose $f$ is such a mapping. Let $I$ be the unit interval, and let $E = f^{-1}(I)$. Then $E$ has the property of Baire. Let $x_1, x_2, \ldots$ be a countable dense subset of $E$, and let $I_i$ be an open interval containing $x_i$ such that

$$m(f(I_i) \cap I) < 1/2^{i+1}.$$

Put $G = \bigcup I_i$. Then $G$ is an open set and $E \subset \overline{G}$. Hence

$$E \subset (G \cap E) \cup (\overline{G} - G).$$

Therefore

$$I = f(E) \subset f(G \cap E) \cup f(\overline{G} - G) \subset \bigcup [f(I_i) \cap I] \cup f(\overline{G} - G).$$

Since $\overline{G} - G$ is nowhere dense, $f(\overline{G} - G)$ is a nullset, and so

$$m(I) \leq \sum m(f(I_i) \cap I) + m(f(\overline{G} - G)) < \sum 1/2^{i+1} + 0 = 1/2.$$

But $m(I) = 1$, a contradiction. Thus no such mapping $f$ exists. $\square$
