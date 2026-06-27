---
role: proof
locale: en
of_concept: lemma-7306594025
source_book: gtm077
source_chapter: "V"
source_section: "§38"
---
# Proof of Lemma (c)

Corresponding to each prime ideal $\mathfrak{P}$ in $K$ there is a relative ring $R_k(\theta)$, where $\mathfrak{P}$ does not divide $\mathfrak{F} = \frac{\Phi'(\theta)}{\mathfrak{D}_k}$.

**Proof.** We need to construct, for a given prime ideal $\mathfrak{P}$ of $K$, a generating integer $\theta$ such that $\mathfrak{P} \nmid \mathfrak{F}$. The proof proceeds by constructing such a $\theta$ using the Chinese remainder theorem and the approximation theorem.

Let $\mathfrak{p}$ be the prime ideal in $k$ lying below $\mathfrak{P}$. Choose an integer $A$ in $K$ such that $A$ is divisible by a sufficiently high power of $\mathfrak{P}$, say $\mathfrak{P}^{e h b}$, where $e$ is the ramification index, $h$ is the class number of $k$, and $b$ is chosen large enough. Let $\mu$ be a number in $k$ such that $\mu \mathfrak{p}^{-h}$ is an ideal prime to $\mathfrak{p}$ (such $\mu$ exists because $\mathfrak{p}^h$ is principal in the ideal class group sense).

Then for an arbitrarily given integer $\Delta$ in $K$, we determine a number $\Gamma$ in $R_k(A)$ such that

$$\Delta \equiv \Gamma \pmod{\mathfrak{P}^{e h b}}.$$

The number $B\mu A^{hb} = (\Delta - \Gamma)\mu A^{hb}$ is then divisible by $\mathfrak{D}_k \mathfrak{F} = \Phi'(A)$, since

$$\frac{B\mu A^{hb}}{\Phi'(A)} = \frac{\pi \mu}{\mathfrak{D}_k \mathfrak{F}} \cdot \frac{B A^{hb}}{\pi} = \frac{\alpha}{\mathfrak{D}_k \mathfrak{F}} \cdot \frac{B A^{hb}}{\mathfrak{P}^{e h b} \mathfrak{U}^{hb}}$$

is integral (where $\pi$ is a generator of the principal part). Applying Lemma (a), we obtain a representation

$$\Delta \mu A^{hb} = \text{number in } R_k(A)$$

for each $\Delta$, from which by Theorem 113, $\mu A^{hb}$ generates an ideal divisible by $\mathfrak{F}$. Thus, in any case, it follows that $\mathfrak{F}$ is prime to $\mathfrak{P}$.

Taking $\theta = A$ gives the desired relative ring $R_k(\theta)$ for which $\mathfrak{P} \nmid \mathfrak{F}$.
