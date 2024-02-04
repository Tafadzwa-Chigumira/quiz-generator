import random
from countries import *

for quiz_num in range(35):
    quiz_file = open('Capitalsquiz%s.txt' % (quiz_num + 1), 'w')
    answer_key_file = open('capitalquizs_answers%s.txt' % (quiz_num + 1), 'w')

    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write((' '*20) + 'Country Capitals Quiz (Form %s)' % (quiz_num+1))
    quiz_file.write('\n\n')

    country = list(country_capitals.keys())

    random.shuffle(country)

    for questionNum in range(50):
        correct_answer = country_capitals[country[questionNum]]
        wrong_answers = list(country_capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers,3)
        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)


        quiz_file.write('%s. What is the capital of %s?\n' % (questionNum + 1,country[questionNum]))

        for i in range(4):
            quiz_file.write('    %s. %s\n' % ('ABCD'[i],answer_options[i]))
        quiz_file.write('\n')

        answer_key_file.write('%s. %s\n' % (questionNum + 1,'ABCD'[answer_options.index(correct_answer)]))




