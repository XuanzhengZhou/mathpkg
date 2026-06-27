---
role: proof
locale: en
of_concept: metacompact-t1-countably-compact-iff-compact
source_book: gtm027
source_chapter: "5"
source_section: "V. Point Finite Covers and Metacompact Spaces"
---

# Proof of Metacompact T1-Space is Countably Compact iff Compact

Let $X$ be a metacompact $T_1$-space. We prove that $X$ is countably compact if and only if it is compact.

($\Leftarrow$) Trivial: every compact space is countably compact.

($\Rightarrow$) Suppose $X$ is countably compact. Let $\mathcal{U}$ be an arbitrary open cover of $X$. Since $X$ is metacompact, $\mathcal{U}$ has a point finite open refinement $\mathcal{V}$. By the countably compact property, every countable subfamily of $\mathcal{V}$ has a finite subcover? No — we need a different argument.

Since $\mathcal{V}$ is point finite, by the result on minimal subcovers (5.V(b)), $\mathcal{V}$ has a minimal subcover $\mathcal{W}$ that covers $X$. We claim $\mathcal{W}$ is finite. Suppose $\mathcal{W}$ is infinite. Enumerate a countably infinite subset $\{W_1, W_2, \ldots\}$ of $\mathcal{W}$. For each $n$, by minimality of $\mathcal{W}$, the family $\mathcal{W} \setminus \{W_n\}$ does not cover $X$, so there exists $x_n \in X \setminus \bigcup (\mathcal{W} \setminus \{W_n\})$, meaning $x_n \in W_n$ and $x_n \notin W_m$ for $m \neq n$. The set $\{x_n : n \in \mathbb{N}\}$ is infinite. Since $X$ is countably compact, this set has a limit point $x$. But each $W_n$ is open and $x_n \in W_n$, and no other $x_m$ belongs to $W_n$, so each $W_n$ contains exactly one point from the set. The point $x$ would belong to some $W_k \in \mathcal{W}$ (since $\mathcal{W}$ is a cover), but $W_k$ contains only $x_k$ from the set, contradicting that $x$ is a limit point. Hence $\mathcal{W}$ must be finite.

Therefore $\mathcal{U}$ has a finite subcover (from the finite refinement $\mathcal{W}$), so $X$ is compact.
