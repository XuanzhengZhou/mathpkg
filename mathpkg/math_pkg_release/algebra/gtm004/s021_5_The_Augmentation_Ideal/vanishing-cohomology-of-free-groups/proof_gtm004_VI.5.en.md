---
role: proof
locale: en
of_concept: vanishing-cohomology-of-free-groups
source_book: gtm004
source_chapter: "VI. Cohomology of Groups"
source_section: "5. The Augmentation Ideal, Derivations, and the Semi-Direct Product"
---

# Proof of Vanishing of Higher Cohomology and Homology of Free Groups

**Corollary 5.6.** For a free group $F$, we have

$$H^n(F, A) = 0 = H_n(F, B)$$

for all $F$-modules $A, B$ and all $n \geq 2$.

*Proof.* By Theorem 5.5, the augmentation ideal $IF$ is an $F$-free module. Indeed, if $S$ is a free generating set of $F$, then for each $s \in S$, the infinite cyclic subgroup $C_s = \langle s \rangle$ of $F$ has augmentation ideal $IC_s$ which is $C_s$-free on $s-1$. Inducing to $F$, one obtains that $IF$ is $F$-free on the set $\{s-1 \mid s \in S\}$. (A more detailed argument uses the discussion preceding Corollary 5.6 in the text: given $F$ free on $S$ and any $F$-module $M$, a set map $f: S \to M$ extends via the semi-direct product construction and Corollary 5.4 to an $F$-module homomorphism $IF \to M$ with $(s-1) \mapsto f(s)$, which proves freeness of $IF$.)

Now consider the short exact sequence of $F$-modules

$$0 \to IF \to \mathbb{Z}F \xrightarrow{\varepsilon} \mathbb{Z} \to 0,$$

where $\varepsilon$ is the augmentation map. Since $IF$ is $F$-free, this sequence provides an $F$-free resolution of $\mathbb{Z}$ of length 1:

$$\cdots \to 0 \to 0 \to IF \to \mathbb{Z}F \to \mathbb{Z} \to 0.$$

Therefore, for any $F$-modules $A$ and $B$, we have:

- $H^n(F, A) = H^n(\operatorname{Hom}_F(\cdots \to IF \to \mathbb{Z}F \to 0, A)) = 0$ for all $n \geq 2$, since the complex vanishes in those degrees.
- $H_n(F, B) = H_n(B \otimes_F (\cdots \to IF \to \mathbb{Z}F \to 0)) = 0$ for all $n \geq 2$, for the same reason.

Thus a free group has cohomological dimension at most 1. $\square$

**Remark.** The vanishing of $H_2(F, B)$ for $F$ free was already used in the proof of Hopf's formula (Section 9) and is a fundamental fact in combinatorial group theory — it implies that free groups have no relations among relations, i.e., every presentation of a group can be used to compute $H_2$ via Hopf's formula $H_2(G) \cong (R \cap [F, F]) / [F, R]$ where $F/R \cong G$.
