---
role: proof
locale: en
of_concept: tarski-undefinability-theorem
source_book: gtm053
source_chapter: "I"
source_section: "11"
---

The proof is modeled on the proof of Theorem 9.5 for the language SELF. Suppose, for contradiction, that there exists a formula $P(x)$ in SAr with one free variable $x$ such that an expression $Q$ satisfies $P$ if and only if $Q$ is a true formula of SAr.

Consider the formula $\neg P_E(x)$, where $P_E(x) = P(x \cdot 10^x)$ as in the Display Lemma (11.3). Let $k$ be the number of the expression $\neg P_E(x)$, and let $Q_0$ be the expression $\neg P_E(\bar{k})$. This is a closed formula of SAr.

Since $\neg P_E(\bar{k})$ is a closed formula, it is either true or false by the standard interpretation of SAr.

**Case 1:** $\neg P_E(\bar{k})$ is true. Then its number $n(Q_0)$ satisfies $\neg P_E$, so $\neg P_E(\overline{n(Q_0)})$ is true. But $n(Q_0) = k$, since $Q_0$ is exactly $\neg P_E(\bar{k})$ and $k$ is the number of $\neg P_E(x)$ (or equivalently the number of the expression obtained by substituting $\bar{k}$ into $\neg P_E(x)$). Thus $\neg P_E(\bar{k})$ is true, which is consistent. However, by the Display Lemma, an expression satisfies $\neg P_E$ if and only if its display satisfies $\neg P$. This means the display of $\neg P_E(\bar{k})$ satisfies $\neg P$, so the display of $Q_0$ is not a true formula. But this contradicts the definition of $P$ as the truth predicate (since the display of $Q_0$ would be a true formula satisfying $P$).

**Case 2:** $\neg P_E(\bar{k})$ is false. Then $P_E(\bar{k})$ is true, so $n(Q_0) = k$ satisfies $P_E$, meaning the display of $Q_0$ satisfies $P$, i.e., the display of $Q_0$ is a true formula. But since $P$ is supposed to define truth, this means $\neg P$ is not satisfied by the display of $Q_0$, which would require $P_E(\bar{k})$ to be false — a contradiction.

Both cases lead to contradiction. Therefore, no such formula $P(x)$ can exist.

For the general case of $?Ar$, the numbering is modified: if $m$ is the number of elements in the alphabet and $v(\bar{1}) = m$, then the numbering is

$$n(a_1 \cdots a_k) = \sum_{i=1}^{k} v(a_i)(m+1)^{k-i} + 1.$$

Under this numbering, $n(Q * Q*) = n(Q)(m+1)^{n(Q)}$, and defining $P_E(x)$ as $P(x \cdot ((m+1) \uparrow x))$ yields the same diagonalization, proving the theorem for $?Ar$ without further alterations.
