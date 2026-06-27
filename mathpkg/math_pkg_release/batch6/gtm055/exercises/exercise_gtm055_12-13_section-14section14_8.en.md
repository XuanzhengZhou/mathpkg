---
role: exercise
locale: en
chapter: "12-13"
section: "Section 14_Section_14"
exercise_number: 8
---

H. Let $\mathcal{E}$ and $\mathcal{F}$ be normed spaces, and suppose that each is a direct sum of two normed spaces—say $\mathcal{E} = \mathcal{E}_1 \oplus_1 \mathcal{E}_2$ and $\mathcal{F} = \mathcal{F}_1 \oplus_1 \mathcal{F}_2$—so that every vector in $\mathcal{E}$ is a pair $(x_1, x_2)$ where $x_i \in \mathcal{E}_i$, $i = 1, 2$, and similarly for $\mathcal{F}$.

(i) If $T \in \mathcal{L}(\mathcal

(iii) Let $\mathcal{G}$ be another normed space that is a direct sum $\mathcal{G} = \mathcal{G}_1 \oplus_1 \mathcal{G}_2$ and let $S \in \mathcal{L}(\mathcal{F}, \mathcal{G})$. Show that if the operator matrix for $S$ relative to the decompositions $\mathcal{F} = \mathcal{F}_1 \oplus_1 \mathcal{F}_2$ and $\mathcal{G} = \mathcal{G}_1 \oplus_1 \mathcal{G}_2$ is

$$\begin{pmatrix} S_{11} & S_{12} \\ S_{21} & S_{22} \end{pmatrix}$$

and if $T$ is as in (i), then the operator matrix for the product $ST$ relative to the decompositions $\mathcal{E} = \mathcal{E}_1 \oplus_1 \mathcal{E}_2$ and $\mathcal{G} = \mathcal{G}_1 \oplus_1 \mathcal{G}_2$ is the matrix

$$\begin{pmatrix} S_{11} T_{11} + S_{12} T_{21} & S_{11} T_{12} + S_{12} T_{22} \\ S_{21} T_{11} + S_{22} T_{21} & S_{21} T_{12} + S_{22} T_{22} \end{pmatrix} = \begin{pmatrix} S_{11} & S_{12} \\ S_{21} & S_{22} \end{pmatrix} \begin{pmatrix} T_{11} & T_{12} \\ T_{21} & T_{22} \end{pmatrix}$$

obtained by forming the formal product $(S_{ij})(T_{ij})$ by the row by column rule.

(iv) If $\mathcal{E}_i = \mathcal{F}_i$, $i = 1, 2$, so 
...
