---
role: proof
locale: en
of_concept: "let-be-a-nonvoid-subset-of-such-that"
source_book: gtm025
source_chapter: "Extending Functionals"
source_section: "9.11"
---

Let $g_0 = \sup\{g: g \in \mathfrak{D}\}$, i.e., $g_0(x) = \sup\{g(x): g \in \mathfrak{D}\}$ for all $x \in X$. Then (7.22.iii) shows that $g_0 \in \mathfrak{M}^+$. There are two cases to consider.

Case I: $\{g_0\} \cup \mathfrak{D} \subset \mathfrak{C}_{00}^+$. Then the family $\{g_0 - g: g \in \mathfrak{D}\}$ satisfies the hypotheses of (9.6), for if $g_3 \geq \max\{g_1, g_2\}$, then

$$g_0 - g_3 \leq \min\{g_0 - g_1, g_0 - g_2\},$$

and

$$\inf\{g_0(x) - g(x): g \in \mathfrak{D}\} = g_0(x) - \sup\{g(x): g \in \mathfrak{D}\} = g_0(x) - g_0(x) = 0$$

for every $x \in X$. Then (9.6) implies that

$$0 = \inf\{I(g_0 - g): g \in \mathfrak{D}\} = \inf\{I(g_0)
