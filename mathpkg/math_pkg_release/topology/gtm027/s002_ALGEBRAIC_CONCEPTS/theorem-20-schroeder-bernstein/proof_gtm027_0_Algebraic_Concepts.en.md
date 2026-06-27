---
role: proof
locale: en
of_concept: theorem-20-schroeder-bernstein
source_book: gtm027
source_chapter: "0"
source_section: "Algebraic Concepts"
---

# Proof of Theorem 20: Schroeder-Bernstein Theorem

**Theorem 20.** If there is a one-to-one function on a set $A$ to a subset of a set $B$ and there is also a one-to-one function on $B$ to a subset of $A$, then $A$ and $B$ are equipollent.

*Proof.* Suppose that $f$ is a one-to-one map of $A$ into $B$ and $g$ is one-to-one on $B$ to $A$. It may be supposed that $A$ and $B$ are disjoint. The proof of the theorem is accomplished by decomposing $A$ and $B$ into classes which are most easily described in terms of parthenogenesis. A point $x$ (of either $A$ or $B$) is an ancestor of a point $y$ iff $y$ can be obtained from $x$ by successive application of $f$ and $g$ (or $f^{-1}$ and $g^{-1}$). Decompose $A$ into three sets: let $A_E$ consist of all points of $A$ which have an even number of ancestors, let $A_O$ consist of points of $A$ which have an odd number of ancestors, and let $A_I$ consist of points with infinitely many ancestors. Decompose $B$ similarly and observe: $f$ maps $A_E$ onto $B_O$ and $A_I$ onto $B_I$, and $g^{-1}$ maps $A_O$ onto $B_E$. Hence the function which agrees with $f$ on $A_E \cup A_I$ and agrees with $g^{-1}$ on $A_O$ is a one-to-one map of $A$ onto $B$.

**Note.** The foregoing proof does not use the axiom of choice. Explicitly, if $E_0 = A \setminus g[B]$, $E_{n+1} = g \circ f[E_n]$ for each $n \in \omega$, and $E = \bigcup \{E_n : n \in \omega\}$, then the function $h$ which is equal to $f$ on $E$ and equal to $g^{-1}$ on $A \setminus E$ is a one-to-one map of $A$ onto $B$. That is, $h = (f \mid E) \cup (g^{-1} \mid A \setminus E)$. The importance of this result lies in the fact that, if $f$ and $g$ have certain pleasant properties (such as being Borel functions), then $h$ retains these properties. The intuitively elegant form of this proof is due to G. Birkhoff and S. MacLane.
