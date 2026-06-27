---
role: proof
locale: en
of_concept: lemma-68c8b93f
source_book: gtm077
source_chapter: "II"
source_section: "7"
---
# Proof of Lemma (b): Replacement Lemma

Let \(\mathfrak{G}\) be a finite abelian group of prime-power order \(p^k\). Let \(B_1, \ldots, B_r\) be a maximal system of independent elements with orders \(h_1 \geq h_2 \geq \cdots \geq h_r > 1\), each a power of \(p\).

**Statement.** Replace \(B_m\) by
\[
A = B_m^u \cdot B_{m+1}^{x_{m+1}} \cdots B_r^{x_r},
\]
where \(u \not\equiv 0 \pmod{p}\) and the \(x_i\) are arbitrary integers. Then the new system (renumbered to decreasing orders) remains a maximal independent system.

**Proof.** First, \(A\) has the same order as \(B_m\). Indeed, since the orders of \(B_{m+1}, \ldots, B_r\) are divisors of the order of \(B_m\) (powers of \(p\) in decreasing sequence), raising the defining expression to the order of \(B_m\) yields \(E\); and since \(u\) is not divisible by \(p\), the exact order is preserved.

Second, each product of powers of \(A, B_{m+1}, \ldots, B_r\) is a product of powers of \(B_m, B_{m+1}, \ldots, B_r\) (by substituting the expression for \(A\)). Conversely, since \(u \not\equiv 0 \pmod{p}\) and we work modulo \(p\)-powers, \(u\) is invertible modulo the order of \(B_m\), so there exists \(v\) with \(uv \equiv 1 \pmod{\operatorname{ord}(B_m)}\), and
\[
B_m = A^v \cdot B_{m+1}^{-v x_{m+1}} \cdots B_r^{-v x_r},
\]
showing that each product of powers of \(B_m, \ldots, B_r\) is a product of powers of \(A, B_{m+1}, \ldots, B_r\).

Therefore the new system spans the same subgroup as the original \(B_i\). Since the original system was independent, the new one is too, and since it spans the same set of elements it is also maximal.

\(\square\)
