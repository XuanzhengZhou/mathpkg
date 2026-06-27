---
role: proof
locale: en
of_concept: theorem-6-2
source_book: gtm012
source_chapter: "3"
source_section: "6"
---

# Proof of Theorem 6.2: Every Periodic Distribution Has Finite Order

**Theorem 6.2.** If $F \in \mathcal{P}'$, then there is an integer $k \ge 0$ such that $F$ is of order $k$.

Recall that $F$ is of order $k$ if there exists a constant $c$ such that

$$|F(u)| \le c\,\{|u| + |Du| + \cdots + |D^k u|\}, \quad \text{all } u \in \mathcal{P}.$$

*Proof.* We argue by contradiction. Suppose $F$ is not of order $k$ for any integer $k \ge 0$. Then for each $k$, there exists a function $u_k \in \mathcal{P}$ such that

$$|F(u_k)| \ge (k+1)\bigl\{|u_k| + |Du_k| + \cdots + |D^k u_k|\bigr\}.$$

Define the normalized function

$$v_k = \frac{u_k}{(k+1)\bigl\{|u_k| + |Du_k| + \cdots + |D^k u_k|\bigr\}}.$$

Then, by linearity of $F$ and the seminorms,

$$|F(v_k)| \ge 1,$$

while

$$|v_k| + |D v_k| + \cdots + |D^k v_k| = \frac{1}{k+1}.$$

As $k \to \infty$, the right-hand side tends to $0$. In particular, for any fixed $m \ge 0$, once $k \ge m$ we have

$$|v_k| + |D v_k| + \cdots + |D^m v_k| \le \frac{1}{k+1} \to 0.$$

This means $v_k \to 0$ in the sense of $\mathcal{P}$ (i.e., all derivatives converge uniformly to $0$). Since $F$ is continuous on $\mathcal{P}$, we must have $F(v_k) \to 0$. But $|F(v_k)| \ge 1$ for all $k$, a contradiction.

Therefore $F$ must be of order $k$ for some integer $k \ge 0$. $\square$
