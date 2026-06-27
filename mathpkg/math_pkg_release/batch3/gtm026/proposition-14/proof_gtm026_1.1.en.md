---
role: proof
locale: en
of_concept: proposition-14
source_book: gtm026
source_chapter: "1"
source_section: "1.57"
---

We prove (2) first. Let $g = p.i$ be a coequalizer-mono factorization, and then let $f.p = p'.i'$ be a coequalizer-mono factorization. As $p'(i'.i)$ is a coequalizer-mono factorization of $f.g$, $i'.i$ is an isomorphism by 1.49. Since $i$ is both split epi and mono, it follows from 1.50 that $i$ is an isomorphism.

To prove (1), let $f = \text{coeq}(a, b)$ and let $p.i$ be a coequalizer-mono factorization of $f.g$. Since $i$ is mono we have $a.p = b.p$ which induces unique $h$ with

with $f.h = p$. As $f$ is epi, $h.i = g$. By (2), $i$ is a coequalizer and hence, by 1.50, an isomorphism.

The following example shows that even a category with all small limits and colimits (and all factorizations as in 1.52 in particular) need not necessarily have coequalizer-mono factorizations.

(1.58) Let $\mathcal{K}$ be the category of abelian groups with no element of order 4 (that is $4x = 0$ implies $2x = 0$) and group homomorphisms. Products, equalizers, and coproducts (1.28) are formed just as they are in the category of all abelian groups. The proof that this category has coequalizers will be postponed until 3.7.13. Therefore, $\mathcal{K}$ has all small limits and colimits. Let $Z, Z_2,$ and $Z_4$ denote, respectively, the abelian groups of integers, integers modulo 2, and integers modulo 4. The homomorphism $2:Z \longrightarrow Z$ (sending $x$ to $2x$) is the equalizer of the morphisms $p, 0:Z \longrightarrow Z_2$ in $\mathcal{K}$ ($p$ is the canonical projection). Composing $2:Z \longrightarrow Z$ with itself gives the $\mathcal{K}$-morphism $4:Z \longrightarrow Z$. While $4:Z \longrightarrow Z$ is the equalizer of $p, 0:Z \longrightarrow Z_4$ in the category of all abelian groups, $Z_4$ is not in $\mathcal{K}$. Suppose that there exists $f, g:Z \longrightarrow A$ in $\mathcal{K}$ with $4 = \text{eq}(f, g)$. As $4f(1) = 4g(1)$ and $A$ is in $\mathcal{K}, 2(f(1) - g(1)) = 0$, that is, $2.f = 2.g$ and there exists a unique $h:Z \long

defined by the diagram:

This is an easy exercise; note that $\mathcal{K}$ must be locally small. $\square$

(1.61) The circle group $S$ (i.e., the complex numbers of modulus 1) is a cogenerator in the category of abelian groups. While this result is well known (the phrase is “there exist enough homomorphisms to the circle”), it is not particularly easy to prove. It follows from 1.60, that every abelian group is isomorphic to a subgroup of a product of circles.

(1.62) In Set, every set with at least two elements is a cogenerator.

(1.63) Let $\mathcal{K}$ be the category of complete semilattices and supremum-preserving functions (1.5.15). Let $C$ be the two-element lattice $\{0, 1\}$ with $0 \leqslant 1$. Then $C$ is a cogenerator. It suffices to show that whenever $a \neq b$ in the complete semilattice $X$ then there exists $h: X \longrightarrow C$ with $ah \neq bh$. If $a < b$, define $h$ by $xh = 0$ if $x \leqslant a$, and $xh = 1$ otherwise. If $a \not\leqslant b$, define $h$ by $xh = 0$ if $x \leqslant b$, and $xh = 1$ otherwise.

(1.64) The category of groups and homomorphisms does not have a cogenerator. Given any set $X$, consider those bijections from $X$ to itself which leave fixed all but finitely many elements; such bijections, which are essentially permutations of a finite set, have parity, that is, are either even or odd. It is well known that the group of all even permutations of the set $X$ forms a simple group if $X$ has any number of elements greater than 4. In particular, if $C$ is a would-be cogenerator there exists a simple group $S$ of cardinal larger than that of $C$. Since $id_S \neq 0$,

(as $j$ is mono) and $t$ is a monomorphism (as $i$ is mono) and we write: $i \leqslant j$. This defines a reflexive and transitive relation on the class of monomorphisms with codomain $X$. $i$ and $j$ are isomorphic if $i \leqslant j$ and $j \leqslant i$; note that $t$ as above is indeed an isomorphism and that “isomorphic” is an equivalence relation. An isomorphism class of $X$-valued monomorphisms is called a monosubobject of $X$. Writing $[i]$ for the isomorphism class of the mono $i: A \rightarrow X$, “$[i] \leqslant [j]$ if $i \leqslant j$” is well defined and defines a partial ordering (“inclusion”) on the class of monosubobjects of $X$.

(1.66) In Set, the passage from $[i]$ to the image of $i$ is well defined and establishes a bijection from the set of monosubobjects of $X$ to the set of subsets of $X$.

1.67 Direct Images. If $\mathcal{K}$ has coequalizer-mono factorizations, each morphism $f: A \rightarrow B$ induces the “direct image map” $[i]f = [j]$ where $(p, j)$ is any coequalizer-mono factorization of $i.f$. The diagram below shows that if $[i] = [i']$ and $(p', j')$ is a coequalizer-mono factorization of $i'.f$ then $[j] = [j']$ (i.e., as $u$ is an isomorphism, $(up, j)$ is another coequalizer-mono factorization of $i'.f$).

1.68 Inverse Images. If $\mathcal{K}$ has pullbacks, every morphism $f: X \rightarrow Y$ induces the “inverse image map” $[i]f^{-1} = [j]$ where $j$ is a pullback of $i$ along $f$. To see that $j$ is mono, if $tj = uj$ then $

induced by

The proof that $[j] = [j']$ if $[i] = [i']$ and that the whole construction is independent of the choice of pullback is an easy exercise.
