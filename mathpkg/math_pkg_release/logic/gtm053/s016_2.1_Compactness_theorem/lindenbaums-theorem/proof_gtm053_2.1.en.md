---
role: proof
locale: en
of_concept: lindenbaums-theorem
source_book: gtm053
source_chapter: "2"
source_section: "2.1"
---

(Uses the axiom of choice.) Let

$$S = \{E' : E \subseteq E' \text{ is a finitely satisfiable set of } L\text{-sentences}\}.$$

Clearly $S$ satisfies the hypothesis of Zorn's lemma (the union of any chain of finitely satisfiable sets is finitely satisfiable), so $S$ contains a maximal element, say $E^\#$. We claim $E^\#$ is complete. Suppose otherwise: then there exists an $L$-sentence $S$ such that $S \notin E^\#$ and $\neg S \notin E^\#$. By maximality, neither $\{S\} \cup E^\#$ nor $\{\neg S\} \cup E^\#$ is finitely satisfiable. Hence there exist finite subsets $E_1 \subseteq E^\#$ and $E_2 \subseteq E^\#$ such that $E_1 \cup \{S\}$ is unsatisfiable and $E_2 \cup \{\neg S\}$ is unsatisfiable. Then $E_1 \cup E_2 \subseteq E^\#$ is a finite subset of $E^\#$, and every model of $E_1 \cup E_2$ must satisfy either $S$ or $\neg S$, leading to a contradiction. Therefore $E^\#$ is complete.
