---
role: proof
locale: en
of_concept: quotient-ring-module-construction
source_book: gtm030
source_chapter: "VI"
source_section: "2"
---

Let $a_1$ and $a_2$ be any two elements of $\mathfrak{A}$ that belong to the same coset modulo $\mathfrak{U}$. Then $a_2 = a_1 + u$ for some $u \in \mathfrak{U}$. Since $\mathfrak{U}$ annihilates $\mathfrak{M}$, for any $x \in \mathfrak{M}$ we have $a_2 x = a_1 x + u x = a_1 x$. It follows that the product

$$(a + \mathfrak{U})x = ax$$

is single-valued from $\mathfrak{A}/\mathfrak{U} \times \mathfrak{M}$ into $\mathfrak{M}$.

Now we verify the module axioms. For $1_l$: $(a + \mathfrak{U})(x + y) = a(x + y) = ax + ay = (a + \mathfrak{U})x + (a + \mathfrak{U})y$. For $2_l$: $((a + \mathfrak{U}) + (b + \mathfrak{U}))x = (a + b + \mathfrak{U})x = (a + b)x = ax + bx = (a + \mathfrak{U})x + (b + \mathfrak{U})x$. For $3_l$: $((a + \mathfrak{U})(b + \mathfrak{U}))x = (ab + \mathfrak{U})x = (ab)x = a(bx) = (a + \mathfrak{U})((b + \mathfrak{U})x)$. Hence $\mathfrak{M}$ is indeed an $\mathfrak{A}/\mathfrak{U}$-module.
