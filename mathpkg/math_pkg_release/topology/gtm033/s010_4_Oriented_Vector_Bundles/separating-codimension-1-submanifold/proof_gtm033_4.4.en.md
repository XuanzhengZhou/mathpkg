---
role: proof
locale: en
of_concept: separating-codimension-1-submanifold
source_book: gtm033
source_chapter: "4"
source_section: "4. Oriented Vector Bundles"
---

# Proof of Lemma 4.4 (Separating Codimension-1 Submanifold)

Let $N$ be a connected manifold and let $M \subset N$ be a connected closed submanifold of codimension $1$, with $\partial M = \partial N = \varnothing$. Assume that $M$ separates $N$.

**Step 1: $M$ is the boundary of each component of $N - M$.** Let $A$ be a connected component of $N - M$. Since $M$ is closed in $N$, the topological boundary $\operatorname{Bd} A = \overline{A} \cap \overline{N - A}$ is a subset of $M \cap \overline{A}$. Moreover, $\operatorname{Bd} A$ is nonempty (otherwise $A$ would be both open and closed in the connected space $N$, forcing $A = N$, contradicting that $M$ separates $N$). Thus $\operatorname{Bd} A$ is a nonempty closed subset of $M$.

Now examine $\operatorname{Bd} A$ using submanifold charts for the pair $(N, M)$. A submanifold chart is a diffeomorphism $\varphi: U \to \mathbb{R}^n$ from an open set $U \subset N$ such that $\varphi(U \cap M) = \mathbb{R}^{n-1} \times \{0\}$. In such a chart, $U - M$ has exactly two components, corresponding to the upper and lower half-spaces $x_n > 0$ and $x_n < 0$. Since $A$ is a component of $N - M$, its intersection with $U$ must be precisely one of these half-space components. Therefore every point $x \in M \cap U$ lies in $\operatorname{Bd} A$ (it is a limit point of $A \cap U$ and also of $(N - M) - A$). Hence $M \cap U \subset \operatorname{Bd} A$, showing that $\operatorname{Bd} A$ is open in $M$.

Since $M$ is connected and $\operatorname{Bd} A$ is a nonempty subset of $M$ that is both open and closed in $M$, we have $\operatorname{Bd} A = M$.

**Step 2: $\overline{A}$ is a submanifold with boundary $M$.** The submanifold charts also show that $\overline{A}$ is a submanifold of $N$ with boundary $\partial \overline{A} = M$. Indeed, in a submanifold chart for $(N, M)$, the set $\overline{A} \cap U$ corresponds to a closed half-space bounded by the hyperplane $\varphi(U \cap M)$. Thus $(\overline{A}, M)$ is a manifold with boundary.

**Step 3: Triviality of the normal bundle.** The normal bundle $\nu$ of $M$ in $N$ is, by definition, $TM|_M / TN|_M$ (or algebraically $TN|_M / TM$). Since $\overline{A}$ is a submanifold of $N$ containing $M$ as its boundary, the normal bundle of $M$ in $N$ coincides with the normal bundle of $M = \partial \overline{A}$ in $\overline{A}$. By Theorem 4.2, the normal bundle of the boundary of any manifold is trivial. Hence $\nu$ is trivial.

**Step 4: $N - M$ has exactly two components.** Let $B$ be another component of $N - M$ (distinct from $A$). By the same reasoning, $\overline{B}$ is also a submanifold of $N$ with boundary $M$, and $\overline{B}$ is closed in $N$. Then $\overline{A} \cup \overline{B}$ is a closed subset of $N$. We claim it is also open. Given $x \in \overline{A} \cup \overline{B}$:

- If $x \in A \cup B$, then $x$ is in the open set $A \cup B \subset \overline{A} \cup \overline{B}$.
- If $x \in M$, then using a submanifold chart, every neighborhood of $x$ meets both half-space components. Since $A$ and $B$ are the only components meeting near $x$ (by the local structure of a codimension-1 submanifold), every point near $x$ lies in $\overline{A} \cup \overline{B}$.

Thus $\overline{A} \cup \overline{B}$ is both open and closed in the connected manifold $N$. Since it is nonempty (it contains $M$), we have $\overline{A} \cup \overline{B} = N$. Consequently, $N - M = A \cup B$, showing there are exactly two components (for if there were a third component $C$, then $C$ would be disjoint from $\overline{A} \cup \overline{B} = N$, impossible).

The (topological) boundary of each component is $M$, as established in Step 1-2.

QED
