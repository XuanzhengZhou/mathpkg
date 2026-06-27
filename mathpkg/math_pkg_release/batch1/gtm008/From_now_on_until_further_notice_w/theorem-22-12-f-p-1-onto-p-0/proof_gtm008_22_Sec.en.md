---
role: proof
locale: en
of_concept: theorem-22-12-f-p-1-onto-p-0
source_book: gtm008
source_chapter: "22"
source_section: "22 The Completion of a Boolean Algebra

For the following let"
---
There are two complete monomorphisms:

$$j: B_{P_0} \rightarrow

Therefore, for all $b_0 \in B_0$ and $b_1 \in B_1$,

$$\#(b_1) \leq b_0 \leftrightarrow b_1 \leq i(b_0)$$
$$\leftrightarrow f(b_1) \leq b_0$$

which gives $\#(b_1) = f(b_1)$.

**Theorem 22.13.** Let $B_0, B_1, B_2$ be complete Boolean algebras, let

$$i_1: B_0 \rightarrow B_1$$
$$i_2: B_1 \rightarrow B_2$$

be complete monomorphisms and let $\#j$ be the open continuous mapping associated with $i_j (j = 1, 2)$, i.e.,

$$B_0 \xrightarrow[i_1]{\leftarrow} B_1 \xrightarrow[i_2]{\leftarrow} B_2.$$

If $i = i_2 \circ i_1$ and $\# = \#_1 \circ \#_2$, then $\#$ induces $i$.

**Proof.** $\#: B_2 \rightarrow B_0$ is open, continuous and onto $B_0$.

$$\#^{-1} = (\#_1 \circ \#_2)^{-1} = \#_2^{-1} \circ \#_1^{-1},$$

hence

$$(\#^{-1})'b_0 = (i_2 \circ i_1)(b_0) = i(b_0).$$

**Remark.** We are mostly interested in the case where $B_0$ is a complete subalgebra of $B_1$ and $i$ is the identity on $B_0$. Suppose that there is a big complete Boolean algebra $B$ such that all the complete Boolean algebras under consideration are complete subalgebras of $B$. Thus, if $B_0, B_1$ are complete subalgebras of $B$ and $B_0 \subseteq B_1$, we denote the map $B_1 \rightarrow B_0$

The topology on $X$ is defined by the following open base.

$$T = \{ \tilde{G}_{\alpha} \mid \alpha < \kappa \land (G_{\alpha} \text{ is open in } X^{\alpha}) \}$$

where

$$\tilde{G}_{\alpha} = \{ f \in X \mid f(\alpha) \in G_{\alpha} \}.$$

We define $p_{\alpha} \colon X \to X^{\alpha}$ by $p_{\alpha}(f) = f(\alpha)$.

Remark. Then the following result is obvious.
