export const meta = {
  name: 'v7-extract-gtm095',
  description: 'GTM095: 43 sections → concept extraction',
  phases: [{ title: 'Extract', detail: 'One agent per section' }]
}

var SECTIONS = ["/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s001_2_We_now_consider_some_more_complicated_examples_involving.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s002_5_In_constructing_a_probabilistic_model_for_a_specific_situa.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s003_2_The_simple_but_important_formula.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s004_7_The_important_notion_of_the_variance_of_a_random_variable.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s005_4_Let_us_write.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s006_1_As_in_the_preceding_section.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s007_3_We_have_plotted_a_graph_of.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s008_7_At_the_end_of_Subsection.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s009_2_It_is_evident_that.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s00_preface.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s010_3_We_now_turn_to_the_question_of_how_fast.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s011_3_Using_the_ideas_and_methods_of_Sect.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s012_3_It_follows_from_the_definition_of_a_martingale_that_the_ex.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s013_3_The_following_theorem_describes_a_wide_class_of_Markov_cha.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s014_6_In_this_subsection_we_consider_a_stronger_version_of_the_M.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s015_5_Let_us_indicate_some_useful_properties.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s016_8_The_above_problems_show_that_we_often_need_to_determine_th.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s017_1_When_dealing_with_subsets.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s018_4_In_addition_to_the_two_examples_illustrating_the_use_of_th.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s019_1_The_models_introduced_in_the_preceding_chapter_enabled_us.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s020_2_We_now_define_a_probabilistic_model.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s021_5_The_measurable_space.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s022_4_The_measurable_space.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s023_3_Properties_of_the_expectation.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s024_11_In_this_subsection_we_discuss_the_relation_between_the_Le.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s025_4_Properties_of_conditional_expectations.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s026_10_The_generalized_Bayes_theorem_stated_above.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s027_2_A_striking_example_of_the_utility_of_the_concept_of_condit.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s028_3_Let_us_consider_the_problem_of_determining_the_distributio.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s029_2_Let_us_now_ask_a_similar_question_for_random_processes.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s030_2_Two_random_variables.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s031_5_The_preceding_theorem_says_that_a_distribution_function.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s032_4_Let_us_discuss_some_properties_of_Gaussian_vectors.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s033_6_We_now_turn_to_the_concept_of_Gaussian_systems_in_general.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s034_2_We_already_know.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s035_3_In_the_next_section.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s036_2_Consider_some_particular_cases_where_Lindeberg.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s037_2_Give_a_direct_proof_of_the_fact_that_in_the_Bernoulli_sche.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s038_1_Establish_formula.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s039_2_To_test_whether_a_given_random_variable.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s040_5_Show_that_the_set_of_all_distribution_functions_endowed_wi.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s041_3_Let_us_assume_that_the_random_elements.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM095)Probability-1(3ed,2016)/s042_2_We_now_turn_to_still_another_measure_of_the_proximity_of_t.md"]
var STAGING = '/home/a123/文档/mathpkg/pipeline_output/concepts_v7/gtm095'
var BOOK_SLUG = 'gtm095'

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
