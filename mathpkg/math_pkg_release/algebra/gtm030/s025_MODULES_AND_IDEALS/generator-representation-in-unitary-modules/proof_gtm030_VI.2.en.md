---
role: proof
locale: en
of_concept: generator-representation-in-unitary-modules
source_book: gtm030
source_chapter: "VI"
source_section: "2"
---

Let $x$ be any element of $\mathfrak{M}$ and write $x = \sum a_i y_i$ for suitable $a_i \in \mathfrak{A}$, $y_i \in \mathfrak{M}$. Since $X$ is a set of generators for the unitary module $\mathfrak{M}$, there exist elements $x_j \in X$ such that

$$y_i = \sum m_{ij} x_j + \sum a_{ij} x_j, \quad m_{ij} \in \mathbb{Z}, \quad a_{ij} \in \mathfrak{A}.$$

Then

$$x = \sum a_i y_i = \sum_i a_i \left( \sum_j m_{ij} x_j + \sum_j a_{ij} x_j \right) = \sum_j \left( \sum_i m_{ij} a_i + \sum_i a_i a_{ij} \right) x_j.$$

Setting

$$b_j = \sum_i m_{ij} a_i + \sum_i a_i a_{ij} \in \mathfrak{A},$$

we obtain $x = \sum_j b_j x_j$, which is of the required form $a_1 x_1 + \cdots + a_r x_r$ with $a_i \in \mathfrak{A}$ and $x_i \in X$.
