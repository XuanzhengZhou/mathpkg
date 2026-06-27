---
role: proof
source_book: gtm-0073
chapter: "VIII"
section: "VIII.7"
proof_technique: change-of-variables-and-induction
locale: en
content_hash: ""
written_against: ""
---
Let \(R = K[u_1, \ldots, u_n]\). If the \(u_i\) are algebraically independent, \(r = n\) and we are done. Otherwise, there is an algebraic relation. By a suitable linear change of variables (choosing positive integers \(m_i\) and setting \(v_i = u_i - u_1^{m_i}\)), one makes \(u_1\) integral over \(K[v_2, \ldots, v_n]\). Then \(R\) is integral over \(K[v_2, \ldots, v_n]\) and \(F\) is algebraic over \(K(v_2, \ldots, v_n)\). By transitivity of integrality (Theorem 5.6), repeatedly applying this process yields an algebraically independent subset of size \(r\) over which \(R\) is integral.
