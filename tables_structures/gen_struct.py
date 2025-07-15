import os


# assignment_comments
# assignments
# attendances
# course_statistics
# extra_grades
# global_question_has_strong_tags
# global_questions
# presences
# submissions
# user_assignments


tables = [ 
    "assignment_comments",
    "assignments", 
    "attendances", 
    "course_statistics", 
    "extra_grades", 
    "global_question_has_strong_tags", 
    "global_questions", 
    "presences", 
    "submissions", 
    "user_assignments"
]

# for table in tables:
#     path = table + '.txt'
#     with open(path, 'w+', encoding='utf-8') as f:
#         continue


for table in tables:
    path = table + '.sql'
    with open(path, 'w+', encoding='utf-8') as f:
        f.write("DESCRIBE " + table)