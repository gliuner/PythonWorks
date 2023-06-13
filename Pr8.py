import re


def main(enter):
    answer = []
    enter = re.split(" |:#|;|data q|data\nq|\\)\\."
                     "|\\)|\\(|'|}|{|\\.|:|#|\n", enter)
    heh = [value for value in enter if value]
    schet = 0
    while schet < len(heh):
        min_answer = []
        min_schet = schet + 1
        while min_schet < len(heh) and\
                (heh[min_schet].isdigit() or heh[min_schet][0] == '-'):
            min_answer.append(int(heh[min_schet]))
            min_schet += 1
        answer.append((heh[schet], min_answer))
        schet = min_schet
    return answer


a = '{data q(abedi_398) : #( 3353; -3650 ; -5071 ;2607).}.{ data q(cequ):\n#( -9851 ; -460 ;-6297 ).}.{ data q(riesqu_63) : #( 6891 ; 8164 ;\n-1253 ). }.'
print(main(a))
