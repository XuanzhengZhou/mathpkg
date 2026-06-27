---
role: proof
source_book: gtm-0073
chapter: "VIII"
section: "VIII.2"
proof_technique: exponent-manipulation
locale: en
content_hash: ""
written_against: ""
---
(i) If \(r \in \operatorname{Rad}(\operatorname{Rad} I)\), then \(r^n \in \operatorname{Rad} I\) and hence \(r^{nm} = (r^n)^m \in I\) for some \(n,m > 0\). Therefore \(r \in \operatorname{Rad} I\).

(ii) If \(r \in \bigcap_j \operatorname{Rad} I_j\), then there are \(m_1, \ldots, m_n > 0\) such that \(r^{m_j} \in I_j\) for each \(j\). Let \(m = m_1 + \cdots + m_n\); then \(r^m = r^{m_1} \cdots r^{m_n} \in I_1 \cdots I_n\), whence \(\bigcap_j \operatorname{Rad} I_j \subset \operatorname{Rad}(I_1 \cdots I_n)\). Since \(I_1 \cdots I_n \subset \bigcap_j I_j\), we have \(\operatorname{Rad}(I_1 \cdots I_n) \subset \operatorname{Rad}(\bigcap_j I_j)\). The reverse inclusion follows from \(\bigcap_j I_j \subset I_j\) for each \(j\).

(iii) is a special case of (ii).
