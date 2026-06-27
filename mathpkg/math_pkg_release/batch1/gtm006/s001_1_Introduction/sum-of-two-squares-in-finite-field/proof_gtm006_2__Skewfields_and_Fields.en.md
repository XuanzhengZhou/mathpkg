---
role: proof
locale: en
of_concept: sum-of-two-squares-in-finite-field
source_book: gtm006
source_chapter: "I. Review of Basic Algebra"
source_section: "2. Skewfields and Fields"
---
Let $K = GF(q)$. From (iii) there is nothing to prove if $p=2$, so suppose $p \neq 2$. Then the squares make up a set $S$ which includes half the non-zero elements plus zero. If there is some element which is not a sum of two squares, then it must be an element $z$ which is also not a square.

Now the non-zero squares $N$ are a subgroup of index two of the multiplicative group and hence, since $N$ has just two cosets in $K^*$, every non-square is equal to $z$ multiplied by a square. If one of these, $zx^2$ say, were a sum $a^2 + b^2$, then $z = (a/x)^2 + (b/x)^2$ would be a sum of two squares as well. So no non-square is a sum of two squares. Thus every sum of two squares is again a square, and the set $S$ is closed under addition, as well as multiplication.

It is now an easy exercise to show that this means that $S$ is a subfield. But $S$ must have $(q-1)/2 + 1 = (q+1)/2$ elements, and clearly has the same characteristic as $GF(q)$. Thus, by the earlier parts of the result, $S$ must also be isomorphic to $GF(p^m)$ for some $m$. But this is impossible since, if $q=p^n$, then $(p^n+1)/2$ is never a power of $p$.
