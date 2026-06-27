---
role: proof
locale: en
of_concept: theorem-27
source_book: gtm077
source_chapter: "II"
source_section: "7"
---
# Proof of Theorem 27: Basis Number

Let \(\mathfrak{G}\) be a finite abelian group of order \(h = p^k\) (the prime-power case suffices by Theorem 23). Let \(B_1, B_2, \ldots, B_r\) be a basis of \(\mathfrak{G}\) with orders \(h_1, h_2, \ldots, h_r\), each a power of \(p\). Let \(B_1, \ldots, B_e\) be those basis elements whose orders are divisible by \(p\) (equivalently, whose orders are \(> 1\) since all orders are powers of \(p\)). The integer \(e\) is called the *basis number* belonging to \(p\).

Any element \(A \in \mathfrak{G}\) can be expressed as
\[
A = B_1^{x_1} B_2^{x_2} \cdots B_e^{x_e} B_{e+1}^{x_{e+1}} \cdots B_r^{x_r},
\]
with \(0 \leq x_i < h_i\). The condition \(A^p = E\) translates to
\[
p x_i \equiv 0 \pmod{h_i} \qquad (i = 1, 2, \ldots, r).
\]

For \(i > e\), the order \(h_i\) is not divisible by \(p\) (hence \(h_i = 1\), meaning those basis elements are trivial). For \(i \leq e\), \(h_i = p^{k_i}\) with \(k_i \geq 1\), and the congruence \(p x_i \equiv 0 \pmod{p^{k_i}}\) means \(x_i \equiv 0 \pmod{p^{k_i-1}}\), so \(x_i\) can take exactly \(p\) values modulo \(p^{k_i}\) (namely \(0, p^{k_i-1}, 2p^{k_i-1}, \ldots, (p-1)p^{k_i-1}\)).

Thus the number of elements \(A\) satisfying \(A^p = E\) is exactly \(p^e\). Since \(e\) is defined purely in terms of \(p\) and the group structure, and the left-hand side \(p^e\) counts the elements regardless of the choice of basis, the basis number \(e\) is independent of the choice of basis.

\(\square\)
