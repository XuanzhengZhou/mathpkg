---
role: proof
locale: en
of_concept: group-associativity-lemma
source_book: gtm077
source_chapter: "II"
source_section: "5"
---
# Proof of Generalized Associativity in Groups

**Lemma.** For an arbitrary integer $k \geq 3$, and arbitrary elements $A_1, A_2, \ldots, A_k$ of a group $\mathfrak{G}$,

$$A_1 \cdot A_2 \cdots A_k = A_1 \cdot (A_2 \cdot A_3 \cdots A_k).$$

*Proof.* We proceed by induction on $k$.

For $k = 3$, the result follows directly from the associative law (axiom (ii)): by definition $A_1 \cdot A_2 \cdot A_3 = (A_1 \cdot A_2) \cdot A_3$, and the associative law gives $(A_1 \cdot A_2) \cdot A_3 = A_1 \cdot (A_2 \cdot A_3)$.

Assume the statement holds for $k = n$ (where $n \geq 3$). Then for $k = n+1$:

$$\begin{aligned}
A_1 \cdot A_2 \cdots A_{n+1} &= (A_1 \cdot A_2 \cdots A_n) \cdot A_{n+1} \quad &\text{(definition of product of $n+1$ elements)}\\
&= \bigl(A_1 \cdot (A_2 \cdot A_3 \cdots A_n)\bigr) \cdot A_{n+1} \quad &\text{(induction hypothesis)}\\
&= A_1 \cdot \bigl((A_2 \cdot A_3 \cdots A_n) \cdot A_{n+1}\bigr) \quad &\text{(associative law (ii))}\\
&= A_1 \cdot (A_2 \cdot A_3 \cdots A_{n+1}) \quad &\text{(definition of product)}.
\end{aligned}$$

Thus the statement holds for $k = n+1$. By induction, the lemma is proved for all $k \geq 3$.

**Corollary (Shifting of Parentheses).** For $1 < l < k$,

$$(A_1 \cdot A_2 \cdots A_l)(A_{l+1} \cdots A_k) = (A_1 \cdot A_2 \cdots A_{l-1})(A_l \cdot A_{l+1} \cdots A_k).$$

*Proof.* Using the recursive definition of the product and the associative law:

$$\begin{aligned}
(A_1 \cdot A_2 \cdots A_l)(A_{l+1} \cdots A_k) &= \bigl((A_1 \cdot A_2 \cdots A_{l-1}) \cdot A_l\bigr) \cdot (A_{l+1} \cdots A_k)\\
&= (A_1 \cdot A_2 \cdots A_{l-1}) \cdot \bigl(A_l \cdot (A_{l+1} \cdots A_k)\bigr)\\
&= (A_1 \cdot A_2 \cdots A_{l-1})(A_l \cdot A_{l+1} \cdots A_k).
\end{aligned}$$

By repeated application, parentheses in a product of arbitrarily many elements may be placed arbitrarily without changing the result. $\square$
