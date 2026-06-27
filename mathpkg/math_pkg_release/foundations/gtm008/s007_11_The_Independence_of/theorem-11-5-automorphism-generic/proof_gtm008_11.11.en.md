---
role: proof
locale: en
of_concept: theorem-11-5-automorphism-generic
source_book: gtm008
source_chapter: "11"
source_section: "11 The Independence of V = L and the CH"
---

**Proof.** First, $S \subseteq P$ is dense if and only if $\pi''S$ is dense, since $\pi$ is an automorphism and $\pi \in M$. Therefore

$$S \cap \pi''G \neq 0 \leftrightarrow \pi^{-1}(S) \cap G \neq 0.$$

Since $G$ is $P$-generic over $M$, $\pi^{-1}(S) \cap G \neq 0$ for every dense $S \in M$, hence $S \cap \pi''G \neq 0$ for every dense $S \in M$. Thus $\pi''G$ is $P$-generic over $M$.

The ultrafilter corresponding to $\pi''G$ is

$$\{b \in B \mid b \cap \pi''G \neq 0\} = \{b \in B \mid \pi^{-1}(b) \cap G \neq 0\}$$
$$= \{b \in B \mid \tilde{\pi}^{-1}(b) \in F\}$$
$$= \tilde{\pi}''F.$$

For the homomorphism: $b \in \tilde{\pi}''F$ if and only if $\tilde{\pi}^{-1}(b) \in F$, which means $h(\tilde{\pi}^{-1}(b)) = 1$, i.e., $(h \circ \tilde{\pi}^{-1})(b) = 1$. So $h \circ \tilde{\pi}^{-1}$ is the homomorphism corresponding to $\pi''G$.

Finally, since $M[G]$, $M[F]$, and $M[h]$ all denote the same generic extension, and similarly for $\pi''G$, $\tilde{\pi}''F$, and $h \circ \tilde{\pi}^{-1}$, we have

$$M[G] = M[F] = M[h] = M[\pi''G] = M[\tilde{\pi}''F] = M[h \circ \tilde{\pi}^{-1}].$$

$\square$
