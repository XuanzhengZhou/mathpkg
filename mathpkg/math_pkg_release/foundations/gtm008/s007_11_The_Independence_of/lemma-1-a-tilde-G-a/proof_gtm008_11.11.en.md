---
role: proof
locale: en
of_concept: lemma-1-a-tilde-G-a
source_book: gtm008
source_chapter: "11"
source_section: "11 The Independence of V = L and the CH"
---

**Proof of Lemma 1.** Let $a \subseteq \omega$. We show $\tilde{a}(\tilde{G}(a)) = a$.

First, if $n \in \tilde{a}(\tilde{G}(a))$, then by definition there exist $p_1, p_2$ such that $n \in p_1$ and $\langle p_1, p_2 \rangle \in \tilde{G}(a)$. By definition of $\tilde{G}(a)$, we have $p_1 \subseteq a$, so $n \in a$. Thus $\tilde{a}(\tilde{G}(a)) \subseteq a$.

Conversely, if $n \in a$, construct the condition $\langle \{n\}, \varnothing \rangle \in P$ (since $\{n\}$ is a finite subset of $a$ and $\varnothing$ is a finite subset of $\omega - a$, disjoint by construction). This condition belongs to $\tilde{G}(a)$ and has $n$ in its first coordinate, so $n \in \tilde{a}(\tilde{G}(a))$. Hence $a \subseteq \tilde{a}(\tilde{G}(a))$.

Therefore $\tilde{a}(\tilde{G}(a)) = a$. $\square$
