---
role: proof
locale: en
of_concept: inclusion-exclusion-principle
source_book: gtm095
source_chapter: "1"
source_section: "14"
---

# Proof of the Inclusion–Exclusion Principle

**Theorem (Inclusion–Exclusion Principle).** Let $\Omega$ be a finite set and $A_1, A_2, \dots, A_n \subseteq \Omega$. Denote $T = \{1, 2, \dots, n\}$. Then the following formulas hold:

**(a) Cardinality of the union:**

$$N\!\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{\varnothing \neq S \subseteq T} (-1)^{|S|+1} \, N\!\left(\bigcap_{i \in S} A_i\right). \tag{8}$$

Equivalently,

$$N(A_1 \cup \cdots \cup A_n) = \sum_{i} N(A_i) - \sum_{i < j} N(A_i \cap A_j) + \sum_{i < j < k} N(A_i \cap A_j \cap A_k) - \cdots + (-1)^{n+1} N(A_1 \cap \cdots \cap A_n). \tag{9}$$

**(b) Cardinality of the complement of the union (elements belonging to none of the $A_i$):**

$$N(\overline{A}_1 \cap \cdots \cap \overline{A}_n) = N(\Omega) - N(A_1 \cup \cdots \cup A_n). \tag{10}$$

**(c) Cardinality with complement sets:**

$$N\!\left(\bigcap_{i=1}^{n} \overline{A}_i\right) = \sum_{S \subseteq T} (-1)^{|S|} \, N\!\left(\bigcap_{i \in S} A_i\right), \tag{11}$$

with the convention $N(\bigcap_{i \in \varnothing} A_i) = N(\Omega)$.

---

**Proof.** It suffices to prove formula (8); all other formulas follow from it by applying De Morgan's laws

$$\overline{A_1 \cup \cdots \cup A_n} = \overline{A}_1 \cap \cdots \cap \overline{A}_n, \qquad \overline{A_1 \cap \cdots \cap A_n} = \overline{A}_1 \cup \cdots \cup \overline{A}_n,$$

and substituting events by their complements.

The proof of (8) can be carried out by induction on $n$ (see Problem 1). However, a more elegant proof relies on the properties of **indicator functions** (also called indicator random variables).

Define the indicator of a set $A \subseteq \Omega$ as:

$$I_A(\omega) = \begin{cases} 1, & \omega \in A, \\ 0, & \omega \notin A. \end{cases}$$

For the union $B = A_1 \cup \cdots \cup A_n$, its complement is

$$\overline{B} = \overline{A}_1 \cap \cdots \cap \overline{A}_n.$$

Hence

$$I_B = 1 - I_{\overline{B}} = 1 - I_{\overline{A}_1 \cap \cdots \cap \overline{A}_n}.$$

Since the indicator of an intersection equals the product of indicators (an element belongs to the intersection iff it belongs to every component),

$$I_{\overline{A}_1 \cap \cdots \cap \overline{A}_n}(\omega) = \prod_{i=1}^{n} I_{\overline{A}_i}(\omega) = \prod_{i=1}^{n} \bigl(1 - I_{A_i}(\omega)\bigr).$$

Therefore,

$$I_{A_1 \cup \cdots \cup A_n}(\omega) = 1 - \prod_{i=1}^{n} \bigl(1 - I_{A_i}(\omega)\bigr).$$

Now expand the product:

$$\prod_{i=1}^{n} (1 - I_{A_i}) = 1 - \sum_{i=1}^{n} I_{A_i} + \sum_{1 \leq i < j \leq n} I_{A_i} I_{A_j} - \sum_{1 \leq i < j < k \leq n} I_{A_i} I_{A_j} I_{A_k} + \cdots + (-1)^n I_{A_1} I_{A_2} \cdots I_{A_n}.$$

Substituting back,

$$I_{A_1 \cup \cdots \cup A_n} = \sum_{i=1}^{n} I_{A_i} - \sum_{1 \leq i < j \leq n} I_{A_i} I_{A_j} + \sum_{1 \leq i < j < k \leq n} I_{A_i} I_{A_j} I_{A_k} - \cdots + (-1)^{n+1} I_{A_1} I_{A_2} \cdots I_{A_n}.$$

Observe that $I_{A_i}(\omega) I_{A_j}(\omega) = I_{A_i \cap A_j}(\omega)$, and more generally for any $S \subseteq T$,

$$\prod_{i \in S} I_{A_i}(\omega) = I_{\bigcap_{i \in S} A_i}(\omega).$$

Now sum both sides over all $\omega \in \Omega$. For any set $D$, $\sum_{\omega \in \Omega} I_D(\omega) = N(D)$. Thus:

$$\sum_{\omega \in \Omega} I_{A_1 \cup \cdots \cup A_n}(\omega) = N\!\left(\bigcup_{i=1}^{n} A_i\right),$$

$$\sum_{\omega \in \Omega} \left(\sum_{i=1}^{n} I_{A_i}(\omega)\right) = \sum_{i=1}^{n} N(A_i),$$

$$\sum_{\omega \in \Omega} \left(\sum_{1 \leq i < j \leq n} I_{A_i}(\omega) I_{A_j}(\omega)\right) = \sum_{1 \leq i < j \leq n} N(A_i \cap A_j),$$

and similarly for higher-order intersections. Collecting terms, we arrive at formula (8):

$$N\!\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{i=1}^{n} N(A_i) - \sum_{1 \leq i < j \leq n} N(A_i \cap A_j) + \sum_{1 \leq i < j < k \leq n} N(A_i \cap A_j \cap A_k) - \cdots + (-1)^{n+1} N(A_1 \cap \cdots \cap A_n).$$

This completes the proof. $\square$

**Remark.** The summation $\sum_{1 \leq i_1 < \cdots < i_m \leq n}$ extends over all unordered subsets of cardinality $m$ of the set $\{1, 2, \dots, n\}$. The number of such subsets is $\binom{n}{m} = C_n^m$.
