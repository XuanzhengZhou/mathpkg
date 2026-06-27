---
role: proof
locale: en
of_concept: characterization-of-completely-distributive-boolean-algebras
source_book: gtm008
source_chapter: "4"
source_section: "Distributive Laws"
---

For each $b \in |B|$ define
$$a_{b0} = -b, \quad a_{b1} = b$$
and set
$$A = \left\{ \prod_{b \in |B|} a_{b,f(b)} \;\middle|\; f \in 2^{|B|} \land \prod_{b \in |B|} a_{b,f(b)} \neq 0 \right\}.$$

For any $f \in 2^{|B|}$ and any $c \in |B|$:
- If $f(c) = 0$ then $a_{c,f(c)} = -c$, so $\prod_{b \in |B|} a_{b,f(b)} \leq -c$, hence $c \prod_{b \in |B|} a_{b,f(b)} = 0$.
- If $f(c) = 1$ then $a_{c,f(c)} = c$, so $\prod_{b \in |B|} a_{b,f(b)} \leq c$, hence $c \prod_{b \in |B|} a_{b,f(b)} = \prod_{b \in |B|} a_{b,f(b)}$.

Thus, if $S = \{\prod_{b \in |B|} a_{b,f(b)} \in A \mid f(c) = 1\}$ then
$$c = \sum_{b \in S} b.$$

Define $F$ on $\mathcal{P}(A)$ by
$$F(S) = \sum_{b \in S} b, \quad S \subseteq A.$$
Then $F$ maps $\mathcal{P}(A)$ onto $|B|$.

**Injectivity:** If $b_1, b_2 \in A$ and $b_1 \neq b_2$, then there exist $f_1, f_2 \in 2^{|B|}$ such that
$$b_1 = \prod_{b \in |B|} a_{b,f_1(b)} \neq \prod_{b \in |B|} a_{b,f_2(b)} = b_2.$$
Hence there exists $b \in |B|$ with $f_1(b) \neq f_2(b)$, so $a_{b,f_1(b)} a_{b,f_2(b)} = 0$ and consequently $b_1 b_2 = 0$. Thus distinct elements of $A$ are disjoint.

If $b \in A$, $S \subseteq A$, and $b \leq F(S)$, then $b F(S) = \sum_{c \in S} bc \neq 0$, so there exists $c \in S$ with $bc \neq 0$. By disjointness, $b = c$, hence $b \in S$. This shows $F$ is one-to-one.

**Preservation of join:** For $S, S' \subseteq A$,
$$F(S \cup S') \leq F(S) + F(S').$$
If $(\forall b \in S \cup S')[b \leq c]$, then $F(S) \leq c$ and $F(S') \leq c$, hence $F(S) + F(S') \leq c$. Therefore
$$F(S \cup S') = F(S) + F(S').$$

**Preservation of complement:** For any $c \in A$,
$$c \leq F(A - S) \iff c \in A - S \iff c \notin S \iff c \not\leq F(S) \iff c \leq -F(S).$$
Therefore $F(A - S) = -F(S)$.

Thus $F$ is an isomorphism of $\mathcal{P}(A)$ onto $|B|$.
