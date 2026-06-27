---
role: exercise
locale: en
chapter: "1"
section: "1"
exercise_number: 13
---

Let $f: X \rightarrow Y$. Define $f_2: \mathbb{P}(Y) \rightarrow \mathbb{P}(X)$ as follows: if $\mathcal{Q} \in \mathbb{P}(Y)$, then $f_2(\mathcal{Q})$ consists of the nonempty members of the collection $\{f^{-1}[Q]: Q \in \mathcal{Q}\}$. First verify that $f_2(\mathcal{Q}) \in \mathbb{P}(X)$; then show that $f$ is an injection (respectively, surjection, bijection) if and only if $f_2$ is a surjection (respectively, injection, bijection).

The remainder of this section is concerned with the notion of “isomorphism” between objects of the kinds we have been considering.

Functions $f: B \rightarrow U$ and $g: C \rightarrow W$ are isomorphic if


(b) If $q$ is a selection-isomorphism from the selection of $f$ to the selection of $g$, then there exists a bijection $p' : B \rightarrow C$ such that $(p', q)$ is a function-isomorphism from $f$ to $g$.

(c) If $p$ is a partition-isomorphism from the partition of $f$ to the partition of $g$ and if $|U| = |W|$, then there exists a bijection $q' : U \rightarrow W$ such that $(p, q')$ is a function-isomorphism from $f$ to $g$.

Proof. (a) Let $S$ be a cell of the partition of $f$, i.e., $S = f^{-1}[x]$ for some $x \in U$. By A19, $p[S] = p[f^{-1}[x]] = g^{-1}[q(x)]$, which is a cell of the partition of $g$. Let $s$ be the selection of $f$ and $t$ the selection of $g$. Let $x \in U$. By definition and A19,

$$t(q(x)) = |g^{-1}[q(x)]| = |p^{-1}[g^{-1}[q(x)]]| = |f^{-1}[x]| = s(x).$$

Thus $tq = s$.

(b) With $s$ and $t$ as in the proof of (a), we assume $tq = s$. For any $x \in U$,

$$|f^{-1}[x]| = s(x) = tq(x) = |g^{-1}[q(x)]|.$$

Hence there exists a bijection $p_x : f^{-1}[x] \rightarrow g^{-1}[q(x)]$. These bijections for all $x \in U$ determine a bijection $p' : B \rightarrow C$ by $p'(w) = p_x(w)$ where $w \in f^{-1}[x]$. Clearly $f = q^{-1}gp'$.

(c) Since $p$ is a partition-isomorphism from the partition of $f$ to the partition of $g$, we have

$$\{g^{-1}[x] : x \in W
