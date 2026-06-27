---
role: proof
locale: en
of_concept: theorem-4-4
source_book: gtm008
source_chapter: "4"
source_section: "4 Distributive Laws

In this section we wish to discuss severa"
---
If $\forall b \in |B|$

$$a_{b0} = -b$$

$$a_{b1} = b$$

and

$$A = \left\{ \prod_{b \in |B|} a_{b,f(b)} \mid f \in 2^{|B|} \land \prod_{b \in |B|

But $\forall f \in 2^{|B|}$ if $f(c) = 0$ then $a_{c,f(c)} = -c$ and
$$\prod_{b \in |B|} a_{b,f(b)} \leq -c$$
i.e.,
$$c \prod_{b \in |B|} a_{b,f(b)} = 0.$$
If $f(c) = 1$ then $a_{c,f(c)} = c$ and
$$\prod_{b \in |B|} a_{b,f(b)} \leq c$$
i.e.,
$$c \prod_{b \in |B|} a_{b,f(b)} = \prod_{b \in |B|} a_{b,f(b)}.$$
Thus, if $S = \{\prod_{b \in |B|} a_{b,f(b)} \in A \mid f(c) = 1\}$ then $c = \sum_{b \in S} b$. Therefore, if we define $F$ on $\mathcal{P}(A)$ by
$$F(S) = \sum_{b \in S} b, S \subseteq A$$
then $F$ maps $\mathcal{P}(A)$ onto $|B|$.
To prove that $F$ is one-to-one we note that if $b_1, b_2 \in A \land b_1 \neq b_2$ then $\exists f_1, f_2 \in 2^{|B|}$
$$b_1 = \prod_{b \in |B|} a_{b,f_1(b)} \neq \prod_{b \in |B|} a_{b,f_2(b)} = b_2.$$
Therefore $\exists b \in |B|, f_1(b) \neq f_2(b)$ and hence
$$a_{b,f_1(b)} a_{b,f_2(b)} = 0.$$
Consequently $b_1 b_2 = 0$.
If $b \in A \land S \subseteq A \land b \leq F(S)$ then
$$bF(S) = \sum_{c \in S} bc \neq 0.$$
Hence $\exists c \in S, bc \neq

Therefore

$$F(S \cup S') \leq F(S) + F(S').$$

If $(\forall b \in S \cup S') [b \leq c]$ then

$$F(S) \leq c \land F(S') \leq c$$

hence

$$F(S) + F(S') \leq c$$

i.e.,

$$F(S \cup S') = F(S) + F(S').$$

Finally $\forall c \in A$

$$c \leq F(A - S) \iff c \in A - S$$

$$\iff c \notin S$$

$$\iff c \not\leq F(S)$$

$$\iff c \leq -F(S).$$

Therefore

$$F(A - S) = -F(S).$$

Thus $F$ is an isomorphism of $\mathcal{P}(A)$ onto $|B|$.
