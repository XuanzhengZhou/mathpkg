---
role: proof
locale: en
of_concept: relative-norm-of-different
source_book: gtm077
source_chapter: "V"
source_section: "§38"
---
# Proof of Theorem 113

**Theorem 113.** The GCD of all ideals in $K$ which contain only numbers in $R_k(\theta)$ is $\mathfrak{F}$, where $\mathfrak{F}\mathfrak{D}_k = \Phi'(\theta)$.

**Proof.** Let $\theta$ be an integer generating $K$ over $k$, with $\Phi(x)$ the minimal polynomial of $\theta$ over $k$. The relative ring $R_k(\theta)$ is the set of all $k$-linear combinations

$$\alpha_0 + \alpha_1\theta + \cdots + \alpha_{m-1}\theta^{m-1}$$

with $\alpha_j$ integers in $k$.

Consider the complementary module of $R_k(\theta)$ with respect to the relative trace form $S_k$. By the general theory of the different (cf. §36, absolute case), the numbers

$$\frac{1}{\Phi'(\theta)}, \frac{\theta}{\Phi'(\theta)}, \ldots, \frac{\theta^{m-1}}{\Phi'(\theta)}$$

form a basis of the complementary module. Hence, for any number $\Delta$ in $K$, the condition that $\Delta$ belongs to the complementary module (i.e., $S_k(\Delta \cdot R_k(\theta))$ is integral) is equivalent to $\Delta \Phi'(\theta) \in R_k(\theta)$.

Now, by definition, the relative different $\mathfrak{D}_k$ is the reciprocal of the complementary module of the full ring of integers of $K$. The ring $R_k(\theta)$ is contained in the full ring of integers, with equality only when $\theta$ generates the full ring of integers.

The conductor $\mathfrak{F}$ is defined by the property that an element belongs to the full ring of integers if and only if when multiplied by $\mathfrak{F}$ it lies in $R_k(\theta)$. More precisely, $\mathfrak{F}$ is the GCD of all ideals $\mathfrak{A}$ in $K$ such that $\mathfrak{A} \subseteq R_k(\theta)$. From Lemma (a), we know that $\mathfrak{D}_k \mid \Phi'(\theta)$. Let $\mathfrak{F}$ be the ideal such that

$$\mathfrak{F} \mathfrak{D}_k = \Phi'(\theta).$$

Then $\mathfrak{F}$ is exactly the GCD of all ideals contained in $R_k(\theta)$, because:

1. If $\mathfrak{A} \subseteq R_k(\theta)$ is an ideal, then for any $A \in \mathfrak{A}$, Lemma (a) gives a representation, and $\mathfrak{A} \mid \mathfrak{F}$ follows.
2. Conversely, $\mathfrak{F}$ itself is contained in $R_k(\theta)$ by Lemma (b), since for $B \in R_k(\theta)$, $B/\Phi'(\theta) = B/(\mathfrak{F}\mathfrak{D}_k)$ has the property that its relative trace with any element of $R_k(\theta)$ is integral.

Thus $\mathfrak{F}$ is the GCD of all ideals in $K$ which contain only numbers in $R_k(\theta)$.
