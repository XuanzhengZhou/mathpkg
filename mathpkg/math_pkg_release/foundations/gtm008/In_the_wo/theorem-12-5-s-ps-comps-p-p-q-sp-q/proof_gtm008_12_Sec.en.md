---
role: proof
locale: en
of_concept: theorem-12-5-s-ps-comps-p-p-q-sp-q
source_book: gtm008
source_chapter: "12"
source_section: "12 The Independence of the AC

In order to prove the independen"
---
Let $D_{M[G]}(t)$ be an $\omega$-sequence of ordinals in $M[G]$. By Theorem 10.9, it suffices to show that $\{p \in P \mid p \models V(t)\}$ is dense, i.e.,

$$(\forall p \in P)(\exists q \leq p)[q \models V(t)]$$

or by Theorem 10.

Claim: $S_2$ is dense in $P_2$.

Let $q_2$ be any element of $P_2$ and define

$$S_1 \triangleq \{p_1 \in P_1 \mid (\{p_1\} \times [q_2]) \cap S \neq 0\}.$$

Then since $S$ is dense in $P$

$(\forall q_1 \in P_1)(\exists p_1, p_2)[\langle p_1, p_2 \rangle \in S \land p_1 \leq q_1 \land p_2 \leq q_2].$$

Therefore $S_1$ is dense in $P_1$ and hence $G_1 \cap S_1 \neq 0$. This implies, by definition of $S_1$, that

$(G_1 \times [q_2]) \cap S \neq 0.$

Thus $S_2$ is dense in $P_2$. Since $S_2 \in M[G_1]$ and $G_2$ is $P_2$-generic over $M[G_1]$, $G_2 \cap S_2 \neq 0$ which means, by definition of $S_2$, that

$(G_1 \times G_2) \cap S \neq 0.$

Therefore $G_1 \times G_2$ is $P$-generic over $M$.

**Theorem 12.7.** If $G$ is $P$-generic over $M$, then there exists a $G_1$ which is $P_1$-generic over $M$ and a $G_2$ which is $P_2$-generic over $M[G_1]$ such that $G = G_1 \times G_2$.

**Proof.** Let $G$ be $P$-generic over $M$ and define

$$G_1 \triangleq \{p_1 \in P_1 \mid \langle p_1, 1 \rangle \in G\},$$

$$G_2 \triangleq \{p_2 \in P_2 \mid \langle

$M[H_1]$. There exists a $q_2 \leq r_2$ such that $q_2 \in D_{M[H_1]}(t)$ and hence there exists $q_1 \leq r_1$ such that $q_1 \not\models' q_2 \in t$. Then $q = \langle q_1, q_2 \rangle \leq r$ and $q \in E$.

Since $E \in M$ and $p \in G$, we have, by Theorem 10.11,

$$G \cap E \neq 0.$$

Let $q = \langle q_1, q_2 \rangle \in G \cap E$. Then

$$M[G_1] \models q_2 \in S.$$

Therefore $G_2 \cap S \neq 0$ and 2 is proved.

13. Boolean-Valued Set Theory

The use of ramified language in Cohen-type independence proofs often requires proofs by induction which may become rather cumbersome in special cases. A different though essentially equivalent approach which avoids ramified language is provided by the theory of Boolean-valued models as developed by Scott and Solovay.

The analogue of the recursive definition of $R(\alpha)$ we define in the following way:

**Definition** 13.1. Let $B = \langle B, +, \cdot, -, 0, 1 \rangle$ be a complete Boolean algebra. Then $V_{\alpha}^{(B)}$ is defined by recursion with respect to $\alpha$ as follows:

$$V_{0}^{(B)} \triangleq 0.$$
$$V_{\alpha}^{(B)} \triangleq \{u \mid [u: \mathcal{D}(u) \rightarrow B] \wedge (\exists \xi < \alpha)[\mathcal{D}(u) \subseteq V_{\xi}^{(B)}]\}, \quad \alpha > 0.$$
$$V^{(B)} \triangleq \bigcup_{\alpha \in O n} V_{\alpha}^{(B)}.$$

**Remark.** Elements of $V^{(B)}$ are called $B$-valued sets, these are functions $u$ from their domain, $\mathcal{D}(u)$, into $B$ where $\mathcal{D}(u)$ itself consists of $B$-valued sets.

**Theorem 13.2.** $\alpha \in K_{\Pi} \rightarrow V_{\alpha}^{(B)} = \bigcup_{\xi < \alpha} V_{\xi}^{(B)}$.

**Remark.** In order to obtain a $B$-valued structure $V^{(B)} = \langle V^{(B)}, \equiv, \bar{\epsilon} \rangle$, we define $\bar{\epsilon}$ and $\bar{\epsilon}$ in the following way.

**Definition** 13.3. For $u, v \in V^{(B)}$,

1. $$[u \bar{\epsilon} v] \triangleq \sum_{y \in \mathcal{D}(v)} (v(y) \cdot [u = y]).$$
2.

where $\alpha \# \beta$ is the natural sum of $\alpha$ and $\beta$. (For a definition and elementary properties of the natural sum of ordinals the reader may consult one of the following monographs: H. Bachmann: Transfinite Zahlers, Ergebnisse elev. Math. Vol. 1 (1955), pp. 102f, or A. A. Fraenkel: Abstract Set Theory (1953), p. 297.)

2. Alternatively, we would use Gödel’s pairing function $J_0$ which is a one-to-one correspondence between $On \times On$ and $On$ with the following property.

$$J_0(\alpha, \beta) < J_0(\alpha', \beta') \iff \max(\alpha, \beta) < \max(\alpha', \beta')$$
$$\vee [[\max(\alpha, \beta) = \max(\alpha', \beta')]] \wedge [\beta < \beta' \vee [\beta = \beta' \wedge \alpha < \alpha']]]]$$.

If we assign to $[u \in v]$ the ordinal $J_0(\text{rank}(v), \text{rank}(u))$ and to $[u = v]$ the ordinal max $(J_0(\text{rank}(u), \text{rank}(v)), J_0(\text{rank}(v), \text{rank}(u)))$, it is easy to see that $[u \in v]$ and $[u = v]$ in 1 and 2 respectively are reduced to $[u = v']$ and $[u' \in v']$ in such a way that the associated ordinals are reduced to lower ordinals.

3. We would also eliminate $\in$ in 2 by substituting the definition 1:

$$[u = v] = \prod_{x \in \mathcal{D}(u)} \left[ u(x) = \sum_{y \in \mathcal{D}(v)} [v(y) \cdot [x = y]] \right]$$
$$\cdot \prod_{y \in \mathcal{D}(v)} \left[ v(y) = \sum_{x \in \mathcal{D}(u)} [u(x
