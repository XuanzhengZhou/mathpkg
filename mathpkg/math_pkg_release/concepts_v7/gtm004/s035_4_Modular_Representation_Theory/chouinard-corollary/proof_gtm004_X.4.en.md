---
role: proof
locale: en
of_concept: chouinard-corollary
source_book: gtm004
source_chapter: "X. Survey of Some Applications"
source_section: "4. Modular Representation Theory"
---

# Proof of Corollary 4.4 (Chouinard) — Projectivity Detection

Let $G$ be a finite group, $k$ a field of characteristic $p$, and $M$ a $kG$-module.

**Corollary 4.4 (Chouinard).** The module $M$ is $kG$-projective if and only if, for every elementary abelian $p$-subgroup $E$ of $G$, the restriction $M_E$ is $kE$-projective.

*Proof.* This corollary follows directly from Theorem 4.3 (Alperin, Evens; Carlson), which states

$$c_G(M) = \max_{E \in \mathcal{E}} c_E(M_E),$$

where $\mathcal{E}$ is the set of elementary abelian $p$-subgroups of $G$ and $c_G(M)$ denotes the complexity of $M$.

Recall from the definition of complexity that $c_G(M) = 0$ if and only if the module $M$ is projective over $kG$. Indeed, if $M$ is projective, then $\operatorname{Ext}_{kG}^n(M, -) = 0$ for all $n \geq 1$, so the sequence $\{\dim_k \operatorname{Ext}_{kG}^n(M, M)\}$ is bounded (in fact, vanishes for $n \geq 1$), giving complexity $0$. Conversely, if $c_G(M) = 0$, the uniform boundedness of the Ext-groups forces $M$ to be projective (this is a fundamental property of the complexity invariant).

Now apply Theorem 4.3:

$$c_G(M) = \max_{E \in \mathcal{E}} c_E(M_E).$$

If $M$ is $kG$-projective, then $c_G(M) = 0$, which forces $c_E(M_E) = 0$ for all $E \in \mathcal{E}$, and thus $M_E$ is $kE$-projective for every elementary abelian $p$-subgroup $E$.

Conversely, if $M_E$ is $kE$-projective for all $E \in \mathcal{E}$, then $c_E(M_E) = 0$ for all $E$, so $\max_E c_E(M_E) = 0$. By Theorem 4.3, $c_G(M) = 0$, and consequently $M$ is $kG$-projective. $\square$

This result, which Chouinard had actually obtained prior to the Alperin-Evens-Carlson theorem, shows that projectivity of a $kG$-module can be detected by examining its restrictions to the elementary abelian $p$-subgroups of $G$ — a striking localization principle in modular representation theory.
