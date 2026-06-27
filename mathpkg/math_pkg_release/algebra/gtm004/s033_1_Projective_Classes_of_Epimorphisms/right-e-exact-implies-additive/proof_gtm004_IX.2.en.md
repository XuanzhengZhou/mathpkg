---
role: proof
locale: en
of_concept: right-e-exact-implies-additive
source_book: gtm004
source_chapter: "IX. Relative Homological Algebra"
source_section: "2. E-Derived Functors"
---

# Proof of Right E-Exact Functor is Additive

**Proposition 2.4.** A right $\mathcal{E}$-exact functor $T : \mathfrak{A} \to \mathfrak{B}$ is additive.

**Proof.** First we show $T(0) = 0$. In an abelian category, an object $A$ is a zero object precisely when the sequence $A \xrightarrow{1_A} A \xrightarrow{1_A} A \to 0$ is exact. Since epimorphisms in an abelian category are admissible in any closed class (the identity is always in $\mathcal{E}$ as a split epimorphism), this sequence is $\mathcal{E}$-exact. Applying the right $\mathcal{E}$-exact functor $T$ yields the exact sequence

$$T(A) \xrightarrow{T(1_A)} T(A) \xrightarrow{T(1_A)} T(A) \to 0.$$

Taking $A = 0$, the exactness forces $T(0) \to 0$ to be surjective, hence $T(0) = 0$.

Now we show $T$ preserves biproducts. For objects $A_1, A_2$ in $\mathfrak{A}$, consider the split exact (hence $\mathcal{E}$-exact) sequences

$$0 \to A_1 \xrightarrow{\iota_1} A_1 \oplus A_2 \xrightarrow{\pi_2} A_2 \to 0,$$
$$0 \to A_2 \xrightarrow{\iota_2} A_1 \oplus A_2 \xrightarrow{\pi_1} A_1 \to 0.$$

These are $\mathcal{E}$-exact because the epimorphisms $\pi_1, \pi_2$ split and splitting epimorphisms belong to any closed class $\mathcal{E}$. Applying $T$ and using right $\mathcal{E}$-exactness, we obtain that $T(\iota_1), T(\iota_2)$ are monic (since $T(0) = 0$) and the sequences are exact at the middle and right terms. Together with the relations $\pi_1 \iota_1 = 1_{A_1}$, $\pi_2 \iota_2 = 1_{A_2}$, $\pi_1 \iota_2 = 0$, $\pi_2 \iota_1 = 0$, which are preserved since $T$ is a functor, we deduce that $T(A_1 \oplus A_2) \cong T(A_1) \oplus T(A_2)$.

Finally, $T$ preserves addition of morphisms: given $f, g : A \to B$, their sum $f + g$ can be expressed as the composite

$$A \xrightarrow{\Delta} A \oplus A \xrightarrow{f \oplus g} B \oplus B \xrightarrow{\nabla} B,$$

where $\Delta$ is the diagonal and $\nabla$ the codiagonal. Since $T$ preserves split exact sequences (and hence biproducts, diagonals, and codiagonals), we obtain $T(f + g) = T(f) + T(g)$. Thus $T$ is additive.
