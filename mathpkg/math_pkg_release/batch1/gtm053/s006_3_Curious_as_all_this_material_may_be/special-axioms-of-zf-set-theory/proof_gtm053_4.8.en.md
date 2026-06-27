---
role: proof
locale: en
of_concept: special-axioms-of-zf-set-theory
source_book: gtm053
source_chapter: "I"
source_section: "4.8"
---

We verify each axiom in the von Neumann universe $V = \bigcup_\alpha V_\alpha$.

\textbf{(a) Axiom of the empty set:} The empty set $\varnothing$ is the unique set with no elements. Its existence in $V$ follows from the construction of the cumulative hierarchy (specifically, $\varnothing \in V_1$). The formula $\forall x \; \neg (x \in \varnothing)$ is true by definition.

\textbf{(b) Axiom of extensionality:} Two sets are equal if and only if they have the same elements. This holds in $V$ because sets in the von Neumann universe are genuine sets, and the membership relation $\in$ is the real membership relation. Hence $x = y$ iff $\forall z(z \in x \Leftrightarrow z \in y)$.

\textbf{(c) Axiom of pairing:} If $U, W \in V_\alpha$, then $\{U, W\} \in \mathcal{P}(V_\alpha) = V_{\alpha+1}$. Thus all pairs lie in $V$, and the pairing axiom holds.

\textbf{(d) Axiom of the union:} If $X \in V$, then $X \in V_{\alpha+1} = \mathcal{P}(V_\alpha)$ for some $\alpha$. The elements of $X$ are subsets of $V_\alpha$, and their union therefore lies in $V_{\alpha+1}$ (in fact, $\cup X \subseteq V_\alpha$, so $\cup X \in V_{\alpha+1}$). Hence the union axiom holds in $V$.

\textbf{(e) Axiom of the power set:} If $X \in V$, then $X \in V_\alpha$ for some $\alpha$. Hence $X \subset V_\alpha$, so $\mathcal{P}(X) \subset \mathcal{P}(V_\alpha) = V_{\alpha+1}$, which gives $\mathcal{P}(X) \in V_{\alpha+2}$. Thus the power set exists in $V$.

\textbf{(f) Axiom of regularity:} Any nonempty set $X \in V$ has an $\in$-minimal element, i.e., there exists $y \in X$ such that $y \cap X = \varnothing$. This is proved in the appendix to the chapter: take $y \in X$ of minimal rank (such a $y$ exists because ranks are ordinals and any nonempty collection of ordinals has a least element). Then no element of $y$ can belong to $X$, for if $z \in y \cap X$, then $\text{rank}(z) < \text{rank}(y)$, contradicting minimality.

The remaining ZF axioms (replacement, choice) are discussed separately in Section 4.9.
