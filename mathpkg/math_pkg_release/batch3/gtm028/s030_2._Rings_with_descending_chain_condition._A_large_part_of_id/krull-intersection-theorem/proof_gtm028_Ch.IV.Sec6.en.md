---
role: proof
locale: en
of_concept: krull-intersection-theorem
source_book: gtm028
source_chapter: "IV"
source_section: "§6. Krull's intersection theorem"
---

Let $\mathfrak{a} = \bigcap_n \mathfrak{m}^n$. Since $\mathfrak{a} \subset \mathfrak{m}$, we have $\mathfrak{a} \subset \mathfrak{m}\mathfrak{a}$? More precisely, by the Artin-Rees property of Noetherian rings, there exists $k$ such that $\mathfrak{m}^n \cap \mathfrak{a} = \mathfrak{m}^{n-k}(\mathfrak{m}^k \cap \mathfrak{a})$ for $n \geq k$. Taking $n$ large, one shows $\mathfrak{a} = \mathfrak{m}\mathfrak{a}$.

If $\mathfrak{a} \neq (0)$, then $\mathfrak{a} = \mathfrak{m}\mathfrak{a}$ with $\mathfrak{a}$ finitely generated (since $R$ is Noetherian). By the determinant trick (or a lemma about finitely generated modules), there exists $z \in \mathfrak{m}$ such that $(1-z)\mathfrak{a} = (0)$. Since $\mathfrak{a} \neq (0)$, $1-z$ is a zero-divisor, and $1-z \in 1-\mathfrak{m}$.

Conversely, if $1-z$ is a zero-divisor for some $z \in \mathfrak{m}$, then $(1-z)c = 0$ for some nonzero $c$. Then $c = zc = z^2c = \cdots$, so $c \in \bigcap_n \mathfrak{m}^n$, proving the intersection is nonzero.
