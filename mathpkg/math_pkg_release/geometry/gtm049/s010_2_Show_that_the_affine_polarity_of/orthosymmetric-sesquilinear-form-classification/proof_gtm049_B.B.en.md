---
role: proof
locale: en
of_concept: orthosymmetric-sesquilinear-form-classification
source_book: gtm049
source_chapter: "B"
source_section: "B"
---

The condition $\perp(\sigma) = \top(\sigma)$ is equivalent to $\mathcal{P}(\sigma) = \mathcal{P}(\tilde{\sigma})$ as before. Assume that $\dim \sigma \geq 2$. Then arguing as in Lemma 4 (p. 97), we deduce $\sigma = z\tilde{\sigma}$ for some $z \neq 0$ (invoking Proposition 1 of Chapter III (p. 45) for semi-linear isomorphisms).

For any $a, b \in V$,
$$0 = \sigma(a + b, a + b) = \sigma(a, b) + \sigma(b, a)$$
and hence, for all $x \in F$,
$$x\sigma(a, b) = \sigma(a, xb) = -\sigma(xb, a) = -(x\zeta)\sigma(b, a) = (x\zeta)\sigma(a, b).$$

If $\sigma \neq 0$, we conclude $x = x\zeta$ for all $x \in F$, and so $\zeta$ is the identity automorphism. Hence $\sigma$ is bilinear.

To extend the structure theorems of §5.4 to sesquilinear forms, we need only consider forms that are not alternating. Theorem 3 is true for (non-alternating) hermitian forms and Theorem 4 is true for arbitrary (but non-alternating) sesquilinear forms. The proofs of both theorems are unchanged up to the point where $\sigma$ is assumed to be non-zero and alternating on $[a]^\perp$. But this implies that the automorphism of the restriction of $\sigma$ to $[a]^\perp$, and so also of $\sigma$ itself, is the identity mapping. Thus $\sigma$ is bilinear and we are genuinely back in the situations of the earlier theorems.
