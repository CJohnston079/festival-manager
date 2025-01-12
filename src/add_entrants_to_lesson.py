def add_entrants_to_lesson(lesson_file, entrants_file):
    lesson_keys = ["Number", "Name", "Max Duration"]
    lessons = []

    lessons_data = read_csv(lesson_file)
    entrants_data = read_csv(entrants_file)

    num_of_entries = {lesson["Number"]: 0 for lesson in lessons_data}

    for entrant in entrants_data:
        lesson_number = entrant["Class Number"]
        if lesson_number in num_of_entries:
            num_of_entries[lesson_number] += 1

    for lesson in lessons_data:
        filtered_lesson = {key: lesson[key] for key in lesson_keys}
        filtered_lesson["Number of entries"] = num_of_entries[lesson["Number"]]
        lessons.append(filtered_lesson)

    return lessons
