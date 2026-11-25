class InvalidMarksError(Exception):
    pass

def validate_marks(marks):
    try:
        marks = float(marks)
    except (ValueError,TypeError):
        raise InvalidMarksError("Marks must be a number")
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100")

    return marks
