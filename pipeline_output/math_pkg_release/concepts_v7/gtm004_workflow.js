export const meta = {
  name: 'v7-extract-gtm004',
  description: 'GTM004: 37 sections → concept extraction',
  phases: [{ title: 'Extract', detail: 'One agent per section' }]
}

var SECTIONS = ["/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s001_2_The_Group_of_Homomorphisms\n\nLet.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s002_3_Sums_and_Products\n\nThe_proof_is_left_to_the_reader.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s003_7_Injective_Modules_over_a_Principal_Ideal_Domain\n\nRecall_th.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s004_8_Cofree_Modules\n\nLet.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s005_II_Categories_and_Functors\n\nIn_Chapter_I_we_discussed_variou.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s006_3_Duality\n\nOur_object_in_this_section_is_to_explain_informal.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s007_III_Extensions_of_Modules\n\nIn_studying_modules.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s008_2_The_Functor_Ext\n\nIn_the_previous_section_we_have_defined_a.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s009_4_Computation_of_some_Ext.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s00_preface.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s010_5_Two_Exact_Sequences\n\nHere_we_shall_deduce_two_exact_sequen.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s011_1_Complexes\n\nLet.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s012_2_The_Long_Exact.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s013_3_Homotopy\n\nLet.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s014_5_Derived_Functors\n\nWe_are_now_prepared_to_tackle_the_main_t.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s015_6_The_Two_Long_Exact_Sequences_of_Derived_Functors\n\nIn_this.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s016_7_The_Functors.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s017_8_The_Functors.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s018_10_Another_Characterization_of_Derived_Functors\n\nWe_have_def.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s019_1_Double_Complexes\n\nDefinition.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s020_VI_Cohomology_of_Groups\n\nIn_this_chapter_we_shall_apply_the.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s021_5_The_Augmentation_Ideal.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s022_VII_Cohomology_of_Lie_Algebras\n\nIn_this_Chapter_we_shall_giv.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s023_2_Definition_of_Cohomology.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s024_4_A_Resolution_of_the_Ground_Field.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s025_VIII_Exact_Couples_and_Spectral_Sequences\n\nIn_this_chapter_w.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s026_2_Filtered_Differential_Objects\n\nIn_this_section_we_describe.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s027_3_Finite_Convergence_Conditions_for_Filtered_Chain_Complexes.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s028_4_The_Ladder_of_an_Exact_Couple\n\nIn_this_section_we_give_a_m.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s029_5_Limits\n\nIn_this_section_we_formulate_the_theory_of_limits.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s030_6_Rees_Systems_and_Filtered_Complexes\n\nIn_Section.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s031_7_The_Limit_of_a_Rees_System\n\nIn_this_section_we_introduce_t.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s032_9_The_Grothendieck_Spectral_Sequence\n\nLet.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s033_1_Projective_Classes_of_Epimorphisms\n\nLet.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s034_4_The_Adjoint_Theorem_and_Examples\n\nFor_the_definition_of_sa.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s035_4_Modular_Representation_Theory\n\nOne_of_the_most_active_fiel.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM004)A Course in Homological Algebra(2ed,1997) /s036_5_Stable_and_Derived_Categories.md"]
var STAGING = '/home/a123/文档/mathpkg/pipeline_output/concepts_v7/gtm004'
var BOOK_SLUG = 'gtm004'

phase('Extract')
log(BOOK_SLUG + ': ' + SECTIONS.length + ' sections')

var results = await pipeline(SECTIONS, function(prev, sp) {
  return async function() {
    var sn = sp.split('/').pop().replace('.md','')
    var dd = STAGING + '/' + sn
    
    var prompt = '=== V7 CONCEPT EXTRACTOR (Per-Section) ===\n\n' +
      'READ: ' + sp + '\n\n' +
      'Extract EVERY theorem, definition, lemma, proposition, corollary, axiom.\n' +
      'For EACH concept, write 3 files in: ' + dd + '/{SLUG}/\n\n' +
      '1. concept.yaml: id,title_en,title_zh:"",type,domain,subdomain,difficulty,tags,depends_on,source_books,content_hash:"",extraction_date:"2026-06-25",extraction_agent:"v7-test"\n' +
      '2. theorem.tex: PURE LaTeX STATEMENT only. NO proof.\n' +
      '3. introduce.en.md: YAML frontmatter(role:introduce,locale:en,content_hash:"",written_against:"") + 2-4 English sentences.\n\n' +
      'CRITICAL: slug = semantic-english-lowercase-hyphen (kummers-theorem NOT ' + key.lower() + '-thm-3-2). ' +
      'source_books = array of OBJECTS. theorem.tex = ZERO natural language.\n\n' +
      'Write .done: echo DONE > ' + dd + '/.done\n' +
      'Write .fail if stuck: echo FAIL > ' + dd + '/.fail'
    
    try { await agent(prompt, { label: sn.substring(0,40), phase: 'Extract' }) } catch(e) {}
    
    // Count on disk
    var cnt = 0
    try {
      var cr = await agent(
        'python3 -c "import os; d=\'' + dd + '\'; print(len([x for x in os.listdir(d) if os.path.isdir(os.path.join(d,x))]) if os.path.exists(d) else 0)"',
        { label: 'cnt-'+sn.substring(0,25), phase: 'Extract' }
      )
      cnt = cr ? parseInt(cr.trim()) || 0 : 0
    } catch(e) {}
    
    return { section: sn.substring(0,50), concepts: cnt }
  }
})

var valid = results.filter(function(r) { return r !== null })
var total = valid.reduce(function(s, r) { return s + (r.concepts || 0) }, 0)
log(BOOK_SLUG + ': ' + total + ' concepts from ' + valid.length + '/' + SECTIONS.length + ' sections')
return { book: BOOK_SLUG, sections: SECTIONS.length, sections_done: valid.length, concepts: total }
