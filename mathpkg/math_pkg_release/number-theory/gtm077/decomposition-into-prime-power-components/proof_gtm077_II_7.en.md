---
role: proof
locale: en
of_concept: decomposition-into-prime-power-components
source_book: gtm077
source_chapter: "II"
source_section: "7"
---
# Decomposition into Prime-Power Order Components

Let \(\mathfrak{G}\) be a finite abelian group of order \(h\). By the Fundamental Theorem of Arithmetic, decompose
\[
h = p_1^{k_1} p_2^{k_2} \cdots p_s^{k_s}
\]
into distinct prime powers. Set \(a_i = p_i^{k_i}\). Then \(h = a_1 a_2 \cdots a_s\) with the \(a_i\) pairwise relatively prime.

**Step 1: Decomposition into \(a_i\)-torsion subgroups.** By Theorem 23, each element \(C \in \mathfrak{G}\) can be uniquely expressed as
\[
C = A_1 \cdot A_2 \cdots A_s,
\]
where \(A_i^{a_i} = E\) for \(i = 1, \ldots, s\). Let
\[
\mathfrak{G}_{(a_i)} = \{A \in \mathfrak{G} \mid A^{a_i} = E\}
\]
be the subgroup of elements whose order divides \(a_i\) (the \(a_i\)-torsion subgroup). Then \(\mathfrak{G}\) is isomorphic to the direct product
\[
\mathfrak{G} \cong \mathfrak{G}_{(a_1)} \times \mathfrak{G}_{(a_2)} \times \cdots \times \mathfrak{G}_{(a_s)}.
\]

**Step 2: Prime-power case.** Each \(\mathfrak{G}_{(a_i)}\) is a finite abelian group of order \(p_i^{k_i}\). As shown in the proof of the Fundamental Theorem of Finite Abelian Groups (Theorem 24/25), every such group admits a basis \(B_{i,1}, \ldots, B_{i,r_i}\) of independent elements whose orders are powers of \(p_i\). Hence
\[
\mathfrak{G}_{(a_i)} \cong \mathbb{Z}/p_i^{m_{i,1}}\mathbb{Z} \times \cdots \times \mathbb{Z}/p_i^{m_{i,r_i}}\mathbb{Z}.
\]

**Step 3: Assembly.** Combining the isomorphisms,
\[
\mathfrak{G} \cong \prod_{i=1}^{s} \prod_{j=1}^{r_i} \mathbb{Z}/p_i^{m_{i,j}}\mathbb{Z},
\]
which exhibits \(\mathfrak{G}\) as a direct product of cyclic groups of prime-power orders. The sequence of prime powers \((p_1^{m_{1,1}}, \ldots, p_1^{m_{1,r_1}}, \ldots, p_s^{m_{s,1}}, \ldots, p_s^{m_{s,r_s}})\) are the *elementary divisors* of \(\mathfrak{G}\) and are uniquely determined (up to ordering) by the group structure.

\(\square\)
