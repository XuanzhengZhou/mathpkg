---
role: proof
source_book: gtm-0073
chapter: "VIII"
section: "VIII.2"
proof_technique: minimal-exponent-argument
locale: en
content_hash: ""
written_against: ""
---
Suppose (i) and (ii) hold. If \(ab \in Q\) with \(a \notin Q\), then \(b \in P \subset \operatorname{Rad} Q\) by (ii), whence \(b^n \in Q\) for some \(n > 0\). Therefore \(Q\) is primary. To show \(Q\) is primary for \(P\) we need only show \(P = \operatorname{Rad} Q\). By (i), \(P \subset \operatorname{Rad} Q\). If \(b \in \operatorname{Rad} Q\), let \(n\) be the least integer such that \(b^n \in Q\). If \(n = 1\), \(b \in Q \subset P\). If \(n > 1\), then \(b^{n-1}b = b^n \in Q\), with \(b^{n-1} \notin Q\) by the minimality of \(n\). By (ii), \(b \in P\). Thus \(b \in \operatorname{Rad} Q\) implies \(b \in P\), whence \(\operatorname{Rad} Q \subset P\). The converse implication is straightforward.
