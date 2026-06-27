---
role: proof
locale: en
of_concept: elementary-sets
source_book: gtm037
source_chapter: "3"
source_section: "1"
---
\begin{proof}
(i) $\chi_0 = C_0^1$, which is elementary by Proposition 2.8(i). Hence $0$ is an elementary set.

(ii) $\chi_\omega = C_1^1$, which is elementary by Proposition 2.8(i). Hence $\omega$ is elementary.

(iii) If $x \in \omega$, then for any $y \in \omega$,
$$\chi_{\{x\}}(y) = \overline{\text{sg}}(|x - y|).$$
Equivalently, $\chi_{\{x\}}(y) = \overline{\text{sg}}(|C_x^1 y - U_0^1 y|)$. Since $\overline{\text{sg}}$ and the absolute difference function are elementary, and composition preserves elementariness, the characteristic function $\chi_{\{x\}}$ is elementary. Therefore $\{x\}$ is an elementary set.
\end{proof}
