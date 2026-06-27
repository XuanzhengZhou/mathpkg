---
role: proof
locale: en
of_concept: measurability-test-sets-lemma
source_book: gtm095
source_chapter: "4"
source_section: "2"
---

# Proof of Test Sets Lemma for Measurability

The necessity is evident. To prove the sufficiency we again use the principle of appropriate sets (Sect. 2).

Let $\mathcal{D}$ be the system of those Borel sets $D$ in $\mathcal{B}(R)$ for which $\xi^{-1}(D) \in \mathcal{F}$. The operation "form the inverse image" is easily shown to preserve the set-theoretic operations of union, intersection, and complement:

$$\xi^{-1}\left(\bigcup_\alpha D_\alpha\right) = \bigcup_\alpha \xi^{-1}(D_\alpha), \quad \xi^{-1}\left(\bigcap_\alpha D_\alpha\right) = \bigcap_\alpha \xi^{-1}(D_\alpha), \quad \xi^{-1}(D^c) = (\xi^{-1}(D))^c.$$

Hence $\mathcal{D}$ is a $\sigma$-algebra. Since $\mathcal{E} \subseteq \mathcal{D}$ by hypothesis, we have

$$\sigma(\mathcal{E}) \subseteq \sigma(\mathcal{D}) = \mathcal{D} \subseteq \mathcal{B}(R).$$

But $\sigma(\mathcal{E}) = \mathcal{B}(R)$ and consequently $\mathcal{D} = \mathcal{B}(R)$. Therefore $\xi^{-1}(B) \in \mathcal{F}$ for all $B \in \mathcal{B}(R)$, which means $\xi$ is $\mathcal{F}$-measurable.
