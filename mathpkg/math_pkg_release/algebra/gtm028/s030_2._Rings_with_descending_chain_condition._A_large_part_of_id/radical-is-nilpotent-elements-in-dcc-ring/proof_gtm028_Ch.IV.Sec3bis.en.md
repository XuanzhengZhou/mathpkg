---
role: proof
locale: en
of_concept: radical-is-nilpotent-elements-in-dcc-ring
source_book: gtm028
source_chapter: "IV"
source_section: "§3bis. Alternative method for studying rings with d.c.c."
---

Let $a$ be a nilpotent element of $R$, so $a^h = 0$ for some $h$. Since $a^h$ belongs to every ideal of $R$, $a$ belongs to every prime ideal of $R$, hence $a \in \mathfrak{r}$.

Conversely, if $a \in \mathfrak{r}$, apply the d.c.c. to the descending sequence of principal ideals $(a^n)$. There exist an integer $h$ and an element $x \in R$ such that $a^h = xa^{h+1}$, i.e., $(1 - xa)a^h = 0$. Since $a \in \mathfrak{r}$, by Lemma 2, $1 - xa$ is a unit, so $a^h = 0$. Thus $a$ is nilpotent.
