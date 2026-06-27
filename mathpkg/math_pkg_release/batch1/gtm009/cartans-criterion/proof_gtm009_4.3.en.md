---
role: proof
locale: en
of_concept: cartans-criterion
source_book: gtm009
source_chapter: "4"
source_section: "4.3"
---

\textbf{Proof of Lemma.} Let $x = s + n$ be the Jordan decomposition of $x$. Fix a basis $v_1, \ldots, v_m$ of $V$ such that $s$ is diagonal: $s(v_i) = a_i v_i$. Let $\mathbb{Q}$ be the rational vector space spanned by the $a_i$. It suffices to show that all $a_i = 0$ (forcing $s = 0$ and $x = n$ nilpotent). Assume otherwise. Let $f: \mathbb{Q} \rightarrow \mathbb{Q}$ be a nonzero $\mathbb{Q}$-linear functional with $f(a_1, \ldots, a_m) \neq 0$. Define $y \in \text{End } V$ by $y(v_i) = f(a_i) v_i$. Then $[s, y] = 0$. One shows $y \in M$ and then $\text{Tr}(xy) = 0$, which forces $\sum f(a_i) a_i = 0$, a contradiction.

\textbf{Proof of Theorem.} It suffices to prove $[LL]$ is nilpotent, i.e., all $x \in [LL]$ are nilpotent endomorphisms. Apply the lemma to the situation: $V$ as given, $A = [LL]$, $B = L$, so $M = \{x \in \mathfrak{gl}(V) \mid [x, L] \subset [LL]\}$. Obviously $L \subset M$.

The hypothesis gives $\text{Tr}(xy) = 0$ for $x \in [LL]$, $y \in L$. To conclude from the lemma that each $x \in [LL]$ is nilpotent, we need $\text{Tr}(xy) = 0$ for $x \in [LL]$, $y \in M$.

For a typical generator $[x, y]$ of $[LL]$ and $z \in M$, the identity
$$\text{Tr}([x, y]z) = \text{Tr}(x[y, z]) = \text{Tr}([y, z]x)$$
holds. By definition of $M$, $[y, z] \in [LL]$, so the right side is 0 by hypothesis. Hence $\text{Tr}([x,y]z) = 0$ for all $z \in M$, and the lemma applies.
