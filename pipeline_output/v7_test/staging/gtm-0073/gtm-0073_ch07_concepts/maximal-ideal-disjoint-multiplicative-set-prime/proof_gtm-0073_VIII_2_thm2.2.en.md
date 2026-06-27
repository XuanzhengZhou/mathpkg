---
role: proof
source_book: gtm-0073
chapter: "VIII"
section: "VIII.2"
proof_technique: zorns-lemma-and-prime-test
locale: en
content_hash: ""
written_against: ""
---
The set \(\mathcal{S}\) of all ideals of \(R\) that are disjoint from \(S\) and contain \(I\) is nonempty since \(I \in \mathcal{S}\). Since \(S \neq \emptyset\), every ideal in \(\mathcal{S}\) is properly contained in \(R\). \(\mathcal{S}\) is partially ordered by inclusion. By Zorn's Lemma there is an ideal \(P\) which is maximal in \(\mathcal{S}\). Let \(A, B\) be ideals of \(R\) such that \(AB \subset P\). If \(A \not\subset P\) and \(B \not\subset P\), then by maximality of \(P\) both \((P + A)\) and \((P + B)\) intersect \(S\). Hence there exist \(s_1 \in S \cap (P + A)\) and \(s_2 \in S \cap (P + B)\). Then \(s_1 s_2 \in S \cap (P + A)(P + B) \subset S \cap P\), contradicting that \(P \cap S = \emptyset\). Therefore \(P\) is prime.
