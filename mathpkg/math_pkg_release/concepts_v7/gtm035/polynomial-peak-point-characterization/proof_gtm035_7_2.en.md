---
role: proof
locale: en
of_concept: polynomial-peak-point-characterization
source_book: gtm035
source_chapter: "Chapter 7"
source_section: "7.2"
---
# Proof of Characterization of Connected Complement via Polynomial Peak Points

**Proof.** If $\mathbb{C} \setminus K$ fails to be connected, we can choose $x^0$ in a bounded component of $\mathbb{C} \setminus K$ and note that (1) violates the maximum principle.

Assume that $\mathbb{C} \setminus K$ is connected. Fix $x^0 \in \mathbb{C} \setminus K$. Then $K \cup \{x^0\}$ is a set with connected complement. Choose points $x_n \to x^0$ and $x_n \neq x^0$. Then

$$f_n(z) = \frac{1}{z - x_n}$$

is holomorphic in a neighborhood of $K \cup \{x^0\}$. Hence by Theorem 7.1 we can find a polynomial $P_n$ with

$$\left|P_n(z) - \frac{1}{z - x_n}\right| < \frac{1}{n}, \quad \text{all } z \in K \cup \{x_0\}.$$

For large $n$, then, $P_n$ satisfies (1).
