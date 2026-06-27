---
role: proof
locale: en
of_concept: existence-of-m-saturated-structures
source_book: gtm037
source_chapter: "28"
source_section: "4. Model Theory"
---

The assumptions of the theorem imply that $|T| \leq n$, and obviously $T \neq 0$. Hence we may write $T = \{(B_\beta, \Delta_\alpha) : \alpha < n\}$. For each $\alpha < n$ we define a function $f_\alpha$ with domain $S$:

$$f_\alpha(\Theta) = \Theta \cup \{\varphi(c) : \varphi \in \Delta_\alpha\}$$

if this set is in $S$, where $c$ is the first member of $C$ not in $B_\alpha$ or in any sentence of $\Theta$;

$$f_\alpha(\Theta) = \Theta \quad \text{otherwise.}$$

Obviously $f_\alpha$ is admissible over $S$.

By the model existence theorem, since $\Gamma' \in S$, let $(\mathfrak{A}, a_c)_{c \in C}$ be a model of $\Gamma'$ such that $A = \{a_c : c \in C\}$, hence $|A| \leq n$, and:

\begin{equation}
\text{if } \alpha < n, \text{ then there is a } \Theta \in S \text{ such that } \Gamma' \subseteq f_\alpha(\Theta) \subseteq \{\varphi : (\mathfrak{A}, a_c)_{c \in C} \models \varphi\}.
\end{equation}

To show that $\mathfrak{A} \upharpoonright \mathcal{L}$ is $m$-saturated, let $B \subseteq C$ with $|B| < m$, and let $\Delta \subseteq \mathrm{Fmla}^1_{\mathcal{L}_B}$ be such that $(\mathfrak{A} \upharpoonright \mathcal{L}, a_c)_{c \in B} \models \exists v_0 \bigwedge \Delta'$ for each finite subset $\Delta'$ of $\Delta$. Thus $\Delta$ is consistent over $\mathrm{Th}((\mathfrak{A} \upharpoonright \mathcal{L}, a_c)_{c \in B})$, so we can extend $\Delta$ to a $1$-type $\Delta^*$ over $\mathrm{Th}((\mathfrak{A} \upharpoonright \mathcal{L}, a_c)_{c \in B})$. By condition (vi), this $1$-type is among the at most $n$ types enumerated. The construction using $f_\alpha$ then guarantees that $\Delta^*$ is realized in $(\mathfrak{A}, a_c)_{c \in C}$, and hence $\Delta$ is realized in $(\mathfrak{A} \upharpoonright \mathcal{L}, a_c)_{c \in B}$. This establishes that $\mathfrak{A} \upharpoonright \mathcal{L}$ is $m$-saturated.
