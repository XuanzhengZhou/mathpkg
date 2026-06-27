---
role: proof
locale: en
of_concept: theorem-11-5
source_book: gtm008
source_chapter: "11"
source_section: "11 The Independence of"
---
$S \subseteq P$ is dense iff $\pi“S$ is dense. Therefore

$$S \cap \pi“G \neq 0 \leftrightarrow \pi^{-1}(S) \cap G \neq 0.$$

Thus $\pi“G$ is $P$-generic over $M$. The ultrafilter corresponding to $\pi“G$ is

$$\{b \in B \mid b \cap \pi“G \neq 0\} = \{b \in B \mid \pi^{-1}(b) \cap G \neq 0\}$$
$$= \{b \in B \mid \tilde{\pi}^{-1}(b) \in F\}$$
$$= \tilde{\pi}“F.$$

Finally

$$b \in \tilde{\pi}“F \leftrightarrow \tilde{\pi}^{-1}(b) \in F$$
$$\le

Remark. Let $P$ be the partial order structure of Definition 11.1 and used for the proof of the independence of $V = L$. For $k \subseteq \omega$ with $\bar{k} < \omega$ we define an automorphism $\pi_k$ of $P$ as follows:

$$\pi_k(\langle p_1, p_2 \rangle) = \langle q_1, q_2 \rangle \quad \text{where} \quad q_1 = (p_1 - k) \cup (p_2 \cap k)$$
$$q_2 = (p_2 - k) \cup (p_1 \cap k).$$

Obviously $\pi_k \in M$. We then obtain the following strengthening of Theorem 11.3.
