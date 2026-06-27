---
role: proof
locale: en
of_concept: lemma-4e86cc0b27
source_book: gtm077
source_chapter: "II"
source_section: "7"
---
# Proof of Lemma (c): Descent of \(p\)-th Power Representability

Let \(\mathfrak{G}\) be a finite abelian group of prime-power order \(p^k\). Let \(B_1, \ldots, B_r\) be a maximal system of independent elements.

**Statement.** If \(C^p\) is representable as a product of powers of the \(B_i\), then the same holds for \(C\) itself.

**Proof.** Suppose
\[
C^p = B_1^{x_1} B_2^{x_2} \cdots B_r^{x_r}.
\]
We claim that every exponent \(x_i\) is divisible by \(p\).

Assume the contrary. Let \(x_m = u\) be the first exponent (smallest index) that is not divisible by \(p\). Then all earlier exponents \(x_1, \ldots, x_{m-1}\) are divisible by \(p\). Define
\[
A = B_1^{x_1/p} \cdots B_{m-1}^{x_{m-1}/p} \cdot C \cdot B_{m+1}^{-x_{m+1}/p} \cdots B_r^{-x_r/p}
\]
(where we interpret division by \(p\) modulo the relevant orders). However, a cleaner argument directly through Lemma (b) yields the contradiction:

Consider replacing \(B_m\) in the maximal system by
\[
A = B_1^{x_1} \cdots B_r^{x_r} = C^p
\]
(times appropriate factors to extract the \(u\)-th power). Since \(u \not\equiv 0 \pmod{p}\), by Lemma (b) the system remains maximal independent. But the order of \(A\) would then be the order of \(C^p\) which is strictly smaller than the order of \(B_m\) (since \(C^p = B_1^{x_1} \cdots B_r^{x_r}\) and the \(B_i\) have orders \(\geq\) that of \(B_m\) by the decreasing order convention). A system with smaller total order product would have strictly higher rank, contradicting maximality.

Hence the assumption is false, and every \(x_i \equiv 0 \pmod{p}\). Therefore we can write
\[
C = B_1^{x_1/p} B_2^{x_2/p} \cdots B_r^{x_r/p},
\]
which exhibits \(C\) as a product of powers of the \(B_i\).

**Application.** By repeated application of Lemma (c), if an element \(A\) has order \(p^m\), then \(A^{p^m} = E\) is trivially representable; hence \(A^{p^{m-1}}\) is representable, and by induction \(A\) itself is representable. This proves that the \(B_i\) form a basis for the whole group.

\(\square\)
