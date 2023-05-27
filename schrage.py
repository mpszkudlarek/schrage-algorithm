import timeit


def schrage_algorithm(task_unarranged):
    measurement_start = timeit.default_timer()
    time = cmax = 0
    task_ready = []
    while task_ready or task_unarranged:
        while task_unarranged and min(task_unarranged, key=lambda x: x[0])[0] <= time:
            sorted_task = min(task_unarranged, key=lambda x: x[0])
            task_ready.append(sorted_task)
            task_unarranged.remove(sorted_task)
        if not task_ready:
            time = min(task_unarranged, key=lambda x: x[0])[0]
        else:
            sorted_task = max(task_ready, key=lambda x: x[2])
            task_ready.remove(sorted_task)

            time += sorted_task[1]
            cmax = max(cmax, time + sorted_task[2])
    measurement_finish = timeit.default_timer()
    measurement_time = measurement_finish - measurement_start
    return cmax, measurement_time
