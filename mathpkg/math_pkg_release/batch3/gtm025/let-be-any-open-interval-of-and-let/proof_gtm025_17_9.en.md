---
role: proof
locale: en
of_concept: "let-be-any-open-interval-of-and-let"
source_book: gtm025
source_chapter: "Haar Measure"
source_section: "17.9"
---

Let $A = \{x \in ]a, b [ : f'_-(x) \text{ exists}, f'_+(x) \text{ exists}, f'_+(x) < f'_-(x)\}$ and let $B = \{x \in ]a, b [ : f'_-(x) \text{ exists}, f'_+(x) \text{ exists}, f'_+(x) > f'_-(x)\}$. For each $x \in A$, choose a rational number $r_x$ such that $f'_+(x) < r_x < f'_-(x)$. Next choose rational numbers $s_x$ and $t_x$ such that $a < s_x < x < t_x < b$,

$$\frac{f(y) - f(x)}{y - x} > r_x \quad \text{if} \quad s_x < y < x,$$

(1)

and

$$\frac{f(y) - f(x)}{y - x} < r_x \quad \text{if} \quad x < y < t_x.$$

(2)

Combining (1) and (2), we have

$$f(y) - f(x) < r_x(y - x)$$

(3)

whenever $y \neq x$ and $s_x < y < t_x$. Thus we obtain a function $\varphi$ from $A$ into the countable set $Q^3$, defined by $\varphi(x) = (r_x, s_x, t_x)$. We will prove that $A$ is countable by showing that $\varphi$ is one-to-one. Assume that there are distinct $x$ and $y$ in $A$ such that $\varphi(x) = \varphi(y)$. Then $]s_y, t_y[ = ]s_x, t_x[$, and $x$ and $y

finite family $\{I_1, \ldots, I_p\} \subset \mathcal{V}$ such that

$$\lambda \left( E \cap \left( \bigcup_{n=1}^{p} I_n \right) ' \right) < \varepsilon.$$

**Proof.** Case I: $\lambda(E) < \infty$. Choose an open set $V$ such that $E \subset V$ and $\lambda(V) < \infty$. Let $\mathcal{V}_0 = \{ I \in \mathcal{V} : I \subset V \}$. Plainly $\mathcal{V}_0$ is a Vitali cover of $E$. Let $I_1 \in \mathcal{V}_0$. If $E \subset I_1$, the construction is complete. Otherwise we continue by induction as follows. Suppose that $I_1, I_2, \ldots, I_n$ have been selected and are pairwise disjoint. If $E \subset \bigcup_{k=1}^{n} I_k$, the construction is complete. Otherwise, write

$$A_n = \bigcup_{k=1}^{n} I_k, \quad U_n = V \cap A_n'.$$

Clearly $A_n$ is closed, $U_n$ is open, and $U_n \cap E \neq \emptyset$. Let

$$\delta_n = \sup \{ \lambda(I) : I \in \mathcal{V}_0, I \subset U_n \}. \tag{1}$$

Choose $I_{n+1} \in \mathcal{V}_0$ such that $I_{n+1} \subset U_n$ and $\lambda(I_{n+1}) > \frac{1}{2} \delta_n$. If our process does not stop after a finite number of steps [in which case there is nothing left to prove], then it yields an infinite sequence $(I_n)_{n=1}^{\infty}$ of pairwise disjoint members of $\mathcal{V}_0$. Let $A = \bigcup_{n=1}^{\infty} I_n$. We must show that $\lambda(E \cap A') = 0$. For each $n$, let $J_n$ be the closed interval having the same midpoint as $I

It follows that

$$I \cap I_q \neq \varnothing$$

and, since $I \subset U_{q-1}$, we have

$$\lambda(I) \leq \delta_{q-1} < 2\lambda(I_q).$$

Since $\lambda(J_q) = 5\lambda(I_q)$, (3) and (4) show that

$$I \subset J_q \subset \bigcup_{n=p}^{\infty} J_n,$$

so that $x \in \bigcup_{n=p}^{\infty} J_n$. Hence we have $E \cap A' \subset \bigcup_{n=p}^{\infty} J_n$, which implies that $\lambda(E \cap A') = 0$.

Now let $\varepsilon > 0$ be given and choose an integer $p$ so large that

$$\sum_{n=p+1}^{\infty} \lambda(I_n) < \varepsilon.$$

Then

$$E \cap A'_p \subset (E \cap A') \cup \bigcup_{n=p+1}^{\infty} I_n),$$

and so

