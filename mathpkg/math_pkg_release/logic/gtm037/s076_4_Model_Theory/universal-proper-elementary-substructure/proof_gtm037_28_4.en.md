---
role: proof
locale: en
of_concept: universal-proper-elementary-substructure
source_book: gtm037
source_chapter: "28"
source_section: "Saturated Structures"
---

Assume the hypothesis. Let $\mathfrak{B}$ be a proper elementary extension of $\mathfrak{A}$. Choose $b \in B \sim A$. Let $(\mathfrak{C}, a, b)_{a \in A}$ be an elementary substructure of $(\mathfrak{B}, a, b)_{a \in A}$ of power $m$. Thus $A \subseteq C$, and in fact $\mathfrak{A} \preceq \mathfrak{C}$. For, if $\varphi$ is any formula and $x \in {}^\omega A$, then $\mathfrak{A} \models \varphi[x]$ iff $\mathfrak{B} \models \varphi[x]$ iff $\mathfrak{C} \models \varphi[x]$. Also, note that $b \notin A$, so $\mathfrak{A}$ is a proper elementary substructure of $\mathfrak{C}$.

Now $|\mathfrak{C}| = m$ and $\mathfrak{A} \equiv_{\text{ee}} \mathfrak{C}$, so by $m^+$-universality of $\mathfrak{A}$ there exists an elementary embedding $f : \mathfrak{C} \to \mathfrak{A}$. Then $f \upharpoonright A$ is an elementary embedding of $\mathfrak{A}$ into itself whose image $f[A]$ is a proper elementary substructure, since $f(b) \notin f[A]$. Composing with the inverse of $f \upharpoonright A$ gives the desired isomorphism.
