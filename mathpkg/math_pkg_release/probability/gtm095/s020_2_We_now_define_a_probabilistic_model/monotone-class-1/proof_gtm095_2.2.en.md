---
role: proof
locale: en
of_concept: monotone-class-1
source_book: gtm095
source_chapter: "2"
source_section: "2"
---

# Proof of Lemma 2 (Algebra is $\sigma$-Algebra iff Monotonic Class)

**Lemma 2.** A necessary and sufficient condition for an algebra $\mathcal{A}$ to be a $\sigma$-algebra is that it is a monotonic class.

*Proof.* **Necessity.** Every $\sigma$-algebra is evidently a monotonic class, because if $A_n \in \mathcal{A}$ and $A_n \uparrow A$, then $A = \bigcup_{n} A_n \in \mathcal{A}$ by the countable union property of $\sigma$-algebras; similarly, if $A_n \downarrow A$, then $A = \bigcap_{n} A_n \in \mathcal{A}$.

**Sufficiency.** Now let $\mathcal{A}$ be an algebra that is also a monotonic class. Take any sequence $A_n \in \mathcal{A}$, $n = 1, 2, \ldots$. Define the partial unions

$$B_n = \bigcup_{i=1}^{n} A_i \in \mathcal{A}.$$

Since $\mathcal{A}$ is an algebra, each finite union $B_n$ belongs to $\mathcal{A}$. Clearly $B_n \subseteq B_{n+1}$, so $B_n \uparrow \bigcup_{i=1}^{\infty} A_i$. Because $\mathcal{A}$ is a monotonic class, the limit of this increasing sequence belongs to $\mathcal{A}$:

$$\bigcup_{i=1}^{\infty} A_i = \lim_{n} B_n \in \mathcal{A}.$$

Similarly, to show closure under countable intersections, consider $C_n = \bigcap_{i=1}^{n} A_i \in \mathcal{A}$. Then $C_n \downarrow \bigcap_{i=1}^{\infty} A_i$, and the monotonic class property again yields $\bigcap_{i=1}^{\infty} A_i \in \mathcal{A}$.

Thus $\mathcal{A}$ is closed under countable unions and countable intersections, and is therefore a $\sigma$-algebra. $\square$