$$\lambda(E \cap A'_p) \leq 0 + \lambda \bigcup_{n=p+1}^{\infty} I_n < \varepsilon.$$

Thus the proof is finished if $\lambda(E) < \infty$.

Case II: $\lambda(E) = \infty$. For each $n \in Z$, let $E_n = E \cap ]n, n+1[$ and let $\mathcal{V}_n = \{I \in \mathcal{V}: I \subset ]n, n+1[$. Clearly $\mathcal{V}_n$ is a Vitali cover of $E_n$. Apply Case I to find a countable pairwise disjoint family $\mathcal{I}_n \subset \mathcal{V}_n$ such that $\lambda(E_n \cap (\bigcup \mathcal{I}_n)') = 0$ for each $n \in Z$. Let $\mathcal{I} = \bigcup_{n=-\infty}^{\infty} \mathcal{I}_n$. Then $\mathcal{I}$ is a countable pairwise disjoint subfamily of $\mathcal{V}$ and

$$E \cap (\bigcup \

such that $\lambda(E_{u,v}) = \alpha > 0$. Let $\varepsilon$ be such that

$$0 < \varepsilon < \frac{\alpha(v - u)}{u + 2v}.$$

Choose an open set $U \supset E_{u,v}$ such that $\lambda(U) < \alpha + \varepsilon$. For each $x \in E_{u,v}$, there exist arbitrarily small positive numbers $h$ such that $[x, x + h] \subset U \cap [a, b]$ and

$$f(x + h) - f(x) < uh.$$

(1)

The family $\mathcal{V}$ of all such closed intervals is a Vitali cover of $E_{u,v}$, and so, by (17.11), there exists a finite, pairwise disjoint subfamily $\{[x_i, x_i + h_i]\}_{i=1}^m$ of $\mathcal{V}$ such that

$$\lambda\left(E_{u,v} \cap \left(\bigcup_{i=1}^{m}[x_i, x_i + h_i]\right)'\right) < \varepsilon.$$

Let $V = \bigcup_{i=1}^{m}[x_i, x_i + h_i]$. Then we have

$$\lambda(E_{u,v} \cap V') < \varepsilon.$$

(2)

The inclusion $V \subset U$ implies that

$$\sum_{i=1}^{m} h_i = \lambda(V) \leq \lambda(U) < \alpha + \varepsilon,$$

and so (1) yields the inequalities

$$\sum_{i=1}^{m}\left(f(x_i + h_i) - f(x_i)\right) < u \sum_{i=1}^{m} h_i < u(\alpha + \varepsilon).$$

(3)

Again, for all $y \in E_{u,v} \cap V$, there exist arbitrarily small positive numbers $k$ such that $[y, y + k] \subset V$ and

$$f(y + k) - f(y) > vk.$$

(4)

The family of all such closed intervals is a Vitali cover of $E_{u,v} \cap V$, and so there is a

have

$$\sum_{j=1}^{n} \left( f(y_j + k_j) - f(y_j) \right) \leq \sum_{i=1}^{m} \left( f(x_i + h_i) - f(x_i) \right).$$

Combining (6), (7), and (3) gives

$$v(\alpha - 2\varepsilon) < u(\alpha + \varepsilon),$$

which contradicts our choice of $\varepsilon$. Thus $\lambda(E) = 0$, and so $f'_+'(x)$ exists a.e. on $[a, b]$. Similarly $f'_-'(x)$ exists a.e. on $[a, b]$. Now apply (17.9) to see that $f'(x)$ exists a.e. on $[a, b]$.

It remains only to show that the set $F$ of points $x$ in $]a, b[$ for which $f'(x) = \infty$ has measure zero. Let $\beta$ be an arbitrary positive number. For each $x \in F$, there exist arbitrarily small positive numbers $h$ such that $[x, x + h] \subseteq ]a, b[$ and

$$f(x + h) - f(x) > \beta h.$$

By VITALI's theorem (17.11), there exists a countable pairwise disjoint family $\{[x_n, x_n + h_n]\}$ of these intervals such that

$$\lambda(F \cap \bigcup_n [x_n, x_n + h_n])' = 0.$$

From this fact and (8) we obtain

$$\beta \lambda(F) \leq \beta \sum_n h_n < \sum_n \left( f(x_n + h_n) - f(x_n) \right) \leq f(b) - f(a).$$

Thus

$$\beta \lambda(F) < f(b) - f(a) \quad \text{for all} \quad \beta \in R,$$

which implies that $\lambda(F) = 0$. $\square$

(17.13) Question. Suppose that $\lambda(A) = 0, A \subseteq [a, b]$. Is it possible to find

Proof. Write $f(x) = V_a^x f - (V_a^x f - f(x))$, where we define $V_a^a f = 0$. Evidently the function $x \rightarrow V_a^x f$ is nondecreasing. The function

$$x \rightarrow V_a^x f - f(x)$$

is also nondecreasing, for if $x' > x$, then

$$V_a^x f - f(x') - (V_a^x f - f(x)) = V_x^x f - (f(x') - f(x)) \geq 0.$$
