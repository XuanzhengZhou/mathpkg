---
role: proof
locale: en
of_concept: vanishing-of-group-cohomology-for-injectives
source_book: gtm004
source_chapter: "VI"
source_section: "2"
---

# Proof of Proposition 2.4: Vanishing of (Co)homology for Injective and Flat Modules

By definition (Section VI.2), for a $G$-module $A$ and a right $G$-module $B$,

$$H^n(G, A) = \operatorname{Ext}_{\mathbb{Z}G}^n(\mathbb{Z}, A), \qquad H_n(G, B) = \operatorname{Tor}_n^{\mathbb{Z}G}(B, \mathbb{Z}), \qquad n \geq 0.$$

These are the right derived functors of $\operatorname{Hom}_G(\mathbb{Z}, -)$ and the left derived functors of $- \otimes_G \mathbb{Z}$, respectively.

**Cohomology vanishing.** If $A$ is an injective $\mathbb{Z}G$-module, then the functor $\operatorname{Hom}_{\mathbb{Z}G}(-, A)$ is exact. Consequently, all its right derived functors vanish in positive degrees:

$$\operatorname{Ext}_{\mathbb{Z}G}^n(\mathbb{Z}, A) = 0 \quad \text{for all } n \geq 1.$$

Hence $H^n(G, A) = 0$ for all $n \geq 1$ whenever $A$ is injective. (For $n = 0$, $H^0(G, A) = A^G$ need not vanish.)

**Homology vanishing.** If $B$ is a flat $\mathbb{Z}G$-module, then the functor $B \otimes_{\mathbb{Z}G} -$ is exact. Consequently, all its left derived functors vanish in positive degrees:

$$\operatorname{Tor}_n^{\mathbb{Z}G}(B, \mathbb{Z}) = 0 \quad \text{for all } n \geq 1.$$

Hence $H_n(G, B) = 0$ for all $n \geq 1$ whenever $B$ is flat. In particular, projective modules are flat, so the statement holds for $B$ projective as well.
