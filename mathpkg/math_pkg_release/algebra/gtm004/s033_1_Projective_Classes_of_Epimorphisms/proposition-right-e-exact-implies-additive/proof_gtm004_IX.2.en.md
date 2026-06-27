---
role: proof
locale: en
of_concept: proposition-right-e-exact-implies-additive
source_book: gtm004
source_chapter: "IX"
source_section: "2. $\mathcal{E}$-Derived Functors"
---

# Proof of Right $\mathcal{E}$-Exact Functors Are Additive

**Proposition 2.4.** A right $\mathcal{E}$-exact functor $T : \mathfrak{A} \to \mathfrak{B}$ is additive.

**Proof.** (1) $T(0) = 0$: In $\mathfrak{A}$, the sequence $A \xrightarrow{1} A \xrightarrow{1} A \to 0$ is exact. Since identity morphisms are always $\mathcal{E}$-admissible (the epimorphism component of the canonical factorization of $1_A$ is an isomorphism, hence belongs to the closed class $\mathcal{E}$), this sequence is $\mathcal{E}$-exact. Right $\mathcal{E}$-exactness of $T$ yields exactness of $TA \xrightarrow{1} TA \xrightarrow{1} TA \to 0$. When $A = 0$, surjectivity of $T(0) \to 0$ forces $T(0) = 0$.

(2) $T$ preserves biproducts: For $A_1, A_2$, the split exact sequences

$$0 \to A_1 \to A_1 \oplus A_2 \to A_2 \to 0$$

are $\mathcal{E}$-exact (split epimorphisms belong to any closed class). Right $\mathcal{E}$-exactness then yields surjectivity of $T(A_1 \oplus A_2) \to T(A_2)$ along the projection, and injectivity of $T(A_1) \to T(A_1 \oplus A_2)$ along the injection (using $T(0) = 0$ and exactness at the right term). From the split relations $\pi_j \iota_i = \delta_{ij}$, we obtain $T(\pi_j) T(\iota_i) = \delta_{ij}$, which implies $T(A_1 \oplus A_2) \cong T(A_1) \oplus T(A_2)$.

(3) $T$ preserves addition: For $f, g : A \to B$, the sum is $f+g = \nabla_B \circ (f \oplus g) \circ \Delta_A$. Since $T$ preserves split exact sequences, it preserves the diagonal $\Delta_A$ and codiagonal $\nabla_B$, and commutes with $f \oplus g$ by the biproduct preservation. Hence $T(f+g) = T(f) + T(g)$. $\square$
