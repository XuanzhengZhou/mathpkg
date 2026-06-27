---
role: proof
locale: en
of_concept: von-neumann-bicommutant-theorem
source_book: gtm015
source_chapter: "10"
source_section: "68"
---

# Proof of Von Neumann bicommutant theorem

Proof. {The hypothesis on the $*$-algebra $A$ is that the intersection of the null spaces of the operators in $A$ is $\{\theta\}$; equivalently, the closed linear span of the ranges of the operators in $A$ is $H$ (cf. (43.14), (42.17)).}

Since $A''$ is ultrastrongly closed (68.12), it contains the ultrastrong closure of $A$. Conversely, assuming $B \in A''$ it is to be shown that $B$ is ultrastrongly adherent to $A$. Thus, given a basic neighborhood $V$ of $B$ for the ultrastrong topology, we must show that $V \cap A \neq \emptyset$.

Let $K$ be the orthogonal sum of $\aleph_0$ copies of $H$, with notations as in (68.10) and (68.18). By (68.13) we can suppose that, for a suitable vector $x = (x_i)$ in $K$,

$$V = \{T \in \mathcal{L}(H) : \sum_{i=1}^{\infty} \|T x_i - B x_i\|^2 \leq 1\} = \{T \in \mathcal{L}(H) : \|\tilde{T}x - \tilde{B}x\| \leq 1\};$$

thus, we seek an operator $A \in A$ such that $\|\tilde{A}x - \tilde{B}x\| \leq 1$.

Let $M = \{\tilde{A}x : A \in A\}$; $M$ is a linear subspace of $K$, whose closure we denote by $N$. In essence, we are trying to approximate $\tilde{B}x$ by vectors in $M$: it will clearly suffice to show that $\tilde{B}x \in N$. This will be accomplished by showing (in reverse order) that (i) $x \in N$, and (ii) $\tilde{B}(N) \subset N$.

(ii) For all $A \in A$, obviously $\tilde{A}(M) \subset M$, therefore $\tilde{A}(N) \subset N$ by continuity. Thus if $P$ denotes the projection operator on $K$ with range $N$ (42.17), then $\tilde{A} P = P \tilde{A} P$ for all $A \in A$. Taking adjoints, $P \tilde{A}^* = P \tilde{A}^* P$; since $A$ is a $*$-algebra, we have $\tilde{A} \in \tilde{A}$ implies $\tilde{A}^* \in \tilde{A}$, so $P \tilde{A} = P \tilde{A} P$ as well. Thus $\tilde{A} P = P \tilde{A}$ for all $A \in A$. By the matrix commutation lemma (68.19), it follows that $A P_{ij} = P_{ij} A$ for all $A \in A$ and all $i, j$, i.e., $P_{ij} \in A'$ for all $i, j$. Since $B \in A''$, we have $B P_{ij} = P_{ij} B$ for all $i, j$, and another application of (68.19) yields $\tilde{B} P = P \tilde{B}$. Consequently $\tilde{B}(N) = \tilde{B} P(K) = P \tilde{B}(K) \subset N$.

(i) Since $A$ is nondegenerate, the intersection of the null spaces of the operators in $A$ is $\{\theta\}$, which implies that the only vector orthogonal to all $\tilde{A}x$ ($A \in A$) is $\theta$. In other words, the orthogonal complement of $M$ in $K$ is $\{\theta\}$, so $N = K$. In particular $x \in N$.

Thus $\tilde{B}x \in N$, which means $\tilde{B}x$ can be approximated by vectors $\tilde{A}x$ with $A \in A$. Hence $B$ belongs to the ultrastrong closure of $A$. Since $A''$ is ultrastrongly closed and contains $A$, we have shown that $A''$ equals the ultrastrong closure of $A$.
