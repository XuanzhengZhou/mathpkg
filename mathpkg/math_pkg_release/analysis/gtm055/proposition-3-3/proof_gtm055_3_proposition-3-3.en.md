---
role: proof
locale: en
of_concept: proposition-3-3
source_book: gtm055
source_chapter: "3"
source_section: "Section 04_Section_4"
---

PROOF. If $C \cap \partial A = \varnothing$ and $x \in C \cap A$, then $x \in A^\circ$. Thus $C \cap A = C \cap A^\circ$ is open relative to $C$. Since $A$ and $X \setminus A$ have the same boundary, this shows that $C \setminus A$ is also open relative to $C$. Thus $C = (C \cap A) \cup (C \setminus A)$ expresses $C$ as the union of two disjoint relatively open subsets, one of which must be empty.

**Example H.** A collection $\%$ of subsets of a set $X$ is said to be chained if for any two sets $C_0, C_1$ in $\%$ there is a finite sequence $\{D_0, \ldots, D_n\}$ of sets in $\%$ such that $D_{i-1} \cap D_i \neq \varnothing$, $i = 1, \ldots, n$, and such that $D_0 = C_0$ and $D_n = C_1$. Suppose given a chained collection $\%$ of connected subsets of a topological space $X$, let $E$ denote the union of the sets in $\%$, and let $A$ be a closed-open subset of $E$. Then $\partial A = \varnothing$ in the subspace $E$. Thus if $C$ is a connected subset of $E$, then either $C \cap A = \varnothing$ or $C \subset A$. In particular, this is true of each of the sets in $\%$. Thus if $A \neq \varnothing$, then $A$ contains some one of the sets in $\%$. But then, since $\%$ is chained, it is seen at once that $A$ must contain every set in $\%$. Thus $A = E$, and we have proved that $E$ is connected.

**Example I.** Every interval or ray in $\mathbb{R}$, open, closed, or half-open (including the space $\mathbb{R}$ itself), is connected. To see this we note first that if $I$ is either an interval or a ray (or $\mathbb{R}$), then the closed

If $U$ is an open subset of $\mathbb{R}$, then $U$ can be expressed uniquely as a countable union of pairwise disjoint nonempty open intervals, and these intervals are the connected components of $U$.

Proof. That (iii) implies (i) was proved in Example I, while the proof that (ii) implies (iii) amounts to nothing more than a careful consideration of cases. Finally, to show that (i) implies (ii) we note that $(-\infty, c) \cup (c, +\infty)$ is a disconnection of the set $\mathbb{R} \setminus \{c\}$ obtained by removing a single point $c$ from $\mathbb{R}$. Hence if $C$ is a connected subset of $\mathbb{R}$ that does not contain $c$, then either $C \subset (-\infty, c)$ or $C \subset (c, +\infty)$.

To prove the last assertion of the proposition we observe that, since $U$ is open, every nonopen interval that is contained in $U$ is contained in an open interval contained in $U$. It follows from this that the connected components of $U$ are all open intervals. That no disjoint collection of nonempty open intervals can be uncountable follows from the fact that $\mathbb{R}$ satisfies the second axiom of countability. To complete the proof it suffices to observe that if $\{I_n\}$ is a disjoint (countable) collection of nonempty open intervals such that $U = \bigcup_n I_n$, and if $V$ is a connected component of $U$ that meets some one $I_n$, then neither endpoint of $I_n$ can belong to $V$, and therefore $V = I_n$ (Prop. 3.6).

If $X$ is a connected space and $f: X \rightarrow Y$ is a continuous mapping, then $f(X)$ is a connected set in $Y$. Thus, in particular, if $f$ is a continuous mapping of a closed interval $[a, b]$ into $Y$, then the range of $f$ is connected in $Y$. Such a mapping is called an arc in $Y$, and $[a, b]$ is the parameter interval of the arc $f$. If $f(a) = y_0$ and $f(b) = y_1$,

but there are some useful things that can be said. (In this discussion we speak of the complex plane $\mathbb{C}$, but the following facts are equally valid for the real plane $\mathbb{R}^2$, which may be identified with $\mathbb{C}$ via the standard homeomorphism $s + it \leftrightarrow (s, t)$.) We begin by recalling that a domain in $\mathbb{C}$ is a nonempty connected open subset of $\mathbb{C}$.
