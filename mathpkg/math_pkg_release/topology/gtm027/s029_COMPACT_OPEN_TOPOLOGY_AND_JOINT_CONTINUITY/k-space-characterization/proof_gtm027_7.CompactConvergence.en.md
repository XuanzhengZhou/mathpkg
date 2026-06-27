---
role: proof
locale: en
of_concept: k-space-characterization
source_book: gtm027
source_chapter: "7"
source_section: "Uniform Convergence on Compacta"
---

# Proof of Theorem 7.13 — Locally Compact or First Countable Hausdorff Spaces are k-Spaces

Assume $X$ is a Hausdorff space. To prove $X$ is a $k$-space, let $B \subset X$ be non-closed and show that $B \cap C$ is not closed for some closed compact set $C$.

Let $x$ be an accumulation point of $B$ with $x \notin B$.

**Case 1: $X$ is locally compact.** Then $x$ has a compact neighborhood $U$. The intersection $B \cap U$ is not closed in $U$ (hence not closed in $X$) because $x \in \overline{B \cap U}$ but $x \notin B \cap U$. Since $U$ is compact and $X$ is Hausdorff, $U$ is closed; take $C = U$.

**Case 2: $X$ satisfies the first axiom of countability.** Then there exists a sequence $\{y_n, n \in \omega\}$ in $B \setminus \{x\}$ converging to $x$. The set $C = \{x\} \cup \{y_n : n \in \omega\}$ is compact (any open cover includes a set containing $x$, which contains all but finitely many $y_n$). The intersection $B \cap C = \{y_n : n \in \omega\}$ is not closed in $C$ (since $x$ is an accumulation point not in the set). Thus $B \cap C$ is not closed.

In both cases we have found a closed compact $C$ with $B \cap C$ not closed, proving $X$ is a $k$-space.
