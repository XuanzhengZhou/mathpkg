---
role: proof
locale: en
of_concept: ideal-product-with-subgroup
source_book: gtm030
source_chapter: "1"
source_section: "1.11"
---
(1) Let $\mathfrak{B}$ be a left ideal and $\mathfrak{C}$ any subgroup of $\mathfrak{A}$. The product $\mathfrak{B}\mathfrak{C} = \{\sum_i b_i c_i \mid b_i \in \mathfrak{B}, c_i \in \mathfrak{C}\}$ is a subgroup since it is closed under addition and contains negatives. For any $a \in \mathfrak{A}$ and $\sum_i b_i c_i \in \mathfrak{B}\mathfrak{C}$, we have $a(\sum_i b_i c_i) = \sum_i (a b_i) c_i$. Since $\mathfrak{B}$ is a left ideal, $a b_i \in \mathfrak{B}$ for each $i$, so the sum belongs to $\mathfrak{B}\mathfrak{C}$. Thus $\mathfrak{B}\mathfrak{C}$ is a left ideal.

(2) Now suppose additionally that $\mathfrak{C}$ is a right ideal. We already know $\mathfrak{B}\mathfrak{C}$ is a left ideal from (1). It remains to check the right ideal property. For any $a \in \mathfrak{A}$ and $\sum_i b_i c_i \in \mathfrak{B}\mathfrak{C}$, we have $(\sum_i b_i c_i)a = \sum_i b_i (c_i a)$. Since $\mathfrak{C}$ is a right ideal, $c_i a \in \mathfrak{C}$ for each $i$, so each term $b_i(c_i a) \in \mathfrak{B}\mathfrak{C}$. Hence $\mathfrak{B}\mathfrak{C}$ is also a right ideal, and therefore a two-sided ideal.
