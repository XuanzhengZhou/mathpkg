---
role: proof
locale: en
of_concept: theorem-7-41-1
source_book: gtm008
source_chapter: "2"
source_section: "2 There is a class"
---
1. If $a \subseteq L$ then $a \subseteq L_a$ since $L \subseteq L_a$. Therefore $a \in L_a$. Since $L[a]$ is the least standard transitive model of $ZF$ that contains $a$ and all the ordinals as elements we have $L[a] \subseteq L_a$.

But, since $a \in L[a]$.

$$(\forall x \in L[a]) [x \cap a \in L[a]].$$

Therefore $L_a \subseteq L[a]$.

2. The proof is left to the reader.

Exercises. 1. If $M$ is a standard transitive model of $ZF$, $On \subseteq M$, and $a \subseteq M$ then $M[a]$ is the smallest standard transitive model $N$ of $ZF$ in the language $\mathcal{L}_0(\{M(), C_a\})$ such that (i) $M \subseteq N$ and (ii) $a \in N$.

2. If $M$ is a standard transitive model of $ZF$, $On \subseteq M$, $K \subseteq M$ and $\mathcal{L} = \mathcal{L}_0(\{M(), K(\cdot)\})$ we define $C = \langle C_\alpha, \bar{M}_\alpha, \bar{K}_\alpha \rangle$ and $M_K$ by recursion:

i) $C_0 = 0$.
ii) $\bar{M}_\alpha = M \cap R(\alpha), \bar{K}_\alpha = C_\alpha \cap K$.
iii) $C_{\alpha+1} = Df(C_\alpha) \cup \bar{M}_{\alpha+1} \cup \bar{K}_\alpha$.
iv) $C_\alpha = \bigcup_{\beta < \alpha} C_\beta, \alpha \in K_{\Pi}$.
v) $M_K = \bigcup

8. Relative Constructibility and Ramified Languages

Using a ramified language we shall give another definition of $L[K; F]$ a definition that has many applications since it only uses the concepts of ordinal number and transfinite induction. On the other hand, to carry out the actual induction steps may become rather complicated in particular cases where definitions by simultaneous recursion are involved.

The symbols of the ramified language $R(K, F)$ are the following.

Variables: $x_0, x_1, \ldots, x_n, \ldots$ $n \in \omega$ (unranked).
$x_0^\alpha, x_1^\alpha, \ldots, x_n^\alpha, \ldots$ $n \in \omega, \alpha \in On$ (ranked).

Predicate constants: $\in, K(), F()$.

Individual constants: $k$ for each $k \in K$, where $K$ is a given class.

Logical symbols: $\neg, \land, \forall$.

Abstraction operator: $\hat{x}_n^\alpha$.

Parentheses: $(,)$.
