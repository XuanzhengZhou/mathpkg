---
role: proof
locale: en
of_concept: l2-norm-is-norm-on-cc
source_book: gtm012
source_chapter: "4. Hilbert Spaces and Fourier Series"
source_section: "§1. An inner product in ℂ, and the space L²"
---

# Proof that the $L^2$ norm is a norm on $\mathcal{C}$

**Corollary 1.2.** The function $u \mapsto \|u\|$ is a norm on $\mathcal{C}$.

*Proof.* Recall that this means $\|u\|$ satisfies the three norm axioms:

(10) $\|u\| \geq 0$, and $\|u\| = 0$ only if $u = 0$;

(11) $\|au\| = |a| \|u\|$ for $a \in \mathbb{C}$;

(12) $\|u + v\| \leq \|u\| + \|v\|$ (triangle inequality).

Property (10) follows from the positivity property (6) of the inner product: $(u, u) \geq 0$ and $(u, u) = 0$ only if $u = 0$. Since $\|u\| = (u, u)^{1/2}$, the same holds.

Property (11) follows from the homogeneity property (2) of the inner product:

$$\|au\| = (au, au)^{1/2} = (a(u, a^*u))^{1/2} = (a a^* (u, u))^{1/2} = (|a|^2 \|u\|^2)^{1/2} = |a| \|u\|.$$

More directly: $\|au\|^2 = (au, au) = a(u, au) = a a^*(u, u) = |a|^2 \|u\|^2$.

To prove the triangle inequality (12), we square both sides and use the Schwarz inequality (Lemma 1.1):

$$\|u + v\|^2 = (u + v, u + v) = (u, u) + (u, v) + (v, u) + (v, v)$$

$$= \|u\|^2 + (u, v) + (u, v)^* + \|v\|^2$$

$$= \|u\|^2 + 2 \operatorname{Re}(u, v) + \|v\|^2$$

$$\leq \|u\|^2 + 2|(u, v)| + \|v\|^2$$

$$\leq \|u\|^2 + 2\|u\| \|v\| + \|v\|^2 \quad \text{(by Lemma 1.1)}$$

$$= (\|u\| + \|v\|)^2.$$

Taking square roots gives $\|u + v\| \leq \|u\| + \|v\|$. ∎
