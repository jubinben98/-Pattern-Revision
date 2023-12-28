def empty_space(st, height: int):
    for _ in range(height): st.write('\n')

def input_dict(pattern:str, example_nihongo:list, example_english:list) -> dict:
    return {
        "pattern": pattern,
        "example": example_nihongo,
        "example_english": example_english
    }