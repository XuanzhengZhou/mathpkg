---
role: proof
locale: en
of_concept: convex-extensions-and-combinations
source_book: gtm036
source_chapter: "13"
source_section: "13.1"
---

(i) If $A$ is convex, then by theorem 5.2(xiii) $A^-$ is convex. If $A^i$ is void, clearly it is convex. Now assume that $A^i$ is non-void. If it is shown that $tA^- + (1 - t)A^i \subset A^i$ for $0 \leq t < 1$, the convexity of $A^i$ also follows. Because $tA^- + (1 - t)A^i$ is open, it is sufficient to prove that $tA^- + (1 - t)A^i \subset A$. Let $x \in A^i$; then $(1 - t)(A^i - x)$ is an open neighborhood of $0$. Therefore, $tA^- \subset (tA)^- \subset tA + (1 - t)(A^i - x) = tA + (1 - t)A^i - (1 - t)x \subset A - (1 - t)x$, and $tA^- + (1 - t)A^i \subset A$ follows.

(iv) The set $\langle A \cup B \rangle$ is the image of $[0:1] \times \langle A \rangle \times \langle B \rangle$ under the continuous mapping $(a,x,y) \rightarrow ax + (1-a)y$. If $\{z_\alpha, \alpha \in C\}$ is a net in $\langle A \cup B \rangle$ which converges to the point $z$ in $E$, and if $z_\alpha = a_\alpha x_\alpha + (1-a_\alpha)y_\alpha$, then by the compactness of $[0:1]$ and $\langle A \rangle$ there are subnets $\{a_\beta, \beta \in D\}$ and $\{x_\beta, \beta \in D\}$ which converge to $a$ in $[0:1]$ and $x$ in $\langle A \rangle$, respectively. If $a = 1$, then $(1-a_\beta)y_\beta \rightarrow 0$ since $\langle B \rangle$ is bounded; hence, since $E$ is a Hausdorff space, $z = x \in \langle A \rangle \subset \langle A \cup B \rangle$. If $a < 1$, then $y_\beta \rightarrow (z - ax)/(1-a)$, which is a member $y$ of $\langle B \rangle$ since $\langle B \rangle$ is closed. Then $z = ax + (1-a)y \in \langle A \cup B \rangle$, so $\langle A \cup B \rangle$ is closed.
