---
role: proof
source_book: gtm-0073
chapter: VII
section: "VII.3"
proof_technique: multiplicative
locale: en
content_hash: ""
written_against: ""
---
(i) By Theorem 3.3, both $f$ and $f(I_n) \cdot d$ are alternating $n$-linear forms taking value $f(I_n)$ at $I_n$, so they are equal by uniqueness.

(ii) For fixed $B$, the map $A \mapsto |AB|$ is an alternating multilinear form, hence equals $|B| \cdot |A|$ by (i).

(iii) If $A$ is invertible, $|A||A^{-1}| = |AA^{-1}| = |I_n| = 1$, so $|A|$ is a unit. Conversely, if $|A|$ is a unit, then $A$ is invertible by Proposition 3.7.

(iv) $|PAP^{-1}| = |P||A||P|^{-1} = |A|$ since $R$ is commutative.

(v) Computed via the Leibniz expansion: $|A^t| = \sum_{\sigma} (\operatorname{sgn} \sigma) a_{\sigma 1,1} \cdots a_{\sigma n,n} = \sum_{\sigma^{-1}} (\operatorname{sgn} \sigma^{-1}) a_{1,\sigma^{-1}1} \cdots a_{n,\sigma^{-1}n} = |A|$.

(vi) For triangular matrices, only the identity permutation contributes a nonzero product $a_{11} \cdots a_{nn}$.
