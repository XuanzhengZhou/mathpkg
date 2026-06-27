---
role: proof
locale: en
of_concept: f-mathcalf-n-omega-rightarrow-exists-nfn-1-notin-fn
source_book: gtm001
source_chapter: "7"
source_section: ""
---

From the Axiom of Infinity, $F$ is a function whose domain is a set. Therefore the range of $F$, $\mathcal{W}(F)$, is a set. Then from the Axiom of Regularity there exists a set $a$ in $\mathcal{W}(F)$ such that

$$\mathcal{W}(F) \cap a = 0.$$

But since $a \in \mathcal{W}(F)$ there exists an integer $n$, such that $a = F'n$. Since $\mathcal{W}(F) \cap a = 0$ and since $F'(n + 1) \in \mathcal{W}(F)$ we have $F'(n + 1) \notin F'n$. $\square$

Remark. Proposition 7.34 assures us that there are no infinite descending $\in$-chains. Given a nonempty set $a_0$, $\exists a_1 \in a_0$. If $a_1 \neq 0$, $\exists a_2 \in a_1$, etc. However, by Theorem 7.34, we see that after a finite number of steps we must arrive at a set $a_n \in a_{n-1}$ with $a_n = 0$.

While every descending $\in$-chain must be of finite length it does not follow that for a given set $a$ there is a bound on the length of the $\in$-chains descending from $a$. Consider, for example, $\omega$:

$$(\forall n)[0 \in 1 \in 2 \in \cdots \in n \in \omega].$$

Exercises

Prove the following.

(1) $\alpha \in K_{\mathrm{II}} \rightarrow \omega \leq \alpha.$

(2) $A \subseteq \omega \land A \neq 0 \rightarrow (\exists k \in A)(\forall i \in A)[k \leq i].$

(3) $F: \omega \rightarrow A \land R \mathrm{Fr
