---
role: proof
locale: en
of_concept: well-definedness-of-conjugation
source_book: gtm050
source_chapter: "4"
source_section: "4.2"
---

If $f(\alpha) = g(\alpha)$ as cyclotomic integers, then the difference $f(\alpha) - g(\alpha)$ is a cyclotomic integer that equals zero. Let $\phi(\alpha) = 1 + \alpha + \alpha^2 + \cdots + \alpha^{\lambda-1}$. By the fundamental relation, $\phi(\alpha) = 0$. Moreover, any representation of a cyclotomic integer that equals zero differs from the zero representation by an integer multiple of $\phi(\alpha)$. Thus $f(\alpha) = g(\alpha) + c \cdot \phi(\alpha)$ for some integer $c$.

Now consider the substitution $\alpha \mapsto \alpha^j$ for $j = 2, 3, \ldots, \lambda-1$. Since $\phi(\alpha^j) = 1 + \alpha^j + \alpha^{2j} + \cdots + \alpha^{(\lambda-1)j}$, and since multiplication by $j$ modulo $\lambda$ (with $j \not\equiv 0 \pmod{\lambda}$) permutes the non-zero residues, the terms of $\phi(\alpha^j)$ are merely a permutation of the terms of $\phi(\alpha)$. Hence $\phi(\alpha^j) = \phi(\alpha) = 0$. Therefore
$$f(\alpha^j) = g(\alpha^j) + c \cdot \phi(\alpha^j) = g(\alpha^j) + c \cdot 0 = g(\alpha^j),$$
establishing the well-definedness of the conjugation map.
