---
role: proof
locale: en
of_concept: li-ideals-lemma
source_book: gtm028
source_chapter: "IV"
source_section: "1"
---

\textbf{Part 1: $L_i(\mathfrak{A})$ is an ideal and $L_i(\mathfrak{A}) \subseteq L_{i+1}(\mathfrak{A})$.}
Let $f(x), g(x) \in \mathfrak{A}$ be elements of degree $i$ with leading coefficients $a, b \in R$ respectively. Then $f(x) + g(x) \in \mathfrak{A}$ and has degree at most $i$; its coefficient of $x^i$ is either $a+b$ (if degree equals $i$) or determined by lower-degree cancellation. In any case, $a+b \in L_i(\mathfrak{A})$. For any $c \in R$, $c f(x) \in \mathfrak{A}$ and has $ca$ as the coefficient of $x^i$, so $ca \in L_i(\mathfrak{A})$. This shows $L_i(\mathfrak{A})$ is an ideal.

To see $L_i(\mathfrak{A}) \subseteq L_{i+1}(\mathfrak{A})$, note that $x f(x) \in \mathfrak{A}$ has degree $i+1$ with the same leading coefficient $a$. Thus every $a \in L_i(\mathfrak{A})$ also belongs to $L_{i+1}(\mathfrak{A})$.

\textbf{Part 2: Equality of leading-coefficient ideals implies equality of ideals.}
Assume $\mathfrak{A} \subseteq \mathfrak{B}$ and $L_i(\mathfrak{A}) = L_i(\mathfrak{B})$ for all $i$. Let $g(x) \in \mathfrak{B}$ have degree $i$. Since $L_i(\mathfrak{A}) = L_i(\mathfrak{B})$, there exists $f_i(x) \in \mathfrak{A}$ of degree $i$ with the same leading coefficient as $g(x)$. Then $g(x) - f_i(x) \in \mathfrak{B}$ has degree at most $i-1$. By descending induction on degree, we construct a finite linear combination of elements of $\mathfrak{A}$ that equals $g(x)$, showing $g(x) \in \mathfrak{A}$. Hence $\mathfrak{A} = \mathfrak{B}$.
