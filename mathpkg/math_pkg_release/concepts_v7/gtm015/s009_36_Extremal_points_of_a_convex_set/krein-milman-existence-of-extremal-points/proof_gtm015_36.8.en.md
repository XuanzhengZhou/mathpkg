---
role: proof
locale: en
of_concept: krein-milman-existence-of-extremal-points
source_book: gtm015
source_chapter: "36. Extremal points of a convex set; Krein-Mil'man theorem"
source_section: "36"
---

# Proof of Krein-Mil'man theorem: existence of extremal points

*Existence of such $H$.* Because $E$ is locally convex and separated, the Hahn-Banach separation theorem guarantees the existence of closed $\mathbb{R}$-hyperplanes tangent to any nonempty compact convex set $A$ (33.13), (30.11). The content of the theorem is that any such hyperplane necessarily contains an extremal point of $A$.

*Step 1: Zorn's lemma yields a minimal closed face.*

Let $\mathcal{F}$ be the family of all closed faces $F$ of $A$ such that $F \subset H$. This family is nonempty: by Proposition (36.6), $H \cap A$ is a face of $A$; moreover, $H$ is closed, so $H \cap A$ is a closed subset of the compact set $A$, hence compact; thus $H \cap A \in \mathcal{F}$.

To find a minimal element of $\mathcal{F}$ with respect to inclusion, we apply Zorn's lemma to the reversed order. Define a partial order $\leq$ on $\mathcal{F}$ by

$$F_1 \leq F_2 \iff F_1 \supset F_2.$$

Thus $\leq$-maximal elements correspond to inclusion-minimal elements.

Let $(F_\iota)_{\iota \in I}$ be a chain in $(\mathcal{F}, \leq)$ (equivalently, a family simply ordered by inclusion). Set $F = \bigcap_{\iota \in I} F_\iota$. We verify that $F \in \mathcal{F}$:

- $F$ is nonempty because $\{F_\iota\}$ is a family of closed subsets of the compact space $A$ with the finite intersection property (they are totally ordered by inclusion, so any finite subfamily has a minimum which is nonempty). By compactness, the total intersection is nonempty.
- $F$ is closed (intersection of closed sets).
- $F$ is a face of $A$ by property (2) of (36.5) (intersection of faces with nonempty intersection).
- $F \subset H$ because each $F_\iota \subset H$.

Moreover, $F \subset F_\iota$ for every $\iota$, so $F_\iota \leq F$ in the reversed order. Thus $F$ is an upper bound for the chain.

By Zorn's lemma, $\mathcal{F}$ possesses a $\leq$-maximal element, i.e., an inclusion-minimal element $F_0$. Thus $F_0$ is a minimal nonempty closed face of $A$ contained in $H$.

*Step 2: The minimal face is a singleton.*

We claim that $F_0$ consists of a single point. Suppose, to the contrary, that $F_0$ contains two distinct points $x \neq y$. Since $E$ is a locally convex separated TVS, its continuous dual separates points (Hahn-Banach theorem). Hence there exists a continuous $\mathbb{R}$-linear form $g$ on $E$ such that $g(x) \neq g(y)$. Set

$$\alpha = \sup\{\,g(z) : z \in F_0\,\}.$$

Because $F_0$ is compact, this supremum is attained; let $H' = \{z \in E : g(z) = \alpha\}$. Then $H'$ is a closed $\mathbb{R}$-hyperplane tangent to $F_0$ (30.10). Moreover, $H' \cap F_0$ is a proper subset of $F_0$: indeed, $g(x) \neq g(y)$ implies at least one of $x, y$ lies outside $H'$.

By Proposition (36.6) applied to the convex set $F_0$ and the tangent hyperplane $H'$, the intersection $H' \cap F_0$ is a face of $F_0$. Being the intersection of closed sets in a compact space, it is closed in $F_0$, hence compact and closed in $A$. By property (3) of (36.5), $H' \cap F_0$ is a face of $A$. Moreover, $H' \cap F_0 \subset F_0 \subset H$, so $H' \cap F_0 \in \mathcal{F}$.

But $H' \cap F_0 \subsetneq F_0$, which contradicts the inclusion-minimality of $F_0$ in $\mathcal{F}$. Therefore $F_0$ cannot contain two distinct points; it is a singleton $\{a\}$.

*Step 3: The point is extremal.*

A singleton $\{a\}$ is a face of $A$ if and only if $a$ is an extremal point of $A$ (this follows directly from the definitions: if $\langle u, v \rangle \subset A$ and $\langle u, v \rangle \cap \{a\} \neq \varnothing$, i.e., $a \in \langle u, v \rangle$, then $\langle u, v \rangle \subset \{a\}$ means $u = v = a$, which is precisely the definition of an extremal point).

Since $a \in F_0 \subset H$, we have exhibited an extremal point of $A$ lying in $H$. $\square$
