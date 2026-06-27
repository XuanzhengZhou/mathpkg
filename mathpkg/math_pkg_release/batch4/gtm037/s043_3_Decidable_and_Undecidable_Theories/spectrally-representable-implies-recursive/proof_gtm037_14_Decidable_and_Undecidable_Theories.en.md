---
role: proof
locale: en
of_concept: spectrally-representable-implies-recursive
source_book: gtm037
source_chapter: "14"
source_section: "Decidable and Undecidable Theories"
---

We give an intuitive proof, thus appealing to Church's thesis. Let $f$, $n$-ary, be spectrally represented by $\varphi$. Let

$$\Gamma = \{\mathbf{R}_i^m : m \in \omega \setminus \{0\}, i \in \omega, \mathbf{R}_i^m \text{ occurs in } \varphi \text{ or } m = 1 \text{ and } i \leq n\}.$$

Thus $\Gamma$ is finite. Let $\mathcal{L}'$ be the reduct of $\mathcal{L}_{\text{un}}$ to the symbols in $\Gamma$. Given inputs $x_0, \ldots, x_{n-1}$, we can effectively search through all finite $\mathcal{L}'$-structures (up to isomorphism) until we find one $\mathfrak{A}$ that is a model of $\varphi$ with $|\mathbf{R}_i^{1}| = x_i$ for each $i < n$. By condition (i) of spectral representability, such a structure exists. By condition (ii), for any such structure we have $|\mathbf{R}_n^{1}| = f(x_0, \ldots, x_{n-1})$. Since the search is effective (the vocabulary is finite and models can be enumerated), $f$ is computable, hence recursive by Church's thesis.

More formally, one divides the symbols of $\mathcal{L}_{\text{un}}$ different from $R_0^{1}, R_1^{1}, R_2^{1}, R_0^{2}, R_1^{2}$ into two disjoint classes, and constructs a translation of $\varphi$ that encodes the input conditions. The finiteness of the relevant vocabulary ensures the search is effective.
