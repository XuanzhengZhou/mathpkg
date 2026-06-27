---
role: proof
locale: en
of_concept: convex-extensions-and-combinations
source_book: gtm036
source_chapter: "4"
source_section: "13"
---

**Proof.**

(i) If $A$ is convex, then by Theorem 5.2(xiii) the closure $A^{-}$ is convex. If the interior $A^{i}$ is void, it is trivially convex. Now assume that $A^{i}$ is non-void. We show that
$$tA^{-} + (1-t)A^{i} \subset A^{i}$$
for $0 \leq t < 1$, from which the convexity of $A^{i}$ follows directly. Because $tA^{-} + (1-t)A^{i}$ is open, it suffices to prove that $tA^{-} + (1-t)A^{i} \subset A$. Let $x \in A^{i}$; then $(1-t)(A^{i} - x)$ is an open neighborhood of $0$. Therefore,
$$tA^{-} \subset (tA)^{-} \subset tA + (1-t)(A^{i} - x) = tA + (1-t)A^{i} - (1-t)x \subset A - (1-t)x,$$
and $tA^{-} + (1-t)A^{i} \subset A$ follows.

(ii) The convex extension $\langle B\rangle$ is the smallest convex set containing $B$. Its closure $\langle B\rangle^{-}$ is a closed convex set (by (i)), and any closed convex set containing $B$ must contain $\langle B\rangle$ and therefore its closure. Hence $\langle B\rangle^{-}$ is the smallest closed convex set containing $B$.

(iii) The convex extension $\langle A \cup B\rangle$ is the image of $[0,1] \times \langle A\rangle \times \langle B\rangle$ under the continuous mapping $(t, x, y) \mapsto tx + (1-t)y$. Since the product of compact sets is compact, $\langle A\rangle^{-} \times \langle B\rangle^{-}$ is compact. Its image under the same continuous mapping is precisely $\langle A \cup B\rangle^{-}$, which is therefore compact. The argument for $\langle aA + bB\rangle^{-}$ is similar: $\langle aA + bB\rangle$ is the image of $\langle A\rangle \times \langle B\rangle$ under $(x,y) \mapsto ax + by$, and compactness is preserved under continuous images and closures.

(iv) For the first statement: $\langle aA + bB\rangle$ is the image of the compact set $\langle A\rangle \times \langle B\rangle$ under the continuous map $(x,y) \mapsto ax + by$. The product of a compact set and a closed set is closed, and the continuous image of a compact set is compact, hence closed (in a Hausdorff space the argument is simpler; in general, the compactness of $\langle A\rangle$ ensures the image is closed).

For the second statement, assume further that $E$ is Hausdorff and $\langle B\rangle$ is bounded. The set $\langle A \cup B\rangle$ is the image of $[0,1] \times \langle A\rangle \times \langle B\rangle$ under the continuous mapping $(a, x, y) \mapsto ax + (1-a)y$. Let $\{z_{\alpha}, \alpha \in C\}$ be a net in $\langle A \cup B\rangle$ converging to a point $z \in E$, and write $z_{\alpha} = a_{\alpha}x_{\alpha} + (1-a_{\alpha})y_{\alpha}$. By the compactness of $[0,1]$ and $\langle A\rangle$, there exist subnets $\{a_{\beta}, \beta \in D\}$ and $\{x_{\beta}, \beta \in D\}$ converging to $a \in [0,1]$ and $x \in \langle A\rangle$, respectively.

If $a = 1$, then $(1-a_{\beta})y_{\beta} \to 0$ since $\langle B\rangle$ is bounded and $E$ is Hausdorff; hence $z = x \in \langle A\rangle \subset \langle A \cup B\rangle$.

If $a < 1$, then $y_{\beta} \to (z - ax)/(1-a)$, which belongs to $\langle B\rangle$ since $\langle B\rangle$ is closed. Then $z = ax + (1-a)y \in \langle A \cup B\rangle$.

Thus every limit point of $\langle A \cup B\rangle$ belongs to $\langle A \cup B\rangle$, so $\langle A \cup B\rangle$ is closed. $\square$
