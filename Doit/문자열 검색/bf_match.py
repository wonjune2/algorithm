# 브루트 포스 문자열 검색하기

def bf_match(txt: str, pat: str) -> int:
    """브루트 포스법으로 문자열 검색"""
    pt = 0  # txt를 따라가는 커사
    pp = 0  # pat를 따라가는 커서

    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        else:
            pt = pt - pp + 1
            pp = 0
        print(pt, pp)
    return pt - pp if pp == len(pat) else - 1
    
if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요.: ')    # 텍스트용 문자열
    s2 = input('패턴을 입력하세여.: ')      # 패턴용 문자열
    
    idx = bf_match(s1, s2)
    
    if idx == -1:
        print("없음")
    else:
        print(f'{(idx + 1)}번째 문자가 일치합니다.')