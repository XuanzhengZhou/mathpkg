---
role: proof
locale: en
of_concept: semisimple-hereditary
source_book: gtm004
source_chapter: "VII"
source_section: "5"
---

# Proof that Semi-simplicity is Hereditary

**Corollary 5.5.** Every ideal and every quotient of a semi-simple Lie algebra is semi-simple.

**Proof.** Let $\mathfrak{g}$ be a semi-simple Lie algebra and let $\mathfrak{a} \subset \mathfrak{g}$ be an ideal.

**Part 1: $\mathfrak{a}$ is semi-simple.** Let $\mathfrak{b} \subset \mathfrak{a}$ be an abelian ideal of $\mathfrak{a}$. Since $\mathfrak{a}$ is an ideal of $\mathfrak{g}$, for any $x \in \mathfrak{g}$ and $y \in \mathfrak{b}$, we have $[x, y] \in \mathfrak{a}$. But we need to show $\mathfrak{b}$ is an ideal of $\mathfrak{g}$.

By Corollary 5.4, $\mathfrak{a}$ has a complementary ideal $\mathfrak{c}$ in $\mathfrak{g}$, so $\mathfrak{g} = \mathfrak{a} \oplus \mathfrak{c}$. For any $x \in \mathfrak{g}$, write $x = a + c$ with $a \in \mathfrak{a}$, $c \in \mathfrak{c}$. For $y \in \mathfrak{b}$,

$$[x, y] = [a, y] + [c, y].$$

Since $\mathfrak{a}$ and $\mathfrak{c}$ are ideals, $[c, y] \in \mathfrak{a} \cap \mathfrak{c} = \{0\}$ (as $y \in \mathfrak{a}$ and $c \in \mathfrak{c}$ implies $[c, y] \in \mathfrak{a} \cap \mathfrak{c}$). Also $[a, y] \in \mathfrak{b}$ since $\mathfrak{b}$ is an ideal of $\mathfrak{a}$. Hence $[x, y] \in \mathfrak{b}$, so $\mathfrak{b}$ is an ideal of $\mathfrak{g}$.

Now $\mathfrak{b}$ is an abelian ideal of the semi-simple Lie algebra $\mathfrak{g}$, hence $\mathfrak{b} = \{0\}$. Therefore $\mathfrak{a}$ has no non-zero abelian ideals, so $\mathfrak{a}$ is semi-simple.

**Part 2: $\mathfrak{g}/\mathfrak{a}$ is semi-simple.** By Proposition 6.6, $\mathfrak{g}/\mathfrak{r}$ is semi-simple where $\mathfrak{r}$ is the radical. However, for a direct proof: the quotient map $\pi : \mathfrak{g} \to \mathfrak{g}/\mathfrak{a}$ splits by Corollary 5.4 (since $\mathfrak{a}$ has a complement $\mathfrak{c} \cong \mathfrak{g}/\mathfrak{a}$), and $\mathfrak{c}$ is an ideal of $\mathfrak{g}$, hence semi-simple by Part 1. Thus $\mathfrak{g}/\mathfrak{a} \cong \mathfrak{c}$ is semi-simple. $\square$
