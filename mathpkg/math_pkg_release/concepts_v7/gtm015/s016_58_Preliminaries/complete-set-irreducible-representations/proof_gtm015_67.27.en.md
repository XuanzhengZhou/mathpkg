---
role: proof
locale: en
of_concept: complete-set-irreducible-representations
source_book: gtm015
source_chapter: "67"
source_section: "States and representations"
---

# Proof of Complete set of irreducible representations

Proof. If $A$ is a $C^*$-algebra with unity and if $a, b \in A, a \neq b$, the assertion is that there exist a Hilbert space $H$ and an irreducible $*-representation x \mapsto T_x$ of $A$ on $H$, such that $T_a \neq T_b$.

The set of all normalized states on $A$ is nonempty (61.10); since all states of $A$ are admissible (67.26), it is consistent with (67.23) to denote this set by $\Omega$. {In (61.14) it was denoted $\Sigma$.} As shown in (61.15), $\Omega$ is a nonempty, weak$^*$ compact, convex subset of the dual space $A'$ of $A$. By the Krein-Mil'man theorem (36.9), $\Omega$ is the weak$^*$ closure of conv $\Omega_{\text{ep}}$, where $\Omega_{\text{ep}}$ is the set of all extremal points of $\Omega$.

Let $c = a - b$. Since $c \neq 0$, there exists $f \in \Omega_{\text{ep}}$ with $f(c^*c) > 0$. {Proof: If, on the contrary, the weak$^*$ continuous linear mapping $g \mapsto g(c^*c)$ ($g \in A'$) vanishes on $\Omega_{\text{ep}}$, then it also vanishes on conv $\Omega_{\text{ep}}$ and hence on its weak$^*$ closure $\Omega$; this means that $g(c^*c) = 0$ for every $g \in \Om
