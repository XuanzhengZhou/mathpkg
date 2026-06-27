---
role: proof
source_book: gtm-0073
chapter: I
section: "I.1"
proof_technique: well-definedness
locale: en
content_hash: ""
written_against: ""
---
If $\bar{a}_1 = \bar{a}_2$ and $\bar{b}_1 = \bar{b}_2$ ($a_i, b_i \in G$), then $a_1 \sim a_2$ and $b_1 \sim b_2$. By hypothesis $a_1b_1 \sim a_2b_2$ so that $\overline{a_1b_1} = \overline{a_2b_2}$. Therefore the binary operation in $G/R$ is well defined. It is associative since $\bar{a}(\bar{b}\bar{c}) = \bar{a}(\overline{bc}) = \overline{a(bc)} = \overline{(ab)c} = (\overline{ab})\bar{c}$. $\bar{e}$ is the identity element since $(\bar{a})(\bar{e}) = \overline{ae} = \bar{a} = \overline{ea} = (\bar{e})(\bar{a})$. Therefore $G/R$ is a monoid. If $G$ is a group, then $\bar{a} \in G/R$ clearly has inverse $\overline{a^{-1}}$ so that $G/R$ is also a group. Similarly, $G$ abelian implies $G/R$ abelian.
