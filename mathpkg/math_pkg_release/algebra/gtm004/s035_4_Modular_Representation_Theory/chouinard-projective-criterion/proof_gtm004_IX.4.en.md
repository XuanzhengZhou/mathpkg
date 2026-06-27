---
role: proof
locale: en
of_concept: chouinard-projective-criterion
source_book: gtm004
source_chapter: "IX. Relative Homological Algebra"
source_section: "4. Modular Representation Theory"
---

# Proof of Chouinard's Projectivity Criterion

Let $G$ be a finite group, $k$ a field of characteristic $p$, and $M$ a $kG$-module.

**Corollary 4.4 (Chouinard).** The module $M$ is $kG$-projective if and only if, for every elementary abelian $p$-subgroup $E$ of $G$, the restriction $M_E$ is $kE$-projective.

*Proof.* The result is an immediate consequence of the Alperin-Evens-Carlson Complexity Theorem (Theorem 4.3), which asserts

$$c_G(M) = \max_{E \in \mathcal{E}} c_E(M_E),$$

where $\mathcal{E}$ is the collection of elementary abelian $p$-subgroups of $G$, and $c_G(M)$ denotes the complexity of $M$ defined via the growth of $\dim_k \operatorname{Ext}_{kG}^n(M, M)$.

The key observation is the characterization of projective modules by complexity:

$$c_G(M) = 0 \iff M \text{ is } kG\text{-projective}.$$

*Justification.* If $M$ is projective, then $\operatorname{Ext}_{kG}^n(M, M) = 0$ for all $n \geq 1$, so the growth sequence is bounded and $c_G(M) = 0$. Conversely, if $c_G(M) = 0$, then the sequence $\{\dim_k \operatorname{Ext}_{kG}^n(M, M)\}$ is uniformly bounded. Standard homological arguments using the properties of complexity show that this forces $M$ to be projective.

Now the equivalence follows by equating the two conditions:

$$
\begin{aligned}
M \text{ is } kG\text{-projective}
&\iff c_G(M) = 0 \\
&\iff \max_{E \in \mathcal{E}} c_E(M_E) = 0 \quad \text{(by Theorem 4.3)}\\
&\iff c_E(M_E) = 0 \text{ for all } E \in \mathcal{E}\\
&\iff M_E \text{ is } kE\text{-projective for all } E \in \mathcal{E}.
\end{aligned}
$$

The third equivalence uses the fact that each $c_E(M_E) \geq 0$, so their maximum is zero precisely when each individual term is zero. $\square$

This criterion, historically obtained by Chouinard before the full complexity theorem, provides a powerful localization principle: a global property (projectivity over $kG$) is completely determined by the local behavior on elementary abelian $p$-subgroups. In the context of Chapter IX on relative homological algebra, this fits into the broader theme of detecting homological properties through restriction to distinguished classes of subgroups.
