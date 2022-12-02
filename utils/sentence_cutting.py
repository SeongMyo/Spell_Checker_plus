def letter_counter(text, spl=False):
    if spl==False:
        text_split = text.split('\n')
    else:
        text_split = text
        
    sum_count = 0
    for idx in range(len(text_split)):
        if len(text_split[idx]) != 0:
            sum_count = sum_count + len(text_split[idx]) + 1
        elif len(text_split[idx]) == 0:
            sum_count = sum_count + 1

    return sum_count


def cutting_idx(text, spl=False):
    if spl==False:
        split_text = text.split('\n')
    else:
        split_text = text
        
    tmp_sum = 0
    idx_cutted = [0]
    for idx in range(len(split_text)):
        if tmp_sum + letter_counter(split_text[idx]) > 500:
            tmp_sum = letter_counter(split_text[idx])
            idx_cutted.append(idx)
        elif tmp_sum + letter_counter(split_text[idx]) <= 500:
            tmp_sum = tmp_sum + letter_counter(split_text[idx])
            
    return idx_cutted

    
def cutting_500_under(text):
    separated_sent = []
    text_split = text.split('\n')
    cut_idx = cutting_idx(text)
    idx_last = len(cut_idx) - 1
    for idx in range(len(cut_idx)):
        if idx != idx_last:
            separated_sent.append('\n'.join(text_split[cut_idx[idx]:cut_idx[idx+1]]))
        else:
            separated_sent.append('\n'.join(text_split[cut_idx[idx]:]))
        
    return separated_sent

