def calculate_lesson_time(num_of_entrants, allocated_time):
    num_of_entrants = float(num_of_entrants)
    allocated_time = float(allocated_time)

    performance_time = num_of_entrants * allocated_time
    adjudication_time = performance_time * 0.4
    changover_time = num_of_entrants * 0.1
    lesson_time = round(
        (performance_time + adjudication_time + changover_time) / 5
    ) * 5

    return lesson_time
