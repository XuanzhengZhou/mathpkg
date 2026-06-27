---
role: proof
source_book: gtm-0073
chapter: "VIII"
section: "VIII.1"
proof_technique: contrapositive
locale: en
content_hash: ""
written_against: ""
---
Suppose \(A\) satisfies the minimum condition and \(A_1 \supset A_2 \supset \cdots\) is a descending chain. The set \(\{A_i \mid i \geq 1\}\) has a minimal element \(A_n\). For \(i \geq n\), \(A_n \supset A_i\) by hypothesis and \(A_n \subset A_i\) by minimality, so \(A_i = A_n\). Thus DCC holds.

Conversely, suppose DCC holds and \(S\) is a nonempty set of submodules with no minimal element. Choose \(B_0 \in S\). For each \(B \in S\), there exists \(B' \in S\) with \(B \supset B'\). Using the Axiom of Choice, select one such \(B'\) for each \(B\), defining \(f: S \to S\). By the Recursion Theorem, there exists \(\varphi: \mathbb{N} \to S\) with \(\varphi(0) = B_0\) and \(\varphi(n+1) = f(\varphi(n))\). This yields an infinite strictly descending chain, contradicting DCC. The ACC case is analogous.
