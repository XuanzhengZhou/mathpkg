---
role: proof
locale: en
of_concept: ring-is-field-iff-only-two-ideals
source_book: gtm028
source_chapter: "IV"
source_section: "1"
---

($\Rightarrow$) Suppose $R$ is a field. Let $\mathfrak{A}$ be an ideal in $R$ with $\mathfrak{A} \neq (0)$. Pick $a \in \mathfrak{A}$, $a \neq 0$. Since $R$ is a field, $a^{-1}$ exists. For any $b \in R$, we have $b = b \cdot 1 = b(a^{-1}a) = (ba^{-1})a \in \mathfrak{A}$ (since $a \in \mathfrak{A}$ and $\mathfrak{A}$ is an ideal). Hence $\mathfrak{A} = R$. The only ideals are $(0)$ and $R$.

($\Leftarrow$) Suppose $R$ has identity $1$ and the only ideals are $(0)$ and $R$. Let $a \in R$, $a \neq 0$. The principal ideal $Ra$ is not the zero ideal (since $a = 1 \cdot a \in Ra$). Therefore $Ra = R$. In particular, $1 \in Ra$, so $1 = xa$ for some $x \in R$. Thus $a$ has a left inverse $x$. Since $R$ is commutative, $x$ is also a right inverse, and $a$ is a unit. Hence every nonzero element is a unit, and $R$ is a field.
