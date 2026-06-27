---
role: proof
locale: en
of_concept: descending-chain-equivalent-minimum-condition
source_book: gtm030
source_chapter: "Chapter VI"
source_section: "4. The chain conditions"
---

**Proof.** We first assume the descending chain condition. Let $\{\mathfrak{N}\}$ be a non-vacuous collection of submodules. Select $\mathfrak{N}_1$ in the collection. Either $\mathfrak{N}_1$ is minimal or there exists $\mathfrak{N}_2$ in the collection with $\mathfrak{N}_2 \subsetneq \mathfrak{N}_1$. If $\mathfrak{N}_2$ is minimal, we are done. Otherwise, continuing in this manner we obtain a strictly decreasing sequence
$$\mathfrak{N}_1 \supsetneq \mathfrak{N}_2 \supsetneq \mathfrak{N}_3 \supsetneq \cdots$$
of submodules in the collection. By the descending chain condition, this sequence must terminate, so there exists an integer $r$ such that $\mathfrak{N}_r$ is minimal in the collection $\{\mathfrak{N}_i\}$. We then certainly have $\mathfrak{N}_r = \mathfrak{N}_{r+1} = \cdots$, and $\mathfrak{N}_r$ is a minimal element of the original collection.

Conversely, assume the minimum condition and let
$$\mathfrak{N}_1 \supseteq \mathfrak{N}_2 \supseteq \mathfrak{N}_3 \supseteq \cdots$$
be a decreasing sequence of submodules. Consider the collection $\{\mathfrak{N}_i\}$. By the minimum condition, this collection contains a minimal element, say $\mathfrak{N}_N$. Then $\mathfrak{N}_N = \mathfrak{N}_{N+1} = \mathfrak{N}_{N+2} = \cdots$, for if some $\mathfrak{N}_k$ with $k > N$ were strictly contained in $\mathfrak{N}_N$, this would contradict the minimality of $\mathfrak{N}_N$ in the collection. Thus the descending chain condition holds.
