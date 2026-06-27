---
role: proof
locale: en
of_concept: basis-extension-theorem
source_book: gtm028
source_chapter: "II. Elements of Field Theory"
source_section: "§12. Transcendental Extensions"
---

We partially order, by set-theoretic inclusion, the set $M$ of all subsets $S_\alpha$ of $S$ such that $L \cap S_\alpha$ is empty and $L \cup S_\alpha$ is a free set. The set $M$ is non-empty since the empty set belongs to $M$. It is immediately seen that $M$ is inductive, for if $\{S_\alpha\}$ is a totally ordered family of sets in $M$, the union $\bigcup_\alpha S_\alpha$ also belongs to $M$ (since any finite subset of $L \cup (\bigcup_\alpha S_\alpha)$ is contained in $L \cup S_\alpha$ for some $\alpha$ and therefore is free). Hence, by Zorn's Lemma, there exists a maximal element $S'$ in $M$.

We assert that $L \cup S'$ is a basis of $V$. Since it is a free set, it suffices to prove that every element $x$ of $S$ belongs to $s(L \cup S')$, for then $V = s(S) \subset s(L \cup S')$, whence $s(L \cup S') = V$. If $x \notin s(L \cup S')$, then by the Lemma on transcendence sets, $L \cup S' \cup \{x\}$ would be a free set. But then $S' \cup \{x\}$ would belong to $M$, contradicting the maximality of $S'$. This completes the proof.
