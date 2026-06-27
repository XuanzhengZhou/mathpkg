---
role: proof
locale: en
of_concept: "let-be-a-locally-compact-hausdorff-space-let"
source_book: gtm025
source_chapter: "Topology"
source_section: "6.78"
---

Let $W$ be any neighborhood of $x$ such that $W^-$ is compact. Let $G = U \cap W$. Then $G$ is a neighborhood of $x$; since $G^-$ is a closed subset of $W^-$, it follows from (6.39) that $G^-$ is compact. We have $G \subset U$, but we do not know that $G^- \subset U$. Recall (6.7.vii) that $\partial G = G^- \cap G^{\circ'} = G^- \cap G'$. Thus $\partial G$ is compact (6.39). If $\partial G = \varnothing$, we may take $V = G$. Thus suppose $\partial G \neq \varnothing$. For each $y \in \partial G$, choose neighborhoods $V_y$ and $H_y$ of $x$ and $y$ respectively such that $V_y \cap H_y = \varnothing$. We may suppose that $V_y \subset G$, for otherwise intersect it with $G$. Then $\{H_y : y \in \partial G\}$ is an open cover of $\partial G$, and by compactness there exist $y_1, \ldots, y_n \in \partial G$ such that $\partial G \subset H_{y_1} \cup \cdots \cup H_{y_n} = H$. Let $V = V_{y_1} \cap \cdots \cap V_{y_n}$. Then $V$ is a neighborhood of $x$ and $V \cap H = \varnothing$. Clearly $V \subset G$, so $V^- \subset G^-$ and $V^-$ is compact. Moreover $V \subset H'$ and $H'$ is closed so $V^- \subset H'$. Thus $V^- \subset G^- \cap H' \subset G^
$t' = \frac{a - 1}{2^n}$ and $t'' = \frac{a + 1}{2^n}$ and notice that $U'_t$ and $U'_{t''}$ are already defined $[a - 1$ and $a + 1$ are even]. We again use (6.79) to obtain an open set $U_t$ such that $U'_{t''} \subset U_t \subset U'_{t''} \subset U_t$. Thus we obtain the desired family $\{U_t\}_{t \in D}$, and we have $U'_{t''} \subset U_s$ whenever $s < t$ in $D$.

Now define $f$ on $X$ by $f(x) = 0$ for $x \in U'_0$ and $f(x) = \sup \{t \in D : x \in U_t\}$ for $x \in U_0$. Clearly $f(x) = 1$ for all $x \in A = U_1$. It remains to show that $f$ is continuous. To this end, let $0 \leq \alpha < 1$ and $0 < \beta \leq 1$. Clearly $f(x) > \alpha$ if and only if $x \in U_t$ for some $t > \alpha$ and therefore $f^{-1}([\alpha, 1]) = \cup \{U_t : t \in D, t > \alpha\}$, which is open. In like manner $f(x) \geq \beta$ if and only if $x \in U_s$ for every $s < \beta$. Therefore $f^{-1}([\beta, 1]) = \cap \{U_s : s \in D, s < \beta\} = \cap \{U'_{t'} : t \in D, t < \beta\}$, which is closed. Taking complements we see that $f^{-1}([0, \beta])$ is open. These facts together with (6.70) show that $f$ is continuous.

We now take up the notions of limit superior and limit inferior for sequences of real numbers.
