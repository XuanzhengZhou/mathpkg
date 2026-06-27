---
role: proof
source_book: gtm-0073
chapter: "VIII"
section: "VIII.4"
proof_technique: minimal-generating-set-and-unit-argument
locale: en
content_hash: ""
written_against: ""
---
(i) \(\Rightarrow\) (ii) If \(j \in J\) and \(1_R - j\) is not a unit, then the ideal \((1_R - j)\) is not \(R\) itself and is contained in a maximal ideal \(M \neq R\). But \(1_R - j \in M\) and \(j \in J \subset M\) imply \(1_R \in M\), contradiction. Therefore \(1_R - j\) is a unit.

(ii) \(\Rightarrow\) (iii) Since \(A\) is finitely generated, there is a minimal generating set \(\{a_1, \ldots, a_n\}\). If \(A \neq 0\), then \(a_1 \neq 0\). Since \(JA = A\), \(a_1 = j_1 a_1 + \cdots + j_n a_n\) with \(j_i \in J\). Thus \((1_R - j_1)a_1 = j_2 a_2 + \cdots + j_n a_n\). Since \(1_R - j_1\) is a unit, \(a_1\) is a linear combination of \(a_2, \ldots, a_n\), contradicting minimality. Hence \(A = 0\).

(iii) \(\Rightarrow\) (iv) Apply (iii) to \(A/B\); since \(J(A/B) = A/B\), we have \(A/B = 0\).
