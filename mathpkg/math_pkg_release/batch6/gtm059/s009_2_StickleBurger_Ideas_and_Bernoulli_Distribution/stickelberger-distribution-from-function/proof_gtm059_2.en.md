---
role: proof
locale: en
of_concept: stickelberger-distribution-from-function
source_book: gtm059
source_chapter: "2"
source_section: "2. Stickelberger Ideals and Bernoulli Distributions"
---

The proof verifies the distribution relation for the constructed family. Let $M \mid N$ and consider the projection $(\mathbb{Z}/N\mathbb{Z})^k \to (\mathbb{Z}/M\mathbb{Z})^k$. For a tuple $\bar{a} \in (\mathbb{Z}/M\mathbb{Z})^k$, the sum of $g_N(\bar{b})$ over all $\bar{b} \in (\mathbb{Z}/N\mathbb{Z})^k$ lying above $\bar{a}$ must equal $g_M(\bar{a})$.

Using the distribution property of $g$ on $\mathbb{Q}/\mathbb{Z}$, the sum over fibers decomposes according to the Chinese Remainder Theorem. The compatibility follows because the Kronecker delta conditions at level $N$ sum to the corresponding condition at level $M$ under the projection map. The key identity is:

$$\sum_{\substack{x \in \mathbb{Z}/N\mathbb{Z} \\ x \equiv a \pmod{M}}} g(x) = g(a),$$

which is precisely the distribution relation for the original distribution $g$ on the projective system $\{\mathbb{Z}/N\mathbb{Z}\}$.
