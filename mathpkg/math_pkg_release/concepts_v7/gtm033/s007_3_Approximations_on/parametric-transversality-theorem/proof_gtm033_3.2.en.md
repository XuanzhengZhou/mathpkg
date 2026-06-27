---
role: proof
locale: en
of_concept: parametric-transversality-theorem
source_book: gtm033
source_chapter: "3"
source_section: "2. Transversality"
---

# Proof of the Parametric Transversality Theorem

**Parametric Transversality Theorem.** Let $F: V \times M \to N$ be a $C^r$ map, $1 \leqslant r \leqslant \infty$, where $V, M, N$ are $C^r$ manifolds. Write $F_v(x) = F(v, x)$. Suppose that:

(a) $F$ is transverse to a $C^r$ submanifold $A \subset N$;

(b) $F$ is continuous for the strong topology on $C^r(M,N)$ (i.e., the map $v \mapsto F_v$ is continuous from $V$ to $C^r_S(M,N)$).

Then the set

$$\phi(F; A) = \{v \in V : F_v \pitchfork A\}$$

is residual and therefore dense. If $A$ is closed in $N$ and $F$ is continuous for the strong topology, then $\phi(F; A)$ is also open.

*Proof.* The last statement (openness) follows from openness of the transversality condition $\bigcap^{\,r}(M,N; A)$ when $A$ is closed, together with continuity of $v \mapsto F_v$ in the strong topology: the preimage of an open set under a continuous map is open.

For the residual property, let $W = (F^{\text{ev}})^{-1}(A) \subset V \times M$, where $F^{\text{ev}}: V \times M \to N$ is the evaluation map $F^{\text{ev}}(v, x) = F(v, x) = F_v(x)$. By hypothesis (a), $F^{\text{ev}}$ is transverse to $A$, so $W$ is a $C^r$ submanifold of $V \times M$ (by the preimage theorem for transverse maps).

Let $\pi: V \times M \to V$ be the projection onto the parameter space. Consider the restricted projection

$$\pi|_W: W \to V.$$

It is readily verified (from the definition of transversality) that $F_v \pitchfork A$ if and only if $v \in V$ is a regular value for the $C^r$ map $\pi|_W: W \to V$.

Indeed, $x \in M$ satisfies $F_v(x) \in A$ exactly when $(v, x) \in W$, and transversality of $F_v$ to $A$ at $x$ means that

$$D(F_v)_x(T_x M) + T_{F(v,x)}A = T_{F(v,x)}N.$$

This is equivalent to the condition that $v$ is a regular value of $\pi|_W$ at $(v, x)$ (the surjectivity of the derivative of $\pi|_W$ onto $T_v V$ is obstructed precisely by failure of transversality).

The dimension of $W$ is

$$\dim W = \dim(V \times M) - \dim N + \dim A = \dim V + \dim M - \dim N + \dim A.$$

By the Morse-Sard Theorem (Theorem 1.3), the set of critical values of $\pi|_W$ has measure zero in $V$. Therefore the set of regular values (which equals $\phi(F; A)$) has full measure and in particular is residual and dense in $V$.

QED
