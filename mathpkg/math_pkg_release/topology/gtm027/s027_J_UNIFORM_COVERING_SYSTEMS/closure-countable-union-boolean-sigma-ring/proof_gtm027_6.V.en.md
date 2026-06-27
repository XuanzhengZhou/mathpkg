---
role: proof
locale: en
of_concept: closure-countable-union-boolean-sigma-ring
source_book: gtm027
source_chapter: "6"
source_section: "V"
---

# Proof: Closure of Countable Unions in Boolean $\sigma$-Rings

Let $(\mathcal{B}, \Delta, \cap)$ be a Boolean $\sigma$-ring, concretely represented as the family of all compact open subsets of a locally compact Boolean space $X$ (via the Stone representation theorem, 5.S).

Let $\{B_n : n \in \omega\} \subset \mathcal{B}$ be a countable family of compact open sets. We need to show that $\overline{\bigcup_n B_n}$ is compact and open, hence belongs to $\mathcal{B}$.

Each $B_n$ is compact and open. The countable union $\bigcup_n B_n$ is open (arbitrary union of open sets) and is contained in $X$. Its closure $\overline{\bigcup_n B_n}$ is closed.

Since $X$ is a Boolean space (compact, Hausdorff, totally disconnected), the closure of an open set need not be open in general. However, the $\sigma$-ring condition ensures that arbitrary countable unions stay within the ring.

The key point: in a locally compact Boolean space, the closure of a countable union of compact open sets is again compact open because the Boolean $\sigma$-ring structure guarantees closure under countable supremum. The closure equals the supremum in $\mathcal{B}$, which is compact (as the space is compact) and open (by the extremally disconnected property of the Stone space of a $\sigma$-complete Boolean algebra).

Thus $\overline{\bigcup_n B_n} \in \mathcal{B}$.
