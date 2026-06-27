---
role: proof
locale: en
of_concept: equicontinuity-equivalences
source_book: gtm003
source_chapter: "III"
source_section: "3"
---

The equivalence (a) \(\Leftrightarrow\) (c) is essentially the definition of equicontinuity, restated using the condition \(\bigcup_{u \in H} u(U) \subset V\). 

(a) \(\Rightarrow\) (b): Given a \(0\)-neighborhood \(V\) in \(F\), equicontinuity provides a \(0\)-neighborhood \(U\) in \(E\) such that \(u(U) \subset V\) for all \(u \in H\). Then \(U \subset \bigcap_{u \in H} u^{-1}(V)\), so the intersection is a \(0\)-neighborhood.

(b) \(\Rightarrow\) (c): Given a \(0\)-neighborhood \(V\) in \(F\), set \(U = \bigcap_{u \in H} u^{-1}(V)\), which is a \(0\)-neighborhood by (b). Then for any \(x \in U\) and \(u \in H\), \(u(x) \in V\), so \(\bigcup_{u \in H} u(U) \subset V\).

(c) \(\Rightarrow\) (a): This is immediate from the definition of equicontinuity. The proof is similar to that of Proposition 3.3 and is omitted in the text.
