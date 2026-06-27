---
role: proof
locale: en
of_concept: open-mapping-theorem
source_book: gtm055
source_chapter: "13"
source_section: "15"
---
It suffices to prove that $T$ is open. Let $U$ be an open set in $\mathcal{E}$, and suppose $y_0$ is a vector belonging to $T(U)$. There exists a vector $x_0$ in $U$ such that $Tx_0 = y_0$, and since $U$ is open, $x_0$ is an interior point of $U$. It follows that the translate $U - x_0$ is a neighborhood of the origin in $\mathcal{E}$, and, by the lemma just established, $T(U - x_0) = T(U) - y_0$ is a neighborhood of the origin in $\mathcal{F}$. Thus $T(U) = (T(U) - y_0) + y_0$ contains $y_0$ as an interior point, and the theorem follows.
