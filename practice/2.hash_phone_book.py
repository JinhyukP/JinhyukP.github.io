# 전화번호 목록
# Description
# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

# 구조대 : 119
# 박준영 : 97 674 223
# 지영석 : 11 9552 4421
# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# phone_book의 길이는 1 이상 1,000,000 이하입니다.
# 각 전화번호의 길이는 1 이상 20 이하입니다.
# 같은 전화번호가 중복해서 들어있지 않습니다.
# 입출력 예제
# phone_book	return
# ["119", "97674223", "1195524421"]	false
# ["123","456","789"]	true
# ["12","123","1235","567","88"]	false
# 입출력 예 설명
# 입출력 예 #1
# 앞에서 설명한 예와 같습니다.

# 입출력 예 #2
# 한 번호가 다른 번호의 접두사인 경우가 없으므로, 답은 true입니다.

# 입출력 예 #3
# 첫 번째 전화번호, “12”가 두 번째 전화번호 “123”의 접두사입니다. 따라서 답은 false입니다.

# # 1. O(n^2) solution
# import re
# def solution(phone_book):
#     phone_book.sort(key=len)
#     for index, phone_num in enumerate(phone_book):
#         for phone_check in phone_book[index+1:]:
#             # print(phone_num, phone_check)
#             if re.match(phone_num, phone_check):
#                 return False
#     return True

# O(n) solution
def solution(phone_book):
    phone_book.sort(key=len)
    phone_dict = [{} for _ in range(20)] # dictionary for each length... from 1 to 20
    # make a dictionary
    for num in phone_book:
        phone_dict[len(num)-1][num] = True
    # check if prefix exist
    for num in phone_book:
        for idx in range(len(num) - 1):  # subset of number (except full number)
            try:
                if phone_dict[idx][num[:idx+1]]:
                    return False
            except:
                pass
            # print(idx+1, num[:idx+1])   # (idx + 1) is length
    return True
            
# Best solution using string.startswith
# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)

#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True


if __name__=="__main__":
    print(solution(["119", "97674223", "1195524421"]))
    print(solution(["123", "456", "789"]))
    print(solution(["12", "123", "1235", "567", "88"]))