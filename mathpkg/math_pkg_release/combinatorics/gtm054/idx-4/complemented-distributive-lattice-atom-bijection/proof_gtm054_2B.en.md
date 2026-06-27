---
role: proof
locale: en
of_concept: complemented-distributive-lattice-atom-bijection
source_book: gtm054
source_chapter: "II"
source_section: "B"
---

Since the meet of any two atoms is $0$, $f$ is a well-defined function. To prove that $f$ is surjective, we first prove that $1$ is the join of all the atoms in $U$. For suppose that $\bigoplus_{a \in A} a = x$ for some $x < 1$. Then $a \leq x$ for all $a \in A$. Since $(U, \leq)$ is complemented, $x'$ exists, and $x' > 0$. Hence the set $\{z \in U: z \leq x'\}$ contains at least one atom $a$. Thus $a \leq x'$, and since $a \leq x$, we have $a \leq x \wedge x' = 0$, which is absurd. Hence $\bigoplus_{a \in A} a = 1$.

Now let $x \in U$ and consider the set $W = \{z \in U: z \leq x\}$. By Exercise B37, $(W, \leq)$ is a complemented distributive sublattice of $(U, \leq)$. Moreover, the atoms of $W$ are precisely the atoms of $U$ that are $\leq x$. Applying the above argument to $W$, we obtain that $x$ is the join of all atoms $a \leq x$. Hence $f(\{a \in A : a \leq x\}) = x$, proving surjectivity.

To prove injectivity, suppose $f(B_1) = f(B_2)$. Let $a \in B_1$. Then $a \leq f(B_1) = f(B_2) = \bigoplus_{b \in B_2} b$. Since $a$ is an atom and the join is of pairwise-disjoint elements, $a$ must equal one of the $b \in B_2$. Hence $B_1 \subseteq B_2$. By symmetry, $B_2 \subseteq B_1$.
