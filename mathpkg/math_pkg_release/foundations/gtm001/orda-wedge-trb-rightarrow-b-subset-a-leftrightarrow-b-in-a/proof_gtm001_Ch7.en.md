---
role: proof
locale: en
of_concept: orda-wedge-trb-rightarrow-b-subset-a-leftrightarrow-b-in-a
source_book: gtm001
source_chapter: "7"
source_section: ""
---

Since $A$ is an ordinal, $A$ is transitive and so by Proposition 7.2

$$B \in A \rightarrow B \subset A.$$

Conversely if $B \subset A$, then $A - B \neq 0$. From Proposition 7.5, $A - B$ has an E-minimal element $b$, that is,

$$(b \in A - B) \wedge (A - B) \cap b = 0.$$

Clearly $b \in A$. To prove that $B \in A$ we will prove that $B = b$. Toward this end we note that since $b \in A$ and $A$ is transitive $b \subset A$. But $(A - B) \cap b = 0$, and so $b \subseteq B$.

To prove that $B \subseteq b$ we observe that if $c \in B$ then, since $B \subset A, c \in A$. But $A$ is an ordinal class and $b \in A$. Therefore

$$c \in b \vee c = b \vee b \in c.$$

From the transitivity of $B$ we see that $[b \in c \vee b =

We first note that $A \cap B \subseteq A$. Furthermore, since $A$ and $B$ are transitive

$$a \in A \cap B \rightarrow a \in A \land a \in B$$
$$\rightarrow a \subset A \land a \subset B$$
$$\rightarrow a \subset A \cap B.$$

Therefore $A \cap B$ is a transitive subclass of the ordinal $A$ and hence by Propositions 7.6 and 7.7, $A \cap B$ is an ordinal class. $\square$
