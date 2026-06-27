---
role: proof
locale: en
of_concept: theorem-6-9-i-ib-i-a-a-i
source_book: gtm008
source_chapter: "5"
source_section: "5 Partial Order Structures and Topological Spaces

In the work"
---
$b_i \leq [[a = a_i]][[a' = a_i]] \leq [[a = a']], i \in I$

$$1 = \sum_{i \in I} b_i \leq [[a = a']] \leq 1.$$

Hence $[[a = a']] = 1$.

Remark. This unique $a$ is sometimes denoted by $\sum_{i \in I} b_i a_i$. We next provide an example of a B-valued structure that is separated and complete.

Example. Define $A = \langle B, \equiv \rangle$ by

$$[[b_1 = b_2]] = b_1 b_2 + (-b_1)(-b_2)$$

i.e., $[[b_1 = b_2]]$ is the Boolean complement of the symmetric difference of $b_1$ and $b_2$.

It is easily proved that $A$ is a B-valued structure that satisfies 1-3 of Definition 6.5. Since

$$[[b_1 = b_2]] = 1 \rightarrow b_1 b_2 + (-b_1)(-b_2) = 1

But the $b_i$'s are pairwise disjoint. Then

$(-a_i)b_i \sum_{j \in I} a_j b_j = (-a_i)a_i b_i = 0$

$a_i b_i \left( -\sum_{j \in I} a_j b_j \right) = 0$.

Then

$b_i [[a = a_i]] = a_i b_i + (-a_i)b_i = b_i$.

Therefore $(\forall i \in I) [b_i \leq [[a = a_i]]]$ i.e., $A$ is complete.

7. Relative Constructibility

Godel’s constructibility was generalized, in a natural way, by Levy and Shoenfield to a relative constructibility which assures us of the existence of a standard transitive model $L[a]$ of $ZF$ for each set $a$. Levy-Shoenfield’s relative constructibility is rather narrow but quite easily generalized. In this section we will study a general theory of relative constructibility and deal with several basic relative constructibilities as special cases. Later we will extend our relative constructibility to Boolean valued relative constructibility from which we will in turn define forcing.

There is a modern tendency to avoid the rather cumbersome theory of relative constructibility. We believe this to be a mistake. Although we do not pursue the subject, it is clear that one can consider wider and wider types of relative constructibility. Accordingly, we have many types of Boolean valued relative constructibility. We feel that these sometimes wild Boolean valued relative constructibilities might be very important for future work. Indeed, it is not at all clear whether the structures they produce can be constructed by the usual method of Scott-Solovay’s Boolean valued models without using relative constructibility.

If $a$ and $b$ are sets there are two different definitions of the notion “$b$ is constructible from $a$” namely $b \in L_a$ or $b \in L[a]$ where

$L_a$ is the smallest class $M$ satisfying

1. $M$ is a standard transitive model of $ZF$.
2. $On \subseteq M$.
3. $(\forall x \in M)[x \cap a \in M]$.

$L[a]$ is the smallest class $M$ satisfying

1. $M$ is a standard transitive model of $ZF$.
2. $On \subseteq M$.
3. $a \in M$.

Obviously, $L_a \subseteq L[a]$.

In this section we will show, by a modification of Gödel’s methods used to define the class $L$ of constructible sets, that the classes $L_a$ and $L[a]$ exist. It should be noted that neither the characterization of $L_a$ nor of $L[a]$ can be formalized in $ZF$.

The main difference between $L_a$ and $L[a]$

independence of the AC from the axioms of ZF using results of this and later sections we must exercise care to avoid the use of the AC in proving the following results.

It is of interest to consider a slightly more general situation allowing $a$ to be a proper class $A$. $L_A$ can be characterized exactly as $L_a$ was. For $L[A]$ there is however a problem in that we cannot have $A \in M$. Instead we define:

$$L[A] = \bigcup_{\alpha \in 0_n} L[A \cap R'_\alpha].$$

We first develop a general theory that allows us to treat $L_A$ and $L[A]$ simultaneously. Let $\mathcal{L}$ be a language with predicate constants

$$R_0, \ldots, R_n$$

and individual constants

$$c_0, \ldots, c_m.$$

Some results of this section remain true if we allow $\mathcal{L}$ to have an arbitrary well-ordered set (possible even uncountably many) of constants.

**Definition 7.1.** If $\mathbf{A} = \langle A, R_0^{\mathbf{A}}, \ldots, R_n^{\mathbf{A}}, c_0^{\mathbf{A}}, \ldots, c_m^{\mathbf{A}} \rangle$ and

$$\mathbf{B} = \langle B, R_0^{\mathbf{B}}, \ldots, R_n^{\mathbf{B}}, c_0^{\mathbf{B}}, \ldots, c_m^{\mathbf{B}} \rangle$$

are two structures for the language $\mathcal{L}$, then $\mathbf{A}$ is a substructure of $\mathbf{B}$, $(\mathbf{A} \subseteq \mathbf{B})$ iff

1. $A \subseteq B$.
2. For each $R_i, i = 0, \ldots, n$ if $R_i$ is $p$-ary then $\forall a_1, \ldots, a_p \in A$

$$R_i^{\mathbf{A}}(a_1, \ldots, a_p) \leftrightarrow R_i^{\mathbf{B}}(a, \ldots, a_p).$$
3. $c_j^{\mathbf{

respect to transitive models of $ZF$. In particular there is a formula $F$ of $\mathcal{L}_0$ involving $A$ as a constant such that $F(x)$ formalizes the notion

“$x$ is the Gödel number of a formula of $\mathcal{L}(C(A))$”

and such that $F$ is absolute with respect to any transitive model $M$ of $ZF$ for which $A \in M$. We then define

$Fml(A) \triangleq \{x \mid F(x)\}$.

$C(x)$: “$x$ is the Gödel number of a closed wff of $\mathcal{L}(C(A))$.”

$\bar{F}(x)$: “$x$ is the Gödel number of a wff of $\mathcal{L}(C(A))$ having at most one free variable.”

$Fml^0(A) \triangleq \{x \mid C(x)\}$.

$Fml^1(A) \triangleq \{x \mid \bar{F}(x)\}$.
