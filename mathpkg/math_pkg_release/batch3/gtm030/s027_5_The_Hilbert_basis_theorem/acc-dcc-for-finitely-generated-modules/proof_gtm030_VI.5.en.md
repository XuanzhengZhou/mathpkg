---
role: proof
locale: en
of_concept: acc-dcc-for-finitely-generated-modules
source_book: gtm030
source_chapter: "VI"
source_section: "5. The Hilbert basis theorem"
---

Let $x_1, x_2, \cdots, x_r$ be a fixed set of generators for $\mathfrak{M}$ and suppose $\mathfrak{N}_1 \subseteq \mathfrak{N}_2 \subseteq \cdots$ is an ascending chain of submodules. For each $j = 1, \dots, r$, the sets $\mathfrak{J}_j(\mathfrak{N}_i)$ form an ascending chain of left ideals in $\mathfrak{A}$. By hypothesis, each of these chains terminates: there exists an integer $N_j$ such that $\mathfrak{J}_j(\mathfrak{N}_{N_j}) = \mathfrak{J}_j(\mathfrak{N}_{N_j+1}) = \cdots$. Let $N = \max(N_1, N_2, \dots, N_r)$. Then $\mathfrak{J}_j(\mathfrak{N}_N) = \mathfrak{J}_j(\mathfrak{N}_{N+1}) = \cdots$ for all $j$. By Lemma 1, $\mathfrak{N}_N = \mathfrak{N}_{N+1} = \cdots$. Thus the ascending chain terminates.

The proof for descending chains is similar: given a descending chain $\mathfrak{N}_1 \supseteq \mathfrak{N}_2 \supseteq \cdots$, the corresponding chains of left ideals $\mathfrak{J}_j(\mathfrak{N}_i)$ are descending and therefore terminate. The same argument with Lemma 1 then yields termination of the descending chain of submodules.
