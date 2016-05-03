def scores_and_grades():
    scores = []
    for value in range(10):
        score = raw_input("Input Score {}:".format(value + 1))
        scores.append(score)
    print "Scores and Grades"
    for score in scores:
        grade = ""
        score = int(score)
        if score >= 60 and score < 70:
            # print 'grade D',score
            grade = 'D'
        elif score >= 70 and score < 80:
            # print 'grade C',score
            grade = 'C'
        elif score >= 80 and score < 90:
            # print 'grade B',score
            grade = 'B'
        elif score >= 90 and score <= 100:
            # print 'grade A',score
            grade = 'A'
        print "Score: {}; Your grade is {}".format(score, grade)
    print "End of the program. Bye!"

scores_and_grades()
