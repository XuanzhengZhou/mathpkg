---
role: proof
locale: en
of_concept: ultrafilter-equivalent-conditions
source_book: gtm037
source_chapter: "18"
source_section: "4"
---

$(i) \Rightarrow (ii)$. Assume that $a \cup b \in F$ while $a \notin F$. Then by $(i)$, $I \setminus a \in F$. Now $(I \setminus a) \cap (a \cup b) \subseteq b$, so $b \in F$.

$(ii) \Rightarrow (iii)$. Say $a \in G \setminus F$. Then $a \cup (I \setminus a) = I \in F$, so by $(ii)$ $I \setminus a \in F \subseteq G$. Hence $\emptyset = a \cap (I \setminus a) \in G$.

$(iii) \Rightarrow (i)$. Assume that $a \subseteq I$ and $a \notin F$. Let
$$G = \{b \subseteq I : \text{there is an } x \in F \text{ with } x \cap a \subseteq b\}.$$
Clearly $F \subset G$, $a \in G$, and $G$ is a filter. In particular $F \subset G$, so $\emptyset \in G$ by $(iii)$. Hence $x \cap a = \emptyset$ for some $x \in F$; hence $x \subseteq I \setminus a$, so $I \setminus a \in F$.
