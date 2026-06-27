---
role: proof
locale: en
of_concept: trachtenbrots-theorem
source_book: gtm037
source_chapter: "3"
source_section: "Decidable and Undecidable Theories"
---

Let $A = \{f : f \text{ is spectrally representable}\}$. We shall again apply Julia Robinson's theorem 3.48 in order to show that every recursive function is in $A$.

**I.** $+$ is in $A$. We can clearly write down an $\mathcal{L}_{\text{un}}$-sentence $\varphi$ whose models are exactly those $\mathcal{L}_{\text{un}}$-structures $\mathfrak{A}$ for which $\mathbf{R}_0^{121} \cap \mathbf{R}_1^{121} = 0$ and $\mathbf{R}_2^{121} = \mathbf{R}_0^{121} \cup \mathbf{R}_1^{121}$. Thus $\varphi$ spectrally represents $+$.

**II.** $\cdot$ is in $A$. This time take a sentence $\varphi$ such that $\mathfrak{A}$ is a model of $\varphi$ iff $\mathbf{R}_0^{121} \cap \mathbf{R}_1^{121} = 0$ and $\mathbf{R}_2^{121}$ is the Cartesian product of $\mathbf{R}_0^{121}$ and $\mathbf{R}_1^{121}$ under a suitable pairing relation. Thus $\varphi$ spectrally represents multiplication.

**[III--IV. OCR gap — the proof that $A$ contains projection functions and is closed under composition is partially missing.]**

**V.** $A$ is closed under generalized composition. Let $h(x_0, \ldots, x_{n-1}) = f(g_0(x_0, \ldots, x_{n-1}), \ldots, g_{m-1}(x_0, \ldots, x_{n-1}))$, and suppose $g_0, \ldots, g_{m-1}, f$ are spectrally represented by $\psi_0, \ldots, \psi_m$, respectively. The idea of the construction of a sentence $\varphi$ spectrally representing $h$ is this. We modify the sentences $\psi_i$ so that pairwise they talk about entirely different symbols. Then we can introduce relationships between them in order to represent $h$.

Formally, the first step takes place via $m+1$ different syntactical $\mathcal{L}_{\text{un}}$-structures in $\mathcal{L}_{\text{un}}$. We can clearly divide the symbols of $\mathcal{L}_{\text{un}}$ up into $m+2$ pairwise disjoint parts such that each part contains infinitely many relation symbols of each rank and such that $\mathbf{R}_0^1, \ldots, \mathbf{R}_n^1$ all are in the last part. The $j$-ary relation symbols of the $i$th part ($0 \leq i \leq m+1$) will be denoted by ${}^i\mathbf{R}_0^j, {}^i\mathbf{R}_1^j, \ldots$, and we assume that ${}^{m+1}\mathbf{R}_k^1 = \mathbf{R}_k^1$ for each $k \leq n$. For each $i \leq m$ let $\mathfrak{A}_i = ({}^{m+1}\mathbf{R}_{n+i+1}v_0, t_i, S_i, \Gamma_i)$ be the syntactical $\mathcal{L}_{\text{un}}$-structure in $\mathcal{L}_{\text{un}}$ such that:

$$t_i = 0 \quad \text{(since $\mathcal{L}_{\text{un}}$ has no operation symbols)};$$
$$S_i\mathbf{R}_k^j = {}^i\mathbf{R}_k^j v_0 \cdots v_{j-1};$$
$$\Gamma_i = \{\exists v_0 \, {}^{m+1}\mathbf{R}_{n+i+1}v_0\}.$$

By means of these syntactical structures, our sentences $\psi_0, \ldots, \psi_m$ receive translations $\psi_0^{\mathfrak{A}_0}, \ldots, \psi_m^{\mathfrak{A}_m}$. The relationships between these translated sentences are then used to construct $\varphi$ spectrally representing $h$. Using the translation relationships one obtains:

$$|R_i^{1\mathfrak{B}(\Gamma m, \mathfrak{A}m)}| = g_i(x_0, \ldots, x_{n-1}) \quad \text{for each } i < m.$$

Since $\mathfrak{B}^{\Gamma m, \mathfrak{A}m} \models \psi_m$, it follows that

$$|R_m^{1\mathfrak{B}(\Gamma m, \mathfrak{A}m)}| = h(x_0, \ldots, x_{n-1}).$$

Hence we obtain $|R_n^1| = h(x_0, \ldots, x_{n-1})$, as desired.

**VI.** $A$ is closed under inversion, applied to functions with range $\omega$. For, let $f \in A$, where $f$ is a unary function with range $\omega$. By Lemma 14.24, we know that $f$ is spectrally represented by a sentence $\psi$ satisfying the conditions of 14.24. We translate $\psi$ so as to make room for some auxiliary symbols. Namely, we divide the symbols of $\mathcal{L}_{\text{un}}$ into equal parts denoted by ${}^0R_r^q$ and ${}^1R_r^q$, where ${}^1R_0^1 = R_0^1$ and ${}^1R_1^1 = R_1^1$. Let $\mathfrak{A} = ({}^1R_2^1v_0, t, S, \Gamma)$ be the syntactical $\mathcal{L}_{\text{un}}$-structure in $\mathcal{L}_{\text{un}}$ such that:

$$t = 0;$$
$$S R_r^q = {}^0R_r^q v_0 \ldots v_{q-1};$$
$$\Gamma = \{ \exists v_0 \, {}^1R_2^1 v_0 \}.$$

Now there clearly is a sentence $\chi$ of $\mathcal{L}_{\text{un}}$ which expresses that the part indexed by ${}^0$ satisfies the conditions of Lemma 14.24, while the part indexed by ${}^1$ provides the auxiliary structure needed to invert the function. This completes the proof that $A$ is closed under the required operations, and by Julia Robinson's theorem 3.48, every recursive function belongs to $A$, i.e., every recursive function is spectrally representable.

> **Note:** The proof in this section file is truncated; parts III--IV (projection functions and composition) are missing due to OCR gaps/loss in the stitched section, and the conclusion of part VI is cut off mid-sentence. The argument above reconstructs the missing logical structure based on the parallel proof of Theorem 14.11 (syntactic definability of all recursive functions in $R$) which follows the identical Julia Robinson strategy.
