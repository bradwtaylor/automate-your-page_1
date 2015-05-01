def generate_lesson_title_html(lesson_title):
    title_html = '''
    <div class="lesson">
        ''' + lesson_title
    return title_html


def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
        <div class="concept">
            <div class="concept-title">
                ''' + concept_title
    html_text_2 = '''
            </div>
            <div class="concept-description">
                ''' + concept_description
    html_text_3 = '''
            </div>
        </div>
    '''
    
    full_html_text =  html_text_1 + html_text_2 + html_text_3
    return full_html_text


        

TEST_TEXT = [['Lesson Title 1',[['title 1', 'description 1'],
 ['title 2', 'description 2'],
 ['title 3', 'description 3']]],['Lesson Title 2',[['title 4', 'description 4'],
 ['title 5', 'description 5'],
 ['title 6', 'description 6']]],['Lesson Title 3',[['title 7', 'description 7'],
 ['title 8', 'description 8'],
 ['title 9', 'description 9'],['title 10', 'description 10']]]]




def generate_all_html(notes):
    all_html = ''
    for lesson in notes:
        lesson_title = lesson[0]
        lesson_title_html = generate_lesson_title_html(lesson_title)
        all_html = all_html + lesson_title_html
        concepts = lesson[1]
        for concept in concepts:
            title = concept[0]
            description = concept[1]
            concept_html = generate_concept_HTML(title, description)
            all_html = all_html +  concept_html
        all_html = all_html + '''
    </div>'''
    return all_html


print generate_all_html(TEST_TEXT)