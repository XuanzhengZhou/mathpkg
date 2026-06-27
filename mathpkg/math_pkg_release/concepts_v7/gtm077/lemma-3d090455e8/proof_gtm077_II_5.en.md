---
role: proof
locale: en
of_concept: lemma-3d090455e8
source_book: gtm077
source_chapter: "II"
source_section: "5"
---
# Proof of Generalized Associative Law

**Lemma.** For an arbitrary integer $k \geq 3$, and arbitrary elements $A_1, A_2, \ldots, A_k$ of a group $\mathfrak{G}$,

$$A_1 \cdot A_2 \cdots A_k = A_1 \cdot (A_2 \cdot A_3 \cdots A_k).$$

*Proof.* We prove this by induction on $k$.

The product of $n+1$ elements is defined recursively by
$$A_1 \cdot A_2 \cdots A_{n+1} = (A_1 \cdot A_2 \cdots A_n) \cdot A_{n+1}.$$

**Base case $k = 3$.** By the definition of the product,
$$A_1 \cdot A_2 \cdot A_3 = (A_1 \cdot A_2) \cdot A_3.$$
Applying the associative law (axiom (ii)), we obtain
$$(A_1 \cdot A_2) \cdot A_3 = A_1 \cdot (A_2 \cdot A_3).$$
Thus the statement holds for $k = 3$.

**Inductive step.** Assume the statement holds for $k = n$ (with $n \geq 3$). Then for $k = n+1$:

$$\begin{aligned}
A_1 \cdot A_2 \cdots A_{n+1} &= (A_1 \cdot A_2 \cdots A_n) \cdot A_{n+1} \\
&= \bigl(A_1 \cdot (A_2 \cdot A_3 \cdots A_n)\bigr) \cdot A_{n+1} \quad \text{(by the induction hypothesis)}\\
&= A_1 \cdot \bigl((A_2 \cdot A_3 \cdots A_n) \cdot A_{n+1}\bigr) \quad \text{(by the associative law)}\\
&= A_1 \cdot (A_2 \cdot A_3 \cdots A_{n+1}) \quad \text{(by the definition of the product)}.
\end{aligned}$$

Thus the lemma holds for $k = n+1$, and by induction for all $k \geq 3$. $\square$

**Corollary (Shifting of Parentheses).** For $1 < l < k$,

$$(A_1 \cdots A_l)(A_{l+1} \cdots A_k) = (A_1 \cdots A_{l-1})(A_l \cdots A_k).$$

*Proof.* Write the first factor as $(A_1 \cdots A_{l-1}) \cdot A_l$ and apply the associative law:

$$\begin{aligned}
(A_1 \cdots A_l)(A_{l+1} \cdots A_k) &= \bigl((A_1 \cdots A_{l-1}) \cdot A_l\bigr) \cdot (A_{l+1} \cdots A_k)\\
&= (A_1 \cdots A_{l-1}) \cdot \bigl(A_l \cdot (A_{l+1} \cdots A_k)\bigr)\\
&= (A_1 \cdots A_{l-1})(A_l \cdots A_k).
\end{aligned}$$

By repeated application, the inner parentheses may be shifted arbitrarily far to the left, and consequently parentheses in a product of finitely many group elements may be placed arbitrarily without changing the result. $\square$
