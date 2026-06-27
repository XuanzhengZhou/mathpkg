---
role: proof
locale: en
of_concept: harnacks-theorem
source_book: gtm011
source_chapter: "2"
source_section: "2.15"
---

**Proof.** (a) To show that $\text{Har}(G)$ is complete, it is sufficient to show that it is a closed subspace of $C(G, \mathbb{R})$. So let $\{u_n\}$ be a sequence in $\text{Har}(G)$ such that $u_n \to u$ in $C(G, \mathbb{R})$. Then, by Lemma IV.2.7, it follows that $u$ has the MVP (Mean Value Property) and so, by Theorem 2.11, $u$ must be harmonic.

(b) We may assume that $u_1 \geq 0$ (if not, consider $\{u_n - u_1\}$). Let $u(z) = \sup \{u_n(z): n \geq 1\}$ for each $z$ in $G$. So for each $z$ in $G$ one of two possibilities occurs: $u(z) = \infty$ or $u(z) \in \mathbb{R}$ and $u_n(z) \to u(z)$.

Define
$$A = \{z \in G: u(z) = \infty\}$$
$$B = \{z \in G: u(z) < \infty\};$$
then $G = A \cup B$ and $A \cap B = \emptyset$. We will show that both $A$ and $B$ are open.

If $a \in A$, let $R > 0$ be such that $\overline{B}(a; R) \subset G$. By Harnack's Inequality (2.17),
$$u_n(z) \geq \frac{R - |z - a|}{R + |z - a|} u_n(a)$$
for all $z \in B(a; R)$. Since $u_n(a) \to \infty$, it follows that $u_n(z) \to \infty$ for every $z \in B(a; R)$. Hence $B(a; R) \subset A$ and $A$ is open.

If $a \in B$, let $R > 0$ be such that $\overline{B}(a; R) \subset G$. Then for any $z \in B(a; R)$,
$$u_n(z) \leq \frac{R + |z - a|}{R - |z - a|} u_n(a)$$
by Harnack's Inequality. Since $u_n(a) \to u(a) < \infty$, it follows that $\{u_n(z)\}$ is bounded above and hence $u(z) < \infty$ for all $z \in B(a; R)$. Thus $B(a; R) \subset B$ and $B$ is open.

Since $G$ is connected (it is a region), either $A = \emptyset$ or $B = \emptyset$. If $B = \emptyset$, then $u(z) = \infty$ for all $z \in G$ and $u_n(z) \to \infty$ uniformly on compact subsets of $G$. If $A = \emptyset$, then $u(z) < \infty$ for all $z \in G$.

To see that $u$ is continuous when $A = \emptyset$, fix $a \in G$ and let $R > 0$ with $\overline{B}(a; R) \subset G$. Applying Harnack's Inequality to the monotone sequence and taking the limit as $n \to \infty$, we obtain for $z \in B(a; R)$:
$$\frac{R - |z - a|}{R + |z - a|} u(a) \leq u(z) \leq \frac{R + |z - a|}{R - |z - a|} u(a).$$

Hence
$$\frac{-2|z - a|}{R + |z - a|} u(a) \leq u(z) - u(a) \leq \frac{2|z - a|}{R - |z - a|} u(a);$$
or
$$|u(z) - u(a)| \leq \frac{2|z - a|}{R - |z - a|} u(a).$$

So as $z \to a$, it is clear that $u(z) \to u(a)$, establishing continuity of $u$ on $G$.

Now that $u$ is continuous, the convergence $u_n \to u$ is monotone and pointwise. One may then apply Dini's Theorem (Exercise VII.1.6) to conclude that the convergence is uniform on compact subsets of $G$. Alternatively, one may use the Monotone Convergence Theorem from measure theory to obtain that $u$ has the Mean Value Property, which together with continuity implies $u \in \text{Har}(G)$ by Theorem 2.11.

Thus $\{u_n\}$ converges in $\text{Har}(G)$ to the harmonic function $u$. $\square$
