---
role: proof
locale: en
of_concept: maschke-theorem-ext
source_book: gtm004
source_chapter: "IX. Relative Homological Algebra"
source_section: "4. Modular Representation Theory"
---

# Proof of Maschke's Theorem in Ext Form

Let $G$ be a finite group and let $k$ be a field of characteristic $p$. Let $kG$ denote the group algebra.

**Theorem 4.1 (Maschke).** There exist $kG$-modules $A, B$ with $\operatorname{Ext}_{kG}^1(A, B) \neq 0$ if and only if $p$ divides the group order $|G|$.

*Proof.* The statement consists of two directions.

($\Leftarrow$) If $p$ does not divide $|G|$, then by Maschke's classical theorem (proved in Chapter VI, Theorem 16.6), every $kG$-module is semisimple. Semisimplicity implies that every short exact sequence of $kG$-modules splits. Hence $\operatorname{Ext}_{kG}^1(A, B) = 0$ for all $kG$-modules $A, B$.

($\Rightarrow$) If $p$ divides $|G|$, then $kG$ is not semisimple. Consider the augmentation homomorphism $\varepsilon: kG \to k$ sending each group element to $1$. Its kernel $I = \ker(\varepsilon)$ is the augmentation ideal. The short exact sequence

$$0 \longrightarrow I \longrightarrow kG \stackrel{\varepsilon}{\longrightarrow} k \longrightarrow 0$$

does not split. Indeed, if it did split, then $kG$ would contain a submodule isomorphic to the trivial module $k$ complementary to $I$, which would force the sum of all group elements $\sum_{g \in G} g$ to act as a nonzero scalar on $k$ while annihilating $I$ — impossible since this element lies in $I$ when $p \mid |G|$ (its augmentation is $|G| \equiv 0 \pmod p$). Thus $\operatorname{Ext}_{kG}^1(k, I) \neq 0$, proving the existence of modules with nonvanishing $\operatorname{Ext}^1$. $\square$

In the context of relative homological algebra, this theorem motivates the study of modular representation theory: the nontrivial extension structure arises precisely when the characteristic $p$ divides $|G|$, and techniques from relative homological algebra are required to analyze the resulting module categories.
