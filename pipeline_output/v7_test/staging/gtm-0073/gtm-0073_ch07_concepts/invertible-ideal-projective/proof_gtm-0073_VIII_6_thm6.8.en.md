---
role: proof
source_book: gtm-0073
chapter: "VIII"
section: "VIII.6"
proof_technique: dual-basis-splitting
locale: en
content_hash: ""
written_against: ""
---
(\(\Rightarrow\)) By Lemma 6.7, \(I = R b_1 + \cdots + R b_n\) with \(b_i \in I\) and \(1_R = \sum a_i b_i\) with \(a_i \in I^{-1}\). Let \(F\) be free on \(\{e_1, \ldots, e_n\}\) with \(\pi(e_i) = b_i\). Define \(\zeta: I \to F\) by \(\zeta(c) = \sum c a_i e_i\) (note \(c a_i \in R\) since \(a_i \in I^{-1}\)). Then \(\pi \circ \zeta = 1_I\), so the sequence splits and \(I\) is a direct summand of a free module, hence projective.

(\(\Leftarrow\)) Let \(X = \{b_j\}\) generate \(I\) projectively, choose \(b_0 \in X\). Let \(F\) be free on \(\{e_j\}\) with \(\phi(e_j) = b_j\). Since \(I\) is projective, \(\operatorname{Ker} \phi\) is a direct summand and there exists a splitting \(\psi: I \to F\). Write \(\psi(b_0) = \sum a_j e_j\) with \(a_j \in R\). One verifies that the \(a_j\) define an element \(\sum a_j b_j^{-1} b_0 \in I^{-1}\) giving the invertibility.
