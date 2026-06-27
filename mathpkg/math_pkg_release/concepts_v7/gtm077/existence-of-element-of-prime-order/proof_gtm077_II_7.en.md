---
role: proof
locale: en
of_concept: existence-of-element-of-prime-order
source_book: gtm077
source_chapter: "II"
source_section: "7"
---
# Proof of Theorem 22: Existence of an Element of Prime Order

Let \(\mathfrak{G}\) be a finite abelian group of order \(h\), and let \(p\) be a prime dividing \(h\).

Let \(C_1, C_2, \ldots, C_h\) be the \(h\) elements of \(\mathfrak{G}\) and let \(c_1, c_2, \ldots, c_h\) be their respective orders. Form all products

\[
C_1^{x_1} C_2^{x_2} \cdots C_h^{x_h},
\]

in which each \(x_i\) runs through a complete residue system modulo \(c_i\). This yields \(c_1 \cdot c_2 \cdots c_h\) formally different products, among which are all elements of \(\mathfrak{G}\).

Since a representation of the unit element is at once obtained from two different representations of the same element, all elements occur equally frequently—say \(Q\) times—in this product form. Consequently,

\[
c_1 c_2 \cdots c_h = h \cdot Q.
\]

The prime \(p\) divides \(h\), hence \(p\) must divide at least one \(c_i\). Without loss of generality let it be \(c_1\). Then set

\[
A = C_1^{c_1/p}.
\]

By Theorem 20 (on the order of powers of an element), the order of \(A\) is \(p\). Thus \(\mathfrak{G}\) contains an element of prime order \(p\).

\(\square\)
