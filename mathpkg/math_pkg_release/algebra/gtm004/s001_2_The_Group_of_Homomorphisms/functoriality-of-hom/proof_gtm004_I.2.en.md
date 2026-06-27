---
role: proof
locale: en
of_concept: functoriality-of-hom
source_book: gtm004
source_chapter: "I. Modules"
source_section: "2. The Group of Homomorphisms"
---

# Proof of Functoriality Rules for $\operatorname{Hom}_\Lambda(A, -)$

Let $A$ be a fixed $\Lambda$-module. For any $\Lambda$-module homomorphism $\beta: B_1 \to B_2$, the induced map

$$\beta_* = \operatorname{Hom}_\Lambda(A, \beta): \operatorname{Hom}_\Lambda(A, B_1) \to \operatorname{Hom}_\Lambda(A, B_2)$$

is defined by $\beta_*(\varphi) = \beta \circ \varphi$ for $\varphi \in \operatorname{Hom}_\Lambda(A, B_1)$.

**1. $\beta_*$ is a homomorphism of abelian groups.** For $\varphi_1, \varphi_2 \in \operatorname{Hom}_\Lambda(A, B_1)$ and $a \in A$,

$$(\beta_*(\varphi_1 + \varphi_2))(a) = \beta((\varphi_1 + \varphi_2)(a)) = \beta(\varphi_1(a) + \varphi_2(a)) = \beta(\varphi_1(a)) + \beta(\varphi_2(a)) = (\beta_*(\varphi_1))(a) + (\beta_*(\varphi_2))(a),$$

so $\beta_*(\varphi_1 + \varphi_2) = \beta_*(\varphi_1) + \beta_*(\varphi_2)$.

**2. Composition rule.** If $\beta: B_1 \to B_2$ and $\beta': B_2 \to B_3$, then $(\beta' \beta)_* = \beta'_* \beta_*$:

For $\varphi \in \operatorname{Hom}_\Lambda(A, B_1)$,
$$(\beta' \beta)_*(\varphi) = (\beta' \beta) \circ \varphi = \beta' \circ (\beta \circ \varphi) = \beta'_*(\beta \circ \varphi) = \beta'_*(\beta_*(\varphi)) = (\beta'_* \beta_*)(\varphi).$$

**3. Identity rule.** If $\beta = 1_B: B \to B$ is the identity, then $\beta_* = 1_{\operatorname{Hom}_\Lambda(A, B)}$:

For $\varphi \in \operatorname{Hom}_\Lambda(A, B)$,
$$(1_B)_*(\varphi) = 1_B \circ \varphi = \varphi = 1_{\operatorname{Hom}_\Lambda(A, B)}(\varphi).$$

These three properties establish that $\operatorname{Hom}_\Lambda(A, -)$ is a covariant functor from the category of $\Lambda$-modules to the category of abelian groups.
