from art import lines, top_positions, bottom_positions

def generate_hourglass(top_grains, bottom_grains):
    top_grains = max(0, min(top_grains, 33))
    bottom_grains = max(0, min(bottom_grains, 14))

    lines_copy = lines[:]

    for i in range(top_grains):
        line_idx, pos = top_positions[i]
        lines_copy[line_idx] = lines_copy[line_idx][:pos] + ':' + lines_copy[line_idx][pos + 1 :]

    for i in range(bottom_grains):
        line_idx, pos, sym = bottom_positions[i]
        lines_copy[line_idx] = lines_copy[line_idx][:pos] + sym + lines_copy[line_idx][pos + 1 :]

    return "\n".join(lines_copy)