---
role: proof
locale: en
of_concept: single-connective-functional-completeness
source_book: gtm037
source_chapter: "8. Sentential Logic"
source_section: "8.2 Elements of Logic"
---

The connective $s$ is the Sheffer stroke (NAND). We show that both negation and conjunction can be expressed using only $s$, after which Theorem 8.43 applies.

Define negation: $\neg \varphi = \langle s \rangle \varphi \varphi$. For any model $h$,
$$h^+ \neg \varphi = g_s(h^+ \varphi, h^+ \varphi).$$
If $h^+ \varphi = 1$, then $g_s(1,1) = 0$; if $h^+ \varphi = 0$, then $g_s(0,0) = 1$. Thus $\neg$ has the correct truth table.

Define conjunction: $\varphi \wedge \psi = \neg (\langle s \rangle \varphi \psi) = \langle s \rangle (\langle s \rangle \varphi \psi) (\langle s \rangle \varphi \psi)$. Then
$$h^+ (\varphi \wedge \psi) = g_s(g_s(h^+ \varphi, h^+ \psi), g_s(h^+ \varphi, h^+ \psi)).$$
When $h^+ \varphi = h^+ \psi = 1$, we get $g_s(g_s(1,1), g_s(1,1)) = g_s(0,0) = 1$. In all other cases, $g_s(h^+ \varphi, h^+ \psi) = 1$, so $g_s(1,1) = 0$. This matches conjunction.

Since $\{\neg, \wedge\}$ is functionally complete by Theorem 8.43, and both are expressible using only $s$, $\mathcal{P}$ is functionally complete.
