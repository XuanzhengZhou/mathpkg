---
role: proof
locale: en
of_concept: lemma-special-words-forward-path
source_book: gtm022
source_chapter: "7"
source_section: "2. Word Problems"
---

Trivially, if such a path exists, then $w \sim w'$. Suppose that $w \sim w'$. Then there exists a path

$$w = w_0 - w_1 - \cdots - w_n = w'$$

from $w$ to $w'$. We may suppose the path is chosen so that the number $n$ of steps is the least possible. (If $n = 0$, then the path consists only of forward steps.) If the path has any backward steps, then there is a last such, say $w_k \leftarrow w_{k+1}$. This cannot be the last step of the path, because there is no forward step away from a terminal word. Thus $k + 1 < n$ and $w_{k+1} \rightarrow w_{k+2}$ is a forward step. But there is at most one forward step away from any special word, since the machine operation is determined. This implies that $w_{k+2} = w_k$, and so

$$w = w_0 - w_1 - \cdots - w_k - w_{k+3} - \cdots - w_n = w'$$

is a shorter path from $w$ to $w'$, contrary to the original choice of path. Hence the shortest path consists only of forward steps. $\square$
