---
role: proof
source_book: gtm-0073
chapter: "VIII"
section: "VIII.4"
proof_technique: minimal-basis-and-nakayama
locale: en
content_hash: ""
written_against: ""
---
Choose a free \(R\)-module \(F\) with a finite basis having a minimal number of elements and an epimorphism \(\pi: F \to P\). Let \(K = \operatorname{Ker} \pi\). Show \(K \subset MF\) where \(M\) is the unique maximal ideal. If \(K \not\subset MF\), then there exists \(k = r_1 x_1 + \cdots + r_n x_n \in K\) with some \(r_i \notin M\). Since \(r_i\) is a unit (Theorem III.4.13), one can express \(x_i\) in terms of the other basis elements modulo \(K\), contradicting minimality. Thus \(K \subset MF\). Since \(P\) is projective, \(F = K \oplus P'\) for some \(P' \cong P\). Then \(K = K \cap MF = MK\), so by Nakayama's Lemma \(K = 0\) and \(P \cong F\) is free.
