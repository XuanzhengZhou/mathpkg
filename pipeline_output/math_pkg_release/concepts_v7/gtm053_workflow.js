export const meta = {
  name: 'v7-extract-gtm053',
  description: 'GTM053: 25 sections → concept extraction',
  phases: [{ title: 'Extract', detail: 'One agent per section' }]
}

var SECTIONS = ["/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM053)A Course in Mathematical Logic for Mathematicians/s001_1_The_first_edition_of_this_book_was_published_in.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM053)A Course in Mathematical Logic for Mathematicians/s002_1_This_book_is_above_all_addressed_to_mathematicians.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM053)A Course in Mathematical Logic for Mathematicians/s003_3_This_book_was_written_for_very_personal_reasons.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM053)A Course in Mathematical Logic for Mathematicians/s004_II_COMPUTABILITY.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM053)A Course in Mathematical Logic for Mathematicians/s005_1_Logic_does_not_concern_itself_with_the_external_world.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM053)A Course in Mathematical Logic for Mathematicians/s006_3_Curious_as_all_this_material_may_be.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM053)A Course in Mathematical Logic for Mathematicians/s007_5_In_conclusion.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM053)A Course in Mathematical Logic for Mathematicians/s008_2_Yet_there_has_been_at_least_one_poetic_system_in_which_gen.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM053)A Course in Mathematical Logic for Mathematicians/s009_12.9_Quantum_logic.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM053)A Course in Mathematical Logic for Mathematicians/s010_3_The_first_levels.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM053)A Course in Mathematical Logic for Mathematicians/s011_13_Each_of_the_sets.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM053)A Course in Mathematical Logic for Mathematicians/s012_18_Connection_with_the_axioms_of.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM053)A Course in Mathematical Logic for Mathematicians/s013_3_Mathematics_and_Cognition.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM053)A Course in Mathematical Logic for Mathematicians/s014_2.7_Proposition.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM053)A Course in Mathematical Logic for Mathematicians/s015_1.1_Embeddings.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM053)A Course in Mathematical Logic for Mathematicians/s016_2.1_Compactness_theorem.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM053)A Course in Mathematical Logic for Mathematicians/s017_2.11_Topological_interpretation.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM053)A Course in Mathematical Logic for Mathematicians/s018_3.1_Definition.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM053)A Course in Mathematical Logic for Mathematicians/s019_3.11_Saturation.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM053)A Course in Mathematical Logic for Mathematicians/s020_4.1_The_theory_of_an_algebraically_closed_field.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM053)A Course in Mathematical Logic for Mathematicians/s021_5.1_Categorical_Theories.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM053)A Course in Mathematical Logic for Mathematicians/s022_6.1_Strongly_minimal_sets_and_pregeometries.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM053)A Course in Mathematical Logic for Mathematicians/s023_6.7_Diophantine_geometry.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM053)A Course in Mathematical Logic for Mathematicians/s024_6.12_Now_we_consider_the_new_class_of_structures.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM053)A Course in Mathematical Logic for Mathematicians/s025_VI_Diophantine_Sets_and_Algorithmic_Undecidability.md"]
var STAGING = '/home/a123/文档/mathpkg/pipeline_output/concepts_v7/gtm053'
var BOOK_SLUG = 'gtm053'

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
