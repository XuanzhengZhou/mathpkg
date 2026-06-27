---
role: proof
locale: en
of_concept: isomorphism-iff-full-representative-replete
source_book: gtm026
source_chapter: "3"
source_section: "3.2"
---

The characterization follows immediately from the definitions. If $U: \mathcal{A} \to \mathcal{B}$ is an isomorphism, then $U$ is bijective on objects (so it is representative and replete) and fully faithful (so it is a full subcategory). Conversely, if $U$ is a full subcategory, then $U$ is faithful and the induced maps on hom-sets are surjective. If $U$ is also representative, then every object of $\mathcal{B}$ is isomorphic to some $AU$, and if $U$ is full replete, then every object of $\mathcal{B}$ is actually equal to some $AU$ (since objects isomorphic to $AU$ are in the image, and the representative property guarantees every object is isomorphic to some $AU$, but combined with repleteness this forces surjectivity on objects). Together, $U$ is bijective on objects and fully faithful on morphisms, hence an isomorphism of categories.
