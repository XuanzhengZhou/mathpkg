---
role: proof
locale: en
of_concept: group-product-associativity-lemma
source_book: gtm077
source_chapter: "II"
source_section: "5"
---
# Proof of Lemma: General Associativity of Group Products

**Lemma.** For an arbitrary integer $k \geq 3$, and arbitrary elements $A_1, A_2, \ldots, A_k$ of a group $\mathfrak{G}$,

$$A_1 \cdot A_2 \cdots A_k = A_1 \cdot (A_2 \cdot A_3 \cdots A_k).$$

*Proof.* By induction on $k$.

**Base case $k = 3$.** By the definition of the product, $A_1 \cdot A_2 \cdot A_3 = (A_1 \cdot A_2) \cdot A_3$. By the associative law (axiom (ii)), $(A_1 \cdot A_2) \cdot A_3 = A_1 \cdot (A_2 \cdot A_3)$. Thus the statement holds for $k = 3$.

**Inductive step.** Assume the statement holds for $k = n$ ($n \geq 3$). For $k = n+1$:

$$\begin{aligned}
A_1 \cdot A_2 \cdots A_{n+1} &= (A_1 \cdot A_2 \cdots A_n) \cdot A_{n+1} \\
&= \bigl(A_1 \cdot (A_2 \cdot A_3 \cdots A_n)\bigr) \cdot A_{n+1} \quad \text{(induction hypothesis)}\\
&= A_1 \cdot \bigl((A_2 \cdot A_3 \cdots A_n) \cdot A_{n+1}\bigr) \quad \text{(associative law)}\\
&= A_1 \cdot (A_2 \cdot A_3 \cdots A_{n+1}).
\end{aligned}$$

Hence the statement holds for $k = n+1$, completing the induction.

**Corollary (Shifting of Parentheses).** For $1 < l < k$, inner parentheses can be shifted one place to the left:

$$(A_1 \cdots A_l)(A_{l+1} \cdots A_k) = (A_1 \cdots A_{l-1})(A_l \cdots A_k).$$

*Proof.* Decompose the first factor by the product definition and reassociate:

$$\begin{aligned}
(A_1 \cdots A_l)(A_{l+1} \cdots A_k) &= \bigl((A_1 \cdots A_{l-1}) \cdot A_l\bigr) \cdot (A_{l+1} \cdots A_k) \\
&= (A_1 \cdots A_{l-1}) \cdot \bigl(A_l \cdot (A_{l+1} \cdots A_k)\bigr) \\
&= (A_1 \cdots A_{l-1})(A_l \cdots A_k). \quad \square
\end{aligned}$$

By repeated shifting, parentheses may be placed arbitrarily in a product of finitely many group elements.
