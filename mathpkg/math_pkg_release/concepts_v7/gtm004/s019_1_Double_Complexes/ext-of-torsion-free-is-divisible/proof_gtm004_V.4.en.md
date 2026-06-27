---
role: proof
locale: en
of_concept: ext-of-torsion-free-is-divisible
source_book: gtm004
source_chapter: "V. Double Complexes"
source_section: "4. Applications of the Künneth Formulas"
---

# Proof that $\operatorname{Ext}(A, B)$ is Divisible for Torsion-Free $A$

**Corollary 4.4.** If $A$ is a torsion-free abelian group, then $\operatorname{Ext}(A, B)$ is divisible for every abelian group $B$.

**Proof.** Since $A$ is torsion-free, $\operatorname{Tor}(A', A) = 0$ for every abelian group $A'$ (a torsion-free abelian group is flat over $\mathbb{Z}$).

Apply the natural isomorphism from Theorem 4.3, equation (4.6):
$$\operatorname{Ext}(\operatorname{Tor}(A', A), B) \cong \operatorname{Ext}(A', \operatorname{Ext}(A, B)).$$

Since $\operatorname{Tor}(A', A) = 0$, the left-hand side is
$$\operatorname{Ext}(0, B) = 0.$$
Therefore,
$$\operatorname{Ext}(A', \operatorname{Ext}(A, B)) = 0 \quad \text{for all abelian groups } A'.$$

Now recall that an abelian group $G$ is divisible (equivalently, injective as a $\mathbb{Z}$-module) if and only if $\operatorname{Ext}(A', G) = 0$ for all abelian groups $A'$. This follows from Baer's criterion: $G$ is injective $\iff$ every extension of $G$ by any $A'$ splits $\iff$ $\operatorname{Ext}(A', G) = 0$ for all $A'$.

Thus $\operatorname{Ext}(A, B)$ is divisible for all $B$.
