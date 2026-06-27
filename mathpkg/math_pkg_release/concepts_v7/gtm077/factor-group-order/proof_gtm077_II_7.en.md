---
role: proof
locale: en
of_concept: factor-group-order
source_book: gtm077
source_chapter: "II"
source_section: "7"
---
# Proof of Theorem 29: Order of the Factor Group

Let \(\mathfrak{G}\) be a (finite) abelian group and \(\mathfrak{U}\) a subgroup of \(\mathfrak{G}\). Let \(N = |\mathfrak{U}|\) and \(h = |\mathfrak{G}|\).

**Cosets.** For \(A \in \mathfrak{G}\), the set
\[
R_A = \{A \cdot U \mid U \in \mathfrak{U}\}
\]
is called the (left) coset of \(A\) with respect to \(\mathfrak{U}\). Since \(\mathfrak{U}\) is a subgroup, two cosets \(R_A\) and \(R_B\) are either identical or disjoint. The number of distinct cosets is the index \([\mathfrak{G} : \mathfrak{U}] = h/N\).

**Composition of cosets.** Define composition of cosets by
\[
R_A \cdot R_B = R_{AB}.
\]
This is well-defined: if \(A' = A U_1\) and \(B' = B U_2\) with \(U_1, U_2 \in \mathfrak{U}\), then
\[
A' B' = A B \cdot U_1 U_2,
\]
so \(A'B'\) lies in the same coset as \(AB\) (here commutativity of \(\mathfrak{G}\) is used since \(U_1 U_2 \in \mathfrak{U}\)).

**Axiom verification.** The cosets form a group under this composition:
- (i) Closure: \(R_A R_B = R_{AB}\) is again a coset.
- (ii) Associativity: follows from associativity in \(\mathfrak{G}\).
- (iii) Identity: \(R_E\) acts as the unit element since \(R_A R_E = R_{AE} = R_A\).
- (iv) Inverse: \(R_{A^{-1}}\) is the inverse of \(R_A\) since \(R_A R_{A^{-1}} = R_E\).

The composition is commutative because \(\mathfrak{G}\) is abelian: \(R_A R_B = R_{AB} = R_{BA} = R_B R_A\).

**Order.** The cosets therefore form an abelian group \(\mathfrak{R}\), called the *factor group* (or quotient group) of \(\mathfrak{G}\) by \(\mathfrak{U}\), denoted
\[
\mathfrak{R} = \mathfrak{G}/\mathfrak{U}.
\]
Its order equals the index of \(\mathfrak{U}\) in \(\mathfrak{G}\):
\[
|\mathfrak{G}/\mathfrak{U}| = \frac{h}{N}.
\]

\(\square\)
