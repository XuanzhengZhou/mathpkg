---
role: proof
locale: en
of_concept: locally-connected-separated-components
source_book: gtm027
source_chapter: "1"
source_section: "S. Locally Connected Spaces"
---

# Proof of Separated Sets for Points in Different Components

Let $X$ be a locally connected space and let $x, y \in X$ belong to different components of $X$. Let $C_x$ and $C_y$ denote the components of $X$ containing $x$ and $y$, respectively. Then $C_x \cap C_y = \varnothing$.

By part (a) applied to the open set $U = X$, each component of $X$ is open in $X$. Hence $C_x$ and $C_y$ are open sets.

Set $A = C_x$ and $B = X \setminus C_x$. Then:
- $x \in A$ and $y \in C_y \subseteq B$ (since $C_y \subseteq X \setminus C_x$).
- $A$ and $B$ are separated: $A$ is open, and $B$ is the complement of $A$, hence closed (and indeed open as well, since $A$ is clopen). Thus $A \cap \overline{B} = \overline{A} \cap B = \varnothing$.
- $X = A \cup B$ by construction.

Thus $A$ and $B$ are separated sets satisfying the required conditions.

$\square$
