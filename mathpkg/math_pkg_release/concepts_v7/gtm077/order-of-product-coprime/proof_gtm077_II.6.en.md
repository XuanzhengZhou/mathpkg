---
role: proof
locale: en
of_concept: order-of-product-coprime
source_book: gtm077
source_chapter: "II"
source_section: "6"
---

# Proof: Order of a Product of Commuting Elements with Coprime Orders

**Theorem.** Let $A$ and $B$ be commuting elements of a group $\mathfrak{G}$ with orders $a$ and $b$ respectively, where $(a, b) = 1$. Then the order of the product $AB$ is $ab$.

**Proof.** Let $c$ denote the order of $AB$.

**Step 1: Upper bound $c \mid ab$.** Since $A$ and $B$ commute, we have

$$(AB)^{ab} = A^{ab} B^{ab} = (A^a)^b (B^b)^a = E^b \cdot E^a = E.$$

Hence the order $c$ of $AB$ divides $ab$.

**Step 2: Lower bound $ab \mid c$.** We show that both $a \mid c$ and $b \mid c$, which together with $(a, b) = 1$ implies $ab \mid c$.

Since $(AB)^c = E$, we have $A^c B^c = E$, so $A^c = B^{-c}$. Let this common value be $X$.

Now $X^a = (A^c)^a = (A^a)^c = E^c = E$. Also $X^b = (B^{-c})^b = (B^b)^{-c} = E^{-c} = E$.

Thus the order of $X$ divides both $a$ and $b$. Since $(a, b) = 1$, the order of $X$ must be 1, so $X = E$.

Therefore $A^c = E$ and $B^c = E$, which implies $a \mid c$ and $b \mid c$. Because $a$ and $b$ are coprime, $ab \mid c$.

**Step 3: Conclusion.** From $c \mid ab$ (Step 1) and $ab \mid c$ (Step 2), we obtain $c = ab$. ∎
