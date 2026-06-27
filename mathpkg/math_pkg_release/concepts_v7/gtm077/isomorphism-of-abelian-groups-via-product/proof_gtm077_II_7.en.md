---
role: proof
locale: en
of_concept: isomorphism-of-abelian-groups-via-product
source_book: gtm077
source_chapter: "II"
source_section: "7"
---
# Direct Product of Abelian Groups

Let \(\mathfrak{G}_1\) and \(\mathfrak{G}_2\) be two abelian groups of orders \(h_1\) and \(h_2\), respectively.

**Definition.** The *direct product* \(\mathfrak{G} = \mathfrak{G}_1 \times \mathfrak{G}_2\) is defined as follows. Its elements are ordered pairs
\[
(A_1, A_2), \qquad A_i \in \mathfrak{G}_i,
\]
with equality \((A_1, A_2) = (B_1, B_2)\) meaning \(A_1 = B_1\) and \(A_2 = B_2\).

The composition law is component-wise:
\[
(A_1, A_2) \cdot (B_1, B_2) = (A_1 B_1, A_2 B_2).
\]

**Properties.**
1. \(\mathfrak{G}\) is an abelian group of order \(h_1 \cdot h_2\).
2. The unit element is \((E_1, E_2)\), where \(E_i\) is the identity of \(\mathfrak{G}_i\).
3. The subset \(\{(A_1, E_2) \mid A_1 \in \mathfrak{G}_1\}\) forms a subgroup isomorphic to \(\mathfrak{G}_1\) via the map \(A_1 \mapsto (A_1, E_2)\).
4. Similarly, \(\{(E_1, A_2) \mid A_2 \in \mathfrak{G}_2\}\) is a subgroup isomorphic to \(\mathfrak{G}_2\).
5. These two subgroups intersect only in the identity \((E_1, E_2)\).
6. Every element \((A_1, A_2)\) can be written uniquely as the product of an element from the first subgroup and an element from the second:
\[
(A_1, A_2) = (A_1, E_2) \cdot (E_1, A_2).
\]

**Generalization.** For \(r\) groups \(\mathfrak{G}_1, \ldots, \mathfrak{G}_r\), the direct product \(\mathfrak{G}_1 \times \cdots \times \mathfrak{G}_r\) is defined analogously with \(r\)-tuples and component-wise composition.

**Relation to Theorem 24/25.** If \(\mathfrak{G}\) has a basis \(B_1, \ldots, B_r\) with orders \(h_1, \ldots, h_r\), then
\[
\mathfrak{G} \cong \langle B_1 \rangle \times \langle B_2 \rangle \times \cdots \times \langle B_r \rangle,
\]
where each \(\langle B_i \rangle\) is a cyclic group of order \(h_i\). The isomorphism sends \(B_1^{x_1} \cdots B_r^{x_r}\) to \((B_1^{x_1}, \ldots, B_r^{x_r})\).

\(\square\)
