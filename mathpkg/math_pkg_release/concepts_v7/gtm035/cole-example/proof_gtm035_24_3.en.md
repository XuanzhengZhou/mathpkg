---
role: proof
locale: en
of_concept: cole-example
source_book: gtm035
source_chapter: "24"
source_section: "24.3"
---
# Proof of Cole Example of Polynomial Hull

**Theorem 24.3 (Cole).** There exists a compact subset $Y$ of $\mathbb{C}^2$ with the projection $\pi(z, w) = z$ onto the closed unit disk $\{|z| \leq 1/2\}$ such that:

1. $\pi(Y) = \{|z| \leq 1/2\}$,
2. $\hat{Y} \setminus Y$ is nonempty,
3. $\hat{Y}$ contains no analytic disk.

**Proof.** The construction proceeds in several steps.

---

**Step 1: Construction of $X$ via polynomial sequences (Lemma 24.4).**

Let $\{a_j\}_{j=1}^{\infty}$ be a countable dense subset of $\{z \in \mathbb{C} : |z| \leq 1/2\}$. By Lemma 24.4, there exist positive constants $c_j$, $\epsilon_j$ and a sequence of polynomials $P_n(z, w)$ such that $c_1 = 1/10$, $c_{j+1} \leq (1/10)c_j$, and:

1. $\{P_n = 0\} = \Sigma(c_1, c_2, \ldots, c_n)$,
2. $\{|P_n| \leq \epsilon_n\} \subseteq \{|P_{n-1}| \leq \epsilon_{n-1}\}$,
3. If $|a| \leq 1/2$ and $|P_n(a, w)| \leq \epsilon_n$, then $\exists w_n$ with $P_n(a, w_n) = 0$ and $|w - w_n| < 1/n$.

Define
$$X = \bigcap_{n=1}^{\infty} \{|P_n(z, w)| \leq \epsilon_n\}.$$
It follows that $X$ is a compact, polynomially convex subset of $\{|z| \leq 1/2\} \subseteq \mathbb{C}^2$.

For each $n$, put
$$\Sigma_n = \{P_n = 0\} = \Sigma(c_1, \ldots, c_n).$$
These are the "Cole varieties" over the disk $\{|z| \leq 1/2\}$. Each $\Sigma_n$ is a one-dimensional algebraic variety given as the zero set of $P_n$.

---

**Step 2: Definition of branch functions.**

For each $j$, define
$$B_j(z) = (z - a_1) \cdots (z - a_{j-1}) \sqrt{z - a_j}.$$
Let $\gamma$ be a suitable closed curve (a rectangle) in the $z$-plane. Let $z_1$ be the midpoint of the left-hand edge of $\gamma$, $z_0$ the midpoint of the right-hand edge, and $\gamma_1 = \gamma \setminus \{z_1\}$.

Each $B_j$ has two single-valued continuous branches on $\gamma_1$. If $a_j$ lies outside $\gamma$, each branch extends continuously to $\gamma$; if $a_j$ lies inside $\gamma$, each branch has a jump at $z_1$. Choose one branch arbitrarily and denote it $\beta_j$. Then $|\beta_j|$ is single-valued and nonvanishing on $\gamma$.

Let $n$ be the smallest index with $a_n$ inside $\gamma$, and let $c_1, \ldots, c_n$ be as in Lemma 24.4. The algebraic function $\sum_{j=1}^{n} c_j B_j$ has $2^n$ branches on $\gamma_1$:

$$\sum_{j=1}^{n} c_j \rho_j \beta_j, \quad \rho_j = \pm 1.$$

Define $\mathcal{K}$ to be the collection of all $2^n$ such functions.

---

**Step 3: Key inequalities.**

**Claim 1.** Fix $z \in \gamma_1$. There exists $k \in \mathcal{K}$ such that
$$|f(z) - k(z)| \leq \frac{1}{4} |\beta_n(z)| c_n.$$
*Proof.* Since $(z, f(z)) \in X$, by Lemma 24.5 there exists $N$ large and $w_N$ such that $f(z)$ is approximated. Using the geometric decay of the $c_j$ ($c_{j+1} \leq c_j/10$), one estimates
$$\sum_{j=n+1}^{N} c_j |\beta_j(z)| \leq \frac{1}{9} |\beta_n(z)| c_n.$$
This together with the approximation from Lemma 24.5 yields the bound. $\square$

