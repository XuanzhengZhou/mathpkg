---
role: proof
locale: en
of_concept: cyclic-group-characterization
source_book: gtm077
source_chapter: "II"
source_section: "7"
---
# Proof of Theorem 28: Characterization of Cyclic Abelian Groups

Let \(\mathfrak{G}\) be a finite abelian group of order \(h\).

**Necessity.** Suppose \(\mathfrak{G}\) is cyclic with generator \(C\):
\[
\mathfrak{G} = \{C, C^2, \ldots, C^{h-1}, C^h = E\}.
\]
Let \(A = C^x\) satisfy \(A^p = E\) for a prime \(p \mid h\). Then \(C^{px} = E\), so \(px \equiv 0 \pmod{h}\), which means \(x \equiv 0 \pmod{h/p}\). Hence \(x\) has exactly \(p\) values modulo \(h\):
\[
x = \frac{h}{p}, \frac{2h}{p}, \ldots, \frac{ph}{p} \pmod{h},
\]
each giving a distinct element \(A\). Thus there are exactly \(p\) elements with \(A^p = E\).

**Sufficiency.** Conversely, suppose for every prime \(p \mid h\) the number of elements \(A\) with \(A^p = E\) is exactly \(p\). By Theorem 27, this means the basis number \(e(p)\) belonging to each \(p\) equals \(1\). Hence exactly one basis element corresponds to each prime dividing \(h\). Decompose \(h\) into distinct prime powers:
\[
h = p_1^{k_1} p_2^{k_2} \cdots p_r^{k_r}.
\]
Then \(\mathfrak{G}\) has a basis \(B_1, \ldots, B_r\) with \(B_i\) of order \(h_i = p_i^{k_i}\). Every element is
\[
A = B_1^{x_1} B_2^{x_2} \cdots B_r^{x_r}.
\]
Now define \(C = B_1 \cdot B_2 \cdots B_r\). If \(u\) is the order of \(C\), then by the basis property \(u \equiv 0 \pmod{h_i}\) for each \(i\), hence \(u\) is a multiple of each \(h_i\), so \(u = h\). Thus the successive powers \(C, C^2, \ldots, C^h = E\) give \(h\) distinct elements—all of \(\mathfrak{G}\). Hence \(\mathfrak{G}\) is cyclic.

\(\square\)
