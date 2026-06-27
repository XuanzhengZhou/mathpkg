---
role: proof
locale: en
of_concept: bourbaki-bilinear-equicontinuity
source_book: gtm003
source_chapter: "III"
source_section: "3"
---

Using the identity (for \(f \in B\)):
\[
f(x, y) - f(x_0, y_0) = f(x - x_0, y - y_0) + f(x - x_0, y_0) + f(x_0, y - y_0)
\]
and the separate equicontinuity of \(B\), it suffices to prove equicontinuity of \(B\) at \((0, 0)\).

Let \(\{U_n\}, \{V_n\}\) be decreasing sequences forming \(0\)-neighborhood bases in \(E, F\) respectively. For a given \(0\)-neighborhood \(W\) in \(G\), choose a \(0\)-neighborhood \(W_1\) with \(W_1 + W_1 + W_1 \subset W\).

For each \(n\), set
\[
A_n = \{x \in E : f(x, V_n) \subset W_1 \text{ for all } f \in B\}.
\]
Since \(B\) is separately equicontinuous, for each \(x \in E\) there exists \(n\) such that \(x \in A_n\); thus \(E = \bigcup_n A_n\). Each \(A_n\) is closed: if \(x \in \overline{A_n}\), then for any \(f \in B\) and \(y \in V_n\), the separate continuity of \(f\) implies \(f(x, y) \in \overline{W_1}\); by choosing \(W_1\) closed, \(f(x, y) \in W_1\), so \(x \in A_n\).

If \(E\) is a Baire space, some \(A_m\) has nonempty interior, so there exists \(m\) and a \(0\)-neighborhood \(U\) with \(U \subset A_m - A_m\). By bilinearity, this gives the required joint equicontinuity.

If \(E\) is barreled and \(G\) is locally convex, one shows each \(A_n\) is a barrel (closed, convex, circled, absorbing), hence a \(0\)-neighborhood, leading to the same conclusion.
