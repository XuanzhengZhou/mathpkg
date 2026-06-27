---
role: proof
locale: en
of_concept: injectivity-of-hom-from-divisible
source_book: gtm004
source_chapter: "I. Modules"
source_section: "8. Cofree Modules"
---

# Proof of Theorem 8.2: Injectivity of $\operatorname{Hom}_{\mathbb{Z}}(\Lambda, G)$ for Divisible $G$

Let $\mu : A \rightarrow B$ be a monomorphism of $\Lambda$-modules, and let $\alpha : A \rightarrow \bar{\Lambda} = \operatorname{Hom}_{\mathbb{Z}}(\Lambda, G)$ be a homomorphism of $\Lambda$-modules. We must show that there exists $\beta : B \rightarrow \bar{\Lambda}$ such that $\beta \mu = \alpha$.

By Proposition 8.1, the $\Lambda$-module homomorphism $\alpha : A \rightarrow \operatorname{Hom}_{\mathbb{Z}}(\Lambda, G)$ corresponds to a homomorphism of abelian groups $\alpha' : A \rightarrow G$ via the adjunction isomorphism

$$\eta_A : \operatorname{Hom}_{\Lambda}(A, \operatorname{Hom}_{\mathbb{Z}}(\Lambda, G)) \xrightarrow{\cong} \operatorname{Hom}_{\mathbb{Z}}(A, G).$$

Since $G$ is a divisible abelian group, it is injective as a $\mathbb{Z}$-module. Thus, given the monomorphism $\mu : A \rightarrow B$ (viewed as a monomorphism of abelian groups by restriction of scalars) and the abelian group homomorphism $\alpha' : A \rightarrow G$, there exists an abelian group homomorphism $\beta' : B \rightarrow G$ such that $\beta' \mu = \alpha'$.

Applying the inverse of the adjunction isomorphism $\eta_B$ to $\beta'$, we obtain a $\Lambda$-module homomorphism

$$\beta = \eta_B^{-1}(\beta') : B \rightarrow \operatorname{Hom}_{\mathbb{Z}}(\Lambda, G) = \bar{\Lambda}.$$

By the naturality of $\eta$ (the commutative diagram in Proposition 8.1), we have $\beta \mu = \alpha$.

Therefore $\bar{\Lambda} = \operatorname{Hom}_{\mathbb{Z}}(\Lambda, G)$ satisfies Baer's criterion and is an injective $\Lambda$-module. $\square$
