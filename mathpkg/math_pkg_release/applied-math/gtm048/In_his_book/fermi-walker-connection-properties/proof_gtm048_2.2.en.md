---
role: proof
locale: en
of_concept: fermi-walker-connection-properties
source_book: gtm048
source_chapter: "2"
source_section: "2.2"
---

The proofs consist of straightforward computations from the definition $F_Y X = [p(\gamma^* D)_Y p + q(\gamma^* D)_Y q]X$.

(a) Since $\gamma_*$ is purely temporal, $p \gamma_* = 0$ and $q \gamma_* = \gamma_*$. Then
$$F_{\gamma_*} \gamma_* = p(D_{\gamma_*}(p\gamma_*)) + q(D_{\gamma_*}(q\gamma_*)) = p(D_{\gamma_*} 0) + q(D_{\gamma_*} \gamma_*) = q(D_{\gamma_*} \gamma_*).$$
Now $g(\gamma_*, \gamma_*) = -1$, so differentiating along $\gamma$ gives $2g(D_{\gamma_*} \gamma_*, \gamma_*) = 0$. Thus $D_{\gamma_*} \gamma_*$ is orthogonal to $\gamma_*$, so its projection onto $T_u = \operatorname{span}\{\gamma_* u\}$ vanishes: $q(D_{\gamma_*} \gamma_*) = 0$. Hence $F_{\gamma_*} \gamma_* = 0$.

(b) If $qX = 0$, then $X = pX$. Thus
$$F_{\gamma_*} X = p(D_{\gamma_*}(pX)) + q(D_{\gamma_*}(qX)) = p(D_{\gamma_*} X) + q(0) = p(D_{\gamma_*} X).$$
Since $p$ projects onto $R_u$, we have $q(p(D_{\gamma_*} X)) = 0$, so $q(F_{\gamma_*} X) = 0$.

(c) If $pX = 0$, then $X = qX$. Thus
$$F_{\gamma_*} X = p(D_{\gamma_*}(pX)) + q(D_{\gamma_*}(qX)) = p(0) + q(D_{\gamma_*} X) = q(D_{\gamma_*} X).$$
Since $q$ projects onto $T_u$, we have $p(q(D_{\gamma_*} X)) = 0$, so $p(F_{\gamma_*} X) = 0$.
