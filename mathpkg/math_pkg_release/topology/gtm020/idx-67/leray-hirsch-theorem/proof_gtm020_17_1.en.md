---
role: proof
locale: en
of_concept: leray-hirsch-theorem
source_book: gtm020
source_chapter: "17"
source_section: "1"
---

**Proof.** For an open subset $U$ of $B$, let $E_{U}$ denote $p^{-1}(U)$, let $j_{U}: E_{U} \to E$ be the natural inclusion, and let $p_{U}: E_{U} \to U$ be the restriction of $p$.

Define two functors $K^{n}(U)$ and $L^{n}(U)$ on the open subsets $U$ of $B$. Let $n(i)$ denote the degree of $a_{i}$, and let $x_{i}$ denote an indeterminate of degree $n(i)$. Set
$$
K^{n}(U) = \bigoplus_{1 \leq i \leq r} H^{n - n(i)}(U) \, x_{i},
$$
and let $L^{n}(U)$ denote $H^{n}(E_{U}, E_{U} \cap E_{0})$. Define the morphism $\theta_{U}: K^{n}(U) \to L^{n}(U)$ by
$$
\theta_{U}\!\left( \sum_{i} c_{i} x_{i} \right) = \sum_{i} p^{*}(c_{i}) \smile a_{i},
$$
where $c_{i} \in H^{n - n(i)}(U)$. Observe that the theorem is true over $U$ if and only if $\theta_{U}$ is an isomorphism.

The proof proceeds by verifying the theorem for sufficiently small open sets and then using Mayer-Vietoris pasting. For an open set $U$ over which the bundle is trivial, the result follows directly from the K\"{u}nneth formula. Consequently, the theorem holds over such open sets $U$.

Finally, it suffices to prove that if the theorem is true over open sets $U$, $V$, and $U \cap V$, then it is true over $U \cup V$. Since $L^{n}(U)$ is constructed from a functor for which the Mayer-Vietoris sequence exists and is exact, and since $K^{n}(U)$ is a direct sum of functors for which the Mayer-Vietoris sequence exists and is exact, we obtain the following commutative diagram with exact rows:

\[
\begin{array}{ccccccc}
\cdots \to & K^{n}(U \cap V) & \to & K^{n}(U) \oplus K^{n}(V) & \to & K^{n}(U \cup V) & \to \\
& \downarrow \theta_{1} & & \downarrow \theta_{2} = \theta \oplus \theta & & \downarrow \theta_{3} & \\
\cdots \to & L^{n}(U \cap V) & \to & L^{n}(U) \oplus L^{n}(V) & \to & L^{n}(U \cup V) & \to
\end{array}
\]

\[
\begin{array}{ccc}
\to & K^{n+1}(U \cap V) & \to \cdots \\
& \downarrow \theta_{4} & \\
\to & L^{n+1}(U \cap V) & \to \cdots
\end{array}
\]

By hypothesis, $\theta_{1}$, $\theta_{2}$, and $\theta_{4}$ are isomorphisms. Applying the Five Lemma to this commutative diagram yields that $\theta_{3}$ is also an isomorphism. Thus the theorem holds over $U \cup V$ whenever it holds over $U$, $V$, and $U \cap V$. By induction over a finite trivializing cover (the bundle is of finite type), the result extends to all of $B$.
