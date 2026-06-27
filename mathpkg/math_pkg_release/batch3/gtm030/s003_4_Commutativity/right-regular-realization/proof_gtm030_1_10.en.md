---
role: proof
locale: en
of_concept: right-regular-realization
source_book: gtm030
source_chapter: "1"
source_section: "10"
---

Consider the product $a_r b_r$. This sends $x$ into $(xa)b$. By the associative law $(xa)b = x(ab)$. Thus $a_r b_r$ has the same effect as $(ab)_r$. Hence

$$a_r b_r = (ab)_r$$

is in $\mathfrak{G}_r$. We note next that $1_r$ is in $\mathfrak{G}_r$ (it is the identity mapping). Finally, $a_r(a^{-1})_r = 1_r = (a^{-1})_r a_r$, so $a_r^{-1} = (a^{-1})_r$ is in $\mathfrak{G}_r$. Thus $\mathfrak{G}_r$ is a transformation group.

Now consider the correspondence $a \to a_r$ of $\mathfrak{G}$ onto $\mathfrak{G}_r$. If $a \neq b$, then $1a_r = a \neq b = 1b_r$, hence $a_r \neq b_r$. Thus $a \to a_r$ is 1-1. Since $a_r b_r = (ab)_r$, the mapping preserves the group operation. Therefore $a \to a_r$ is an isomorphism.
