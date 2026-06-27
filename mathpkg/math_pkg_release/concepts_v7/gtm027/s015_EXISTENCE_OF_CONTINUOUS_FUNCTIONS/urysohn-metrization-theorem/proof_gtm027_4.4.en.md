---
role: proof
locale: en
of_concept: urysohn-metrization-theorem
source_book: gtm027
source_chapter: "4"
source_section: "Existence of Continuous Functions"
---

# Proof of Urysohn Metrization Theorem

**Urysohn Metrization Theorem.** A regular $T_1$-space whose topology has a countable base is homeomorphic to a subspace of the cube $[0,1]^\omega$ and is hence metrizable.

*Proof.* It is sufficient to show that there is a countable family of continuous functions on $X$ to $[0,1]$ which distinguishes points and closed sets.

Let $\mathcal{B}$ be a countable base for the topology of $X$ and let $\mathcal{P}$ be the set of all pairs $(U,V)$ such that $U$ and $V$ belong to $\mathcal{B}$ and $U^{-} \subset V$. Surely $\mathcal{P}$ is countable.

For each pair $(U,V)$ in $\mathcal{P}$, choose a continuous function $f$ on $X$ to $[0,1]$ such that $f$ is zero on $U$ and one on $X \sim V$. Such a function exists because of the Tychonoff lemma 4.1 (a regular Lindelöf space is normal) and the Urysohn lemma 4.4 (which provides the function on a normal space). Let $F$ be the family of functions so obtained; $F$ is countable.

It remains to prove that $F$ distinguishes points and closed sets. If $B$ is closed and $x \in X \sim B$, choose a member $V$ of $\mathcal{B}$ such that $x \in V \subset X \sim B$. Since $X$ is regular, there is a member $U$ of $\mathcal{B}$ with $x \in U \subset U^{-} \subset V$. Then $(U,V) \in \mathcal{P}$ and the corresponding function $f \in F$ satisfies $f(x) = 0$ and $f = 1$ on $X \sim V \supset B$, so $f(x) \notin f[B]^{-} = \{1\}$. Thus $F$ distinguishes points and closed sets.

By the embedding lemma 4.5, the evaluation map embeds $X$ into $[0,1]^F$. Since $F$ is countable, $[0,1]^F \cong [0,1]^\omega$, which is metrizable by Theorem 14. Hence $X$ is metrizable.

