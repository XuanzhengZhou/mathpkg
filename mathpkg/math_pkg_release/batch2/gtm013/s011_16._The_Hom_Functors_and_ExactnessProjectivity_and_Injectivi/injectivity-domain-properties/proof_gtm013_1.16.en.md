---
role: proof
locale: en
of_concept: injectivity-domain-properties
source_book: gtm013
source_chapter: "1"
source_section: "§16. The Hom Functors and Exactness—Projectivity and Injectivity"
---

(1) The proof is dual to that of (16.12.1). If $f: K' \to M'$ is monic, then so is $hf: K' \to M$. Thus $f^* h^* = (hf)^*$ is epic, so $f^*$ is epic, and hence $U$ is $M'$-injective. To see $U$ is $M''$-injective, assume $M' \leq K \leq M$ and $M'' = M/M'$. Apply $Hom_R(-, U)$ to the canonical diagram:

$$\begin{array}{c}
0 \\
\uparrow \\
0 \to M' \to M \to M/M' \to 0 \\
\uparrow \quad \uparrow \quad \uparrow \\
0 \to M' \to K \to K/M' \to 0 \\
\uparrow \quad \uparrow \quad \uparrow \\
0 \quad 0 \quad 0
\end{array}$$

and the conclusion follows from exactness properties.

(2) Let $M = \bigoplus_A M_\alpha$ and let $N$ be a submodule of $M$. Let $\bar{h}: N \to U$ be a homomorphism. Consider the family of all extensions of $\bar{h}$ to submodules of $M$ containing $N$. By Zorn's Lemma, there exists a maximal extension. Using the $M_\alpha$-injectivity hypothesis, one shows that the domain of this maximal extension must contain each $M_\alpha$, hence equals all of $M$.
