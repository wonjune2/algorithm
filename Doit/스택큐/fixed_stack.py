# 고정 길이 스택 클래스 FiexedStack 구현하기

from typing import Any

class FixedStack:
    """고정 길이 스택 클래스"""

    class Empty(Exception):
        """비어있는 FixedStack에 팝 또는 픽할 때 내보내는 예외 처리"""
        pass

    class Full(Exception):
        """가득 찬 FixedStack에 푸시할 때 내보내는 예외 처리"""
        pass

    def __init__(self, capacity: int = 256) -> None:
        """스택 초기화"""
        self.stk = [None] * capacity # 스택 본체
        self.capacity = capacity     # 스택의 크기
        self.ptr = 0                 # 스택의 포인터

    def __len___(self) -> int:
        """스택에 쌓여 있는 데이터 개수를 반환"""
        return self.ptr

    def is_empty(self) -> bool:
        """스택이 비어 있는지 판단"""
        return self.ptr <= 0

    def is_full(self) -> bool:
        """스택이 가득 차 있는지 판단"""
        return self.ptr >= self.capacity