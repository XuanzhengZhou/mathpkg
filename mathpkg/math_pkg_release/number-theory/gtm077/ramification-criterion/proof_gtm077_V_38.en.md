---
role: proof
locale: en
of_concept: ramification-criterion
source_book: gtm077
source_chapter: "V"
source_section: "§38"
---
# Proof of Theorem 114: Ramification Criterion via the Different

**Theorem 114.** Let $\mathfrak{P}$ be a prime ideal in $K$ dividing the prime ideal $\mathfrak{p}$ in $k$ to the power $e > 1$. Then $\mathfrak{P}$ divides the relative different $\mathfrak{D}_k$.

**Proof.** Let $\mathfrak{p}$ be a prime ideal in $k$ and let

$$\mathfrak{p} = \mathfrak{P}^e \mathfrak{P}_2^{e_2} \cdots \mathfrak{P}_r^{e_r}$$

be the decomposition of $\mathfrak{p}$ into prime ideals in $K$, with $e \geq 1$ being the ramification index of $\mathfrak{P}$. We need to show that if $e > 1$, then $\mathfrak{P} \mid \mathfrak{D}_k$.

Let $\alpha$ be a nonintegral number in $k$ with ideal denominator $\mathfrak{p}$; that is,

$$\alpha = \frac{\mathfrak{a}}{\mathfrak{p}}, \quad (\mathfrak{a}, \mathfrak{p}) = 1.$$

Such an $\alpha$ exists because we can take any number whose denominator (in the sense of fractional ideals) is exactly $\mathfrak{p}$. For instance, choose an element $\pi \in \mathfrak{p} \setminus \mathfrak{p}^2$ and set $\alpha = \mathfrak{a}/\mathfrak{p}$ with $\mathfrak{a}$ chosen appropriately.

Consider the set $\mathfrak{P}^{e-1}\mathfrak{A}$ where $\mathfrak{A}$ is an ideal prime to $\mathfrak{P}$ such that $\mathfrak{P}^{e-1}\mathfrak{A} = \mathfrak{a}/\mathfrak{P}$ (in the sense of fractional ideals). Let $A$ run through all numbers of $\mathfrak{P}^{e-1}\mathfrak{A}$, that is, all numbers of $\mathfrak{a}/\mathfrak{P}$.

For each such $A$, consider the product $\alpha A$. Since $\alpha$ has denominator $\mathfrak{p}$ and $A$ has denominator $\mathfrak{P}$ (in the fractional sense), the product $\alpha A$ is integral in $K$. Moreover, $\alpha A$ belongs to the ideal $\mathfrak{P}^{e-1}$.

Now compute the relative trace:

$$\alpha S_k(A) = S_k(\alpha A).$$

Since $\alpha$ lies in $k$, it commutes with the relative trace. The right-hand side $S_k(\alpha A)$ is the relative trace of an integral number $\alpha A \in K$, hence it is an integer in $k$. Therefore, $\alpha S_k(A)$ is integral in $k$ for all $A \in \mathfrak{P}^{e-1}\mathfrak{A}$.

But $\alpha$ is nonintegral (it has denominator $\mathfrak{p}$). This forces $S_k(A)$ to contain a factor of $\mathfrak{p}$ in its denominator to compensate. More precisely, the condition that $\alpha S_k(A)$ is integral for all such $A$ implies, by the definition of the relative different, that the elements of the complementary module are not all integral. Hence $\mathfrak{P}$ divides the relative different $\mathfrak{D}_k$.

The converse of Theorem 114 is also valid (if $\mathfrak{P} \mid \mathfrak{D}_k$, then $e > 1$) but is more difficult to prove. It holds in full generality, though here we only treat the special case of relative Galois fields $K$ (see Theorem 115).
