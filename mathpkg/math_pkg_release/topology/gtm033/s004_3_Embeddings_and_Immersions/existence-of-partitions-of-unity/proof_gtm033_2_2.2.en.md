---
role: proof
locale: en
of_concept: existence-of-partitions-of-unity
source_book: gtm033
source_chapter: "2. Function Spaces"
source_section: "2.2"
---

# Proof of Existence of Partitions of Unity

**Theorem.** Let $M$ be a $C^r$ paracompact manifold, $0 \leqslant r \leqslant \infty$. Then every open cover of $M$ admits a subordinate $C^r$ partition of unity.

*Proof.* The proof proceeds in several steps. First we construct a $C^\infty$ bump function on $\mathbb{R}^n$, then use it to build a partition of unity on $M$.

**Step 1: Smooth bump functions on $\mathbb{R}^n$.** Start with the $C^\infty$ map $\alpha: \mathbb{R} \to \mathbb{R}$ defined by

$$\alpha(x) = \begin{cases} 0 & \text{if } x \leqslant 0 \\ e^{-1/x} & \text{if } x > 0. \end{cases}$$

Next define $\beta: \mathbb{R} \to \mathbb{R}$ by

$$\beta(x) = \alpha(x - a)\alpha(b - x),$$

which is positive on $(a,b)$ and zero outside. Then define $\gamma: \mathbb{R} \to [0,1]$ by

$$\gamma(x) = \frac{\int_x^b \beta}{\int_a^b \beta},$$

so that $\gamma$ decreases smoothly from $1$ at $a$ to $0$ at $b$. Finally define $\lambda: \mathbb{R}^n \to [0,1]$ by

$$\lambda(x) = \gamma(|x|),$$

which equals $1$ on a neighborhood of $0$ and vanishes outside a compact set.

Using translations and dilations, we can construct for any open ball $B \subset \mathbb{R}^n$ a $C^\infty$ function that is positive on $B$ and zero outside $\bar{B}$.

**Step 2: Reduction to a locally finite refinement.** Let $\mathcal{U} = \{U_i\}_{i \in \Lambda}$ be an open cover of $M$. Since $M$ is paracompact, there exists a locally finite refinement $\mathcal{V} = \{V_\alpha\}_{\alpha \in A}$. If $\mathcal{V}$ has a subordinate $C^r$ partition of unity, then so does $\mathcal{U}$ (by summing the functions corresponding to the same original index). Thus it suffices to construct a partition of unity subordinate to a locally finite open cover.

**Step 3: Construction subordinate to a locally finite cover.** Let $\mathcal{V} = \{V_\alpha\}_{\alpha \in A}$ be a locally finite open cover of $M$. By paracompactness we can find a shrinking $\mathcal{W} = \{W_\alpha\}_{\alpha \in A}$ whose closures $\bar{W}_\alpha$ are compact and satisfy $\bar{W}_\alpha \subset V_\alpha$.

For each $\alpha \in A$, take a chart $(\varphi_\alpha, V_\alpha)$ (after possibly refining so each $V_\alpha$ is a coordinate domain). Identify $V_\alpha$ with an open subset of $\mathbb{R}^n$ via $\varphi_\alpha$. Since $\bar{W}_\alpha$ is compact in $V_\alpha$, we can cover $\varphi_\alpha(\bar{W}_\alpha)$ by finitely many coordinate balls $B(\alpha,1), \ldots, B(\alpha,k(\alpha))$ whose closures lie in $\varphi_\alpha(V_\alpha)$.

For each such ball, construct a $C^\infty$ function $\lambda_{\alpha,j}: \mathbb{R}^n \to [0,\infty)$ (using Step 1) such that

$$\lambda_{\alpha,j}(x) > 0 \quad \text{if and only if} \quad x \in \operatorname{Int} B(\alpha,j).$$

Put

$$\lambda_\alpha = \sum_{j=1}^{k(\alpha)} \lambda_{\alpha,j} : \mathbb{R}^n \to [0,\infty).$$

Then

$$\lambda_\alpha(x) > 0 \quad \text{if} \quad x \in \varphi_\alpha(\bar{W}_\alpha),$$

$$\lambda_\alpha(x) = 0 \quad \text{if} \quad x \in \mathbb{R}^n - \bigcup_j B(\alpha,j).$$

Now define $\mu_\alpha: M \to [0,\infty)$ by

$$\mu_\alpha(x) = \begin{cases} \lambda_\alpha(\varphi_\alpha(x)) & \text{if } x \in V_\alpha \\ 0 & \text{if } x \in M - V_\alpha. \end{cases}$$

Then $\mu_\alpha$ is $C^r$, $\mu_\alpha > 0$ on $\bar{W}_\alpha$, and $\operatorname{Supp} \mu_\alpha \subset V_\alpha$.

**Step 4: Normalization.** Since $\{\bar{W}_\alpha\}_{\alpha \in A}$ covers $M$, the sum $\sum_{\alpha \in A} \mu_\alpha$ is strictly positive everywhere on $M$. (Local finiteness of $\mathcal{V}$ ensures the sum is locally finite, hence well-defined.) Define

$$v_\alpha = \frac{\mu_\alpha}{\sum_{\beta \in A} \mu_\beta}.$$

Then $\{v_\alpha\}_{\alpha \in A}$ is a $C^r$ partition of unity subordinate to $\mathcal{V}$, with

$$\operatorname{Supp} v_\alpha \subset V_\alpha \quad (\alpha \in A),$$

$$\{\operatorname{Supp} v_\alpha\}_{\alpha \in A} \text{ is locally finite},$$

$$\sum_{\alpha \in A} v_\alpha(x) = 1 \quad (x \in M).$$

$\square$

**Remark.** A partition of unity is used to glue together locally defined maps into $\mathbb{R}^n$ to make a globally defined map. For instance, if $\{\lambda_i\}_{i \in A}$ is a $C^s$ partition of unity subordinate to an open cover $\{U_i\}_{i \in A}$ of $M$, and $g_i: U_i \to \mathbb{R}^n$ is $C^s$ for each $i$, we can define $g: M \to \mathbb{R}^n$ by

$$g(x) = \sum_{i \in A} \lambda_i(x) g_i(x),$$

summed over $\{i \in A : x \in U_i\}$. This is a well-defined $C^s$ map.
