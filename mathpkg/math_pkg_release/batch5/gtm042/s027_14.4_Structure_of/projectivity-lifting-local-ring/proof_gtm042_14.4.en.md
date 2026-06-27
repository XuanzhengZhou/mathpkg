---
role: proof
locale: en
of_concept: projectivity-lifting-local-ring
source_book: gtm042
source_chapter: "14"
source_section: "14.4"
---

**(a)** If $P$ is $\Lambda[G]$-projective, then $\bar{P}$ is $k_{\Lambda}[G]$-projective by base change. Conversely, if $\bar{P}$ is $k_{\Lambda}[G]$-projective, the preceding lemma (Lemma 20) applied to $k_\Lambda$ shows that there exists a $k_{\Lambda}$-endomorphism $\bar{u}$ of $\bar{P}$ such that $\sum_{s \in G} s \cdot \bar{u} \cdot s^{-1} = 1$. By lifting $\bar{u}$, we obtain a $\Lambda$-endomorphism $u$ of $P$ such that $u' \equiv 1 \pmod{\mathfrak{m}_{\Lambda} P}$, where $u' = \sum_{s \in G} s \cdot u \cdot s^{-1}$. Consequently $u'$ is an automorphism of $P$ (since it is congruent to the identity modulo the radical, and $P$ is $\Lambda$-free of finite type), which moreover commutes with $G$. Thus $\sum_{s \in G} s \cdot (uu'^{-1}) \cdot s^{-1} = 1$, which shows by Lemma 20 that $P$ is projective over $\Lambda[G]$.

**(b)** If $P$ and $P'$ are projective, and if $\bar{w}: \bar{P} \to \bar{P}'$ is a $k_{\Lambda}[G]$-isomorphism, the fact that $P$ is projective shows that there exists a $\Lambda[G]$-homomorphism $w: P \to P'$ which lifts $\bar{w}$. Since $\bar{w}$ is an isomorphism, Nakayama's lemma (applied to the $\Lambda$-free modules $P$ and $P'$) implies that $w$ is also an isomorphism.
