---
role: proof
locale: en
of_concept: coprime-order-decomposition
source_book: gtm077
source_chapter: "II"
source_section: "7"
---
# Proof of Theorem 23: Decomposition by Coprime Orders

Let \(\mathfrak{G}\) be a finite abelian group whose order \(h\) decomposes as

\[
h = a_1 \cdot a_2 \cdots a_r
\]

with the \(a_i\) pairwise relatively prime.

**Existence.** For each \(i = 1, 2, \ldots, r\) choose integers \(u_i, v_i\) such that

\[
u_i \cdot \frac{h}{a_i} + v_i \cdot a_i = 1,
\]

which is possible since \((a_i, h/a_i) = 1\) by the pairwise coprimality of the \(a_j\). Set

\[
A_i = C^{u_i \cdot h/a_i}.
\]

Then by Theorem 21 (which controls the order of powers of elements),

\[
A_i^{a_i} = C^{u_i \cdot h} = (C^h)^{u_i} = E^{u_i} = E.
\]

Moreover, since composition in \(\mathfrak{G}\) is commutative, the product of the \(A_i\) reconstructs \(C\):

\[
A_1 \cdot A_2 \cdots A_r = C^{\sum_i u_i \cdot h/a_i}.
\]

From the relation \(u_i \cdot h/a_i + v_i \cdot a_i = 1\) one deduces (using the Chinese remainder argument) that \(\sum_i u_i \cdot h/a_i \equiv 1 \pmod{h}\), hence

\[
C = A_1 \cdot A_2 \cdots A_r.
\]

**Uniqueness.** Suppose \(C = B_1 \cdot B_2 \cdots B_r\) is another representation with \(B_i^{a_i} = E\). Raise both representations to the power \(h/a_1\):

\[
(B_1 \cdots B_r)^{h/a_1} = (A_1 \cdots A_r)^{h/a_1}.
\]

Since the group is abelian (commutativity is used here for the first time in the proof), we expand:

\[
B_1^{h/a_1} \cdot B_2^{h/a_1} \cdots B_r^{h/a_1} = A_1^{h/a_1} \cdot A_2^{h/a_1} \cdots A_r^{h/a_1}.
\]

Now \(h/a_1\) is a multiple of each \(a_2, a_3, \ldots, a_r\), so the factors with indices \(2, 3, \ldots, r\) are all \(E\) by the condition \(B_i^{a_i} = E\) (and similarly for \(A_i\)). Hence

\[
B_1^{h/a_1} = A_1^{h/a_1}.
\]

Since \((a_1, h/a_1) = 1\), there exist integers \(x, y\) with \(a_1 x + (h/a_1) y = 1\). Using \(E = B_1^{a_1} = A_1^{a_1}\),

\[
B_1 = B_1^{a_1 x + (h/a_1) y} = A_1^{a_1 x + (h/a_1) y} = A_1.
\]

By symmetry and induction, \(A_i = B_i\) for all \(i\).

\(\square\)
