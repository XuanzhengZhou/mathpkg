---
role: proof
locale: en
of_concept: theorem-10-12-p-x-x-q-p-t-tq-g-q-t
source_book: gtm008
source_chapter: "5"
source_section: "5 For each formula"
---
$$p \models (\exists x) \varphi(x) \leftrightarrow p \in \sum_{t \in T} [\varphi(t)] = \left( \bigcup_{t \in T} [\varphi(t)] \right)^{-0}$$

$$\leftrightarrow [p] \subseteq \left( \bigcup_{t \in T} [\varphi(t)] \right)^{-1}.$$

So $p \models (\exists x) \varphi(x)$ implies that $\bigcup_{t \in T} [\varphi(t)]$ is dense beneath $p$, and the same holds for $S' = [p] \cap \bigcup_{t \in T} [\varphi(t)]$. Also $S' \in M$ since $B \in M$. Therefore by Theorem 10.11

$$p \models (\exists x) \varphi(x) \rightarrow (\exists q \in G) \left[ q \leq p \land q \in \bigcup_{t \in T} [\varphi(t)] \right]$$

$$