**Claim 2.** For distinct $g, h \in \mathcal{K}$,
$$|g(z) - h(z)| \geq \frac{3}{2} |\beta_n(z)| c_n.$$
*Proof.* Write $g = \sum c_j \rho_j \beta_j$, $h = \sum c_j \rho_j' \beta_j$. Let $j_0$ be the first index where $\rho_j \neq \rho_j'$. Then
$$g(z) - h(z) = \pm 2c_{j_0} \beta_{j_0}(z) + \sum_{j=j_0+1}^{n} c_j (\rho_j - \rho_j') \beta_j(z).$$
Hence
$$|g(z) - h(z)| \geq 2c_{j_0} |\beta_{j_0}(z)| - 2 \sum_{j=j_0+1}^{n} c_j |\beta_j(z)| \geq \frac{3}{2} |\beta_n(z)| c_n.$$
$\square$

---

**Step 4: Tracking a continuous section $f$.**

Suppose there exists a continuous function $f$ on $\gamma$ such that $(z, f(z)) \in X$ for all $z \in \gamma$. By Claim 1 and Claim 2, using a continuity/openness argument, there exists a unique $k_0 \in \mathcal{K}$ such that on all of $\gamma_1$:
$$|f(z) - k_0(z)| \leq \frac{1}{3} |\beta_n(z)| c_n.$$

Now consider limits as $z \to z_1$ along $\gamma_1$. Since $f$ is continuous at $z_1$, the jump of $k_0$ at $z_1$ must be at most $(2/3)|\beta_n(z_1)|c_n$. But by Claim 2, any two distinct branches in $\mathcal{K}$ differ by at least $(3/2)|\beta_n(z_1)|c_n$, so the jump of $k_0$ would be at least $(3/2)|\beta_n(z_1)|c_n$ — a contradiction.

Thus **no such continuous section $f$ exists** whenever some $a_j$ lies inside $\gamma$.

---

**Step 5: $X = \hat{Y}$ where $Y = X \cap \{|z| = 1/2\}$ and no analytic disk.**

Let $Y = X \cap \{|z| = 1/2\}$. We show $X = \hat{Y}$.

Since $X$ is polynomially convex, $\hat{Y} \subseteq X$. For the reverse, fix $(z, w) \in X$ and choose $(z, w_k) \in \Sigma_k$ converging to $(z, w)$. For any polynomial $Q$ on $\mathbb{C}^2$, by the maximum principle on $\Sigma_k$,
$$|Q(z, w_k)| \leq |Q(z_k', w_k')|, \quad (z_k', w_k') \in \Sigma_k \cap \{|z| = 1/2\}.$$
Let $(z^*, w^*)$ be an accumulation point. Using the nesting property $\{|P_k| \leq \epsilon_k\} \subseteq \{|P_{n_0}| \leq \epsilon_{n_0}\}$ for $k > n_0$, we get $(z^*, w^*) \in X$ with $|z^*| = 1/2$, i.e., $(z^*, w^*) \in Y$. Hence $|Q(z, w)| \leq \max_Y |Q|$, so $(z, w) \in \hat{Y}$.

Thus $X = \hat{Y}$, and by Lemmas 24.7, 24.8, and 24.9, $\hat{Y}$ contains **no analytic disk**. Moreover, $\pi(Y) = \{|z| = 1/2\}$, a proper subset of the full disk. The fibers $\pi^{-1}(z)$ for $|z| = 1/2$ consist of points approximable from $\Sigma_n$.

---

**Conclusion.** $Y \subseteq X = \hat{Y}$ but $\hat{Y} \setminus Y = X \cap \{|z| < 1/2\}$ is nonempty (it contains points over interior $z$). Yet $\hat{Y}$ contains no analytic disk. This is the Cole example. $\square$
