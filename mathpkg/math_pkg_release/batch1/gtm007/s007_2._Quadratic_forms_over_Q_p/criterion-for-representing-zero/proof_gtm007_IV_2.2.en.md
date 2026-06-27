---
role: proof
locale: en
of_concept: criterion-for-representing-zero
source_book: gtm007
source_chapter: "IV"
source_section: "§2.2.2"
---

Write $f$ in the form $f \sim a_1 X_1^2 + \cdots + a_n X_n^2$ and consider separately the cases $n = 2, 3, 4$ and $n \geq 5$.

**i) The case $n = 2$.** The form $f \sim a_1 X_1^2 + a_2 X_2^2$ represents $0$ nontrivially if and only if $-a_1/a_2$ is a square. But $-a_1/a_2 = -a_1 a_2 = -d$ in $k^*/k^{*2}$. Hence the condition is $d = -1$ in $k^*/k^{*2}$. When this holds, $\varepsilon(f) = (a_1, a_2) = (a_1, -a_1) = 1$.

**ii) The case $n = 3$.** Write $f \sim a_1 X_1^2 + a_2 X_2^2 + a_3 X_3^2$ and consider $g = a_1 X_1^2 + a_2 X_2^2$, a form of rank $2$. Then $f$ represents $0$ iff $g$ represents $-a_3$. Applying the corollary for representing an element by a rank $2$ form, $g$ represents $-a_3$ iff $(-a_3, -d(g)) = \varepsilon(g)$, i.e., $(-a_3, -a_1 a_2) = (a_1, a_2)$. Using Hilbert symbol properties, $(-a_3, -a_1 a_2) = (-1, -a_1 a_2 a_3)(a_3, -a_1 a_2)$. Simplifying, this condition is equivalent to $\varepsilon(f) = (-1, -d)$.

**iii) The case $n = 4$.** Write $f \sim a_1 X_1^2 + a_2 X_2^2 + a_3 X_3^2 + a_4 X_4^2$ and decompose it as the sum of two binary forms: $a_1 X_1^2 + a_2 X_2^2$ and $-a_3 X_3^2 - a_4 X_4^2$.

By case (ii) of the corollary, an $x \in k^*/k^{*2}$ is represented by $a_1 X_1^2 + a_2 X_2^2$ iff $(x, -a_1 a_2) = (a_1, a_2)$, and by $-a_3 X_3^2 - a_4 X_4^2$ iff $(x, a_3 a_4) = (-a_3, -a_4)$.

Let $A$ be the subset of $k^*/k^{*2}$ defined by the first condition, and $B$ the subset defined by the second. The form $f$ represents $0$ iff $A \cap B \neq \varnothing$ (there exists $x$ represented by both parts). Now $A$ and $B$ are nonempty (e.g., $a_1 \in A$ and $-a_3 \in B$).

By part (c) of the lemma, $A \cap B = \varnothing$ iff $a_1 a_2 = a_3 a_4$ and $(a_1, a_2) = -(-a_3, -a_4)$.

The first condition means $d = 1$ (in $k^*/k^{*2}$). If $d = 1$, then:

$$\varepsilon = (a_1, a_2)(a_3, a_4)(a_3 a_4, a_3 a_4).$$

Using $(x, x) = (-1, x)$, we get $a_3 a_4 = a_1 a_2 = d = 1$ (mod squares), so:

$$\varepsilon = (a_1, a_2)(a_3, a_4)(-1, a_3 a_4) = (a_1, a_2)(-a_3, a_4)(-1, -1).$$

Hence the second condition $A \cap B = \varnothing$ is equivalent to $\varepsilon = -(-1, -1)$. Therefore $f$ represents $0$ iff either $d \neq 1$, or $d = 1$ and $\varepsilon = (-1, -1)$.

**iv) The case $n \geq 5$.** It suffices to treat $n = 5$. By the lemma and part (ii) of the corollary, one shows that any form in $5$ variables must represent $0$. The form can be decomposed as a sum of a binary and a ternary form; using the fact that every element is represented by a form in $3$ variables (since $n \geq 4$ in the representation corollary), one finds a nontrivial zero.
