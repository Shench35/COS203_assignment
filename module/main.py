

from input_module import get_score
from logic_module import get_grade
from output_module import display_result

score = get_score()
grade = get_grade(score)
display_result(score, grade)
