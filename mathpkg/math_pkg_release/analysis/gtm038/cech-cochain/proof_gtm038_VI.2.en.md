---
role: proof
locale: en
of_concept: cech-cochain
source_book: gtm038
source_chapter: "VI"
source_section: "2. The Čech Cohomology"
---
**Proof.** Let $\mathfrak{U} = \{U_i\}$ be an open covering of $ and $\mathcal{F}$ a sheaf. A 569JNRXghklcochain is a family  = (c_{i_0\ldots i_q})$ where {i_0\ldots i_q} \in \mathcal{F}(U_{i_0} \cap \cdots \cap U_{i_q})$, alternating in the indices. The coboundary operator $\delta$ is defined by

3050631(\delta c)_{i_0\ldots i_{q+1}} = \sum_{k=0}^{q+1} (-1)^k c_{i_0\ldots \hat{i}_k \ldots i_{q+1}}|_{U_{i_0}\cap\cdots\cap U_{i_{q+1}}}.3050631

A computation shows $\delta^2 = 0$, giving the Čech cochain complex. The Čech cohomology $\check{H}^q(\mathfrak{U}, \mathcal{F})$ is the cohomology of this complex. $\square$
