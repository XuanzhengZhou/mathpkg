---
role: proof
locale: en
of_concept: additive-functor-characterization
source_book: gtm004
source_chapter: "II"
source_section: "9"
---

# Proof of Characterization of Additive Functors

Let $F: \mathfrak{A} \to \mathfrak{B}$ be a functor between additive categories. The following are equivalent:

**(i) $\Rightarrow$ (ii).** Assume $F$ preserves sums (coproducts) of two objects. We must show $F$ preserves products. First, $F$ maps zero objects to zero objects: let $0$ be a zero object of $\mathfrak{A}$. For any $A \in \mathfrak{A}$, $A$ is the sum of $A$ and $0$ with injections $1_A: A \to A$ and $0: 0 \to A$. Hence $FA$ is the sum of $FA$ and $F(0)$ with injections $1_{FA}$ and $\beta = F(0)$. Let $B = F(0)$. Consider the zero morphism $0: FA \to B$ and the identity $1_B: B \to B$. By the universal property of the coproduct, there exists a unique $\theta: FA \to B$ such that $\theta \circ 1_{FA} = 0$ and $\theta \circ \beta = 1_B$. Thus $\theta = 0$ and $1_B = \theta \circ \beta = 0 \circ \beta = 0$, so $1_B = 0$, which forces $B$ to be a zero object. Hence $F(0) \cong 0$.

Now for $A_1, A_2 \in \mathfrak{A}$, the product $A_1 \oplus A_2$ is also the coproduct (Proposition 9.1). Since $F$ preserves coproducts, $F(A_1 \oplus A_2) \cong FA_1 \oplus FA_2$ as a coproduct in $\mathfrak{B}$, which by Proposition 9.1 applied to $\mathfrak{B}$ is also the product. Moreover, the canonical injections $F(i_1) = \{1_{FA_1}, 0\}$ and $F(i_2) = \{0, 1_{FA_2}\}$ and projections $F(p_1), F(p_2)$ satisfy the biproduct identities.

**(ii) $\Rightarrow$ (i).** Follows by duality (or by the symmetric argument using Proposition 9.1).

**(ii) $\Rightarrow$ (iii).** Assume $F$ preserves products. For $f, g: A \to A'$, their sum is expressed via the biproduct:

$$f + g = \nabla \circ (f \oplus g) \circ \Delta,$$

where $\Delta = \{1_A, 1_A\}: A \to A \oplus A$, $\nabla = \langle 1_{A'}, 1_{A'} \rangle: A' \oplus A' \to A'$, and $f \oplus g = \{f p_1, g p_2\}$.

Since $F$ preserves products, $F(A \oplus A) \cong FA \oplus FA$ with $F(p_i)$ as projections and $F(i_j)$ as injections. Then

$$F(f + g) = F(\nabla) \circ F(f \oplus g) \circ F(\Delta).$$

Because $F$ preserves products, $F(\Delta) = \{1_{FA}, 1_{FA}\}$, $F(\nabla) = \langle 1_{FA'}, 1_{FA'} \rangle$, and $F(f \oplus g) = \{Ff \circ Fp_1, Fg \circ Fp_2\} = Ff \oplus Fg$. Hence

$$F(f + g) = \nabla_{FA'} \circ (Ff \oplus Fg) \circ \Delta_{FA} = Ff + Fg,$$

so $F$ is additive on hom-sets.

**(iii) $\Rightarrow$ (ii).** Conversely, if $F$ is a homomorphism on each hom-set, then we show $\{Fp_1, Fp_2\}: F(A_1 \oplus A_2) \to FA_1 \oplus FA_2$ is an isomorphism with inverse $F(i_1) p_1 + F(i_2) p_2$. Compute:

$$(F(i_1) p_1 + F(i_2) p_2) \circ \{Fp_1, Fp_2\} = F(i_1) p_1 \{Fp_1, Fp_2\} + F(i_2) p_2 \{Fp_1, Fp_2\}$$
$$= F(i_1) F(p_1) + F(i_2) F(p_2) = F(i_1 p_1 + i_2 p_2) \quad (\text{since } F \text{ is additive})$$
$$= F(1) = 1.$$

Thus $F$ preserves products (and dually, coproducts).

Therefore all three conditions are equivalent. A functor satisfying any of them is called an **additive functor**.
