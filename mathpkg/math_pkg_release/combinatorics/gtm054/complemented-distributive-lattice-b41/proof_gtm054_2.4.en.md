---
role: proof
locale: en
of_concept: complemented-distributive-lattice-b41
source_book: gtm054
source_chapter: "2"
source_section: "IIC"
---

Since the meet of any two atoms is 0, $f$ is a well-defined function. To prove that $f$ is surjective, we first prove that 1 is the join of all the atoms in $U$. For suppose that $\bigoplus_{a \in A} a = x$ for some $x < 1$. Then $a \leq x$ for all $a \in A$. Since $(U, \leq)$ is complemented, $x'$ exists, and $x' > 0$. Hence the set $\{z \in U: z \leq x'\}$ contains at least one atom $a$. Thus $a \leq x'$, and since $a \leq x$, we have $a \leq x \wedge x' = 0$, which is absurd. Hence $\bigoplus_{a \in A} a = 1$.

Now let $x \in U$ and consider the set $W = \{z \in U: z \leq x\}$. By Exercise B37, $(W, \leq)$ is a complemented distributive sublattice of $(U, \leq)$. Moreover

IIC Connectedness and Components

In the previous section we considered minimal, nonzero elements of a lattice ("atoms"); in this section we begin by considering the collection $M(\mathcal{A})$ of minimal, nonempty subsets belonging to a collection $\mathcal{A}$ of sets. Like the set of atoms of a lattice, $M(\mathcal{A})$ is an incommensurable collection. These subsets are called the elementary sets in $\mathcal{A}$. For example, $M(\mathcal{P}(U)) = \mathcal{P}_1(U)$ and $M(\mathcal{E}(U)) = \mathcal{P}_2(U)$. It holds not only in these two examples, but in general, that if $\mathcal{A}$ is a subspace of $\mathcal{P}(U)$, then $M(\mathcal{A})$ spans $\mathcal{A}$. We shall look to $M(\mathcal{A})$ to yield further properties about $\mathcal{A}$. Throughout this section $\mathcal{A}$ will denote a subspace of $(\mathcal{P}(U), +)$.
