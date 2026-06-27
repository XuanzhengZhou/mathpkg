---
role: proof
locale: en
of_concept: direct-product-of-injectives
source_book: gtm004
source_chapter: "I. Modules"
source_section: "6. Dualization, Injective Modules"
---

# Proof: Direct Product of Injective Modules is Injective

**($\Rightarrow$)** Assume each $I_j$, $j \in J$, is injective. Let $\alpha : A \to \prod_{j \in J} I_j$ be a homomorphism and $\mu : A \hookrightarrow B$ be a monomorphism. For each $j \in J$, let $\pi_j : \prod_{j \in J} I_j \to I_j$ be the canonical projection, and set $\alpha_j = \pi_j \circ \alpha : A \to I_j$.

Since $I_j$ is injective, there exists a homomorphism $\beta_j : B \to I_j$ such that $\beta_j \circ \mu = \alpha_j$ for each $j \in J$. By the universal property of the direct product (Proposition 3.3), there exists a unique homomorphism $\beta : B \to \prod_{j \in J} I_j$ such that $\pi_j \circ \beta = \beta_j$ for all $j \in J$.

Then for each $j \in J$,

$$\pi_j \circ (\beta \circ \mu) = (\pi_j \circ \beta) \circ \mu = \beta_j \circ \mu = \alpha_j = \pi_j \circ \alpha.$$

By the uniqueness part of the universal property of the direct product, $\beta \circ \mu = \alpha$. Hence $\prod_{j \in J} I_j$ is injective.

**($\Leftarrow$)** Assume $\prod_{j \in J} I_j$ is injective. To show a particular $I_k$ is injective, let $\alpha_k : A \to I_k$ be a homomorphism and $\mu : A \hookrightarrow B$ be a monomorphism. Define $\alpha : A \to \prod_{j \in J} I_j$ by setting its $j$-th component to be $\alpha_k$ for $j = k$ and zero otherwise. Since $\prod I_j$ is injective, there exists $\beta : B \to \prod I_j$ such that $\beta \circ \mu = \alpha$. Then $\beta_k = \pi_k \circ \beta : B \to I_k$ satisfies $\beta_k \circ \mu = \alpha_k$, proving $I_k$ is injective.
