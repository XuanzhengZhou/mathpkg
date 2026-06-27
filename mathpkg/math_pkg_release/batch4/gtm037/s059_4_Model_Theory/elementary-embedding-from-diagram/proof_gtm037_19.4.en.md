---
role: proof
locale: en
of_concept: elementary-embedding-from-diagram
source_book: gtm037
source_chapter: "19"
source_section: "4. Model Theory"
---

**Proof.** Again, let the new constants of $L'$ be $c_a$ for $a \in A$. By Proposition 19.10, $l$ is an embedding of $A$ into $B$. Now for any $L$-formula $\varphi$, say with $\operatorname{Fv} \varphi \subseteq \{v_0, \ldots, v_{m-1}\}$, we have for any $a_0, \ldots, a_{m-1} \in A$:

$$
A \models \varphi[a_0, \ldots, a_{m-1}] \iff (A, a)_{a \in A} \models \varphi(c_{a_0}, \ldots, c_{a_{m-1}})
$$

by condition (1) from the definition of satisfaction. Since $(B, l_a)_{a \in A}$ is a model of the elementary $L'$-diagram $\Gamma$ of $A$, the sentence $\varphi(c_{a_0}, \ldots, c_{a_{m-1}})$ belongs to $\Gamma$ if and only if $A \models \varphi[a_0, \ldots, a_{m-1}]$. Hence

$$
A \models \varphi[a_0, \ldots, a_{m-1}] \implies B \models \varphi[l_{a_0}, \ldots, l_{a_{m-1}}].
$$

The converse direction follows similarly by considering $\neg\varphi$. Thus $l$ is an elementary embedding of $A$ into $B$. $\square$
