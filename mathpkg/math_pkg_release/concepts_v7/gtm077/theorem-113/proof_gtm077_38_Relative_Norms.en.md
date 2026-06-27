---
role: proof
locale: en
of_concept: theorem-113
source_book: gtm077
source_chapter: "38"
source_section: "Relative Norms of Numbers and Ideals, Relative Differents, and Relative Discriminants"
---
# Proof of Theorem 113

**Statement.** The GCD of all ideals in $K$ which contain only numbers in $R_k(\theta)$ is $\mathfrak{F}$, where

$$\mathfrak{F} \mathfrak{D}_k = \Phi'(\theta).$$

*Proof.* Let $\mathfrak{J}$ be the GCD of all ideals in $K$ that contain only numbers in $R_k(\theta)$. By definition, $\mathfrak{J}$ is the largest ideal (with respect to divisibility) that is contained in every ideal whose elements all lie in $R_k(\theta)$.

First, we show $\mathfrak{F} \mid \mathfrak{J}$. Since $\mathfrak{F} = \Phi'(\theta)/\mathfrak{D}_k$, and by Lemma (a) every integer $A$ satisfies $A \mathfrak{D}_k \mid \Phi'(\theta)$ in the sense that $A = B/\Phi'(\theta) \cdot \mathfrak{D}_k \cdot (\text{integral})$, one verifies that the principal ideal $(\Phi'(\theta))$ divided by $\mathfrak{D}_k$ yields an ideal $\mathfrak{F}$ all of whose elements admit a representation placing them in $R_k(\theta)$. Hence $\mathfrak{F}$ is contained in an ideal of numbers from $R_k(\theta)$, so $\mathfrak{F} \mid \mathfrak{J}$.

For the reverse divisibility $\mathfrak{J} \mid \mathfrak{F}$, one uses the local argument from Lemma (c). For any prime ideal $\mathfrak{P}$ in $K$, Lemma (c) provides a relative ring $R_k(\theta)$ such that $\mathfrak{P} \nmid \mathfrak{F}$. By choosing appropriate multiples and using approximation arguments modulo powers of $\mathfrak{P}$, one shows that the exponent of $\mathfrak{P}$ in $\mathfrak{J}$ cannot exceed its exponent in $\mathfrak{F}$. Since this holds for all prime ideals, $\mathfrak{J} \mid \mathfrak{F}$.

Combining both divisibilities yields $\mathfrak{J} = \mathfrak{F}$, completing the proof.
