---
role: proof
source_book: gtm-0073
chapter: "VIII"
section: "VIII.3"
proof_technique: maximal-counterexample-and-module-construction
locale: en
content_hash: ""
written_against: ""
---
Let \(\mathcal{S}\) be the set of all submodules of \(B\) that do not have a primary decomposition. If \(\mathcal{S}\) is nonempty, then by Theorem 1.4 \(\mathcal{S}\) contains a maximal element \(C\). Since \(C\) is not primary, there exist \(r \in R\) and \(b \in B \setminus C\) such that \(rb \in C\) but \(r^n B \not\subset C\) for all \(n > 0\). Let \(B_n = \{x \in B \mid r^n x \in C\}\). Then \(B_1 \subset B_2 \subset \cdots\). By the ACC there exists \(k > 0\) such that \(B_i = B_k\) for \(i \geq k\). Define \(D = \{x \in B \mid x = r^k y + c \text{ for some } y \in B, c \in C\}\). One shows \(B_k \cap D = C\). Since \(b \in B_k \setminus C\) and \(r^k B \not\subset C\), both \(B_k\) and \(D\) strictly contain \(C\). By maximality, \(B_k\) and \(D\) have primary decompositions, which intersect to yield a primary decomposition for \(C\), a contradiction.
