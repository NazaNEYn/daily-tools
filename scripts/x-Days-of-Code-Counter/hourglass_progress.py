from hourglass_art import HOURGLASS_STAGES


def display_hourglass(current_day, total_days):

    if total_days == 0:
        percentage = 0
    else:
        percentage = (current_day / total_days) * 100

    max_stage_index = len(HOURGLASS_STAGES) - 1

    art_index = min(int(percentage / 10), max_stage_index)

    print(HOURGLASS_STAGES[art_index])
