---
role: proof
locale: en
of_concept: "let-and-be-measurable-spaces-and-let-then"
source_book: gtm025
source_chapter: "Hilbert Spaces and Spectral Theory"
source_section: "21.4"
---

To prove (i), let $\mathcal{S} = \{E \in \mathcal{M} \times \mathcal{N} : E_x \in \mathcal{N}$ for all $x \in X\}$. For any measurable rectangle $A \times B$ and any $x \in X$, we have

$$ (A \times B)_x = \begin{cases} B \text{ if } x \in A, \\ \emptyset \text{ if } x \notin A. \end{cases} $$

Thus $\mathcal{S}$ contains all measurable rectangles. To complete the proof of (i), we need only show that $\mathcal{S}$ is a $\sigma$-algebra. If $(E_n)_{n=1}^{\infty} \subset \mathcal{S}$, then it is easy to see that $\left( \bigcup_{n=1}^{\infty} E_n \right)_x = \bigcup_{n=1}^{\infty} (E_n)_x \in \mathcal{N}$ for all $x \in X$; hence $\mathcal{S}$ is closed under the formation of countable unions. For $E \in \mathcal{S}$, we have $(E')_x = (E_x)' \in \mathcal{N}$ for all $x \in X$, and so $\mathcal{S}$ is also closed under complementation. This proves (i). The proof of (ii) is similar.
