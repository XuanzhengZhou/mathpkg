---
role: proof
locale: en
of_concept: inclusion-exclusion-theorem-general
source_book: gtm095
source_chapter: "1"
source_section: "14"
---

# Proof of the Inclusion–Exclusion Theorem (General Form)

**Theorem (Inclusion–Exclusion, General Form).** Let $\Omega$ be a finite set and $A_1, A_2, \dots, A_n$ be subsets of $\Omega$. Set $T = \{1, 2, \dots, n\}$ and denote by $N(D)$ the cardinality of a set $D$. Then the following relations hold:

**(a) Union formula:**

$$N\!\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{\varnothing \neq S \subseteq T} (-1)^{|S|+1} \, N\!\left(\bigcap_{i \in S} A_i\right). \tag{8}$$

**(b) Intersection via unions:**

$$N\!\left(\bigcap_{i=1}^{n} A_i\right) = \sum_{\varnothing \neq S \subseteq T} (-1)^{|S|+1} \, N\!\left(\bigcup_{i \in S} A_i\right). \tag{c}$$

**(c) Complement formulas:** For the events $\overline{A}_1, \dots, \overline{A}_n$,

$$N\!\left(\bigcup_{i=1}^{n} \overline{A}_i\right) = \sum_{S \subseteq T} (-1)^{|S|} \, N\!\left(\bigcap_{i \in S} A_i\right),$$

$$N\!\left(\bigcap_{i=1}^{n} \overline{A}_i\right) = \sum_{S \subseteq T} (-1)^{|S|} \, N\!\left(\bigcup_{i \in S} A_i\right),$$

with the convention $N(\bigcap_{i \in \varnothing} A_i) = N(\Omega)$ and $N(\bigcup_{i \in \varnothing} A_i) = 0$.

---

**Proof.** The key is to prove formula (8) for the union; all remaining formulas are obtained from it using De Morgan's laws,

$$\overline{\bigcup_{i} A_i} = \bigcap_{i} \overline{A}_i, \qquad \overline{\bigcap_{i} A_i} = \bigcup_{i} \overline{A}_i,$$

along with the identity $N(\overline{D}) = N(\Omega) - N(D)$.

We prove (8) using **indicator functions**. For each set $A \subseteq \Omega$, define its indicator $I_A : \Omega \to \{0, 1\}$ by

$$I_A(\omega) = \begin{cases} 1, & \omega \in A, \\ 0, & \omega \notin A. \end{cases}$$

Two fundamental properties of indicators are used:

1. **Intersection to product:** $I_{A \cap B}(\omega) = I_A(\omega) \cdot I_B(\omega)$, and more generally $\prod_{i \in S} I_{A_i} = I_{\bigcap_{i \in S} A_i}$.

2. **Complement:** $I_{\overline{A}}(\omega) = 1 - I_A(\omega)$.

Let $B = \bigcup_{i=1}^{n} A_i$. Then $\overline{B} = \bigcap_{i=1}^{n} \overline{A}_i$, and

$$I_B = 1 - I_{\overline{B}} = 1 - \prod_{i=1}^{n} I_{\overline{A}_i} = 1 - \prod_{i=1}^{n} (1 - I_{A_i}).$$

Expand the product $\prod_{i=1}^{n} (1 - I_{A_i})$:

$$\prod_{i=1}^{n} (1 - I_{A_i}) = 1 - \sum_{i} I_{A_i} + \sum_{i < j} I_{A_i} I_{A_j} - \sum_{i < j < k} I_{A_i} I_{A_j} I_{A_k} + \cdots + (-1)^n \prod_{i=1}^{n} I_{A_i}.$$

Hence

$$I_B = 1 - \left[\, 1 - \sum_{i} I_{A_i} + \sum_{i < j} I_{A_i} I_{A_j} - \cdots + (-1)^n \prod_{i=1}^{n} I_{A_i} \right]$$

$$= \sum_{i} I_{A_i} - \sum_{i < j} I_{A_i} I_{A_j} + \sum_{i < j < k} I_{A_i} I_{A_j} I_{A_k} - \cdots + (-1)^{n+1} \prod_{i=1}^{n} I_{A_i}.$$

For any $S \subseteq T = \{1, \dots, n\}$ with $|S| = m$, the product $\prod_{i \in S} I_{A_i}$ is precisely $I_{\bigcap_{i \in S} A_i}$. Summing $I_B$ over all $\omega \in \Omega$ and using $\sum_{\omega} I_D(\omega) = N(D)$ for any set $D$, we obtain

$$N\!\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{i} N(A_i) - \sum_{i < j} N(A_i \cap A_j) + \sum_{i < j < k} N(A_i \cap A_j \cap A_k) - \cdots + (-1)^{n+1} N(A_1 \cap \cdots \cap A_n),$$

which is precisely formula (8). The other formulas follow by algebraic manipulation using De Morgan's laws. $\square$

**Remark.** Each summation $\sum_{1 \leq i_1 < \cdots < i_m \leq n}$ runs over all $\binom{n}{m}$ unordered $m$-subsets of $\{1, 2, \dots, n\}$.
