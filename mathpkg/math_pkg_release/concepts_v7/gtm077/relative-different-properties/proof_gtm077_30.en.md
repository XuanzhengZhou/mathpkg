---
role: proof
locale: en
of_concept: relative-different-properties
source_book: gtm077
source_chapter: "30"
source_section: "30"
---

# Proof of Theorem 104

If $\omega \equiv 0 \pmod{\mathfrak{f}}$, then $\alpha = \omega/F'(\theta)$ is a number with denominator $\mathfrak{d}$, and by Lemma (a) of §36, $\alpha F'(\theta)$ must be a number of the ring $R(\theta)$. Hence the first part of our theorem is proved.

Conversely, if all numbers of $\mathfrak{a}$ are numbers of the ring $R(\theta)$, one shows that $\mathfrak{a}$ is divisible by $\mathfrak{f} = F'(\theta)/\mathfrak{d}$. This follows by a deeper argument using the conductor of the ring: arrange that $\theta$ is different from all of its conjugates, and in addition

$$\theta \equiv 0 \pmod{\mathfrak{a}}, \quad \text{where } p = \mathfrak{p}^e \mathfrak{a}, (\mathfrak{a}, \mathfrak{p}) = 1,$$

and $p$ is the rational prime which is divisible by $\mathfrak{p}$.

If we let $\gamma_i$ in (68) run through the $N(\mathfrak{p})$ numbers

$$0, \theta, \theta^2, \ldots, \theta^{N(\mathfrak{p})-1}$$

which are incongruent mod $\mathfrak{p}$, we see that each residue class mod $\mathfrak{p}^h$ can be represented by a number of the ring $R(\theta)$. But then, if (69) holds, the conductor $\mathfrak{f}$ of the ring cannot be divisible by $\mathfrak{p}$. For if

$$N(\mathfrak{d}\mathfrak{f}) = p^k a, \quad \text{where } (a, p) = 1,$$

then to begin with, by the above, to each integer $\omega$ there is a number $\rho$ of the ring such that

$$\pi = \omega - \rho \equiv 0 \pmod{\mathfrak{p}^{ek}}.$$

Here $\pi a\theta^k$ is divisible by $F'(\theta) = \mathfrak{d}\mathfrak{f}$, as the decomposition

$$\frac{\pi a\theta^k}{F'(\theta)} = \frac{\pi\theta^k N(\mathfrak{d}\mathfrak{f})}{\mathfrak{d}\mathfrak{f}p^k} = \frac{N(\mathfrak{d}\mathfrak{f})}{\mathfrak{d}\mathfrak{f}} \frac{\pi\theta^k}{\mathfrak{p}^{ek}\mathfrak{a}^k}$$

shows by (69). Hence by Lemma (a), this number can be represented in the form $\rho'/F'(\theta)$ with $\rho' \in R(\theta)$. It follows that all integers of the field lie in $R(\theta)$, meaning the conductor is trivial, and $\mathfrak{a}$ is indeed divisible by $\mathfrak{f}$.
