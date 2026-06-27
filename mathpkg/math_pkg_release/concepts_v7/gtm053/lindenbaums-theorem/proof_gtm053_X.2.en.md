---
role: proof
locale: en
of_concept: lindenbaums-theorem
source_book: gtm053
source_chapter: "X"
source_section: "2"
---

# Proof of Lindenbaum's Theorem

**Theorem 2.3 (Lindenbaum's Theorem).** Let $E$ be a finitely satisfiable set of $L$-sentences. Then $E$ can be completed; that is, there exists a complete finitely satisfiable set of $L$-sentences $E^\sharp$ such that $E \subseteq E^\sharp$.

*Proof.* The proof uses the Axiom of Choice (in the form of Zorn's Lemma). Consider the family

$$S = \{E' : E \subseteq E' \text{ is a finitely satisfiable set of } L\text{-sentences}\},$$

partially ordered by inclusion. We verify that $S$ satisfies the hypothesis of Zorn's Lemma. Let $\{E_\alpha\}_{\alpha \in I}$ be a chain in $S$. Set $E^* = \bigcup_{\alpha \in I} E_\alpha$. Then $E^*$ is finitely satisfiable: any finite subset of $E^*$ is contained in some $E_\alpha$ (since the chain is totally ordered), and $E_\alpha$ is finitely satisfiable by definition. Moreover, $E \subseteq E^*$. Hence $E^* \in S$ and $E^*$ is an upper bound for the chain.

By Zorn's Lemma, $S$ contains a maximal element, call it $E^\sharp$. We claim that $E^\sharp$ is complete. Suppose, for contradiction, that there exists an $L$-sentence $S$ such that $S \notin E^\sharp$ and $\neg S \notin E^\sharp$. By maximality of $E^\sharp$, neither $\{S\} \cup E^\sharp$ nor $\{\neg S\} \cup E^\sharp$ belongs to $S$, i.e., neither is finitely satisfiable.

This means there exist finite subsets $E_1, E_2 \subseteq E^\sharp$ such that $E_1 \cup \{S\}$ is not satisfiable and $E_2 \cup \{\neg S\}$ is not satisfiable. Then $E_1 \cup E_2$ is a finite subset of $E^\sharp$, hence satisfiable. But in any model of $E_1 \cup E_2$, either $S$ or $\neg S$ must hold, which contradicts that neither $E_1 \cup \{S\}$ nor $E_2 \cup \{\neg S\}$ is satisfiable.

Therefore, $E^\sharp$ is complete, finitely satisfiable, and $E \subseteq E^\sharp$. $\square$
