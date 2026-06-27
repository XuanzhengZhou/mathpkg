---
role: proof
locale: en
of_concept: moritas-theorem
source_book: gtm013
source_chapter: "4"
source_section: "22"
---

**Necessity.** Suppose $F$ and $G$ are inverse equivalences. Set $P = F(R)$ with its natural bimodule structure ${}_S P_R$, where the right $R$-action is induced by the ring homomorphism $R \cong \operatorname{End}({}_R R) \to \operatorname{End}({}_S F(R))$. Then ${}_S P = F({}_R R)$ is a progenerator since ${}_R R$ is clearly a progenerator and $F$ is an equivalence (by (21.6) and (21.8)). In particular, since ${}_S P$ is a generator, it is balanced (17.8.1). But $R$, with its natural action on ${}_S P$, is isomorphic to $\operatorname{End}({}_S P)$. Thus ${}_S P_R$ is a faithfully balanced bimodule. Therefore, by (17.7), $P_R$ is also a progenerator.

Similarly, $Q = G(S)$ has, induced by $S_S$, a natural faithfully balanced bimodule structure ${}_R Q_S$ with ${}_R Q$ and $Q_S$ both progenerators. This establishes conditions (1) and (2).

Now let ${}_R M$ be a left $R$-module. Since the $\mathbb{Z}$-isomorphism $\phi$ of (21.1) is natural in the first variable,
$$\phi \colon \operatorname{Hom}_S(S, F(M)) \to \operatorname{Hom}_R(G(S), M) = \operatorname{Hom}_R(Q, M)$$
is a left $S$-isomorphism (20.4). Then the $S$-isomorphisms
$$F(M) \cong \operatorname{Hom}_S(S, F(M)) \cong \operatorname{Hom}_R(Q, M)$$
are natural in $M$, whence $F \cong \operatorname{Hom}_R(Q, -)$. Similarly, $G \cong \operatorname{Hom}_S(P, -)$.

Then at ${}_R R_R$ and at ${}_S S_S$ these natural isomorphisms are bimodule isomorphisms (see (20.4)):
$${}_S P_R = {}_S F(R)_R \cong \operatorname{Hom}_R(Q, R)$$
and
$$\operatorname{Hom}_S(P, -) \cong (Q \otimes_S -).$$

Thus condition (3) holds: $F \cong (P \otimes_R -)$ and $G \cong \operatorname{Hom}_S(P, -)$. The final assertion about $Q = \operatorname{Hom}_R(P, R)$ follows from the above bimodule isomorphisms.

**Sufficiency.** Conversely, suppose that ${}_S P_R$ is a bimodule satisfying (1) and (2). Then for each ${}_R M$ and each ${}_S N$ there are natural isomorphisms:

$$\begin{aligned}
\operatorname{Hom}_S(P, P \otimes_R M) &\cong \operatorname{Hom}_S(P, P) \otimes_R M \quad \text{(20.10)}\\
&\cong R \otimes_R M \quad \text{(by (2), balancedness)}\\
&\cong M \quad \text{(20.1)}
\end{aligned}$$

and

$$\begin{aligned}
P \otimes_R \operatorname{Hom}_S(P, N) &\cong \operatorname{Hom}_S(\operatorname{Hom}_R(P, P), N) \quad \text{(21.11)}\\
&\cong \operatorname{Hom}_S(S, N) \quad \text{(by (2), balancedness)}\\
&\cong N \quad \text{(21.1)}.
\end{aligned}$$

Thus $F = (P \otimes_R -)$ and $G = \operatorname{Hom}_S(P, -)$ are inverse equivalences.
