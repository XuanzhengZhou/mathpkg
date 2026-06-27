---
role: proof
locale: en
of_concept: normal-subgroup-of-alternating-group-contains-three-cycle
source_book: gtm030
source_chapter: "V: Groups with Operators"
source_section: "5: Application — simplicity of the alternating group"
---

Let $\alpha$ be a permutation belonging to $\mathfrak{H}$ that is $\neq 1$ and that leaves fixed as many elements as any other permutation $\neq 1$ in $\mathfrak{H}$.

If $\alpha$ is not a three-cycle, either $\alpha$ contains a cycle of length $\geq 3$ and moves more than three elements, or $\alpha$ is a product of at least two disjoint transpositions. Accordingly we may assume that either

$$\alpha = (123\cdots)(\quad)\cdots$$

or

$$\alpha = (12)(34)\cdots.$$

In the first case $\alpha$ moves at least two other numbers, say $4, 5$, since $\alpha$ is not one of the odd permutations $(123k)$. Now let $\beta = (345)$ and form $\alpha_1 = \beta^{-1}\alpha\beta$. If $\alpha$ is as in the first case,

$$\alpha_1 = (124\cdots)(\quad)\cdots$$

and if $\alpha$ is as in the second case,

$$\alpha_1 = (12)(45)\cdots$$

Now it is clear that if a number $i > 5$ is left fixed by $\alpha$, then it is also left fixed by $\alpha_1$, and hence it is left fixed by $\alpha_1\alpha^{-1}$. Moreover, $1\alpha_1\alpha^{-1} = 1$ if $\alpha$ is of the first type, and $1\alpha_1\alpha^{-1} = 1$ and $2\alpha_1\alpha^{-1} = 2$ if $\alpha$ is of the second type.

Thus $\alpha_1\alpha^{-1}$ leaves invariant more elements than $\alpha$. Since $\alpha_1\alpha^{-1} \neq 1$ (because $\mathfrak{H}$ is invariant and $\alpha_1\alpha^{-1} \in \mathfrak{H}$), this contradicts our choice of $\alpha$. Hence $\alpha$ must be a three-cycle.
