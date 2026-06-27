---
role: proof
locale: en
of_concept: lemma-73065940
source_book: gtm077
source_chapter: "38"
source_section: "Relative Norms of Numbers and Ideals, Relative Differents, and Relative Discriminants"
---
# Proof of Lemma (c)

**Statement.** Corresponding to each prime ideal $\mathfrak{P}$ in $K$ there is a relative ring $R_k(\theta)$, where $\mathfrak{P}$ does not divide

$$\mathfrak{F} = \frac{\Phi'(\theta)}{\mathfrak{D}_k}.$$

*Proof.* By the definition of $\mathfrak{F}$ from Theorem 113, we have $\mathfrak{F}\mathfrak{D}_k = \Phi'(\theta)$. The proof proceeds by constructing a suitable primitive element $\theta$. One starts with an arbitrary integer $A$ in $K$ and uses an approximation argument modulo a sufficiently high power of $\mathfrak{P}$. Specifically, one determines a number $\Gamma$ in $R_k(A)$ such that

$$\Delta \equiv \Gamma \pmod{\mathfrak{P}^{eha}}$$

for an arbitrarily given integer $\Delta$ in $K$. Then the number $B\mu A^{ha} = (\Delta - \Gamma)\mu A^{ha}$ is divisible by $\mathfrak{D}_k\mathfrak{F} = \Phi'(A)$. Applying Lemma (a) yields a representation

$$\Delta\mu A^{ha} = \text{number in } R_k(A)$$

for each $\Delta$. From this, by Theorem 113, $\mu A^{ha}$ generates an ideal divisible by $\mathfrak{F}$. Consequently, $\mathfrak{F}$ is prime to $\mathfrak{P}$, which means $\mathfrak{P} \nmid \mathfrak{F}$. Thus the relative ring $R_k(\theta)$ with $\theta = A$ satisfies the required condition.
