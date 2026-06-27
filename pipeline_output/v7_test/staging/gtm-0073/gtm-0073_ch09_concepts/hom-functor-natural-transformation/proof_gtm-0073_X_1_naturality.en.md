---
role: proof
source_book: gtm-0073
chapter: X
section: "X.1"
proof_technique: diagram-chase
locale: en
content_hash: ""
written_against: ""
---
(i) Let $C$ be an object of $\mathcal{C}$ and $g \in \hom_{\mathcal{C}}(A,C)$. By hypothesis the diagram
\[
\begin{CD}
h_A(A) = \hom_{\mathcal{C}}(A,A) @>{\alpha_A}>> T(A) \\
@V{h_A(g)}VV @VV{T(g)}V \\
h_A(C) = \hom_{\mathcal{C}}(A,C) @>{\alpha_C}>> T(C)
\end{CD}
\]
is commutative. Consequently,
\[
\alpha_C(g) = \alpha_C(g \circ 1_A) = \alpha_C[h_A(g)(1_A)] = [\alpha_C h_A(g)](1_A) = (T(g)\alpha_A)(1_A) = T(g)[\alpha_A(1_A)] = T(g)(u).
\]

(ii) We must show that for every morphism $k : B \to C$ of $\mathcal{C}$ the diagram
\[
\begin{CD}
h_A(B) = \hom_{\mathcal{C}}(A,B) @>{\beta_B}>> T(B) \\
@V{h_A(k)}VV @VV{T(k)}V \\
h_A(C) = \hom_{\mathcal{C}}(A,C) @>{\beta_C}>> T(C)
\end{CD}
\]
is commutative. For any $f \in \hom_{\mathcal{C}}(A,B)$,
\[
\beta_C h_A(k)(f) = \beta_C(k \circ f) = T(k \circ f)(u) = T(k)T(f)(u) = T(k)\beta_B(f).
\]
Thus the diagram commutes. Finally, $\beta_A(1_A) = T(1_A)(u) = 1_{T(A)}(u) = u$.
