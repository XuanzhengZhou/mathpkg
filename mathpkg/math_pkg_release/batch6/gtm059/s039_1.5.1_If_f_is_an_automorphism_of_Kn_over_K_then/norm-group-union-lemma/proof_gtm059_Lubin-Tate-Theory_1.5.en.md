---
role: proof
locale: en
of_concept: norm-group-union-lemma
source_book: gtm059
source_chapter: "Lubin-Tate Theory"
source_section: "1.5"
---

*Proof.* Suppose an element $s$ belongs to $\bigcup_{k=1}^{\infty} N_k(v^*)$. Then $s = N_k(u_k)$ for some $u_k \in v^*$ and sufficiently large $k$. By Theorem 2.2, every element of $v^*$ is a norm from each extension $K_k$. Hence $(v_k, N_k)(K_k) = (N_k v_k)(K_k) = 1$, which implies that $N_k(s)$ is a power of $v$, so $s \in N_k^*(v^*)$. This proves the inclusion $\bigcup N_k(v^*) \subseteq N_k^*(v^*)$.

Conversely, suppose $s \in N_k^*(v^*)$, so that $N_k(s)$ is a power of $v$ for all sufficiently large $k$, say $k \ge k_0$. Then for each such $k$, we have

$$1 = (v_k, N_k)(K_k) = (N_k v_k)(K_k).$$

Let $N_k^* = v^*$ where $v$ is a unit in $K$. Since $s$ is a norm from $K_k$ by Theorem 2.2, we conclude that

$$(v_k, N_k)(K_k) = 1 \quad \text{for all } k.$$

Hence $s \equiv 1 \pmod{\mathfrak{m}^k}$ for all $k$, so $s = 1$ (in the relevant quotient), which shows $s$ lies in the union of norm images. This proves the reverse inclusion and establishes the lemma.
