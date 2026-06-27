---
role: proof
locale: en
of_concept: corollary-22-31-1-satisfies-the-chain-condition-and
source_book: gtm008
source_chapter: "22"
source_section: "22 The Completion of a Boolean Algebra

For the following let"
---
Define $C_\alpha (\alpha \leq \kappa)$ and $C$ as follows.

i) $C_0 = \{b \in B_0 \mid b > 0\}$.
ii) $C_{\alpha+1} = \{b \in B_{\alpha+1} \mid \#_\alpha(b) \in C_\alpha\}$.
iii) $C_\alpha = \bigcup_{\beta < \alpha} C_\beta$ for every limit ordinal $\alpha$.
iv) $C = C_\kappa$.

Define $P_\alpha = \langle C_\alpha, \leq \rangle$ and apply the theorem.

23. Boolean Algebras That Are Not Sets

When for a given axiom $(\forall \alpha)A(\alpha)$, one wishes to build a model of $ZF + (\forall \alpha)A(\alpha)$, he is often lead to the existence of complete Boolean algebras $B_\beta$, for which

1. $V^{B_\beta}$ satisfies $ZF + (\forall \alpha < \beta)A(\alpha)$, and
2. The cardinality of $|B_\beta|$ increases as $\beta$ increases.

In this situation, the natural idea is to find a certain limit $B$ of $B_\beta$ and to prove that $V^{B}$ is a model of $ZF + (\forall \alpha)A(\alpha)$.

In almost all cases, however, the limit algebra $B$ is not a set, it is a proper class. In general if a complete Boolean algebra is not a set, then $V^{B}$ may not satisfy the Axiom Schema of Replacement or the Axiom of Powers. Therefore we need a general theory about conditions we should impose upon $B$ in order that $V^{B}$ satisfy the Axiom Schema of Replacement and the Axiom of Powers.

Another interesting problem is this: We do not have many useful ways to define limits of Boolean algebras. Therefore we tend to think in terms of limits of topological spaces or limits of partial order structures. At least one can make a partial order structure $P_\beta$ which is dual to $B_\beta$. Then we can take $P$, a limit of $P_\beta$, and define a limit of $B_\beta$ as the dual Boolean algebra of $P$. In our opinion, one of the most interesting problems in set theory is to investigate what effects the special kinds of limits of partial order structures or topological spaces have on the limit Boolean algebra $B$ and the Boolean valued universe $V^{B}$. In this section we will see that a limit topological space which is simultaneously a direct limit and an inverse limit of a certain sequence of topological spaces plays an important role. We believe strongly in the importance of the investigation of many other kinds of limits of Boolean algebras.

Until now we have considered only Boolean algebras which are sets. This requirement enabled us to prove the A

which is stronger than $ZF$. Note also that for $B$ as above the completion of $B$ is of type $\tilde{B}$.

If we consider $B$ as above we do not require that $B$ be complete but satisfy the following weaker condition:

$$(\forall A \subseteq B)[\mathcal{M}(A) \rightarrow (\exists x \in B)[x = \sup A]].$$

On the other hand we always require that a Boolean algebra of type $\tilde{B}$ be complete, i.e., sup $A$ exists in $\tilde{B}$ for every class $A \subseteq \tilde{B}$. Under these assumptions we define $V^{(B)}$ and $V^{(\tilde{B})}$ in two different ways. $V^{(B)}$ is defined as follows:

**Definition 23.1.** Let $C_{\alpha} = B \cap R(\alpha)$ for $\alpha \in On$. Then

1. $V_{0}^{(\tilde{B})} \triangleq 0$.
2. $V_{\alpha}^{(\tilde{B})} \triangleq \{u \in C_{\alpha} \mathcal{D}(u) \mid (\exists \xi < \alpha)[\mathcal{D}(u) \subseteq V_{\xi}^{(\tilde{B})}]\}$.
3. $V^{(\tilde{B})} \triangleq \bigcup_{\alpha \in On} V_{\alpha}^{(\tilde{B})}$.

**Remark.** This is a definition in the framework of $ZF$. Moreover,

$$V^{(\tilde{B})} = \{u \mid \mathcal{D}(u) \subseteq V^{(\tilde{B})} \wedge u: \mathcal{D}(u) \rightarrow B\}$$

as in the case of a set $B$. Note that $V_{\alpha}^{(\tilde{B})}$ is a set for each $\alpha$ and $V^{(\tilde{B})}$ is a class of sets.

$V^{(\tilde{B})}$ is defined as follows:

**Definition 23.2.**

1. $V_{0}^{(\tilde{B})} \triangleq 0$.
2. $V_{\alpha}^{(\tilde{B})

We can define

1. $$[M(u)] \triangleq \sum_{k \in V} [u = \check{k}]$$

in $V^{(B)}$ and $V^{(\tilde{B})}$ as before. In the case of $V^{(\tilde{B})}$ the existence of the supremum is assured by our assumption that $\tilde{B}$ is complete. On the other hand, in the case of $V^{(B)}$ we have from Theorem 23.3 that for $u \in V^{(B)}$

$$(\exists \alpha) \left[ \sum_{k \in V} [u = \check{k}] = \sum_{k \in R(\alpha)} [u = \check{k}] \right]$$

and therefore the sum in 1 is actually only a sum over the index set $R(\alpha)$. Similar remarks apply to the definitions of $\check{B}$, $\check{+}$, $\check{*}$, $F$ below in the case of $V^{(B)}$:

2. $$[u \in \check{B}] \triangleq \sum_{b \in B} [u = \check{b}]$$.

3. $$[+\check{(u, v, w)}] \triangleq \sum_{b_1, b_2 \in B} [u = \check{b}_1] \cdot [v = \check{b}_2] \cdot [w = (b_1 + b_2)^{-1}]$$.

4. $$[\cdot(u, v, w)] \triangleq \sum_{b_1, b_2 \in B} [u = \check{b}_1] \cdot [v = \check{b}_2] \cdot [w = (b \cdot b_2)^{-1}]$$.

5. $$[u \in F] \triangleq \sum_{b \in B} [u = \check{b}] \cdot b$$.

Finally, we let

$$V^{(B)} \triangleq \langle V^{(B)}, \overline{=}, \overline{\in}, M, \check{B}, \check{+}, \check{*}, F \rangle,$$

$$V^{(\tilde{B})} \triangle
