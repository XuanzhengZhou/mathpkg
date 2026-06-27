---
role: proof
locale: en
of_concept: relations-between-ideals-in-r-and-r-m
source_book: gtm028
source_chapter: "III"
source_section: "10"
---

\textbf{Proof of (a).} An element $b \in R$ belongs to $\mathfrak{a}^{ec}$ if and only if $h(b) = \mathfrak{a}^e$. Now $h(b) \in \mathfrak{a}^e$ means there exist $a \in \mathfrak{a}$ and $m \in M$ such that $h(b) = h(a)/h(m)$ in $R_M$. This is equivalent to the existence of $m' \in M$ such that $h(m')h(b)h(m) = h(m')h(a)$ in $R_M$, i.e., $m'bm = m'a$ in $R$, which implies $b(mm') \in \mathfrak{a}$. Thus $b \in \mathfrak{a}^{ec}$ if and only if there exists $m \in M$ with $bm \in \mathfrak{a}$, proving (a).

\textbf{Proof of (b).} From (a), $\mathfrak{a}^e = R_M$ is equivalent to $1 \in \mathfrak{a}^{ec}$, which means there exists $m \in M$ such that $1 \cdot m \in \mathfrak{a}$, i.e., $m \in \mathfrak{a} \cap M$. Conversely, if $m \in \mathfrak{a} \cap M$, then $1 = h(m)/h(m) \in \mathfrak{a}^e$, so $\mathfrak{a}^e = R_M$. Thus $\mathfrak{a}^e = R_M$ if and only if $\mathfrak{a} \cap M \neq \emptyset$.

\textbf{Proof of (c).} If $\mathfrak{a}'$ is an ideal in $R_M$, any element $x'$ of $\mathfrak{a}'$ may be written in the form $x' = h(x)/h(m)$ with $x \in R$, $m \in M$. Then $h(x) = x' \cdot h(m) \in \mathfrak{a}'$, so $x \in \mathfrak{a}'^{c}$, and therefore $x' = h(x)/h(m) \in \mathfrak{a}'^{ce}$. Thus $\mathfrak{a}' \subset \mathfrak{a}'^{ce}$. Since the reverse inclusion $\mathfrak{a}'^{ce} \subset \mathfrak{a}'$ holds for any extension-contraction pair, equality follows.

\textbf{Proof of (d).} Part (c) shows that the contraction map $\mathfrak{a}' \mapsto \mathfrak{a}'^{c}$ is injective, since if $\mathfrak{a}'^{c} = \mathfrak{b}'^{c}$, then $\mathfrak{a}' = \mathfrak{a}'^{ce} = \mathfrak{b}'^{ce} = \mathfrak{b}'$. Its image is by definition the set of contracted ideals. That the correspondence preserves addition, multiplication, intersection, and quotient follows from the fact that extension preserves all these operations and contraction preserves intersection and quotient; the claim for the remaining operations follows from (c).
