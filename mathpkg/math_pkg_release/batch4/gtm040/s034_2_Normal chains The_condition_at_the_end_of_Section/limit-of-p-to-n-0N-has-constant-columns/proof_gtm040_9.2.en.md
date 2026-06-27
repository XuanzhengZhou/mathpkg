---
role: proof
locale: en
of_concept: limit-of-p-to-n-0N-has-constant-columns
source_book: gtm040
source_chapter: "9"
source_section: "2"
---

Fix a state $j$ and define
$$f_k = \begin{cases} \alpha_j / \alpha_0 & \text{for } k = 0 \\ -1 & \text{for } k = j \\ 0 & \text{otherwise.} \end{cases}$$

Since $\alpha f = 0$, the identity $(I - P){}^0N f = f$ holds (by properties of the fundamental matrix). Hence
$$\begin{aligned}
\lim_n \big[(I + P + \cdots + P^{n-1})f\big]_i
&= \lim_n \big[(I + P + \cdots + P^{n-1})(I - P){}^0N f\big]_i \\
&= \lim_n \big[(I - P^n){}^0N f\big]_i \\
&= ({}^0N f)_i + \lim_n (P^n {}^0N)_{ij}.
\end{aligned}$$

This limit exists for some $i$ by hypothesis. Therefore, by Theorem 9-15, $f$ is a charge and $\lim_n (P^n {}^0N)_{kj}$ exists for all $k$. Since $j$ was arbitrary, the matrix limit $\lim_n (P^n {}^0N)$ exists for all entries. The limit matrix has the form $1 \cdot \nu$ for some row vector $\nu$, establishing that the columns are constant. Finiteness of the entries follows from the boundedness of the quantities involved.
