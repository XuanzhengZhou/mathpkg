---
role: proof
locale: en
of_concept: unique-comparison-functor-lemma
source_book: gtm005
source_chapter: "VI"
source_section: "7"
---

Let $\langle F, G, \eta, \varepsilon \rangle: X \rightharpoonup A$ and $\langle F', G', \eta', \varepsilon' \rangle: X \rightharpoonup A'$ be two adjunctions defining the same monad $\langle T, \eta, \mu \rangle$ in $X$. Assume $G$ satisfies hypothesis (iii) of Beck's theorem.

For any object $a' \in A'$, consider its canonical presentation in $A'$:
$$F'G'F'G'a' \xrightarrow[\varepsilon'_{F'G'a'}]{F'G'\varepsilon'_{a'}} F'G'a' \xrightarrow{\varepsilon'_{a'}} a'.$$
Applying $G'$, we obtain a split fork in $X$ (the $T$-algebra structure split fork for $\langle G'a', G'\varepsilon'_{a'} \rangle$).

Since $F'G'a' = TG'a' = GFG'a'$ and $F'G'F'G'a' = T^2G'a' = GFGFG'a'$, and using that both adjunctions define the same monad, we can reinterpret this as a parallel pair in $A$:
$$FGFG'a' \xrightarrow[\varepsilon_{FG'a'}]{FG\varepsilon_a?} FG'a'$$
whose image under $G$ has a split coequalizer in $X$. By hypothesis (iii), $G$ creates a coequalizer for this pair, yielding a unique object $Ma' \in A$ and a unique map $Ma'$ making the appropriate diagram commute.

Specifically, we have the parallel pair in $A$:
$$FGFG'a' \rightrightarrows FG'a'$$
given by $\varepsilon_{FG'a'}$ and $F(G\varepsilon'_{a'} \circ \eta_{G'a'})$. Its image under $G$ is the standard split fork for the $T$-algebra $\langle G'a', G'\varepsilon'_{a'} \rangle$, which has a split coequalizer $\varepsilon'_{a'}: FG'a' \to a'$ in $X$. Since $G$ creates coequalizers for such pairs, there exists a unique $e: FG'a' \to Ma'$ in $A$ with $Ge = G'\varepsilon'_{a'}$ and such that $e$ is a coequalizer of the parallel pair.

This defines $M$ on objects. For a morphism $f: a' \to b'$ in $A'$, the naturality of the canonical presentation gives a commutative diagram whose $G$-image in $X$ factors uniquely through the coequalizers, defining $Mf: Ma' \to Mb'$. Functoriality follows from uniqueness.

The conditions $MF' = F$ and $GM = G'$ are verified by construction. Uniqueness of $M$ follows because any comparison must preserve the canonical presentations, and the coequalizer construction above is forced.
